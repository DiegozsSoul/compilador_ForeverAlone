import ply.lex as lex
import ply.yacc as yacc

from tablafunc import tablaFunciones
from cuadruplos import cuadruplos
from cubosemantico import ConsideracionesSemanticas

proc = tablaFunciones()
sema = ConsideracionesSemanticas()
tipoVar = ''
varId   = ''
tipoFun = ''
idFun   = ''
contLine= 0
expTipo = ''
funcionActual = []
cuadruplo = []

class AVAIL(object):
	def __init__(self):
		self.AvailC = 0
		self.Temp = "t"

	def next(self):
		self.AvailC+=1
		return self.Temp + str(self.AvailC)

#Pilas para cuadroplus
POper  = []
PilaO  = []
PTipo  = []
PSalto = []
Avail = AVAIL()


#Reads the document
 
Info= open("test.txt", "r") 
data=Info.read()

# Reserved words
reserved = {
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'string' : 'STRING',
    'void' : 'VOID',
    'programa' : 'PROGRAMA',
    'principal' : 'PRINCIPAL',
    'funcion' : 'FUNCION',
    'regresa' : 'REGRESA',
    'lee' : 'LEE',
    'escribe' : 'ESCRIBE',
    'si' : 'SI',
    'entonces' : 'ENTONCES',
    'sino' : 'SINO',
    'mientras' : 'MIENTRAS',
    'haz' : 'HAZ',
    'desde' : 'DESDE',
    'hasta' : 'HASTA',
    'hacer' : 'HACER',
    'var' : 'VAR'
 }

 # List of token names.   This is always required
tokens = [
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'COLON',
    'SEMICOL',
    'LBRACKET',
    'RBRACKET',
    'LBRACK',
    'RBRACK',
    'LTHAN',
    'GTHAN',
    'EQLOP',
    'GEQUAL',
    'LEQUAL',
    'ABRACKET',
    'COMMA',
    'CTEI',
    'CTEF',
    'CTEC',
    'CTES',
    'COMMENT'
 ] + list(reserved.values())
 
 # Regular expression rules for simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_EQUAL     = r'\='
t_COLON     = r'\:'
t_SEMICOL   = r'\;'
t_LBRACKET  = r'\{'
t_RBRACKET  = r'\}'
t_LBRACK    = r'\['
t_RBRACK    = r'\]'
t_LTHAN     = r'\<'
t_GTHAN     = r'\>'
t_GEQUAL    = r'\>='
t_LEQUAL    = r'\<='
t_EQLOP     = r'\=='
t_ABRACKET  = r'\<>'
t_COMMA     = r'\,'
t_STRING    = r'\".*\"'
t_CTEC      = r'[a-zA-Z]'
     
 
 # A regular expression rule with some action code
def t_NUMBER(t):
     r'\d+'
     t.value = int(t.value)    
     return t

def t_CTEF(t):
    r'\d+[eE][-+]?\d+|(\.\d+|\d+\.\d+)([eE][-+]?\d+)?'
    t.value = float(t.value)              
    return t

 # Define a rule so we can track line numbers
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)
 
 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
t_ignore_COMMENT  = r'\%%.*'

 # Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
 
def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'ID')    # Check for reserved words
     return t


 # Build the lexer


lexer = lex.lex()

 #Give the lexer some input
lexer.input(data)

 
print ("Despliegue de Tokens \n")
while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     print(tok) 

def p_programa(p):
    '''
    programa : PROGRAMA agregarfuncmain ID SEMICOL programab
    '''
def p_programab(p):
    '''
    programab : vars funcion programac
    | programac
    '''
def p_programac(p):
    '''
    programac : PRINCIPAL LPAREN RPAREN bloque
    '''
def p_agregarfuncmain(p):
    '''
    agregarfuncmain : 
    '''
    global idFun
    global tipoFun
    global proc
    idFun = 'programa'
    tipoFun = 'void'
    proc.agregaf(idFun, tipoFun)
    #print("aki merongo " , p[-1])
    funcionActual.append(p[-1])

