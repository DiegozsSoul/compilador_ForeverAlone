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
contPara= 0
contVarL= 0
expTipo = ''
funcionActual = []
cuadruplo = []
paramTable = []
paramType = []
constTable = []
arrVarL = []
nuevaFunc = False
nuevaFunc2 = False
temp = []
auxPilaParam = []
auxTipoParam = []
k = 0

class AVAIL(object):

	def __init__(self):
		self.AvailC = 0
		self.Temp = "t"
	def next(self):
		self.AvailC+=1
		return self.Temp + str(self.AvailC)
	def reset(self):
		self.AvailC = 0

#Pilas para cuadroplus
POper  = []
PilaO  = []
PTipo  = []
PSalto = []
Avail = AVAIL()
#Memoria Virtual
# APUNTADORES A MEMORIA
MemoriaVirtual = {
    'gint'   :1000,
    'gfloat' :2000,
    'gstring':3000,
    'gbool'  :4000,
    'lint'   :5000,
    'lfloat' :6000,
    'lstring':7000,
    'lbool'  :8000,
    'tint'   :9000,
    'tfloat' :10000,
    'tstring':11000,
    'tbool'  :12000,
    'const'  :13000,
}
#Reads the document
 
Info= open("test3.txt", "r") 
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
t_STRING    = r'\'.*\''
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
    programac : PRINCIPAL  agregarfuncmain2  LPAREN RPAREN prinn bloque
    '''
def p_prinn(p):
    '''
    prinn : empty
    '''
    global contLine
    false = PSalto.pop()
    PSalto.append(contLine)
    FILL(false, contLine+1)

def p_agregafuncmain2(p):
    '''
    agregarfuncmain2 : 
    '''
    global idFun
    global tipoFun
    global proc
    global contVarL
    idFun= 'principal'
    tipofun ='void'
    proc.agregaf(idFun,tipoFun,None,None,None,contVarL,None,None)
    #print("AKIIII ", p[-1])
    funcionActual.append(p[-1])


def p_agregarfuncmain(p):
    '''
    agregarfuncmain : 
    '''
    global idFun
    global tipoFun
    global proc
    global contLine
    idFun = 'programa'
    tipoFun = 'void'
    proc.agregaf(idFun, tipoFun, None,None,None,None,None,None)
    #print("aki merongo " , p[-1])
    funcionActual.append(p[-1])
    contLine += 1
    quad = ("GOTO",None,None,contLine)
    cuadruplo.append(quad)
    PSalto.append(contLine)



def p_id(p):
    '''
    id : ID agregavar
    | ID agregavar LBRACK cte RBRACK
    '''
    global nuevaFunc2
    global contVarL
    global funcionActual
    global arrVarL
    global paramTable
    if(funcionActual[-1]!='principal'):
        contVarL += 1
        if(funcionActual[-1]!='programa'):
            if(p[-2]=='(' or p[-2]==','):
                paramTable.append(p[1])
                proc.agregaPilaParam(funcionActual[-1],paramTable)

def p_tipovar(p):
    '''
    tipovar : INT agregatipo
    | FLOAT agregatipo
    | CHAR agregatipo
    '''
def p_tipovarfunc(p):
    '''
    tipovarfunc : INT agregatipo
    | FLOAT agregatipo
    | CHAR agregatipo
    '''
    global nuevaFunc2
    global contPara
    global paramType
    global funcionActual
    if(nuevaFunc2):
        paramType.append(p[1])
        contPara += 1

def p_tipofun(p):
    '''
    tipofun : INT 
    | FLOAT
    | CHAR
    | VOID
    '''
    global tipoFun
    tipoFun=p[1]

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
    |  contVReset empty
    '''

def p_varsc(p):
    '''
    varsc : id COMMA varsc
    |  id SEMICOL varsb
    |  empty
    '''
def p_contVReset(p):
    '''
    contVReset : empty
    '''
    global contVarL
    global arrVarL
    arrVarL.append(contVarL)
    contVarL = 0

def p_varsfunc(p):
    '''
    varsfunc :  tipovarfunc varsfuncb
    '''

def p_varsfuncb(p):
    '''
    varsfuncb : id COMMA varsfuncb
    | varsfunc
    |  id
    '''

