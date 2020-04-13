import ply.lex as lex
import ply.yacc as yacc

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
    programa : PROGRAMA ID SEMICOL programab
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
def p_id(p):
    '''
    id : ID 
    | ID LBRACK NUMBER RBRACK
    '''
def p_tipovar(p):
    '''
    tipovar : INT 
    | FLOAT
    | CHAR
    '''
def p_tipofun(p):
    '''
    tipofun : INT 
    | FLOAT
    | CHAR
    | VOID
    '''
def p_vars(p):
    '''
    vars : VAR varsb
    '''
def p_varsb(p):
    '''
    varsb :  tipovar varsc
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
    | FUNCION tipofun ID LPAREN funcionb
    | empty
    '''
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
    decision : SI LPAREN expresion RPAREN ENTONCES decisionb
    '''
def p_decisionb(p):
    '''
    decisionb : bloque
    | bloque SINO bloque
    '''
def p_repeticioncond(p):
    '''
    repeticioncond : MIENTRAS LPAREN expresion RPAREN HAZ bloque
    '''
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
def p_expb(p):
    '''
    expb : PLUS exp
    | MINUS exp
    '''
def p_termino(p):
    '''
    termino : factor
    | factor terminob
    '''
def p_terminob(p):
    '''
    terminob : TIMES exp
    | DIVIDE exp
    '''
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

def p_error(p):
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"
	

    print(f"Syntax error: Unexpected {token}")

# Build the parser
parser = yacc.yacc()
result = parser.parse(data)
print("DONE")