def p_id(p):
    '''
    id : ID agregavar
    | ID agregavar LBRACK cte RBRACK
    '''
def p_tipovar(p):
    '''
    tipovar : INT agregatipo
    | FLOAT agregatipo
    | CHAR agregatipo
    '''
def p_tipofun(p):
    '''
    tipofun : INT 
    | FLOAT
    | CHAR
    | VOID
    '''
    global tipoFun
    tipoFun[0]

def p_agregatipo(p):
    '''
    agregatipo :
    '''
    global tipoVar
    tipoVar = p[-1] 
    
def p_vars(p):
    '''
    vars : VAR varsb
    '''

def p_varsb(p):
    '''
    varsb : tipovar varsc
    |  empty
    '''
def p_varsc(p):
    '''
    varsc : id COMMA varsc
    |  id SEMICOL varsb
    |  empty
    '''
def p_varsfunc(p):
    '''
    varsfunc :  tipovar varsfuncb
    '''
def p_varsfuncb(p):
    '''
    varsfuncb : id COMMA varsfuncb
    |  id
    '''

def p_funcion(p):
    '''
    funcion : FUNCION ID LPAREN funcionb
    | FUNCION tipofun ID agregafunc LPAREN funcionb
    | empty
    '''

def p_agregafunc(p):
    '''
    agregafunc : 
    '''
    global idFun
    global proc
    idFun = p[-1]
    proc.agregaf(idFun, tipoFun)
    #print("ESTA FUNCION ES ", idFun)
    funcionActual.append(idFun)

def p_funcionb(p):
    '''
    funcionb : RPAREN funcionc
    | varsfunc RPAREN funcionc
    '''
def p_funcionc(p):
    '''
    funcionc : vars bloque funcion
    | bloque funcion
    | empty
    '''
def p_bloque(p):
    '''
    bloque : LBRACKET estatuto bloqueb
    | LBRACKET RBRACKET
    '''
def p_bloqueb(p):
    '''
    bloqueb : RBRACKET
    | estatuto bloqueb
    '''
def p_asign(p):
    '''
    asign : LBRACK expresion RBRACK
    | LBRACK CTEI RBRACK
    | LBRACK CTEC RBRACK
    '''
def p_asignacion(p):
    '''
    asignacion : ID EQUAL asignacionb
    | ID asign EQUAL asignacionb	
    '''

