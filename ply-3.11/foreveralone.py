import ply.lex as lex
import ply.yacc as yacc

from tablafunc import tablaFunciones
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
r = 0
pointerTable =[]
varLectura = []
TempIntTable = []
TempFloatTable = []
auxPilaParamCont = 0
banderaGlobalNoCond = False
#VARIABLES ARREGLOS
arrId = ''
limSup = 0
isArray = False
dim = 1
pilaDim = []
kArr = 0
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

    'gint'   :5000,
    'gfloat' :6000,
    'gstring':7000,
    'gbool'  :7500,
    'lint'   :8000,
    'lfloat' :9000,
    'lstring':10000,
    'lbool'  :11000,
    'tint'   :13000,
    'tfloat' :13500,
    'tstring':13800,
    'tbool'  :14000,
    'tpointer':21000,
    'const'  :12000,
}
Memoria =[None] * 25000

#Reads the document
 
Info= open("test5.txt", "r") 
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
def t_CTEF(t):
    r'[0-9]+[.][0-9]+'
    t.value = float(t.value)              
    return t

def t_NUMBER(t):
     r'[0-9]+'
     t.value = int(t.value)    
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
    programac : PRINCIPAL  agregarfuncmain2  LPAREN RPAREN prinn bloque endpro
    '''
def p_endpro(p):
    '''
    endpro : empty
    '''
    global contLine
    contLine += 1
    quad = ("END", None, None,None, contLine)
    cuadruplo.append(quad)

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
    | ID agregavar LBRACK arreglo cte RBRACK arreglo2
    '''
    global nuevaFunc2
    global contVarL
    global funcionActual
    global arrVarL
    global paramTable
    print("")
    if(funcionActual[-1]!='principal'):
        contVarL += 1
        if(funcionActual[-1]!='programa'):
            if(p[-2]=='(' or p[-2]==','):
                paramTable.append(p[1])
                proc.agregaPilaParam(funcionActual[-1],paramTable)
def p_arreglo(p):
    '''
    arreglo : empty
    '''
    global isArray
    global arrId
    #print("ARRAY",p[-3])
    if(p[-1] =='['):
        isArray = True
        arrId = p[-3]

