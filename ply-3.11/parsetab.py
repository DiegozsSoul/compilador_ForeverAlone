
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRACKET CHAR COLON COMMA COMMENT CTEC CTEF CTEI CTES DESDE DIVIDE ENTONCES EQLOP EQUAL ESCRIBE FLOAT FUNCION GEQUAL GTHAN HACER HASTA HAZ ID INT LBRACK LBRACKET LEE LEQUAL LPAREN LTHAN MIENTRAS MINUS NUMBER PLUS PRINCIPAL PROGRAMA RBRACK RBRACKET REGRESA RPAREN SEMICOL SI SINO STRING TIMES VAR VOID\n    programa : PROGRAMA agregarfuncmain ID SEMICOL programab\n    \n    programab : vars funcion programac\n    | programac\n    \n    programac : PRINCIPAL LPAREN RPAREN bloque\n    \n    agregarfuncmain : \n    \n    id : ID agregavar\n    | ID agregavar LBRACK NUMBER RBRACK\n    \n    tipovar : INT agregatipo\n    | FLOAT agregatipo\n    | CHAR agregatipo\n    \n    tipofun : INT \n    | FLOAT\n    | CHAR\n    | VOID\n    \n    agregatipo :\n    \n    vars : VAR varsb\n    \n    varsb : tipovar varsc\n    |  empty\n    \n    varsc : id COMMA varsc\n    |  id SEMICOL varsb\n    |  empty\n    \n    varsfunc :  tipovar varsfuncb\n    \n    varsfuncb : id COMMA varsfuncb\n    |  id\n    \n    funcion : FUNCION ID LPAREN funcionb\n    | FUNCION tipofun ID agregafunc LPAREN funcionb\n    | empty\n    \n    agregafunc : \n    \n    funcionb : RPAREN funcionc\n    | varsfunc RPAREN funcionc\n    \n    funcionc : vars bloque funcion\n    | bloque funcion\n    | empty\n    \n    bloque : LBRACKET estatuto bloqueb\n    | LBRACKET RBRACKET\n    \n    bloqueb : RBRACKET\n    | estatuto bloqueb\n    \n    asign : LBRACK expresion RBRACK\n    | LBRACK CTEI RBRACK\n    | LBRACK CTEC RBRACK\n    \n    asignacion : ID EQUAL asignacionb\n    | ID asign EQUAL asignacionb\t\n    \n    asignacionb : expresion SEMICOL\n    | ID asign SEMICOL\n    \n    retorno : REGRESA LPAREN expresion RPAREN SEMICOL\n    \n    funcionvoid : ID LPAREN expresion RPAREN SEMICOL\n    \n    lee : LEE LPAREN id leeb\n    \n    leeb : RPAREN SEMICOL\n    | COMMA id leeb\n    \n    escritura : ESCRIBE LPAREN expresion escriturab\n    | ESCRIBE LPAREN STRING escriturab\n    \n    escriturab : COMMA STRING  escriturab\n    | COMMA expresion escriturab\n    | RPAREN SEMICOL\n    \n    decision : SI LPAREN expresion RPAREN ENTONCES decisionb\n    \n    decisionb : bloque\n    | bloque SINO bloque\n    \n    repeticioncond : MIENTRAS LPAREN expresion RPAREN HAZ bloque\n    \n    repeticionnocond : DESDE id EQUAL exp HASTA exp HACER bloque\n    \n    cte : ID \n    | NUMBER\n    | CTEF \n    | CTEC\n    | STRING\n    \n    expresion : exp\n    | exp GTHAN exp\n    | exp LTHAN exp\n    | exp EQLOP exp\n    | exp GEQUAL exp\n    | exp LEQUAL exp\n    | exp ABRACKET exp\n    \n    exp : termino\n    | termino expb\n    \n    expb : PLUS exp\n    | MINUS exp\n    \n    termino : factor\n    | factor terminob\n    \n    terminob : TIMES exp\n    | DIVIDE exp\n    \n    factor : LPAREN expresion RPAREN\n    | ID LPAREN expresion RPAREN\n    | PLUS cte\n    | MINUS cte\n    | cte\n    | ID asign\n    \n    estatuto : asignacion\n    | funcionvoid\n    | retorno\n    | lee\n    | escritura\n    | decision\n    | repeticioncond\n    | repeticionnocond\n    | expresion\n    empty :agregavar : '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,6,8,21,41,52,90,91,125,],[0,-1,-3,-2,-4,-35,-34,-36,-37,]),'ID':([2,3,12,15,17,18,19,23,24,25,26,27,32,33,34,38,42,46,51,52,53,54,55,56,57,58,59,60,61,62,63,67,70,71,72,73,74,75,76,77,78,79,89,90,91,92,93,94,95,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,125,127,129,134,135,136,143,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,167,168,169,171,175,176,177,178,179,183,186,187,188,189,190,191,192,196,197,],[-5,4,22,31,-15,-15,-15,37,-11,-12,-13,-14,-8,-9,-10,31,62,31,62,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,97,-64,31,-65,-72,-76,117,-84,117,-61,-62,-63,62,-34,-36,126,-85,97,97,-60,97,31,97,97,97,97,97,97,97,97,97,-73,97,97,-77,97,97,-82,-60,-83,31,-37,-41,126,-80,97,-85,97,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,31,-50,97,-51,-44,-46,-81,-45,-48,-54,97,-49,-52,-53,-55,-56,-58,-57,-59,]),'SEMICOL':([4,29,31,40,67,71,72,73,75,77,78,79,97,110,113,116,117,118,124,126,128,134,136,144,145,146,147,148,149,150,151,152,153,156,159,160,161,162,164,166,170,177,],[5,39,-96,-6,-64,-65,-72,-76,-84,-61,-62,-63,-60,-73,-77,-82,-60,-83,-7,-60,157,-80,-85,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,175,176,-38,-39,-40,178,179,183,-81,]),'VAR':([5,44,84,],[9,9,9,]),'PRINCIPAL':([5,7,9,11,13,14,15,16,17,18,19,28,30,32,33,34,38,39,43,44,48,49,52,80,82,83,84,90,91,119,120,121,123,125,154,],[10,-95,-95,10,-27,-16,-95,-18,-15,-15,-15,-17,-21,-8,-9,-10,-95,-95,-25,-95,-19,-20,-35,-29,-95,-33,-95,-34,-36,-95,-32,-30,-26,-37,-31,]),'FUNCION':([7,9,14,15,16,17,18,19,28,30,32,33,34,38,39,48,49,52,82,90,91,119,125,],[12,-95,-16,-95,-18,-15,-15,-15,-17,-21,-8,-9,-10,-95,-95,-19,-20,-35,12,-34,-36,12,-37,]),'INT':([9,12,36,39,87,],[17,24,17,17,17,]),'FLOAT':([9,12,36,39,87,],[18,25,18,18,18,]),'CHAR':([9,12,36,39,87,],[19,26,19,19,19,]),'LBRACKET':([9,14,15,16,17,18,19,28,30,32,33,34,35,38,39,44,48,49,81,84,184,185,194,195,],[-95,-16,-95,-18,-15,-15,-15,-17,-21,-8,-9,-10,42,-95,-95,42,-19,-20,42,42,42,42,42,42,]),'LPAREN':([10,22,37,42,47,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,75,77,78,79,89,90,91,92,93,94,95,97,98,100,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,125,126,127,129,134,135,136,143,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,168,169,171,175,176,177,178,179,183,186,187,188,189,190,191,192,196,197,],[20,36,-28,63,87,63,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,94,63,98,99,100,-64,101,102,-65,-72,-76,-84,-61,-62,-63,63,-34,-36,63,-85,63,63,135,63,63,63,63,63,63,63,63,63,63,-73,63,63,-77,63,63,-82,-60,-83,-37,135,-41,63,-80,63,-85,63,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,-50,63,-51,-44,-46,-81,-45,-48,-54,63,-49,-52,-53,-55,-56,-58,-57,-59,]),'VOID':([12,],[27,]),'RPAREN':([20,31,36,40,45,67,71,72,73,75,77,78,79,85,86,87,96,97,110,113,116,117,118,124,130,134,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,153,155,160,161,162,163,177,180,181,182,],[35,-96,44,-6,84,-64,-65,-72,-76,-84,-61,-62,-63,-22,-24,44,134,-60,-73,-77,-82,-60,-83,-7,159,-80,-85,164,166,170,170,172,173,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-23,-38,-39,-40,177,-81,166,170,170,]),'COMMA':([29,31,40,67,71,72,73,75,77,78,79,86,97,110,113,116,117,118,124,134,136,138,139,140,144,145,146,147,148,149,150,151,152,153,160,161,162,177,180,181,182,],[38,-96,-6,-64,-65,-72,-76,-84,-61,-62,-63,122,-60,-73,-77,-82,-60,-83,-7,-80,-85,167,169,169,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-38,-39,-40,-81,167,169,169,]),'LBRACK':([31,40,62,97,126,],[-96,50,95,95,95,]),'EQUAL':([31,40,62,93,103,124,160,161,162,],[-96,-6,92,129,143,-7,-38,-39,-40,]),'RBRACKET':([42,51,52,53,54,55,56,57,58,59,60,61,62,67,71,72,73,75,77,78,79,89,90,91,93,97,110,113,116,117,118,125,127,134,136,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,168,171,175,176,177,178,179,183,187,188,189,190,191,192,196,197,],[52,91,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,-64,-65,-72,-76,-84,-61,-62,-63,91,-34,-36,-85,-60,-73,-77,-82,-60,-83,-37,-41,-80,-85,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,-50,-51,-44,-46,-81,-45,-48,-54,-49,-52,-53,-55,-56,-58,-57,-59,]),'REGRESA':([42,51,52,53,54,55,56,57,58,59,60,61,62,67,71,72,73,75,77,78,79,89,90,91,93,97,110,113,116,117,118,125,127,134,136,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,168,171,175,176,177,178,179,183,187,188,189,190,191,192,196,197,],[64,64,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,-64,-65,-72,-76,-84,-61,-62,-63,64,-34,-36,-85,-60,-73,-77,-82,-60,-83,-37,-41,-80,-85,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,-50,-51,-44,-46,-81,-45,-48,-54,-49,-52,-53,-55,-56,-58,-57,-59,]),'LEE':([42,51,52,53,54,55,56,57,58,59,60,61,62,67,71,72,73,75,77,78,79,89,90,91,93,97,110,113,116,117,118,125,127,134,136,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,168,171,175,176,177,178,179,183,187,188,189,190,191,192,196,197,],[65,65,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,-64,-65,-72,-76,-84,-61,-62,-63,65,-34,-36,-85,-60,-73,-77,-82,-60,-83,-37,-41,-80,-85,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,-50,-51,-44,-46,-81,-45,-48,-54,-49,-52,-53,-55,-56,-58,-57,-59,]),'ESCRIBE':([42,51,52,53,54,55,56,57,58,59,60,61,62,67,71,72,73,75,77,78,79,89,90,91,93,97,110,113,116,117,118,125,127,134,136,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,168,171,175,176,177,178,179,183,187,188,189,190,191,192,196,197,],[66,66,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,-64,-65,-72,-76,-84,-61,-62,-63,66,-34,-36,-85,-60,-73,-77,-82,-60,-83,-37,-41,-80,-85,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,-50,-51,-44,-46,-81,-45,-48,-54,-49,-52,-53,-55,-56,-58,-57,-59,]),'SI':([42,51,52,53,54,55,56,57,58,59,60,61,62,67,71,72,73,75,77,78,79,89,90,91,93,97,110,113,116,117,118,125,127,134,136,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,168,171,175,176,177,178,179,183,187,188,189,190,191,192,196,197,],[68,68,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,-64,-65,-72,-76,-84,-61,-62,-63,68,-34,-36,-85,-60,-73,-77,-82,-60,-83,-37,-41,-80,-85,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,-50,-51,-44,-46,-81,-45,-48,-54,-49,-52,-53,-55,-56,-58,-57,-59,]),'MIENTRAS':([42,51,52,53,54,55,56,57,58,59,60,61,62,67,71,72,73,75,77,78,79,89,90,91,93,97,110,113,116,117,118,125,127,134,136,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,168,171,175,176,177,178,179,183,187,188,189,190,191,192,196,197,],[69,69,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,-64,-65,-72,-76,-84,-61,-62,-63,69,-34,-36,-85,-60,-73,-77,-82,-60,-83,-37,-41,-80,-85,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,-50,-51,-44,-46,-81,-45,-48,-54,-49,-52,-53,-55,-56,-58,-57,-59,]),'DESDE':([42,51,52,53,54,55,56,57,58,59,60,61,62,67,71,72,73,75,77,78,79,89,90,91,93,97,110,113,116,117,118,125,127,134,136,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,168,171,175,176,177,178,179,183,187,188,189,190,191,192,196,197,],[70,70,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,-64,-65,-72,-76,-84,-61,-62,-63,70,-34,-36,-85,-60,-73,-77,-82,-60,-83,-37,-41,-80,-85,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,-50,-51,-44,-46,-81,-45,-48,-54,-49,-52,-53,-55,-56,-58,-57,-59,]),'PLUS':([42,51,52,53,54,55,56,57,58,59,60,61,62,63,67,71,72,73,75,77,78,79,89,90,91,92,93,94,95,97,98,100,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,125,126,127,129,133,134,135,136,140,143,144,145,146,147,148,149,150,151,152,153,156,157,158,159,160,161,162,165,168,169,171,175,176,177,178,179,181,183,186,187,188,189,190,191,192,196,197,],[74,74,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,74,-64,-65,111,-76,-84,-61,-62,-63,74,-34,-36,74,-85,74,74,-60,74,74,74,74,74,74,74,74,74,74,-73,74,74,-77,74,74,-82,-60,-83,-37,-60,-41,74,-63,-80,74,-85,-64,74,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-85,-43,-42,-81,-38,-39,-40,-47,-50,74,-51,-44,-46,-81,-45,-48,-64,-54,74,-49,-52,-53,-55,-56,-58,-57,-59,]),'MINUS':([42,51,52,53,54,55,56,57,58,59,60,61,62,63,67,71,72,73,75,77,78,79,89,90,91,92,93,94,95,97,98,100,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,125,126,127,129,133,134,135,136,140,143,144,145,146,147,148,149,150,151,152,153,156,157,158,159,160,161,162,165,168,169,171,175,176,177,178,179,181,183,186,187,188,189,190,191,192,196,197,],[76,76,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,76,-64,-65,112,-76,-84,-61,-62,-63,76,-34,-36,76,-85,76,76,-60,76,76,76,76,76,76,76,76,76,76,-73,76,76,-77,76,76,-82,-60,-83,-37,-60,-41,76,-63,-80,76,-85,-64,76,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-85,-43,-42,-81,-38,-39,-40,-47,-50,76,-51,-44,-46,-81,-45,-48,-64,-54,76,-49,-52,-53,-55,-56,-58,-57,-59,]),'NUMBER':([42,50,51,52,53,54,55,56,57,58,59,60,61,62,63,67,71,72,73,74,75,76,77,78,79,89,90,91,92,93,94,95,97,98,100,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,125,127,129,134,135,136,143,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,168,169,171,175,176,177,178,179,183,186,187,188,189,190,191,192,196,197,],[77,88,77,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,77,-64,-65,-72,-76,77,-84,77,-61,-62,-63,77,-34,-36,77,-85,77,77,-60,77,77,77,77,77,77,77,77,77,77,-73,77,77,-77,77,77,-82,-60,-83,-37,-41,77,-80,77,-85,77,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,-50,77,-51,-44,-46,-81,-45,-48,-54,77,-49,-52,-53,-55,-56,-58,-57,-59,]),'CTEF':([42,51,52,53,54,55,56,57,58,59,60,61,62,63,67,71,72,73,74,75,76,77,78,79,89,90,91,92,93,94,95,97,98,100,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,125,127,129,134,135,136,143,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,168,169,171,175,176,177,178,179,183,186,187,188,189,190,191,192,196,197,],[78,78,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,78,-64,-65,-72,-76,78,-84,78,-61,-62,-63,78,-34,-36,78,-85,78,78,-60,78,78,78,78,78,78,78,78,78,78,-73,78,78,-77,78,78,-82,-60,-83,-37,-41,78,-80,78,-85,78,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,-50,78,-51,-44,-46,-81,-45,-48,-54,78,-49,-52,-53,-55,-56,-58,-57,-59,]),'CTEC':([42,51,52,53,54,55,56,57,58,59,60,61,62,63,67,71,72,73,74,75,76,77,78,79,89,90,91,92,93,94,95,97,98,100,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,125,127,129,134,135,136,143,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,168,169,171,175,176,177,178,179,183,186,187,188,189,190,191,192,196,197,],[79,79,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,79,-64,-65,-72,-76,79,-84,79,-61,-62,-63,79,-34,-36,79,-85,79,133,-60,79,79,79,79,79,79,79,79,79,79,-73,79,79,-77,79,79,-82,-60,-83,-37,-41,79,-80,79,-85,79,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,-50,79,-51,-44,-46,-81,-45,-48,-54,79,-49,-52,-53,-55,-56,-58,-57,-59,]),'STRING':([42,51,52,53,54,55,56,57,58,59,60,61,62,63,67,71,72,73,74,75,76,77,78,79,89,90,91,92,93,94,95,97,98,100,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,125,127,129,134,135,136,143,144,145,146,147,148,149,150,151,152,153,157,158,159,160,161,162,165,168,169,171,175,176,177,178,179,183,186,187,188,189,190,191,192,196,197,],[67,67,-35,-86,-87,-88,-89,-90,-91,-92,-93,-94,-60,67,-64,-65,-72,-76,67,-84,67,-61,-62,-63,67,-34,-36,67,-85,67,67,-60,67,140,67,67,67,67,67,67,67,67,-73,67,67,-77,67,67,-82,-60,-83,-37,-41,67,-80,67,-85,67,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-43,-42,-81,-38,-39,-40,-47,-50,181,-51,-44,-46,-81,-45,-48,-54,67,-49,-52,-53,-55,-56,-58,-57,-59,]),'SINO':([52,90,91,125,191,],[-35,-34,-36,-37,194,]),'TIMES':([62,67,73,75,77,78,79,93,97,116,117,118,126,133,134,136,140,156,159,160,161,162,177,181,],[-60,-64,114,-84,-61,-62,-63,-85,-60,-82,-60,-83,-60,-63,-80,-85,-64,-85,-81,-38,-39,-40,-81,-64,]),'DIVIDE':([62,67,73,75,77,78,79,93,97,116,117,118,126,133,134,136,140,156,159,160,161,162,177,181,],[-60,-64,115,-84,-61,-62,-63,-85,-60,-82,-60,-83,-60,-63,-80,-85,-64,-85,-81,-38,-39,-40,-81,-64,]),'GTHAN':([62,67,71,72,73,75,77,78,79,93,97,110,113,116,117,118,126,133,134,136,140,150,151,152,153,156,159,160,161,162,177,181,],[-60,-64,104,-72,-76,-84,-61,-62,-63,-85,-60,-73,-77,-82,-60,-83,-60,-63,-80,-85,-64,-74,-75,-78,-79,-85,-81,-38,-39,-40,-81,-64,]),'LTHAN':([62,67,71,72,73,75,77,78,79,93,97,110,113,116,117,118,126,133,134,136,140,150,151,152,153,156,159,160,161,162,177,181,],[-60,-64,105,-72,-76,-84,-61,-62,-63,-85,-60,-73,-77,-82,-60,-83,-60,-63,-80,-85,-64,-74,-75,-78,-79,-85,-81,-38,-39,-40,-81,-64,]),'EQLOP':([62,67,71,72,73,75,77,78,79,93,97,110,113,116,117,118,126,133,134,136,140,150,151,152,153,156,159,160,161,162,177,181,],[-60,-64,106,-72,-76,-84,-61,-62,-63,-85,-60,-73,-77,-82,-60,-83,-60,-63,-80,-85,-64,-74,-75,-78,-79,-85,-81,-38,-39,-40,-81,-64,]),'GEQUAL':([62,67,71,72,73,75,77,78,79,93,97,110,113,116,117,118,126,133,134,136,140,150,151,152,153,156,159,160,161,162,177,181,],[-60,-64,107,-72,-76,-84,-61,-62,-63,-85,-60,-73,-77,-82,-60,-83,-60,-63,-80,-85,-64,-74,-75,-78,-79,-85,-81,-38,-39,-40,-81,-64,]),'LEQUAL':([62,67,71,72,73,75,77,78,79,93,97,110,113,116,117,118,126,133,134,136,140,150,151,152,153,156,159,160,161,162,177,181,],[-60,-64,108,-72,-76,-84,-61,-62,-63,-85,-60,-73,-77,-82,-60,-83,-60,-63,-80,-85,-64,-74,-75,-78,-79,-85,-81,-38,-39,-40,-81,-64,]),'ABRACKET':([62,67,71,72,73,75,77,78,79,93,97,110,113,116,117,118,126,133,134,136,140,150,151,152,153,156,159,160,161,162,177,181,],[-60,-64,109,-72,-76,-84,-61,-62,-63,-85,-60,-73,-77,-82,-60,-83,-60,-63,-80,-85,-64,-74,-75,-78,-79,-85,-81,-38,-39,-40,-81,-64,]),'RBRACK':([67,71,72,73,75,77,78,79,88,97,110,113,116,117,118,131,132,133,134,136,144,145,146,147,148,149,150,151,152,153,160,161,162,177,],[-64,-65,-72,-76,-84,-61,-62,-63,124,-60,-73,-77,-82,-60,-83,160,161,162,-80,-85,-66,-67,-68,-69,-70,-71,-74,-75,-78,-79,-38,-39,-40,-81,]),'HASTA':([67,72,73,75,77,78,79,97,110,113,116,117,118,134,136,150,151,152,153,160,161,162,174,177,],[-64,-72,-76,-84,-61,-62,-63,-60,-73,-77,-82,-60,-83,-80,-85,-74,-75,-78,-79,-38,-39,-40,186,-81,]),'HACER':([67,72,73,75,77,78,79,97,110,113,116,117,118,134,136,150,151,152,153,160,161,162,177,193,],[-64,-72,-76,-84,-61,-62,-63,-60,-73,-77,-82,-60,-83,-80,-85,-74,-75,-78,-79,-38,-39,-40,-81,195,]),'CTEI':([95,],[132,]),'ENTONCES':([172,],[184,]),'HAZ':([173,],[185,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'agregarfuncmain':([2,],[3,]),'programab':([5,],[6,]),'vars':([5,44,84,],[7,81,81,]),'programac':([5,11,],[8,21,]),'funcion':([7,82,119,],[11,120,154,]),'empty':([7,9,15,38,39,44,82,84,119,],[13,16,30,30,16,83,13,83,13,]),'varsb':([9,39,],[14,49,]),'tipovar':([9,36,39,87,],[15,46,15,46,]),'tipofun':([12,],[23,]),'varsc':([15,38,],[28,48,]),'id':([15,38,46,70,99,122,167,],[29,29,86,103,138,86,180,]),'agregatipo':([17,18,19,],[32,33,34,]),'agregavar':([31,],[40,]),'bloque':([35,44,81,84,184,185,194,195,],[41,82,119,82,191,192,196,197,]),'funcionb':([36,87,],[43,123,]),'varsfunc':([36,87,],[45,45,]),'agregafunc':([37,],[47,]),'estatuto':([42,51,89,],[51,89,89,]),'asignacion':([42,51,89,],[53,53,53,]),'funcionvoid':([42,51,89,],[54,54,54,]),'retorno':([42,51,89,],[55,55,55,]),'lee':([42,51,89,],[56,56,56,]),'escritura':([42,51,89,],[57,57,57,]),'decision':([42,51,89,],[58,58,58,]),'repeticioncond':([42,51,89,],[59,59,59,]),'repeticionnocond':([42,51,89,],[60,60,60,]),'expresion':([42,51,63,89,92,94,95,98,100,101,102,129,135,169,],[61,61,96,61,128,130,131,137,139,141,142,128,163,182,]),'exp':([42,51,63,89,92,94,95,98,100,101,102,104,105,106,107,108,109,111,112,114,115,129,135,143,169,186,],[71,71,71,71,71,71,71,71,71,71,71,144,145,146,147,148,149,150,151,152,153,71,71,174,71,193,]),'termino':([42,51,63,89,92,94,95,98,100,101,102,104,105,106,107,108,109,111,112,114,115,129,135,143,169,186,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'factor':([42,51,63,89,92,94,95,98,100,101,102,104,105,106,107,108,109,111,112,114,115,129,135,143,169,186,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'cte':([42,51,63,74,76,89,92,94,95,98,100,101,102,104,105,106,107,108,109,111,112,114,115,129,135,143,169,186,],[75,75,75,116,118,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'funcionc':([44,84,],[80,121,]),'varsfuncb':([46,122,],[85,155,]),'bloqueb':([51,89,],[90,125,]),'asign':([62,97,126,],[93,136,156,]),'expb':([72,],[110,]),'terminob':([73,],[113,]),'asignacionb':([92,129,],[127,158,]),'leeb':([138,180,],[165,187,]),'escriturab':([139,140,181,182,],[168,171,188,189,]),'decisionb':([184,],[190,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAMA agregarfuncmain ID SEMICOL programab','programa',5,'p_programa','foreveralone.py',166),
  ('programab -> vars funcion programac','programab',3,'p_programab','foreveralone.py',170),
  ('programab -> programac','programab',1,'p_programab','foreveralone.py',171),
  ('programac -> PRINCIPAL LPAREN RPAREN bloque','programac',4,'p_programac','foreveralone.py',175),
  ('agregarfuncmain -> <empty>','agregarfuncmain',0,'p_agregarfuncmain','foreveralone.py',179),
  ('id -> ID agregavar','id',2,'p_id','foreveralone.py',192),
  ('id -> ID agregavar LBRACK NUMBER RBRACK','id',5,'p_id','foreveralone.py',193),
  ('tipovar -> INT agregatipo','tipovar',2,'p_tipovar','foreveralone.py',197),
  ('tipovar -> FLOAT agregatipo','tipovar',2,'p_tipovar','foreveralone.py',198),
  ('tipovar -> CHAR agregatipo','tipovar',2,'p_tipovar','foreveralone.py',199),
  ('tipofun -> INT','tipofun',1,'p_tipofun','foreveralone.py',203),
  ('tipofun -> FLOAT','tipofun',1,'p_tipofun','foreveralone.py',204),
  ('tipofun -> CHAR','tipofun',1,'p_tipofun','foreveralone.py',205),
  ('tipofun -> VOID','tipofun',1,'p_tipofun','foreveralone.py',206),
  ('agregatipo -> <empty>','agregatipo',0,'p_agregatipo','foreveralone.py',213),
  ('vars -> VAR varsb','vars',2,'p_vars','foreveralone.py',220),
  ('varsb -> tipovar varsc','varsb',2,'p_varsb','foreveralone.py',225),
  ('varsb -> empty','varsb',1,'p_varsb','foreveralone.py',226),
  ('varsc -> id COMMA varsc','varsc',3,'p_varsc','foreveralone.py',230),
  ('varsc -> id SEMICOL varsb','varsc',3,'p_varsc','foreveralone.py',231),
  ('varsc -> empty','varsc',1,'p_varsc','foreveralone.py',232),
  ('varsfunc -> tipovar varsfuncb','varsfunc',2,'p_varsfunc','foreveralone.py',236),
  ('varsfuncb -> id COMMA varsfuncb','varsfuncb',3,'p_varsfuncb','foreveralone.py',240),
  ('varsfuncb -> id','varsfuncb',1,'p_varsfuncb','foreveralone.py',241),
  ('funcion -> FUNCION ID LPAREN funcionb','funcion',4,'p_funcion','foreveralone.py',246),
  ('funcion -> FUNCION tipofun ID agregafunc LPAREN funcionb','funcion',6,'p_funcion','foreveralone.py',247),
  ('funcion -> empty','funcion',1,'p_funcion','foreveralone.py',248),
  ('agregafunc -> <empty>','agregafunc',0,'p_agregafunc','foreveralone.py',253),
  ('funcionb -> RPAREN funcionc','funcionb',2,'p_funcionb','foreveralone.py',264),
  ('funcionb -> varsfunc RPAREN funcionc','funcionb',3,'p_funcionb','foreveralone.py',265),
  ('funcionc -> vars bloque funcion','funcionc',3,'p_funcionc','foreveralone.py',269),
  ('funcionc -> bloque funcion','funcionc',2,'p_funcionc','foreveralone.py',270),
  ('funcionc -> empty','funcionc',1,'p_funcionc','foreveralone.py',271),
  ('bloque -> LBRACKET estatuto bloqueb','bloque',3,'p_bloque','foreveralone.py',275),
  ('bloque -> LBRACKET RBRACKET','bloque',2,'p_bloque','foreveralone.py',276),
  ('bloqueb -> RBRACKET','bloqueb',1,'p_bloqueb','foreveralone.py',280),
  ('bloqueb -> estatuto bloqueb','bloqueb',2,'p_bloqueb','foreveralone.py',281),
  ('asign -> LBRACK expresion RBRACK','asign',3,'p_asign','foreveralone.py',285),
  ('asign -> LBRACK CTEI RBRACK','asign',3,'p_asign','foreveralone.py',286),
  ('asign -> LBRACK CTEC RBRACK','asign',3,'p_asign','foreveralone.py',287),
  ('asignacion -> ID EQUAL asignacionb','asignacion',3,'p_asignacion','foreveralone.py',291),
  ('asignacion -> ID asign EQUAL asignacionb','asignacion',4,'p_asignacion','foreveralone.py',292),
  ('asignacionb -> expresion SEMICOL','asignacionb',2,'p_asignacionb','foreveralone.py',299),
  ('asignacionb -> ID asign SEMICOL','asignacionb',3,'p_asignacionb','foreveralone.py',300),
  ('retorno -> REGRESA LPAREN expresion RPAREN SEMICOL','retorno',5,'p_retorno','foreveralone.py',345),
  ('funcionvoid -> ID LPAREN expresion RPAREN SEMICOL','funcionvoid',5,'p_funcionvoid','foreveralone.py',349),
  ('lee -> LEE LPAREN id leeb','lee',4,'p_lee','foreveralone.py',353),
  ('leeb -> RPAREN SEMICOL','leeb',2,'p_leeb','foreveralone.py',357),
  ('leeb -> COMMA id leeb','leeb',3,'p_leeb','foreveralone.py',358),
  ('escritura -> ESCRIBE LPAREN expresion escriturab','escritura',4,'p_escritura','foreveralone.py',362),
  ('escritura -> ESCRIBE LPAREN STRING escriturab','escritura',4,'p_escritura','foreveralone.py',363),
  ('escriturab -> COMMA STRING escriturab','escriturab',3,'p_escriturab','foreveralone.py',367),
  ('escriturab -> COMMA expresion escriturab','escriturab',3,'p_escriturab','foreveralone.py',368),
  ('escriturab -> RPAREN SEMICOL','escriturab',2,'p_escriturab','foreveralone.py',369),
  ('decision -> SI LPAREN expresion RPAREN ENTONCES decisionb','decision',6,'p_decision','foreveralone.py',373),
  ('decisionb -> bloque','decisionb',1,'p_decisionb','foreveralone.py',377),
  ('decisionb -> bloque SINO bloque','decisionb',3,'p_decisionb','foreveralone.py',378),
  ('repeticioncond -> MIENTRAS LPAREN expresion RPAREN HAZ bloque','repeticioncond',6,'p_repeticioncond','foreveralone.py',382),
  ('repeticionnocond -> DESDE id EQUAL exp HASTA exp HACER bloque','repeticionnocond',8,'p_repeticionnocond','foreveralone.py',386),
  ('cte -> ID','cte',1,'p_cte','foreveralone.py',390),
  ('cte -> NUMBER','cte',1,'p_cte','foreveralone.py',391),
  ('cte -> CTEF','cte',1,'p_cte','foreveralone.py',392),
  ('cte -> CTEC','cte',1,'p_cte','foreveralone.py',393),
  ('cte -> STRING','cte',1,'p_cte','foreveralone.py',394),
  ('expresion -> exp','expresion',1,'p_expresion','foreveralone.py',425),
  ('expresion -> exp GTHAN exp','expresion',3,'p_expresion','foreveralone.py',426),
  ('expresion -> exp LTHAN exp','expresion',3,'p_expresion','foreveralone.py',427),
  ('expresion -> exp EQLOP exp','expresion',3,'p_expresion','foreveralone.py',428),
  ('expresion -> exp GEQUAL exp','expresion',3,'p_expresion','foreveralone.py',429),
  ('expresion -> exp LEQUAL exp','expresion',3,'p_expresion','foreveralone.py',430),
  ('expresion -> exp ABRACKET exp','expresion',3,'p_expresion','foreveralone.py',431),
  ('exp -> termino','exp',1,'p_exp','foreveralone.py',436),
  ('exp -> termino expb','exp',2,'p_exp','foreveralone.py',437),
  ('expb -> PLUS exp','expb',2,'p_expb','foreveralone.py',458),
  ('expb -> MINUS exp','expb',2,'p_expb','foreveralone.py',459),
  ('termino -> factor','termino',1,'p_termino','foreveralone.py',489),
  ('termino -> factor terminob','termino',2,'p_termino','foreveralone.py',490),
  ('terminob -> TIMES exp','terminob',2,'p_terminob','foreveralone.py',494),
  ('terminob -> DIVIDE exp','terminob',2,'p_terminob','foreveralone.py',495),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor','foreveralone.py',523),
  ('factor -> ID LPAREN expresion RPAREN','factor',4,'p_factor','foreveralone.py',524),
  ('factor -> PLUS cte','factor',2,'p_factor','foreveralone.py',525),
  ('factor -> MINUS cte','factor',2,'p_factor','foreveralone.py',526),
  ('factor -> cte','factor',1,'p_factor','foreveralone.py',527),
  ('factor -> ID asign','factor',2,'p_factor','foreveralone.py',528),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','foreveralone.py',533),
  ('estatuto -> funcionvoid','estatuto',1,'p_estatuto','foreveralone.py',534),
  ('estatuto -> retorno','estatuto',1,'p_estatuto','foreveralone.py',535),
  ('estatuto -> lee','estatuto',1,'p_estatuto','foreveralone.py',536),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','foreveralone.py',537),
  ('estatuto -> decision','estatuto',1,'p_estatuto','foreveralone.py',538),
  ('estatuto -> repeticioncond','estatuto',1,'p_estatuto','foreveralone.py',539),
  ('estatuto -> repeticionnocond','estatuto',1,'p_estatuto','foreveralone.py',540),
  ('estatuto -> expresion','estatuto',1,'p_estatuto','foreveralone.py',541),
  ('empty -> <empty>','empty',0,'p_empty','foreveralone.py',544),
  ('agregavar -> <empty>','agregavar',0,'p_agregavar','foreveralone.py',547),
]