def p_asignacionb(p):
    '''
    asignacionb : expresion SEMICOL
    | ID asign SEMICOL
    '''
    if(p[-1]=='='):
        POper.append('=')
    #print("it this z ? ", p[-2])
    #proc.testerVariable('fact')
    if(p[-2]!= None):
        PilaO.append(p[-2])
    #print("LOOKIN 4 ERROR ", PilaO[-1])
    if type(p[-2]) is int or type(p[-2]) is float:
        PTipo.append(type(p[-2]))
    else:
        #print("######## ", p[-3],p[-2] ,p[-1], p[0],p[1])
        #Checa si es un arreglo o una variable normal
        if( p[-2] == None):
            PilaO.append(p[-3])
            buscador = proc.buscador = proc.getDir(funcionActual[-1])
            varfinder = buscador['tvar'].getvar(p[-3])
            #print("RESULTS ", buscador, varfinder)
            if varfinder == None:
                buscador=proc.getDir(funcionActual[0])
                varfinder=buscador['tvar'].getvar(p[-3])
                #print("RESULTS ", buscador, varfinder)               
            if varfinder == None:
                print("Variable Arreglo asignacion no declarada ")
            else:
                varhelper = varfinder['tipo']
                PTipo.append(varhelper)
        #Si no es variable de arreglo entonces es normal
        else:
            buscador=proc.getDir(funcionActual[-1])
            varfinder=buscador['tvar'].getvar(p[-2])
            #Si no se encuentra en la funcion actual se busca en global
            if varfinder == None:
                buscador=proc.getDir(funcionActual[0])
                varfinder=buscador['tvar'].getvar(p[-2])
            if varfinder == None:
                print("Variable Normal asignacion no declarada", p[-2], funcionActual[-1])
            else:
                varhelper = varfinder['tipo']
                PTipo.append(varhelper)
        ##################
        #buscador=proc.getDir(funcionActual[-1])
        #varfinder=buscador['tvar'].getvar(p[-2])

        #if varfinder == None:
        #    buscador=proc.getDir(funcionActual[0])
        #    varfinder=buscador['tvar'].getvar(p[1])
        #if varfinder == None:
        #    print("Vairable no declarada")
        #else:
        #    varhelper = varfinder['tipo']
        #    PTipo.append(varhelper)

    #print("ESTOS SON TODOS LOS OPERADORES ", *POper)
    #print("ESTOS SON TODOS LOS OPERANDOS ", *PilaO)
    #print("ESTOS SON TODOS LOS TIPOS ", *PTipo)
    if(POper[-1] == '='):
        right_operand = PilaO.pop()
        right_type    = PTipo.pop()
        left_operand  = PilaO.pop()
        left_type     = PTipo.pop()
        operator      = POper.pop()
        resultType    = sema.getTipo(left_type,right_type,operator)
        if(resultType != 'TypeError'):
            result = Avail.next()
            global contLine
            contLine += 1 #TEST
            quad= (operator, left_operand, None, right_operand,contLine)
            cuadruplo.append(quad)
            PilaO.append(result)
            PTipo.append(resultType)
            
            #print(operator, left_operand, None ,right_operand)
        else:
            print("Type mismatch")
            
def p_retorno(p):
    '''
    retorno : REGRESA LPAREN expresion RPAREN SEMICOL
    '''
def p_funcionvoid(p):
    '''
    funcionvoid : ID LPAREN expresion RPAREN SEMICOL
    '''
def p_lee(p):
    '''
    lee : LEE LPAREN id leeb
    '''
def p_leeb(p):
    '''
    leeb : RPAREN SEMICOL
    | COMMA id leeb
    ''' 
def p_escritura(p):
    '''
    escritura : ESCRIBE LPAREN expresion escriturab
    | ESCRIBE LPAREN STRING escriturab
    '''
def p_escriturab(p):
    '''
    escriturab : COMMA STRING  escriturab
    | COMMA expresion escriturab
    | RPAREN SEMICOL
    '''
def p_decision(p):
    '''
    decision : SI LPAREN expresion pn1 RPAREN ENTONCES decisionb
    '''
    #print("DECISION ", p[-1],p[-2])

def p_pn1(p):
    '''
    pn1 : empty
    '''
    global contLine
    expTipo = PTipo.pop()
    contLine += 1
    if(expTipo != "bool"):
        print("Type mismatch")
    else:
        result = PilaO.pop()
       #quad = ("GotoF", result, None, contLine) 
        quad = ("GotoF", result, None, contLine)
        cuadruplo.append(quad)
        PSalto.append(contLine)
        print("PSalto", *PSalto)

def p_decisionb(p):
    '''
    decisionb : bloque pn2
    | bloque SINO pn3 bloque pn2
    '''
    #print("DECISION 2", p[-1],p[-2])

def p_pn2(p):
    '''
    pn2 : empty
    '''
    end = PSalto.pop()
    FILL(end, contLine+1)
def p_pn3(p):
    '''
    pn3 : empty
    '''
    global contLine
    contLine += 1
    quad = ("GOTO",None,None,contLine)
    cuadruplo.append(quad)
    false = PSalto.pop()
    PSalto.append(contLine)
    print("Pila Salto", *PSalto)
    FILL(false, contLine+1)