def p_arreglo2(p):
    '''
    arreglo2 : empty
    '''
    global constTable
    global arrId
    #CHECO SI LA VARIABLE ES LOCAL
    buscador = proc.getDir(funcionActual[-1])
    varfinder = buscador['tvar'].getvar(arrId)
    isGlobal = False

    if varfinder == None:
        #CHECO SI LA VARIABLE ES GLOBAL
        isGlobal = True
        buscador = proc.getDir(funcionActual[0])
        varfinder = buscador['tvar'].getvar(arrId)
    if varfinder == None:
        print("Variable Arreglo no existe ",arrId)
    else:
        if(isGlobal):
            buscador = proc.getDir(funcionActual[0])
            getLocMem = buscador['tvar'].getLocacionMemoria(arrId)
        else:
            buscador = proc.getDir(funcionActual[-1])
            getLocMem = buscador['tvar'].getLocacionMemoria(arrId)


    if(getLocMem not in dict(constTable)):
        constante = (getLocMem,MemoriaVirtual['const'])
        constTable.append(constante)
        MemoriaVirtual['const'] += 1
    #SAVEPOINT
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
        proc.agregav('programa', idFun, tipoFun, MemoriaVirtual['g'+ tipoFun],None)
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
    global TempIntTable
    global TempFloatTable
    global proc
    contLine += 1

    #print("TEMP",funcionActual[-1],Avail.AvailC)
    proc.agregaContTemp(funcionActual[-1],Avail.AvailC)
    Avail.reset()
    MemoriaVirtual['lint'] = 8000
    MemoriaVirtual['lfloat'] = 9000
    MemoriaVirtual['lstring'] = 10000
    MemoriaVirtual['lbool'] = 11000
    MemoriaVirtual['tint'] = 13000
    MemoriaVirtual['tfloat'] = 13500
    MemoriaVirtual['tstring'] = 13800
    MemoriaVirtual['tbool'] = 14000
    MemoriaVirtual['tpointer'] = 21000

    TempIntTable = []
    TempFloatTable = []
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
    asign : LBRACK arrn expresion arrn2 RBRACK arrn3
    | LBRACK arrn CTEI arrn2 RBRACK arrn3
    | LBRACK arrn CTEC arrn2 RBRACK arrn3
    '''

def p_arrn(p):
    '''
    arrn : empty
    '''
    global dim
    global pilaDim
    global PilaO
    #CHECO SI LA VARIABLE ES LOCAL
    buscador = proc.getDir(funcionActual[-1])
    varfinder = buscador['tvar'].getvar(p[-2])
    isGlobal = False

    if varfinder == None:
        #CHECO SI LA VARIABLE ES GLOBAL
        #print("Variable Arreglo no existe en funcion",funcionActual[-1], "buscando globalmente")
        isGlobal = True
        buscador=proc.getDir(funcionActual[0])
        varfinder=buscador['tvar'].getvar(p[-2])
    if varfinder == None:
        print("Variable Arreglo no existe ",arrId)
    else:
        if(isGlobal):
            buscador = proc.getDir(funcionActual[0])
            tipoArr = buscador['tvar'].getTipoVar(p[-2])
            PilaO.append(p[-2])
            PTipo.append(tipoArr)
        else:
            buscador = proc.getDir(funcionActual[-1])
            tipoArr = buscador['tvar'].getTipoVar(p[-2])
            PilaO.append(p[-2])
            PTipo.append(tipoArr)
    auxId = PilaO.pop()
    auxTipo = PTipo.pop()
    dim = 1
    auxPilaDim = (p[-2],dim)
    pilaDim.append(auxPilaDim)
    POper.append("FakeBottom")

def p_arrn2(p):
    '''
    arrn2 : empty
    '''
    #print("NAME ARR?",p[-4])
    global contLine
    global PilaO
    global constTable
    global proc
    buscador = proc.getDir(funcionActual[-1])
    varfinder = buscador['tvar'].getvar(p[-4])
    isGlobal = False
    if varfinder == None:
        #CHECO SI LA VARIABLE ES GLOBAL
        #print("Variable Arreglo no existe en funcion",funcionActual[-1], "buscando globalmente")
        isGlobal = True
        buscador = proc.getDir(funcionActual[0])
        varfinder = buscador['tvar'].getvar(p[-4])
    if varfinder == None:
        print("Variable Arreglo no existe ",arrId)
    else:
        if(isGlobal):
            buscador = proc.getDir(funcionActual[0])
            getTArr = buscador['tvar'].getTabArr(p[-4])
            contLine += 1
            d = dict(constTable)
            limitInf = d[getTArr[0]]
            limitSup = d[getTArr[1]]

            #valorMem = buscador['tvar'].getLocacionMemoria(PilaO[-1])

            #buscador = proc.getDir(funcionActual[-1])
            #varAux = buscador['tvar'].getvar(PilaO[-1])
            #print("Constante",varAux)
            if(PilaO[-1] in dict(constTable)):
                d = dict(constTable)
                valorMem = d[PilaO[-1]]
            else:
                buscador = proc.getDir(funcionActual[-1])
                varAux = buscador['tvar'].getvar(PilaO[-1])
                isGlobal2 = False
                if varAux == None:
                    #CHECO SI LA VARIABLE ES GLOBAL
                    #print("Variable Arreglo no existe en contexto local, buscando globalmente")
                    isGlobal2 = True
                    buscador = proc.getDir(funcionActual[0])
                    varAux = buscador['tvar'].getvar(PilaO[-1])
                if varAux == None:
                    print("Variable Arreglo no existe ",varAux)
                else:
                    if(isGlobal2):
                        buscador = proc.getDir(funcionActual[0])
                        valorMem = buscador['tvar'].getLocacionMemoria(PilaO[-1])
                    else:
                        buscador = proc.getDir(funcionActual[-1])
                        valorMem = buscador['tvar'].getLocacionMemoria(PilaO[-1])
            quad = ("VER",valorMem ,limitInf, limitSup, contLine)



            #print("QUIERO VER PILAO",*PilaO)
            cuadruplo.append(quad)
        else:
            buscador = proc.getDir(funcionActual[-1])
            getTArr = buscador['tvar'].getTabArr(p[-4])
            contLine += 1

            d = dict(constTable)
            limitInf = d[getTArr[0]]
            limitSup = d[getTArr[1]]

            #buscador = proc.getDir(funcionActual[-1])
            #varAux = buscador['tvar'].getvar(PilaO[-1])

            if(PilaO[-1] in dict(constTable)):
                d = dict(constTable)
                valorMem = d[PilaO[-1]]
            else:
                buscador = proc.getDir(funcionActual[-1])
                varAux = buscador['tvar'].getvar(PilaO[-1])
                isGlobal2 = False
                if varAux == None:
                    #CHECO SI LA VARIABLE ES GLOBAL
                    #print("Variable Arreglo no existe en contexto local, buscando globalmente")
                    isGlobal2 = True
                    buscador = proc.getDir(funcionActual[0])
                    varAux = buscador['tvar'].getvar(PilaO[-1])
                if varAux == None:
                    print("Variable Arreglo no existe ",varAux)
                else:
                    if(isGlobal2):
                        buscador = proc.getDir(funcionActual[0])
                        valorMem = buscador['tvar'].getLocacionMemoria(PilaO[-1])
                    else:
                        buscador = proc.getDir(funcionActual[-1])
                        valorMem = buscador['tvar'].getLocacionMemoria(PilaO[-1])

            quad = ("VER",valorMem,limitInf, limitSup, contLine)
            #print("QUIERO VER PILAO",*PilaO)
            cuadruplo.append(quad)

def p_arrn3(p):
    '''
    arrn3 : empty
    '''
    global kArr
    global contLine
    global Avail
    global pointerTable
    #print("ARRN3",p[-6])

    #CHECO SI LA VARIABLE ES LOCAL
    buscador = proc.getDir(funcionActual[-1])
    varfinder = buscador['tvar'].getvar(p[-6])
    isGlobal = False

    if varfinder == None:
        #CHECO SI LA VARIABLE ES GLOBAL
        isGlobal = True
        buscador = proc.getDir(funcionActual[0])
        varfinder = buscador['tvar'].getvar(p[-6])
    if varfinder == None:
        print("Variable Arreglo no existe ",p[-6])
    else:
        if(isGlobal):
            buscador = proc.getDir(funcionActual[0])
            getLocMem = buscador['tvar'].getLocacionMemoria(p[-6])
        else:
            buscador = proc.getDir(funcionActual[-1])
            getLocMem = buscador['tvar'].getLocacionMemoria(p[-6])

    d = dict(constTable)
    auxMem = d[getLocMem]


    aux1 = PilaO.pop() ########
    contLine += 1 ##########

    #result = Avail.next()
    result = MemoriaVirtual['tint'] #########
    TempIntTable.append(MemoriaVirtual['tint'])########

    ###############################

    if(aux1 in dict(constTable)):
        d = dict(constTable)
        valorMem = d[aux1]
    else:
        buscador = proc.getDir(funcionActual[-1])
        varAux = buscador['tvar'].getvar(aux1)
        isGlobal2 = False
        if varAux == None:
            #CHECO SI LA VARIABLE ES GLOBAL
            #print("Variable Arreglo no existe en contexto local, buscando globalmente")
            isGlobal2 = True
            buscador = proc.getDir(funcionActual[0])
            varAux = buscador['tvar'].getvar(aux1)
        if varAux == None:
            print("Variable Arreglo no existe ",aux1)
        else:
            if(isGlobal2):
                buscador = proc.getDir(funcionActual[0])
                valorMem = buscador['tvar'].getLocacionMemoria(aux1)
            else:
                buscador = proc.getDir(funcionActual[-1])
                valorMem = buscador['tvar'].getLocacionMemoria(aux1)
    #####################
    if(-(int(kArr)) in dict(constTable)):
        d = dict(constTable)
        newkArr = d[-(int(kArr))]

    quad = ("+",valorMem, newkArr, result,contLine)
    cuadruplo.append(quad)
    contLine += 1
    MemoriaVirtual['tint'] += 1
    auxresult = result

    result = MemoriaVirtual['tint']

   


    #pointerAux = (MemoriaVirtual['tpointer'],result)
    #pointerTable.append(pointerAux)
    pointerTable.append(MemoriaVirtual['tpointer'])
    TempIntTable.append(MemoriaVirtual['tint'])


    #FALTA ARREGLAR EL SEGUNDO QUAD,RESULT DEBE LLEVAR A POINTER
                                    #21000
    quad = ("+",auxresult , auxMem, MemoriaVirtual['tpointer'], contLine)
    #MemoriaVirtual['tint'] += 1
    cuadruplo.append(quad)
    PilaO.append((MemoriaVirtual['tpointer']))
    MemoriaVirtual['tpointer'] += 1
    POper.pop()

    #print("ARRN3",aux1)

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
            """
            PilaO.append(p[-3])
            print("IS DIS ARREGLO?",p[-3])      
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
            """

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
            arrAuxOp = []
            pointerFlag = False
            arrAux = [right_operand,left_operand]
            for i in range(len(arrAux)):
                #CHECO SI LA VARIABLE ES LOCAL
                buscador = proc.getDir(funcionActual[-1])
                aux = arrAux.pop()
               #print("TABLA INT TEMP",*TempIntTable)
                if(aux in dict(constTable)):
                    d = dict(constTable)
                    auxMem = d[aux]
                    arrAuxOp.append(auxMem)
                elif(aux in TempIntTable):

                    #print("ENTRE AL ELIF",aux)
                    arrAuxOp.append(aux)
                elif(aux in pointerTable):
                    #print("ENTRE AL ELIF ASIGNACION",aux)
                    #c = dict(pointerTable)
                    #auxMem = c[aux] 
                    #print("BUSCANDO POINTER",auxMem)             
                    #arrAuxOp.append(auxMem)
                    pointerFlag = True
                    arrAuxOp.append(aux)

                else:
                    varfinder = buscador['tvar'].getvar(aux)
                    isGlobal = False

                    if varfinder == None:
                        #CHECO SI LA VARIABLE ES GLOBAL
                        #print("Variable Arreglo no existe en contexto local, buscando globalmente")
                        isGlobal = True
                        buscador=proc.getDir(funcionActual[0])
                        varfinder=buscador['tvar'].getvar(aux)
                    if varfinder == None:
                        print("Variable Arreglo no existe ",aux)
                    else:
                        if(isGlobal):
                            buscador = proc.getDir(funcionActual[0])
                            arrAuxOp.append(buscador['tvar'].getLocacionMemoria(aux))
                        else:
                            buscador = proc.getDir(funcionActual[-1])
                            arrAuxOp.append(buscador['tvar'].getLocacionMemoria(aux))
            #print("XXXXXXXXXXXXXXXXXXXXXXXXXXX",*arrAuxOp)
            if(pointerFlag):
                right_operand = arrAuxOp.pop()
                left_operand = arrAuxOp.pop()
                quad= (operator, right_operand, None, left_operand,contLine)
                cuadruplo.append(quad)
                #PilaO.append(result) ESTO RESUELVE ERROR EN TEMPORALES????
                PTipo.append(resultType)
                pointerFlag = False
            else:

                right_operand = arrAuxOp.pop()
                left_operand = arrAuxOp.pop()
                quad= (operator, left_operand, None, right_operand,contLine)
                cuadruplo.append(quad)
                #PilaO.append(result) ESTO RESUELVE ERROR EN TEMPORALES????
                PTipo.append(resultType)
            """
            if(resultType == 'int'):

                quad = (operator, left_operand,right_operand,MemoriaVirtual['t'+resultType], contLine)
                print("OPERATOR T",quad)
                TempIntTable.append(MemoriaVirtual['t'+resultType])
            else:
                quad = (operator, left_operand,right_operand,MemoriaVirtual['t'+resultType], contLine)
                print("OPERATOR F",quad)
                TempIntTable.append(MemoriaVirtual['t'+resultType])
            """
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
    print("IS DIS INICIA?", variable)
    validaTipoV = helper['tvar'].getTipoVar(variable)
    if(validaTipoF=='void'):
        print("Error, funcion tipo void")
    elif(validaTipoV != None):
        validaTipoV 
 
    else:
        #Int
        if( (variable >= 5000 and variable <= 5999) or (variable >= 8000 and variable <= 8999) or (variable >= 13000 and variable <= 13499) ):
            validaTipoV = 'int'
        #Float
        elif((variable >= 6000 and variable <= 6999) or (variable >= 9000 and variable <= 9999) or (variable >= 13500 and variable <= 13799) ):
            validaTipoV = 'float'
        #String
        elif((variable >= 7000 and variable <= 7499) or (variable >= 10000 and variable <= 10999) or (variable >= 13800 and variable <= 13999)):
            validaTipoV = 'string'
        #Bool
        elif((variable >= 7500 and variable <= 7999) or (variable >= 11000 and variable <= 11999) or (variable >= 14000 and variable <= 20999)):
            validaTipoV = 'bool'
        #Const
        elif(variable >= 12000 and variable <=12999):
            validaTipoV = 'int'




    #print("VALIDACION Funcion", validaTipoF,"FUNCION" ,funcionActual[-1],"VALIDACION Variable",validaTipoV, "VARIABLE",variable)
    if(validaTipoF==validaTipoV):

        ##########################
        if(variable in dict(constTable)):
            d = dict(constTable)
            auxMem = d[variable]
            
        elif(variable in TempIntTable):

            #print("ENTRE AL ELIF SUMA",aux)
            auxMem = variable

        elif(variable in pointerTable):
            #print("ENTRE AL ELIF SUMA",aux)
            #c = dict(pointerTable)
            #auxMem = c[aux]                    
            #arrAuxOp.append(auxMem)
            auxMem = variable
        else:
            buscador = proc.getDir(funcionActual[-1])
            varfinder = buscador['tvar'].getvar(variable)
            isGlobal = False

            if varfinder == None:
                #CHECO SI LA VARIABLE ES GLOBAL
                #print("Variable Arreglo no existe en contexto local, buscando globalmente")
                isGlobal = True
                buscador=proc.getDir(funcionActual[0])
                varfinder=buscador['tvar'].getvar(variable)
            if varfinder == None:
                print("Variable Arreglo no existe ",variable)
            else:
                if(isGlobal):
                    buscador = proc.getDir(funcionActual[0])
                    auxMem = (buscador['tvar'].getLocacionMemoria(variable))
                else:
                    buscador = proc.getDir(funcionActual[-1])
                    auxMem = (buscador['tvar'].getLocacionMemoria(variable))

        ##########################
        contLine += 1
        #print("NUEVO RETURN ",auxMem)
        quad = ("Regresa",None,None,auxMem,contLine)
        cuadruplo.append(quad)
        #AQUIESTOY

def p_funcionvoid(p):
    '''
    funcionvoid : ID  LPAREN fnvn1 expresion fnvn2 funcionvoidb 
    '''
def p_funcionvoidb(p):
    '''
    funcionvoidb : COMMA expresion fnvn2 funcionvoidb 
    | RPAREN fnvn3 SEMICOL
    '''   

def p_fnvn1(p):
    '''
    fnvn1 : empty
    '''
    global proc
    global contLine
    global auxTipoParam
    global auxPilaParam
    global auxPilaParamCont 
    auxPilaParamCont = proc.getContPilaParam(p[-2])
    if(proc.funcionExiste(p[-2])):
        contLine += 1
        quad = ("ERA",None,None,p[-2],contLine)
        cuadruplo.append(quad)
        auxTipoParam = proc.getTipoParam(p[-2])
        auxPilaParam = proc.getPilaParam(p[-2])
        #print("CHECK",auxTipoParam,auxPilaParam, p[-2])

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
    global auxPilaParamCont

    #print("CHECK2",*PTipo,"SPACE",*PilaO)
    tempTipo = PTipo.pop()
    tempOper = PilaO.pop()

    ##############################

    #print("TABLA INT TEMP",*TempIntTable)
    if(tempOper in dict(constTable)):
        d = dict(constTable)
        auxMem = d[tempOper]
        
    elif(tempOper in TempIntTable):

        #print("ENTRE AL ELIF SUMA",aux)
        auxMem = tempOper

    elif(tempOper in pointerTable):
        #print("ENTRE AL ELIF SUMA",aux)
        #c = dict(pointerTable)
        #auxMem = c[aux]                    
        #arrAuxOp.append(auxMem)
        auxMem = tempOper
    else:
        buscador = proc.getDir(funcionActual[-1])
        varfinder = buscador['tvar'].getvar(tempOper)
        isGlobal = False

        if varfinder == None:
            #CHECO SI LA VARIABLE ES GLOBAL
            #print("Variable Arreglo no existe en contexto local, buscando globalmente")
            isGlobal = True
            buscador=proc.getDir(funcionActual[0])
            varfinder=buscador['tvar'].getvar(tempOper)
        if varfinder == None:
            print("Variable Arreglo no existe ",tempOper)
        else:
            if(isGlobal):
                buscador = proc.getDir(funcionActual[0])
                auxMem = (buscador['tvar'].getLocacionMemoria(tempOper))
            else:
                buscador = proc.getDir(funcionActual[-1])
                auxMem = (buscador['tvar'].getLocacionMemoria(tempOper))

    ###############################


    #print("CHECK3",tempTipo,tempOper)
    tempAuxTipo = auxTipoParam
    tempAuxPila = auxPilaParam
    tempTipoPop = tempAuxTipo.pop(0)
    if(tempTipo == tempTipoPop):
        k+=1
        contLine+=1
        tempPilaPop = tempAuxPila[-1]
        #print("K1",k,contLine)
        quad = ("Param",auxMem,"para"+str(auxPilaParamCont),contLine )
        cuadruplo.append(quad)
        auxPilaParamCont-=1
    else:
        print("Error no es el mismo tipo",tempTipo,tempTipoPop)
    
def p_fnvn3(p):
    '''
    fnvn3 : empty
    '''    
    global contLine
    global k
    global proc

    #print("???????",p[-1],p[-2],p[-3],p[-4],p[-5],p[-6],p[-7],p[-8],p[-9])
    if(proc.getContPilaParam(p[-6]) != k ):
        print("Numero de argumentos no coincide en la funcion 1",p[-6])
    else:
        #print("SI ENTRE AL FNVN3")
        contLine += 1
        iniciocuadruplo = proc.getInicioCuadruplo(p[-9])
        quad = ("GoSub",p[-6],None,iniciocuadruplo,contLine)
        cuadruplo.append(quad)


        aux = proc.getDir('programa')
        auxVarSearch = aux['tvar'].getLocacionMemoria(p[-6])
        print("IS DIS INICIA2?",p[-6])
        auxTipoSearch = aux['tvar'].getTipoVar(p[-6])
        #ESTE IF CHECA QUE LA FUNCION NO SEA VOID, SI ES VOID NO REGRESA NADA
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
    leeb : RPAREN leen SEMICOL
    | COMMA leen id  leeb
    ''' 