def p_funcion(p):
    '''
    funcion : FUNCION aux2 ID LPAREN funcionb
    | FUNCION aux2 tipofun ID agregafunc LPAREN funcionb
    | empty
    '''
def p_aux2(p):
    '''
    aux2 : empty
    '''    
    global nuevaFunc2
    global contPara
    global contVarL
    global proc
    global funcionActual
    global arrVarL
    global paramTable

    nuevaFunc2 = True
    #print("Cantidad",funcionActual[-1],arrVarL[-1],contPara)
    proc.agregaCantidadVarLoc(funcionActual[-1],contVarL+contPara)
    paramTable = []
    contPara = 0
    #MARKER

def p_agregafunc(p):
    '''
    agregafunc : empty
    '''
    global idFun
    global proc
    global nuevaFunc
    idFun = p[-1]
    proc.agregaf(idFun, tipoFun,None,None,None,None,None,None)
    #print("ESTA FUNCION ES ", idFun)
    funcionActual.append(idFun)
    nuevaFunc = True

    if(tipoFun!='void'):
        #print("TIPO DE FUN",tipoFun, idFun)
        proc.agregav('programa', idFun, tipoFun, MemoriaVirtual['g'+ tipoFun])
        MemoriaVirtual['g'+tipoFun] += 1    

def p_funcionb(p):
    '''
    funcionb : RPAREN testeru funcionc
    | varsfunc RPAREN testeru funcionc
    '''

def p_testeru(p):
    '''
    testeru : empty 
    '''   
    global paramType
    global contPara
    global proc
    global nuevaFunc2 
    global funcionActual

    if(funcionActual[-1]!='programa' ):
        proc.agregaTablaTipoParam(funcionActual[-1], paramType, len(paramType))
        #print("TEST GOOD",proc.getDir(funcionActual[-1]))
        paramType = []


def p_funcionc(p):
    '''
    funcionc : vars  agregacont bloque reinicio funcion
    | agregacont bloque reinicio funcion
    | empty
    '''
def p_agregacont(p):
    '''
    agregacont : empty
    '''
    global contLine
    global proc
    global funcionActual
    proc.agregaContCuadruplo(funcionActual[-1],contLine+1)

def p_reinicioMemoriaVariable(p):
    '''
    reinicio : empty
    '''
    global MemoriaVirtual
    global contLine
    global funcionActual
    global proc
    contLine += 1

    #print("TEMP",funcionActual[-1],Avail.AvailC)
    proc.agregaContTemp(funcionActual[-1],Avail.AvailC)
    Avail.reset()
    MemoriaVirtual['lint'] = 5000 
    quad = ('ENDFUNC',None,None,None,contLine)
    cuadruplo.append(quad)   
    #AQUI VOY

def p_bloque(p):
    '''
    bloque : LBRACKET estatuto bloqueb
    | LBRACKET RBRACKET
    '''

def p_bloqueb(p):
    '''
    bloqueb : RBRACKET helper
    | estatuto bloqueb
    '''
def p_helper(p):
    '''
    helper : empty
    '''
    global nuevaFunc2
    nuevaFunc2 = False

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
            #result = Avail.next() ESTO RESUELVE ERROR EN TEMPORALES????
            global contLine
            contLine += 1 #TEST
            quad= (operator, left_operand, None, right_operand,contLine)
            cuadruplo.append(quad)
            #PilaO.append(result) ESTO RESUELVE ERROR EN TEMPORALES????
            PTipo.append(resultType)
            
            #print(operator, left_operand, None ,right_operand)
        else:
            print("Type mismatch")
            
def p_retorno(p):
    '''
    retorno : REGRESA LPAREN expresion retn RPAREN SEMICOL
    '''
def p_retn(p):
    '''
    retn : empty
    ''' 
    global proc
    global contLine
    validaTipoF = proc.getTipoFunc(funcionActual[-1])
    helper = proc.getDir(funcionActual[-1])
    variable = PilaO.pop()
    validaTipoV = helper['tvar'].getTipoVar(variable)
    print("VALIDACION", validaTipoF,validaTipoV)
    if(validaTipoF==validaTipoF):
        contLine += 1
        quad = ("Regresa",None,None,variable,contLine)
        cuadruplo.append(quad)
        #AQUIESTOY