def p_repeticioncond(p):
    '''
    repeticioncond : MIENTRAS rcn1 LPAREN expresion RPAREN HAZ rcn2 bloque rcn3
    '''

def p_rcn1(p):
    '''
    rcn1 : empty
    '''
    PSalto.append(contLine)

def p_rcn2(p):
    '''
    rcn2 : empty 
    '''
    exp_tipo = PTipo.pop()
    if(exp_tipo != "bool"):
        print("Type mismatch")
    else:
        result = PilaO.pop()
        global contLine
        contLine += 1
        quad = ("GotoF", result, None, contLine)
        cuadruplo.append(quad)
        PSalto.append(contLine)

def p_rcn3(p):
    '''
    rcn3 : empty
    '''
    end = PSalto.pop()
    regresa = PSalto.pop()
    global contLine
    contLine += 1
    quad = ("GOTO", None, None, regresa+1)
    cuadruplo.append(quad)
    FILL(end,contLine+1)

def p_repeticionnocond(p):
    '''
    repeticionnocond : DESDE id EQUAL exp HASTA exp HACER bloque
    '''
def p_cte(p):
    '''
    cte : ID 
    | NUMBER
    | CTEF 
    | CTEC
    | STRING
    '''
    PilaO.append(p[1])
    #proc.testerVariable('fact')
    #print("Lookin for array ", p[-2]) ##Nombre de la variable array p[-1] es el [
    #print("ESTA ES pilaO", PilaO[-1])
    if( type(p[1]) is int or type(p[1]) is float):
        PTipo.append(type(p[1]).__name__)

    else:
        #print("Funcion Actual ", funcionActual[-1] )
        #Se busca si la variable es arreglo y si ya fue declarada en la funcion actual 
        if( p[-1] == '['):
            #print("NOMBRE DE ARREGLO ", p[-2])
            #proc.testerVariable(funcionActual[0])
            buscador = proc.buscador = proc.getDir(funcionActual[-1])
            varfinder = buscador['tvar'].getvar(p[-2])
            #print("RESULTS ", buscador, varfinder)
            if varfinder == None:
                buscador=proc.getDir(funcionActual[0])
                varfinder=buscador['tvar'].getvar(p[-2])
            if varfinder == None:
                print("Variable Arreglo no declarada ")
            else:
                varhelper = varfinder['tipo']
                PTipo.append(varhelper)
        else:
            buscador = proc.getDir(funcionActual[-1])
            varfinder = buscador['tvar'].getvar(p[1])
            #Si no se encuentra en la funcion actual se busca en global
            if varfinder == None:
                buscador=proc.getDir(funcionActual[0])
                varfinder=buscador['tvar'].getvar(p[1])
            if varfinder == None:
                print("Variable Normal no declarada")
            else:
                varhelper = varfinder['tipo']
                PTipo.append(varhelper)

def p_expresion(p):
    '''
    expresion : exp
    | exp GTHAN exp
    | exp LTHAN exp
    | exp EQLOP exp
    | exp GEQUAL exp
    | exp LEQUAL exp
    | exp ABRACKET exp
    '''

def p_exp(p):
    '''
    exp : termino
    | termino expb
    '''
    if(p[-1] == '>' or p[-1] == '<' or p[-1] == '==' or p[-1] == '>=' or p[-1] == '<=' or p[-1] == '<>'):
        POper.append(p[-1])
        right_operand = PilaO.pop()
        right_type    = PTipo.pop()
        left_operand  = PilaO.pop()
        left_type     = PTipo.pop()
        operator      = POper.pop()
        resultType    = sema.getTipo(left_type,right_type,operator)
        if(resultType != 'TypeError'):
            result = Avail.next()
            global contLine
            contLine += 1
            quad = (operator, left_operand, right_operand, result, contLine)
            cuadruplo.append(quad)
            PilaO.append(result)
            PTipo.append(resultType)
            #print(operator, left_operand, right_operand, result)
        else:
            print("Type mismatch")