def p_leen(p):
    '''
    leen : empty
    ''' 
    global varId
    global contLine
    global varLectura
    varLectura.append(varId)
    contLine += 1
    aux = varLectura.pop()
    ################
    buscador = proc.getDir(funcionActual[-1])   
    varfinder = buscador['tvar'].getvar(aux)
    isGlobal = False
    if varfinder == None:
        #CHECO SI LA VARIABLE ES GLOBAL
        isGlobal = True
        buscador=proc.getDir(funcionActual[0])
        varfinder=buscador['tvar'].getvar(aux)
    if varfinder == None:
        print("Variable Arreglo no existe ",aux)
    else:
        if(isGlobal):
            buscador = proc.getDir(funcionActual[0])
            auxLee = buscador['tvar'].getLocacionMemoria(aux)

        else:
            buscador = proc.getDir(funcionActual[-1])
            auxLee = buscador['tvar'].getLocacionMemoria(aux)



    ################
    quad=("LEE",None,None,auxLee,contLine)
    cuadruplo.append(quad)

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
   
    global contLine
    contLine += 1


    test = PilaO.pop()
    ###################
    #print("TABLA INT TEMP",*TempIntTable)
    if(test in dict(constTable)):
        d = dict(constTable)
        auxImprime = d[test]
    elif(test in TempIntTable):
        #print("ENTRE AL ELIF SUMA",aux)
        auxImprime = test
    elif(test in pointerTable):
        #print("ENTRE AL ELIF SUMA",aux)
        auxImprime = test                   
    else:
        buscador = proc.getDir(funcionActual[-1])   
        varfinder = buscador['tvar'].getvar(test)
        isGlobal = False
        if varfinder == None:
            #CHECO SI LA VARIABLE ES GLOBAL
            isGlobal = True
            buscador=proc.getDir(funcionActual[0])
            varfinder=buscador['tvar'].getvar(test)
        if varfinder == None:
            print("Variable Arreglo no existe ",test)
        else:
            if(isGlobal):
                buscador = proc.getDir(funcionActual[0])
                auxImprime = buscador['tvar'].getLocacionMemoria(test)

            else:
                buscador = proc.getDir(funcionActual[-1])
                auxImprime = buscador['tvar'].getLocacionMemoria(test)



    ###################
    quad = ("Escritura", None, None, auxImprime,contLine)
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
    repeticionnocond : DESDE asignacioncond HASTA exp repnoconn HACER bloque repnoconn2
    '''
    ###########################
def p_asignacioncond(p):
    '''
    asignacioncond : ID EQUAL asignacioncondb
    | ID asign EQUAL asignacioncondb	
    '''
def p_repnoconn(p):
    '''
    repnoconn : empty 
    '''
    global contLine
    global banderaGlobalNoCond
    PSalto.append(contLine)
    limiteSup = PilaO.pop()
    contador = PilaO.pop()
    tipoDatoContador = PTipo.pop()

    if(limiteSup in dict(constTable)):
        d = dict(constTable)
        limiteSupAux = d[limiteSup]
    elif(limiteSup in TempIntTable):
        limiteSupAux = limiteSup
    elif(limiteSup in pointerTable):
        #c = dict(pointerTable)
        #auxMem = c[aux]                    
        #arrAuxOp.append(auxMem)
        limiteSupAux = limiteSup

    #print("FLEEEEEET",limiteSup,contador,tipoDatoContador)
    if(banderaGlobalNoCond):
        auxMem = MemoriaVirtual['g'+tipoDatoContador]
        MemoriaVirtual['g'+tipoDatoContador] += 1 
    else:
        auxMem = MemoriaVirtual['l'+tipoDatoContador]
        MemoriaVirtual['l'+tipoDatoContador] += 1

    contLine += 1
    quad = (">=", contador, limiteSupAux, auxMem, contLine)
    PilaO.append(contador)
    cuadruplo.append(quad)
    contLine+=1
    quad = ("GotoF",auxMem,None,contLine)
    cuadruplo.append(quad)
    PSalto.append(contLine)
def p_repnoconn2(p):
    '''
    repnoconn2 : empty 
    '''
    global contLine
    global PilaO
    contador = PilaO.pop()
    end = PSalto.pop()
    regresa = PSalto.pop()

    if(1 in dict(constTable)):
        d = dict(constTable)
        unoMem = d[1]
    else:
        constante = (1,MemoriaVirtual['const'])
        constTable.append(constante)
        unoMem = MemoriaVirtual['const']
        MemoriaVirtual['const'] += 1

    contLine += 1
    quad = ("+",unoMem,contador,contador,contLine)
    print("QUAD",quad)
    cuadruplo.append(quad)

    contLine += 1
    quad = ("GOTO", None, None, regresa+1)
    cuadruplo.append(quad)
    FILL(end,contLine+1)

def p_asignacioncondb(p):
    '''
    asignacioncondb : exp 
    | ID asign 
    '''
    global proc
    global PTipo
    global funcionActual
    global PilaO
    print("CONDICIONAL",p[-1],p[-2])
    if(p[-1]=='='):
        POper.append('=')
    #print("it this z ? ", p[-2])
    #proc.testerVariable('fact')
    if(p[-2]!= None):
        PilaO.append(p[-2])
    #CHECA SI P[-2] ES UN NUM ENTERO 1 O FLOTANTE 2.0, NO ENTRA SI ES VARIABLE X,Y,Z,ETC.
    if type(p[-2]) is int or type(p[-2]) is float:
        PTipo.append(type(p[-2]))
    else:
        #CHECA SI ES UN ARREGLO O SI ES UNA VARIABLE X,Y,Z,ETC. SI P[-2] ES NONE ENTONCES SIGNIFICA QUE ES ARREGLO
        if( p[-2] == None):
            print("YEEET")
        #COMO NO ES ARREGLO, QUIERE DECIR QUE ES UNA VARIABLE X,Y,Z,ETC.
        else:
            #ESTO BUSCARA LA VARIABLE PRIMERO EN EL CONTEXTO LOCAL
            buscador=proc.getDir(funcionActual[-1])
            varfinder=buscador['tvar'].getvar(p[-2])
            #SI ESTO REGERSA UN NONE, ENTONCES SIGNFICIA QUE LA VARIABLE NO ES LOCAL
            if varfinder == None:
                #AHORA HARA UNA BUSQUEDA DE LA VARIABLE EN EL CONTEXTO GLOBAL 
                buscador=proc.getDir(funcionActual[0])
                varfinder=buscador['tvar'].getvar(p[-2])
            #EN EL CASO DE VOLVER A SALIR NONE, ESTO QUIERE DECIR QUE NO EXISTE LA VARIABLE DECLARADA EN NINGUNO DE LOS DOS CONTEXTOS
            if varfinder == None:
                print("Variable Normal asignacionCOND no declarada", p[-2], funcionActual[-1])
            else:
                varhelper = varfinder['tipo']
                PTipo.append(varhelper)
    
    print("TIPO DE LA VARIABLE",varhelper)
    #AHORA QUE SABEMOS QUE TIPO ES LA VARIABLE LA CUAL SE ASIGNARA UN VALOR, ES HORA DE PREPARAR LAS VARIABLES PARA EL CUADRUPLO 
    if(POper[-1] == '='):
        right_operand = PilaO.pop()
        right_type    = PTipo.pop()
        left_operand  = PilaO.pop()
        left_type     = PTipo.pop()
        operator      = POper.pop()
        resultType    = sema.getTipo(left_type,right_type,operator)
        if(resultType != 'TypeError'):
            global contLine
            contLine += 1 #TEST
            arrAuxOp = []
            pointerFlag = False
            arrAux = [right_operand,left_operand]

            for i in range(len(arrAux)):
                #CHECO SI LA VARIABLE ES LOCAL
                buscador = proc.getDir(funcionActual[-1])
                aux = arrAux.pop()
               #print("TABLA INT TEMP",*TempIntTable)
                if(aux in dict(constTable)):
                    d = dict(constTable)
                    auxMem = d[aux]
                    arrAuxOp.append(auxMem)
                elif(aux in TempIntTable):

                    #print("ENTRE AL ELIF",aux)
                    arrAuxOp.append(aux)
                elif(aux in pointerTable):
                    #print("ENTRE AL ELIF ASIGNACION",aux)
                    #c = dict(pointerTable)
                    #auxMem = c[aux] 
                    #print("BUSCANDO POINTER",auxMem)             
                    #arrAuxOp.append(auxMem)
                    pointerFlag = True
                    arrAuxOp.append(aux)

                else:
                    varfinder = buscador['tvar'].getvar(aux)
                    isGlobal = False

                    if varfinder == None:
                        #CHECO SI LA VARIABLE ES GLOBAL
                        #print("Variable Arreglo no existe en contexto local, buscando globalmente")
                        isGlobal = True
                        buscador=proc.getDir(funcionActual[0])
                        varfinder=buscador['tvar'].getvar(aux)
                    if varfinder == None:
                        print("Variable Arreglo no existe ",aux)
                    else:
                        if(isGlobal):
                            buscador = proc.getDir(funcionActual[0])
                            arrAuxOp.append(buscador['tvar'].getLocacionMemoria(aux))
                            banderaGlobalNoCond = True
                        else:
                            buscador = proc.getDir(funcionActual[-1])
                            arrAuxOp.append(buscador['tvar'].getLocacionMemoria(aux))
                            banderaGlobalNoCond = False
            if(pointerFlag):
                right_operand = arrAuxOp.pop()
                left_operand = arrAuxOp.pop()
                quad = (operator, right_operand, None, left_operand,contLine)
                cuadruplo.append(quad)
                PilaO.append(left_operand)
                #PilaO.append(result) ESTO RESUELVE ERROR EN TEMPORALES????
                PTipo.append(resultType)
                pointerFlag = False
            else:

                right_operand = arrAuxOp.pop()
                left_operand = arrAuxOp.pop()
                quad = (operator, left_operand, None, right_operand,contLine)
                cuadruplo.append(quad)
                PilaO.append(right_operand)
                #PilaO.append(result) ESTO RESUELVE ERROR EN TEMPORALES????
                PTipo.append(resultType)

        else:
            print("Type mismatch")
            

    ###########################

def p_cte(p):
    '''
    cte : ID 
    | NUMBER saveconst
    | CTEF saveconst
    | CTEC
    | STRING savestringconst
    '''
    PilaO.append(p[1])
    #proc.testerVariable('fact')
    #print("Lookin for array ", p[-2]) ##Nombre de la variable array p[-1] es el [
    #print("ESTA ES pilaO", PilaO[-1])
    if( type(p[1]) is int or type(p[1]) is float):
        PTipo.append(type(p[1]).__name__)
        ####ARREGLO
        global isArray
        global arrId
        global kArr
        global sizeArr
        global r
        global funcionActual
        global MemoriaVirtual
        if(isArray):
            global limSup
            limSup = p[1]
            r = 1 * (limSup - (-1) + 1)
            sizeArr = r
            m0 = r
            d1 = limSup - (-1) + 1
            m1 = m0/d1
            offs = 0 + m1 * (-1)
            kArr = offs
            isArray = False
            #print("ESTA ES MI K",kArr)

            if(proc.busca(funcionActual[-1]) == True):
                if(funcionActual[-1] == "programa"):
                    MemoriaVirtual['g'+tipoVar] += r-1
                else:
                    MemoriaVirtual['l'+tipoVar] += r-1
            else:
                print("La funcion no esta declarada")

            #CHECO SI LA VARIABLE ES LOCAL
            buscador = proc.getDir(funcionActual[-1])
            varfinder = buscador['tvar'].getvar(arrId)
            isGlobal = False

            if varfinder == None:
                #CHECO SI LA VARIABLE ES GLOBAL
                #print("Variable Arreglo no existe en contexto local, buscando globalmente")
                isGlobal = True
                buscador=proc.getDir(funcionActual[0])
                varfinder=buscador['tvar'].getvar(arrId)
            if varfinder == None:
                print("Variable Arreglo no existe ",arrId)
            else:
                if(isGlobal):
                    buscador = proc.getDir(funcionActual[0])
                    datosArr = (-1,limSup,-(int(kArr)))
                    buscador['tvar'].agregaTabArr(arrId,datosArr)
                else:
                    buscador = proc.getDir(funcionActual[-1])
                    datosArr = (-1,limSup,-(int(kArr)))
                    buscador['tvar'].agregaTabArr(arrId,datosArr)

    
    else:
        #print("Funcion Actual ", funcionActual[-1] )
        #Se busca si la variable es arreglo y si ya fue declarada en la funcion actual
        if( p[-1] == '['):
            #print("NOMBRE DE ARREGLO ", p[-2])
            #proc.testerVariable(funcionActual[0])
            #CHECO SI LA VARIABL ES LOCAL

            #buscador = proc.buscador = proc.getDir(funcionActual[-1])
            buscador = proc.getDir(funcionActual[-1])
            varfinder = buscador['tvar'].getvar(p[-2])
            #print("RESULTS ", buscador, varfinder)

            #CHECO SI LA VARIABLE ES GLOBAL
            if varfinder == None:
                buscador=proc.getDir(funcionActual[0])
                varfinder=buscador['tvar'].getvar(p[-2])
            if varfinder == None:
                print("Variable Arreglo no declarada ")
            else:
                varhelper = varfinder['tipo']
                PTipo.append(varhelper)
                
                ####ARREGLO
                """
                global limSup
                limSup = p[1]
                print("DEBUGING ",limSup,p[1])
                
                r = 1 * (limSup - (-1) + 1)
                m0 = r
                d1 = limSup - (-1) + 1
                m1 = m0/d1
                offs = 0 + m1 * (-1)
                kArr = offs
                print("ESTA ES MI K",kArr)
                """


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
    if(p[-2] == "-"):
        if(-p[-1] not in dict(constTable)):
            constante = (-p[-1],MemoriaVirtual['const'])
            constTable.append(constante)
            MemoriaVirtual['const'] += 1
    #print("LISTA DE CONSTANTES",*constTable)
def p_savestringconst(p):
    '''
    savestringconst : empty
    '''
    global constTable
    if(p[-1] not in dict(constTable)):
        constante = (p[-1],MemoriaVirtual['const'])
        constTable.append(constante)
        MemoriaVirtual['const'] += 1  

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
            global TempIntTable
            contLine += 1
            arrAuxOp = []
            arrAux = [right_operand,left_operand]

            for i in range(len(arrAux)):
                #CHECO SI LA VARIABLE ES LOCAL
                buscador = proc.getDir(funcionActual[-1])
                aux = arrAux.pop()

                if(aux in dict(constTable)):
                    d = dict(constTable)
                    auxMem = d[aux]
                    arrAuxOp.append(auxMem)
                elif(aux in TempIntTable):
                   #print("ENTRE AL ELIF",aux)
                    arrAuxOp.append(aux)
                else:
                    varfinder = buscador['tvar'].getvar(aux)
                    isGlobal = False

                    if varfinder == None:
                        #CHECO SI LA VARIABLE ES GLOBAL
                        #print("Variable Arreglo no existe en contexto local, buscando globalmente")
                        isGlobal = True
                        buscador=proc.getDir(funcionActual[0])
                        varfinder=buscador['tvar'].getvar(aux)
                    if varfinder == None:
                        print("Variable Arreglo no existe ",aux)
                    else:
                        if(isGlobal):
                            buscador = proc.getDir(funcionActual[0])
                            arrAuxOp.append(buscador['tvar'].getLocacionMemoria(aux))
                        else:
                            buscador = proc.getDir(funcionActual[-1])
                            arrAuxOp.append(buscador['tvar'].getLocacionMemoria(aux))

            right_operand = arrAuxOp.pop()
            left_operand = arrAuxOp.pop()
            quad = (operator, left_operand, right_operand, MemoriaVirtual['t'+resultType], contLine)
            cuadruplo.append(quad)
            PilaO.append(MemoriaVirtual['t'+resultType])
            PTipo.append(resultType)
            MemoriaVirtual['t'+resultType] += 1
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
        #print("RESULT TYPE ",left_type,left_operand, right_type,right_operand)

        resultType    = sema.getTipo(left_type,right_type,operator)

        if(resultType != 'TypeError'):
            result = Avail.next()
            global contLine
            global TempIntTable
            contLine += 1
            arrAuxOp = []
            arrAux = [right_operand,left_operand]
            #print("ARRAUX",*arrAux)
            for i in range(len(arrAux)):
                #CHECO SI LA VARIABLE ES LOCAL
                buscador = proc.getDir(funcionActual[-1])
                aux = arrAux.pop()
                #print("TABLA INT TEMP",*TempIntTable)
                if(aux in dict(constTable)):
                    d = dict(constTable)
                    auxMem = d[aux]
                    arrAuxOp.append(auxMem)
                elif(aux in TempIntTable):

                    #print("ENTRE AL ELIF SUMA",aux)
                    arrAuxOp.append(aux)
                elif(aux in pointerTable):
                    #print("ENTRE AL ELIF SUMA",aux)
                    #c = dict(pointerTable)
                    #auxMem = c[aux]                    
                    #arrAuxOp.append(auxMem)
                    arrAuxOp.append(aux)
                else:
                    varfinder = buscador['tvar'].getvar(aux)
                    isGlobal = False

                    if varfinder == None:
                        #CHECO SI LA VARIABLE ES GLOBAL
                        #print("Variable Arreglo no existe en contexto local, buscando globalmente")
                        isGlobal = True
                        buscador=proc.getDir(funcionActual[0])
                        varfinder=buscador['tvar'].getvar(aux)
                    if varfinder == None:
                        print("Variable Arreglo no existe ",aux)
                    else:
                        if(isGlobal):
                            buscador = proc.getDir(funcionActual[0])
                            arrAuxOp.append(buscador['tvar'].getLocacionMemoria(aux))
                        else:
                            buscador = proc.getDir(funcionActual[-1])
                            arrAuxOp.append(buscador['tvar'].getLocacionMemoria(aux))
            #print("XXXXXXXXXXXXXXXXXXXXXXXXXXX",*arrAuxOp)
            right_operand = arrAuxOp.pop()
            left_operand = arrAuxOp.pop()
            if(resultType == 'int'):

                quad = (operator, left_operand,right_operand,MemoriaVirtual['t'+resultType], contLine)
                TempIntTable.append(MemoriaVirtual['t'+resultType])
            else:
                quad = (operator, left_operand,right_operand,MemoriaVirtual['t'+resultType], contLine)
                TempIntTable.append(MemoriaVirtual['t'+resultType])


            cuadruplo.append(quad)
            PilaO.append(MemoriaVirtual['t'+resultType])
            PTipo.append(resultType)
            MemoriaVirtual['t'+resultType] += 1
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
        #print("RESULT TYPE ",resultType,"LEFT TYPE",left_type, "LEFT OP",left_operand , "RIGHT TYPE",right_type,"LEFT OP",right_operand)
        #print("Tipo2 " , left_type, right_type)
        #print("Tipo Res ", resultType)
        if(resultType != 'TypeError'):
            result = Avail.next()
            global contLine
            global TempIntTable
            contLine += 1
            arrAuxOp = []
            arrAux = [right_operand,left_operand]
            for i in range(len(arrAux)):

                #CHECO SI LA VARIABLE ES LOCAL
                buscador = proc.getDir(funcionActual[-1])
                aux = arrAux.pop()
                #print("TABLA INT TEMP",*TempIntTable)
                if(aux in dict(constTable)):
                    d = dict(constTable)
                    auxMem = d[aux]
                    arrAuxOp.append(auxMem)
                elif(aux in TempIntTable):

                    #print("ENTRE AL ELIF MULT",aux)
                    arrAuxOp.append(aux)
                elif(aux in pointerTable):
                    #c = dict(pointerTable)
                    #auxMem = c[aux]                    
                    #arrAuxOp.append(auxMem)
                    arrAuxOp.append(aux)
                else:
                    varfinder = buscador['tvar'].getvar(aux)

                    isGlobal = False
                    if varfinder == None:
                        #CHECO SI LA VARIABLE ES GLOBAL
                        #print("Variable Arreglo no existe en contexto local, buscando globalmente",aux)
                        isGlobal = True
                        buscador=proc.getDir(funcionActual[0])
                        varfinder=buscador['tvar'].getvar(aux)
                    if varfinder == None:
                        print("Variable Arreglo no existe ",aux)
                    else:
                        if(isGlobal):
                            buscador = proc.getDir(funcionActual[0])
                            arrAuxOp.append(buscador['tvar'].getLocacionMemoria(aux))

                        else:
                            buscador = proc.getDir(funcionActual[-1])
                            arrAuxOp.append(buscador['tvar'].getLocacionMemoria(aux))
            right_operand = arrAuxOp.pop()
            left_operand = arrAuxOp.pop()
            if(resultType == 'int'):

                quad = (operator, left_operand,right_operand,MemoriaVirtual['t'+resultType], contLine)
                TempIntTable.append(MemoriaVirtual['t'+resultType])
            else:
                quad = (operator, left_operand,right_operand,MemoriaVirtual['t'+resultType], contLine)
                TempIntTable.append(MemoriaVirtual['t'+resultType])

                
            cuadruplo.append(quad)
            PilaO.append(MemoriaVirtual['t'+resultType])
            PTipo.append(resultType)
            MemoriaVirtual['t'+resultType] += 1
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
 
    tempTipoPop = tempAuxTipo[-1]
   
    if(tempTipo == tempTipoPop):
        k += 1 
        contLine += 1
        tempPilaPop = tempAuxPila[-1]
        #print("K",k,contLine)
        kont = k
        quad = ("Param",tempOper, "para1", contLine)
        cuadruplo.append(quad)
    else:
        print("Error en llamadafun2")
 
def p_llamadafun3(p):
    '''
    llamadafun3 : empty
    '''    
    global proc
    global contLine
    global k
    #print("!!!!!!!",p[-1],p[-2],p[-3],p[-4],p[-5],p[-6],p[-7],p[-8],p[-9])
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
            #print("GUADALUPANO2",aux,auxVarSearch, auxTipoSearch,p[-6])
            contLine += 1
            quad = ('=',auxVarSearch,None,MemoriaVirtual['t'+auxTipoSearch],contLine)
            print("ESTA ES LA MEMORIA PERDIDA",MemoriaVirtual['t'+auxTipoSearch])
            TempIntTable.append(MemoriaVirtual['t'+auxTipoSearch])
            PilaO.append(MemoriaVirtual['t'+auxTipoSearch])
            MemoriaVirtual['t'+auxTipoSearch] += 1
            #Sprint("TIPO DE ARREGLO ",auxTipoSearch)

 


            cuadruplo.append(quad)
            #YEEEEEEET
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
    global r
    varId = p[-1]
    if(proc.busca(idFun) == True):
        if(idFun == "programa"):

            proc.agregav(idFun,varId,tipoVar,MemoriaVirtual['g'+tipoVar],None)
            MemoriaVirtual['g'+tipoVar] += 1
        elif(idFun!='principal'):
            proc.agregav(idFun,varId,tipoVar,MemoriaVirtual['l'+tipoVar],None)
            MemoriaVirtual['l'+tipoVar] += 1

            #print("VARIABLES LOCALES ",varId, MemoriaVirtual['l'+tipoVar])          
            #print("VARIABLE AGREGANDOSE ",varId)
            #print("TEST", paramType)
            #paramTable.append(paramType)
       # if(nuevaFunc):

        #paramTable.append(tipoVar)

    else:
        print("La funcion no esta declarada")
    r=0
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
print("TABLA DE POINTER",*pointerTable)
print("TABLA DE CONST",*constTable)
print("TABLA DE Funciones")
proc.arref()
print("XXXXXXXXXXXXXXXXXXXXX")
print("TABLA DE VARIABLES1", proc.testerVariable('programa'))
print("TABLA DE VARIABLES2", proc.testerVariable('fact'))
print("TABLA DE VARIABLES3", proc.testerVariable('inicia'))
despliegaQuad()
print("DONE")

print("MAQUINA VIRTUAL")
#SE METE TODA LA LISTA DE CUADRUPLOS PARA QUE SEAN PROCESADOS

operador    = cuadruplo[0][0]
operando1   = cuadruplo[0][1]
operando2   = cuadruplo[0][2]
resultado   = cuadruplo[0][3]
#lineaConteo = cuadruplo[0][4]
i = 1
#print(operador,operando1,operando2,resultado)
while(operador!='END'):
    print(operador,operando1,operando2,resultado)
    if(operador == '*'):
        if(Memoria[operando1] == None):
            Memoria[operando1] = operando1
        if(Memoria[operando2] == None):
            Memoria[operando2] = operando2
        Memoria[resultado] = Memoria[operando1] * Memoria[operando2]

    if(operador == '/'):
        if(Memoria[operando1] == None):
            Memoria[operando1] = operando1
        if(Memoria[operando2] == None):
            Memoria[operando2] = operando2
        Memoria[resultado] = Memoria[operando1] / Memoria[operando2]

    if(operador == '+'):
        if(Memoria[operando1] == None):
            Memoria[operando1] = operando1
        if(Memoria[operando2] == None):
            Memoria[operando2] = operando2
        Memoria[resultado] = Memoria[operando1] + Memoria[operando2]
        #print("DEBUG", Memoria[resultado])

    if(operador == '-'):
        if(Memoria[operando1] == None):
            Memoria[operando1] = operando1
        if(Memoria[operando2] == None):
            Memoria[operando2] = operando2
        Memoria[resultado] = Memoria[operando1] - Memoria[operando2]
        print("RESTA", Memoria[operando1], Memoria[operando2])
  
    if(operador == '='):
        if(Memoria[operando1] == None):
            #BUSCA LA DIRECCION EN LA TABLA DE CONSTANTE PARA TRAER EL VALOR ORIGINAL
            for key, value in constTable:
                if value == operando1:
                    nuevoOperando1 = key
            Memoria[operando1] = nuevoOperando1

        Memoria[resultado] = Memoria[operando1]

    if(operador == 'Escritura'):
        if(Memoria[resultado] == None):
            print(resultado)
        else:
            print(Memoria[resultado])
    
    operador    = cuadruplo[i][0]
    operando1   = cuadruplo[i][1]
    operando2   = cuadruplo[i][2]
    resultado   = cuadruplo[i][3]
    i += 1
    #print("DEBUGING", Memoria[5002])

    
    