def p_funcionvoid(p):
    '''
    funcionvoid : ID  LPAREN fnvn1 expresion fnvn2 RPAREN fnvn3 SEMICOL
    '''

def p_fnvn1(p):
    '''
    fnvn1 : empty
    '''
    global proc
    global contLine
    global auxTipoParam
    global auxPilaParam

    print("RESOLVE",p[-2])
    if(proc.funcionExiste(p[-2])):
        contLine += 1
        quad = ("ERA",None,None,p[-2],contLine)
        cuadruplo.append(quad)
        auxTipoParam = proc.getTipoParam(p[-2])
        auxPilaParam = proc.getPilaParam(p[-2])
        #print("CHECK",auxTipoParam,auxPilaParam)

    else:
        print("LA FUNCION NO EXISTE")

def p_fnvn2(p):
    '''
    fnvn2 : empty
    '''
    global proc
    global k
    global contLine
    global auxTipoParam
    global auxPilaParam

    tempTipo = PTipo.pop()
    tempOper = PilaO.pop()

    tempAuxTipo = auxTipoParam
    tempAuxPila = auxPilaParam

    tempTipoPop = tempAuxTipo.pop()
    
    if(tempTipo == tempTipoPop):
        k+=1
        contLine+=1
        tempPilaPop = tempAuxPila[-1]
        print("K1",k,contLine)
        quad = ("Param",tempOper,k,contLine )
        cuadruplo.append(quad)
    else:
        print("Error")
    
def p_fnvn3(p):
    '''
    fnvn3 : empty
    '''    
    global contLine
    global k
    global proc
    print("MARKER",p[-6])
    if(proc.getContPilaParam(p[-6]) != k ):
        print("Numero de argumentos no coincide en la funcion",p[-6])
    else:
        contLine += 1
        iniciocuadruplo = proc.getInicioCuadruplo(p[-6])
        quad = ("GoSub",p[-6],None,iniciocuadruplo,contLine)
        cuadruplo.append(quad)


        aux = proc.getDir('programa')
        auxVarSearch = aux['tvar'].getLocacionMemoria(p[-6])
        auxTipoSearch = aux['tvar'].getTipoVar(p[-6])
        if(auxTipoSearch != None):
            #print("GUADALUPANO",aux,auxVarSearch, auxTipoSearch,p[-6])
            contLine += 1
            quad = ('=',auxVarSearch,None,MemoriaVirtual['t'+auxTipoSearch],contLine)
            MemoriaVirtual['t'+auxTipoSearch] += 1
            cuadruplo.append(quad)
    k = 0

    #MARKER

def p_lee(p):
    '''
    lee : LEE LPAREN id leeb
    '''
def p_leeb(p):
    '''
    leeb : RPAREN SEMICOL
    | COMMA id leeb
    ''' 

#Checar si la expresion ESCRIBE LPAREN STRING sirve, creo que la primera ya viene eso incluido
def p_escritura(p):
    '''
    escritura : ESCRIBE LPAREN expresion prin1 escriturab
    '''
def p_escriturab(p):
    '''
    escriturab : COMMA expresion prin1 escriturab
    | RPAREN SEMICOL
    '''


def p_prin1(p):
    '''
    prin1 : empty 
    '''
    test = PilaO.pop()
    global contLine
    contLine += 1
    quad = ("Escritura", None, None, test)
    cuadruplo.append(quad)

def p_decision(p):
    '''
    decision : SI LPAREN expresion pn1 RPAREN  ENTONCES decisionb
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
        #print("PSalto", *PSalto)

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
    #print("Pila Salto", *PSalto)
    FILL(false, contLine+1)
    #AQUIVOOOOY

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
    | NUMBER saveconst
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
        elif(p[1][0]== "'"):
            filler=True

        else:
            buscador = proc.getDir(funcionActual[-1])
            varfinder = buscador['tvar'].getvar(p[1])
            #Si no se encuentra en la funcion actual se busca en global
            if varfinder == None:
                buscador=proc.getDir(funcionActual[0])
                varfinder=buscador['tvar'].getvar(p[1])
            if varfinder == None:
                print("Variable Normal no declarada aki")
            else:
                varhelper = varfinder['tipo']
                PTipo.append(varhelper)

def p_saveconst(p):
    '''
    saveconst : empty
    '''
    global constTable
  
    if(p[-1] not in dict(constTable)):
        constante = (p[-1],MemoriaVirtual['const'])
        constTable.append(constante)
        MemoriaVirtual['const'] += 1    
    #print("LISTA DE CONSTANTES",*constTable)

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
    | ID LPAREN llamadafun expresion llamadafun2 RPAREN llamadafun3
    | PLUS cte
    | MINUS cte
    | cte
    | ID asign
    '''