def p_expb(p):
    '''
    expb : PLUS exp
    | MINUS exp
    '''
    if(p[1]== '+'):
        POper.append('+')
    else:
        POper.append('-')
    #print("ESTOS SON TODOS LOS OPERADORES ", *POper)
    #print("ESTOS SON TODOS LOS OPERANDOS ", *PilaO)
    #print("ESTOS SON TODOS LOS TIPOS ", *PTipo)
    
    if(POper[-1]=='+' or POper[-1]=='-'):
        right_operand = PilaO.pop()
        right_type    = PTipo.pop()
        left_operand  = PilaO.pop()
        left_type     = PTipo.pop()
        operator      = POper.pop()
        #print("Operandos " , right_operand, left_operand)
        resultType    = sema.getTipo(left_type,right_type,operator)
        #print("Tipos ", left_type, right_type)
        #print("Tipo Res ", resultType)
        if(resultType != 'TypeError'):
            result = Avail.next()
            global contLine
            contLine += 1
            quad = (operator, left_operand,right_operand,result, contLine)
            cuadruplo.append(quad)
            PilaO.append(result)
            PTipo.append(resultType)
            #print(operator, left_operand, right_operand,result)
        else:
            print("Type mismatch")

def p_termino(p):
    '''
    termino : factor
    | factor terminob
    '''
def p_terminob(p):
    '''
    terminob : TIMES termino
    | DIVIDE termino
    '''
    if(p[1]== '*'):
        POper.append('*')
    else:
        POper.append('/')
    #print("ESTOS SON TODOS LOS OPERADORES ", *POper)

    if(POper[-1]=='*' or POper[-1]=='/'):
        right_operand = PilaO.pop()
        right_type    = PTipo.pop()
        left_operand  = PilaO.pop()
        left_type     = PTipo.pop()
        operator      = POper.pop()
        #print("Operandos2 " , right_operand, left_operand)
        resultType    = sema.getTipo(left_type,right_type,operator)  
        #print("Tipo2 " , left_type, right_type)
        #print("Tipo Res ", resultType)
        if(resultType != 'TypeError'):
            result = Avail.next()
            global contLine
            contLine += 1
            quad = (operator, left_operand, right_operand,result, contLine)
            cuadruplo.append(quad)
            PilaO.append(result)
            PTipo.append(resultType)
            #print(operator, left_operand, right_operand,result)
            
        else: 
            print("Type mismatch")

def p_factor(p):
    '''
    factor : LPAREN expresion RPAREN
    | ID LPAREN expresion RPAREN
    | PLUS cte
    | MINUS cte
    | cte
    | ID asign
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion
    | funcionvoid
    | retorno
    | lee
    | escritura
    | decision
    | repeticioncond
    | repeticionnocond
    | expresion
    '''
def p_empty(p):
     'empty :'
     pass
def p_agregavar(p):
    '''agregavar : '''
    global proc
    global varId
    varId = p[-1]
    if(proc.busca(idFun) == True):
        proc.agregav(idFun, varId, tipoVar)
    else:
        print("La funcion no esta declarada")

def despliegaQuad():
    print("----Desplegando Cuadruplos----")
    for elem in cuadruplo:
        print(elem)

def FILL(input1, input2):
    for i in range(0, len(cuadruplo)):
        if(input1 == cuadruplo[i][3]):
            aux1 = cuadruplo[i][0]
            aux2 = cuadruplo[i][1]
            aux3 = cuadruplo[i][2]
            quad = (aux1, aux2, aux3, input2)
            cuadruplo[i] = quad
            #print("AKI ESTOY" ,i , cuadruplo[i])

def p_error(p):
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"
	

    print(f"Syntax error: Unexpected {token}")

# Build the parser
parser = yacc.yacc()
result = parser.parse(data)
despliegaQuad()
print("DONE")