def p_llamadafun(p):
    '''
    llamadafun : empty
    '''    
    global proc
    global contLine
    global auxPilaParam
    global auxTipoParam
    if(proc.funcionExiste(p[-2])):
        contLine += 1
        quad = ("ERA",None,None,p[-2],contLine)
        cuadruplo.append(quad)
        auxTipoParam = proc.getTipoParam(p[-2])
        auxPilaParam = proc.getPilaParam(p[-2])
    else:
        print("La funcion no existe")

def p_llamadafun2(p):
    '''
    llamadafun2 : empty
    '''    
    global proc
    global contLine
    global k
    global auxTipoParam
    global auxPilaParam

    tempTipo = PTipo.pop()
    tempOper = PilaO.pop()
    
    tempAuxTipo = auxTipoParam
    tempAuxPila = auxPilaParam
    print("DEBUG", *tempAuxTipo)
 
    tempTipoPop = tempAuxTipo[-1]
   
    if(tempTipo == tempTipoPop):
        k += 1 
        contLine += 1
        tempPilaPop = tempAuxPila[-1]
        print("K",k,contLine)
        kont = k
        quad = ("Param",tempOper, kont, contLine)
        cuadruplo.append(quad)
    else:
        print("Error")
 
def p_llamadafun3(p):
    '''
    llamadafun3 : empty
    '''    
    global proc
    global contLine
    global k

    print("MARKER2",p[-6])
    if(proc.getContPilaParam(p[-6]) !=k):
        print("Numero de argumentos no coincide en la funcion2",p[-6])
    else:
        contLine += 1
        inicioCuadruplo = proc.getInicioCuadruplo(p[-6])
        quad = ("GoSub",p[-6],None,inicioCuadruplo,contLine)
        cuadruplo.append(quad)

        aux = proc.getDir('programa')
        auxVarSearch = aux['tvar'].getLocacionMemoria(p[-6])
        auxTipoSearch = aux['tvar'].getTipoVar(p[-6])
        if(auxTipoSearch != None):
            print("GUADALUPANO2",aux,auxVarSearch, auxTipoSearch,p[-6])
            contLine += 1
            quad = ('=',auxVarSearch,None,MemoriaVirtual['t'+auxTipoSearch],contLine)
            MemoriaVirtual['t'+auxTipoSearch] += 1
            cuadruplo.append(quad)
    k = 0

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
    global paramTable
    varId = p[-1]
    if(proc.busca(idFun) == True):
        if(idFun == "programa"):
            proc.agregav(idFun,varId,tipoVar,MemoriaVirtual['g'+tipoVar])
            MemoriaVirtual['g'+tipoVar] += 1 
            
        else:
            proc.agregav(idFun,varId,tipoVar,MemoriaVirtual['l'+tipoVar])
            MemoriaVirtual['l'+tipoVar] += 1
            #print("VARIABLE AGREGANDOSE ",varId)
            #print("TEST", paramType)
            #paramTable.append(paramType)
       # if(nuevaFunc):

        #paramTable.append(tipoVar)

    else:
        print("La funcion no esta declarada")
    #print(idFun)
    #print("TABLA DE FUNCION")
    #print(proc.getDir(funcionActual[-1]))
    #proc.testerVariable(idFun)
    #print("PARAM TYPE",*paramTable)

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
#print("TABLA DE FUNCION")
#print("TEST",proc.getDir('fact'))
#print("TEST",proc.getDir('inicia')) 
print("TABLA DE Funciones")
proc.arref()
print("XXXXXXXXXXXXXXXXXXXXX")
print("TABLA DE VARIABLES1",proc.testerVariable('programa'))
print("TABLA DE VARIABLES2",proc.testerVariable('fact'))
print("TABLA DE VARIABLES3", proc.testerVariable('inicia'))
despliegaQuad()
print("DONE")
