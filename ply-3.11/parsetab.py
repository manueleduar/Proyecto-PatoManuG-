
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COMILLA COMMA CTEC CTEF CTEI CTESTRING DETERMINANTE DIV ELSE END EQUALS FLOAT FOR FROM FUN GT GTE ID IF INT INVERSA LBRACKET LCURLY LPAREN LT LTE MAIN MINUS MUL NE OR PLUS PRINT PROGRAM RBRACKET RCURLY READ RETURN RPAREN SEMICOLON TO TRANSPUESTA VAR VOID WHILE\n        programa :  PROGRAM ID SEMICOLON addP programa1 \n        addP :\n\tprograma1 : vars modules programa2\n\tprograma1 : vars modules\n\t          | programa2\n\t\n\tprograma2 :  main\n\t\n\tmain : MAIN LPAREN param RPAREN LCURLY vars statement RCURLY END\n\t\n    tipo : INT guardaTipoVar\n         | FLOAT guardaTipoVar\n         | CHAR guardaTipoVar \n    guardaTipoVar : \n    vars : var \n         | empty\n    \n    var : VAR var2 \n    \n        var1 : ID\n            | ID COMMA var1 addV saveId\n            | ID arr \n            | ID arr COMMA var1 addV saveId\n            | ID mat COMMA var1 addV saveId\n            | ID mat \n            | ID mat especial \n            | empty \n    addV :\n        var2 : var2 tipo var1 SEMICOLON addV saveId\n             | empty\n    \n    especial : TRANSPUESTA\n             | INVERSA\n             | DETERMINANTE\n    \n    arr : LBRACKET CTEI RBRACKET\n        | LBRACKET exp RBRACKET \n    \n    \n    mat : LBRACKET CTEI RBRACKET LBRACKET CTEI RBRACKET\n        | LBRACKET exp RBRACKET LBRACKET exp RBRACKET\n        | LBRACKET exp RBRACKET LBRACKET CTEI RBRACKET\n        | LBRACKET CTEI RBRACKET LBRACKET exp RBRACKET\n    \n    modules : function modules\n            | empty\n    \n     save_fun : \n    function : FUN VOID function1 \n             | FUN INT function2 \n             | FUN CHAR function2 \n             | FUN FLOAT function2 \n    \n    function1 : ID save_fun LPAREN param RPAREN SEMICOLON LCURLY vars statement RCURLY \n    \n    function2 : ID save_fun LPAREN param RPAREN SEMICOLON LCURLY vars statement RETURN exp SEMICOLON RCURLY \n    \n    statement :  statement1 statement\n              | empty\n    \n    statement1 : asignacion SEMICOLON\n               | llamada SEMICOLON\n               | lectura SEMICOLON\n               | escritura SEMICOLON\n               | for\n               | if\n               | while\n    \n    asignacion : ID EQUALS exp\n               | ID arr EQUALS exp\n               | ID mat EQUALS exp\n    \n    param : tipo param1  \n          | empty\n    \n    \n    param1 : ID\n           | ID COMMA param1\n           | empty \n    \n    llamada : ID LPAREN exp RPAREN\n    \n    if : IF LPAREN exp RPAREN LCURLY statement RCURLY\n       | IF LPAREN exp RPAREN LCURLY statement RCURLY else\n    \n    else : ELSE LCURLY statement RCURLY\n         | empty\n    \n    for : FOR LPAREN for1 RPAREN LCURLY statement RCURLY\n    \n    for1 : FROM asignacion TO exp\n    \n    while : WHILE LPAREN exp RPAREN LCURLY statement RCURLY\n    \n    escritura : PRINT LPAREN escritura1 RPAREN\n    \n    escritura1 : escritura2 COMMA escritura2\n               | escritura2\n    \n    escritura2 : CTESTRING  \n               | CTEI\n               | CTEF \n               | exp\n    \n    lectura : READ LPAREN var1 RPAREN\n    \n    exp : nexp  \n        | nexp  OR saveOperator nexp \n    \n    nexp : compexp\n         | compexp  AND saveOperator compexp \n    \n    compexp : sumexp \n            | compexp1 sumexp\n    \n    compexp1 : sumexp   GT saveOperator sumexp \n             | sumexp  LT saveOperator sumexp \n             | sumexp  GTE saveOperator sumexp \n             | sumexp  LTE saveOperator sumexp \n             | sumexp  NE saveOperator sumexp \n    \n    sumexp : mulexp  \n           | mulexp PLUS saveOperator mulexp\n           | mulexp MINUS saveOperator mulexp\n    \n    mulexp : pexp  \n           | pexp MUL saveOperator pexp\n           | pexp DIV saveOperator pexp\n    \n    pexp : var1  \n         | CTEI\n         | CTEF\n         | CTEC\n         | llamada\n         | LPAREN exp RPAREN\n    \n    empty :\n    saveId : saveOperator : '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,4,5,6,7,8,9,10,11,12,14,15,16,18,19,21,22,34,36,38,39,52,61,87,178,222,233,],[0,-2,-100,-1,-100,-5,-12,-13,-6,-100,-4,-100,-36,-14,-25,-3,-35,-38,-39,-40,-41,-23,-101,-24,-7,-42,-43,]),'ID':([2,9,10,12,18,19,23,24,25,26,27,28,29,30,32,41,42,43,44,45,52,53,54,55,56,57,58,61,62,63,64,65,66,67,68,74,75,76,77,78,79,80,81,82,83,87,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,107,109,115,116,117,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,146,147,148,149,150,153,154,156,157,160,161,168,169,170,171,172,173,174,175,176,177,180,181,190,193,194,195,196,197,198,203,209,210,212,213,214,215,223,224,225,226,228,230,232,235,],[3,-12,-13,-100,-14,-25,35,37,37,37,41,-11,-11,-11,48,-15,-22,-8,-9,-10,-23,41,-17,-20,82,-100,48,-101,-23,41,41,-21,-26,-27,-28,82,-88,-91,-94,-96,-97,-98,82,-15,118,-24,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-95,-102,-102,-102,-102,82,118,-50,-51,-52,-16,-101,-101,82,82,82,82,82,82,82,82,82,82,82,82,82,-99,-46,-47,-48,-49,82,41,82,82,82,-18,-19,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,82,82,206,-100,-100,-31,-34,-32,-33,82,118,118,118,82,118,118,82,-66,-62,-68,-63,-65,118,-64,]),'SEMICOLON':([3,27,28,29,30,40,41,42,43,44,45,53,54,55,62,63,64,65,66,67,68,71,72,73,74,75,76,77,78,79,80,82,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,111,112,113,114,124,125,126,127,128,131,132,133,134,135,136,137,138,139,140,141,142,150,160,161,166,167,168,169,170,171,172,173,174,175,176,177,179,180,181,195,196,197,198,199,200,201,202,223,227,],[4,-100,-11,-11,-11,52,-15,-22,-8,-9,-10,-100,-17,-20,-23,-100,-100,-21,-26,-27,-28,-77,-79,-81,-100,-88,-91,-94,-96,-97,-98,-15,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-82,-95,-102,-102,-102,-102,146,147,148,149,158,159,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-18,-19,-78,-80,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,-53,-100,-100,-31,-34,-32,-33,-54,-55,-76,-69,-100,231,]),'VAR':([4,5,57,193,194,],[-2,12,12,12,12,]),'MAIN':([4,5,7,9,10,12,14,15,16,18,19,22,34,36,38,39,52,61,87,222,233,],[-2,13,-100,-12,-13,-100,13,-100,-36,-14,-25,-35,-38,-39,-40,-41,-23,-101,-24,-42,-43,]),'FUN':([4,5,7,9,10,12,15,18,19,34,36,38,39,52,61,87,222,233,],[-2,-100,17,-12,-13,-100,17,-14,-25,-38,-39,-40,-41,-23,-101,-24,-42,-43,]),'READ':([9,10,12,18,19,52,57,61,83,87,109,115,116,117,146,147,148,149,193,194,209,210,212,214,215,224,225,226,228,230,232,235,],[-12,-13,-100,-14,-25,-23,-100,-101,119,-24,119,-50,-51,-52,-46,-47,-48,-49,-100,-100,119,119,119,119,119,-66,-62,-68,-63,-65,119,-64,]),'PRINT':([9,10,12,18,19,52,57,61,83,87,109,115,116,117,146,147,148,149,193,194,209,210,212,214,215,224,225,226,228,230,232,235,],[-12,-13,-100,-14,-25,-23,-100,-101,120,-24,120,-50,-51,-52,-46,-47,-48,-49,-100,-100,120,120,120,120,120,-66,-62,-68,-63,-65,120,-64,]),'FOR':([9,10,12,18,19,52,57,61,83,87,109,115,116,117,146,147,148,149,193,194,209,210,212,214,215,224,225,226,228,230,232,235,],[-12,-13,-100,-14,-25,-23,-100,-101,121,-24,121,-50,-51,-52,-46,-47,-48,-49,-100,-100,121,121,121,121,121,-66,-62,-68,-63,-65,121,-64,]),'IF':([9,10,12,18,19,52,57,61,83,87,109,115,116,117,146,147,148,149,193,194,209,210,212,214,215,224,225,226,228,230,232,235,],[-12,-13,-100,-14,-25,-23,-100,-101,122,-24,122,-50,-51,-52,-46,-47,-48,-49,-100,-100,122,122,122,122,122,-66,-62,-68,-63,-65,122,-64,]),'WHILE':([9,10,12,18,19,52,57,61,83,87,109,115,116,117,146,147,148,149,193,194,209,210,212,214,215,224,225,226,228,230,232,235,],[-12,-13,-100,-14,-25,-23,-100,-101,123,-24,123,-50,-51,-52,-46,-47,-48,-49,-100,-100,123,123,123,123,123,-66,-62,-68,-63,-65,123,-64,]),'RCURLY':([9,10,12,18,19,52,57,61,83,87,108,109,110,115,116,117,145,146,147,148,149,193,209,212,214,215,216,218,220,221,224,225,226,228,230,231,232,234,235,],[-12,-13,-100,-14,-25,-23,-100,-101,-100,-24,144,-100,-45,-50,-51,-52,-44,-46,-47,-48,-49,-100,-100,-100,-100,-100,222,224,225,226,-66,-62,-68,-63,-65,233,-100,235,-64,]),'RETURN':([9,10,12,18,19,52,61,87,109,110,115,116,117,145,146,147,148,149,194,210,217,224,225,226,228,230,235,],[-12,-13,-100,-14,-25,-23,-101,-24,-100,-45,-50,-51,-52,-44,-46,-47,-48,-49,-100,-100,223,-66,-62,-68,-63,-65,-64,]),'INT':([12,17,18,19,20,52,59,60,61,87,],[-100,24,28,-25,28,-23,28,28,-101,-24,]),'FLOAT':([12,17,18,19,20,52,59,60,61,87,],[-100,26,29,-25,29,-23,29,29,-101,-24,]),'CHAR':([12,17,18,19,20,52,59,60,61,87,],[-100,25,30,-25,30,-23,30,30,-101,-24,]),'LPAREN':([13,35,37,41,42,50,51,53,54,55,56,62,63,64,65,66,67,68,74,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,107,118,119,120,121,122,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,154,156,157,160,161,168,169,170,171,172,173,174,175,176,177,180,181,195,196,197,198,203,213,223,],[20,-37,-37,-15,-22,59,60,-100,-17,-20,81,-23,-100,-100,-21,-26,-27,-28,81,-88,-91,-94,-96,-97,-98,81,107,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-95,-102,-102,-102,-102,81,107,153,154,155,156,157,-16,-101,-101,81,81,81,81,81,81,81,81,81,81,81,81,81,-99,81,81,81,81,-18,-19,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,81,81,-31,-34,-32,-33,81,81,81,]),'VOID':([17,],[23,]),'RPAREN':([20,28,29,30,31,32,33,41,42,43,44,45,47,48,49,53,54,55,58,59,60,62,63,64,65,66,67,68,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,126,127,128,131,132,133,134,135,136,137,138,139,140,141,142,143,153,154,156,157,160,161,166,167,168,169,170,171,172,173,174,175,176,177,182,183,184,185,186,187,188,189,191,192,195,196,197,198,203,211,213,219,],[-100,-11,-11,-11,46,-100,-57,-15,-22,-8,-9,-10,-56,-58,-60,-100,-17,-20,-100,-100,-100,-23,-100,-100,-21,-26,-27,-28,-77,-79,-81,-100,-88,-91,-94,-96,-97,-98,-100,-15,-59,124,125,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-82,-95,-102,-102,-102,-102,142,-100,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-99,177,-100,-100,-100,-100,-18,-19,-78,-80,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,201,202,-71,-72,-73,-74,-75,204,207,208,-31,-34,-32,-33,-100,-70,-100,-67,]),'MUL':([41,42,53,54,55,56,62,63,64,65,66,67,68,69,74,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,107,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,154,156,157,160,161,162,165,168,169,170,171,172,173,174,175,176,177,180,181,186,187,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,-100,-23,-100,-100,-21,-26,-27,-28,-95,-100,-88,104,-94,-96,-97,-98,-100,-15,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-95,-102,-102,-102,-102,-100,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-100,-100,-100,-18,-19,-95,-95,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,-100,-100,-95,-96,-31,-34,-32,-33,-100,-100,-100,]),'DIV':([41,42,53,54,55,56,62,63,64,65,66,67,68,69,74,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,107,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,154,156,157,160,161,162,165,168,169,170,171,172,173,174,175,176,177,180,181,186,187,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,-100,-23,-100,-100,-21,-26,-27,-28,-95,-100,-88,105,-94,-96,-97,-98,-100,-15,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-95,-102,-102,-102,-102,-100,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-100,-100,-100,-18,-19,-95,-95,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,-100,-100,-95,-96,-31,-34,-32,-33,-100,-100,-100,]),'PLUS':([41,42,53,54,55,56,62,63,64,65,66,67,68,69,74,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,107,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,154,156,157,160,161,162,165,168,169,170,171,172,173,174,175,176,177,180,181,186,187,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,-100,-23,-100,-100,-21,-26,-27,-28,-95,-100,102,-91,-94,-96,-97,-98,-100,-15,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-95,-102,-102,-102,-102,-100,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-100,-100,-100,-18,-19,-95,-95,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,-100,-100,-95,-96,-31,-34,-32,-33,-100,-100,-100,]),'MINUS':([41,42,53,54,55,56,62,63,64,65,66,67,68,69,74,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,107,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,154,156,157,160,161,162,165,168,169,170,171,172,173,174,175,176,177,180,181,186,187,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,-100,-23,-100,-100,-21,-26,-27,-28,-95,-100,103,-91,-94,-96,-97,-98,-100,-15,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-95,-102,-102,-102,-102,-100,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-100,-100,-100,-18,-19,-95,-95,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,-100,-100,-95,-96,-31,-34,-32,-33,-100,-100,-100,]),'GT':([41,42,53,54,55,56,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,101,102,103,104,105,107,126,127,128,129,130,131,132,138,139,140,141,142,150,154,156,157,160,161,162,165,173,174,175,176,177,180,181,186,187,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,-100,-23,-100,-100,-21,-26,-27,-28,-95,95,-88,-91,-94,-96,-97,-98,-100,-15,-101,-23,-23,-29,-30,-102,-102,-95,-102,-102,-102,-102,-100,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-100,-100,-100,-18,-19,-95,-95,-89,-90,-92,-93,-61,-100,-100,-95,-96,-31,-34,-32,-33,-100,-100,-100,]),'LT':([41,42,53,54,55,56,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,101,102,103,104,105,107,126,127,128,129,130,131,132,138,139,140,141,142,150,154,156,157,160,161,162,165,173,174,175,176,177,180,181,186,187,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,-100,-23,-100,-100,-21,-26,-27,-28,-95,96,-88,-91,-94,-96,-97,-98,-100,-15,-101,-23,-23,-29,-30,-102,-102,-95,-102,-102,-102,-102,-100,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-100,-100,-100,-18,-19,-95,-95,-89,-90,-92,-93,-61,-100,-100,-95,-96,-31,-34,-32,-33,-100,-100,-100,]),'GTE':([41,42,53,54,55,56,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,101,102,103,104,105,107,126,127,128,129,130,131,132,138,139,140,141,142,150,154,156,157,160,161,162,165,173,174,175,176,177,180,181,186,187,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,-100,-23,-100,-100,-21,-26,-27,-28,-95,97,-88,-91,-94,-96,-97,-98,-100,-15,-101,-23,-23,-29,-30,-102,-102,-95,-102,-102,-102,-102,-100,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-100,-100,-100,-18,-19,-95,-95,-89,-90,-92,-93,-61,-100,-100,-95,-96,-31,-34,-32,-33,-100,-100,-100,]),'LTE':([41,42,53,54,55,56,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,101,102,103,104,105,107,126,127,128,129,130,131,132,138,139,140,141,142,150,154,156,157,160,161,162,165,173,174,175,176,177,180,181,186,187,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,-100,-23,-100,-100,-21,-26,-27,-28,-95,98,-88,-91,-94,-96,-97,-98,-100,-15,-101,-23,-23,-29,-30,-102,-102,-95,-102,-102,-102,-102,-100,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-100,-100,-100,-18,-19,-95,-95,-89,-90,-92,-93,-61,-100,-100,-95,-96,-31,-34,-32,-33,-100,-100,-100,]),'NE':([41,42,53,54,55,56,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,101,102,103,104,105,107,126,127,128,129,130,131,132,138,139,140,141,142,150,154,156,157,160,161,162,165,173,174,175,176,177,180,181,186,187,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,-100,-23,-100,-100,-21,-26,-27,-28,-95,99,-88,-91,-94,-96,-97,-98,-100,-15,-101,-23,-23,-29,-30,-102,-102,-95,-102,-102,-102,-102,-100,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-100,-100,-100,-18,-19,-95,-95,-89,-90,-92,-93,-61,-100,-100,-95,-96,-31,-34,-32,-33,-100,-100,-100,]),'AND':([41,42,53,54,55,56,62,63,64,65,66,67,68,69,72,73,74,75,76,77,78,79,80,81,82,88,89,90,91,92,93,95,96,97,98,99,100,101,102,103,104,105,107,126,127,128,129,130,131,133,134,135,136,137,138,139,140,141,142,150,154,156,157,160,161,162,165,168,169,170,171,172,173,174,175,176,177,180,181,186,187,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,-100,-23,-100,-100,-21,-26,-27,-28,-95,94,-81,-100,-88,-91,-94,-96,-97,-98,-100,-15,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-82,-95,-102,-102,-102,-102,-100,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-100,-100,-100,-18,-19,-95,-95,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,-100,-100,-95,-96,-31,-34,-32,-33,-100,-100,-100,]),'OR':([41,42,53,54,55,56,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,88,89,90,91,92,94,95,96,97,98,99,100,101,102,103,104,105,107,126,127,128,129,130,132,133,134,135,136,137,138,139,140,141,142,150,154,156,157,160,161,162,165,167,168,169,170,171,172,173,174,175,176,177,180,181,186,187,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,-100,-23,-100,-100,-21,-26,-27,-28,-95,93,-79,-81,-100,-88,-91,-94,-96,-97,-98,-100,-15,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-82,-95,-102,-102,-102,-102,-100,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-100,-100,-100,-18,-19,-95,-95,-80,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,-100,-100,-95,-96,-31,-34,-32,-33,-100,-100,-100,]),'RBRACKET':([41,42,53,54,55,56,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,195,196,197,198,],[-15,-22,-100,-17,-20,-100,-23,-100,-100,-21,-26,-27,-28,91,92,-77,-79,-81,-100,-88,-91,-94,-96,-97,-98,-15,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-82,-95,-102,-102,-102,-102,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-99,-18,-19,195,196,197,198,-78,-80,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,-31,-34,-32,-33,]),'TO':([41,42,53,54,55,62,63,64,65,66,67,68,71,72,73,74,75,76,77,78,79,80,82,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,126,127,128,131,132,133,134,135,136,137,138,139,140,141,142,150,160,161,166,167,168,169,170,171,172,173,174,175,176,177,179,180,181,195,196,197,198,199,200,205,],[-15,-22,-100,-17,-20,-23,-100,-100,-21,-26,-27,-28,-77,-79,-81,-100,-88,-91,-94,-96,-97,-98,-15,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-82,-95,-102,-102,-102,-102,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-18,-19,-78,-80,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,-53,-100,-100,-31,-34,-32,-33,-54,-55,213,]),'COMMA':([41,42,48,53,54,55,62,63,64,65,66,67,68,71,72,73,74,75,76,77,78,79,80,82,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,126,127,128,131,132,133,134,135,136,137,138,139,140,141,142,154,160,161,166,167,168,169,170,171,172,173,174,175,176,177,184,185,186,187,188,195,196,197,198,],[53,-22,58,-100,63,64,-23,-100,-100,-21,-26,-27,-28,-77,-79,-81,-100,-88,-91,-94,-96,-97,-98,53,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-82,-95,-102,-102,-102,-102,-16,-101,-101,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-99,-100,-18,-19,-78,-80,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,203,-72,-73,-74,-75,-31,-34,-32,-33,]),'CTEI':([41,42,53,54,55,56,62,63,64,65,66,67,68,74,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,107,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,154,156,157,160,161,168,169,170,171,172,173,174,175,176,177,180,181,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,69,-23,-100,-100,-21,-26,-27,-28,101,-88,-91,-94,-96,-97,-98,101,-15,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-95,-102,-102,-102,-102,101,-16,-101,-101,162,165,101,101,101,101,101,101,101,101,101,101,101,-99,101,186,101,101,-18,-19,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,101,101,-31,-34,-32,-33,186,101,101,]),'CTEF':([41,42,53,54,55,56,62,63,64,65,66,67,68,74,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,107,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,154,156,157,160,161,168,169,170,171,172,173,174,175,176,177,180,181,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,78,-23,-100,-100,-21,-26,-27,-28,78,-88,-91,-94,-96,-97,-98,78,-15,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-95,-102,-102,-102,-102,78,-16,-101,-101,78,78,78,78,78,78,78,78,78,78,78,78,78,-99,78,187,78,78,-18,-19,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,78,78,-31,-34,-32,-33,187,78,78,]),'CTEC':([41,42,53,54,55,56,62,63,64,65,66,67,68,74,75,76,77,78,79,80,81,82,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,107,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,154,156,157,160,161,168,169,170,171,172,173,174,175,176,177,180,181,195,196,197,198,203,213,223,],[-15,-22,-100,-17,-20,79,-23,-100,-100,-21,-26,-27,-28,79,-88,-91,-94,-96,-97,-98,79,-15,-101,-23,-23,-29,-30,-102,-102,-102,-102,-102,-102,-102,-95,-102,-102,-102,-102,79,-16,-101,-101,79,79,79,79,79,79,79,79,79,79,79,79,79,-99,79,79,79,79,-18,-19,-83,-84,-85,-86,-87,-89,-90,-92,-93,-61,79,79,-31,-34,-32,-33,79,79,79,]),'LBRACKET':([41,82,91,92,118,206,],[56,56,129,130,56,56,]),'LCURLY':([46,158,159,204,207,208,229,],[57,193,194,212,214,215,232,]),'TRANSPUESTA':([55,195,196,197,198,],[66,-31,-34,-32,-33,]),'INVERSA':([55,195,196,197,198,],[67,-31,-34,-32,-33,]),'DETERMINANTE':([55,195,196,197,198,],[68,-31,-34,-32,-33,]),'EQUALS':([91,92,118,151,152,195,196,197,198,206,],[-29,-30,150,180,181,-31,-34,-32,-33,150,]),'END':([144,],[178,]),'CTESTRING':([154,203,],[185,185,]),'FROM':([155,],[190,]),'ELSE':([225,],[229,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'addP':([4,],[5,]),'programa1':([5,],[6,]),'vars':([5,57,193,194,],[7,83,209,210,]),'programa2':([5,14,],[8,21,]),'var':([5,57,193,194,],[9,9,9,9,]),'empty':([5,7,12,15,20,27,32,53,56,57,58,59,60,63,64,74,81,83,107,109,129,130,131,132,133,134,135,136,137,138,139,140,141,150,153,154,156,157,180,181,193,194,203,209,210,212,213,214,215,223,225,232,],[10,16,19,16,33,42,49,42,42,10,49,33,33,42,42,42,42,110,42,110,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,10,10,42,110,110,110,42,110,110,42,230,110,]),'main':([5,14,],[11,11,]),'modules':([7,15,],[14,22,]),'function':([7,15,],[15,15,]),'var2':([12,],[18,]),'tipo':([18,20,59,60,],[27,32,32,32,]),'param':([20,59,60,],[31,85,86,]),'function1':([23,],[34,]),'function2':([24,25,26,],[36,38,39,]),'var1':([27,53,56,63,64,74,81,107,129,130,131,132,133,134,135,136,137,138,139,140,141,150,153,154,156,157,180,181,203,213,223,],[40,62,77,89,90,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,182,77,77,77,77,77,77,77,77,]),'guardaTipoVar':([28,29,30,],[43,44,45,]),'param1':([32,58,],[47,84,]),'save_fun':([35,37,],[50,51,]),'arr':([41,82,118,206,],[54,54,151,151,]),'mat':([41,82,118,206,],[55,55,152,152,]),'addV':([52,62,89,90,],[61,88,127,128,]),'especial':([55,],[65,]),'exp':([56,81,107,129,130,150,154,156,157,180,181,203,213,223,],[70,106,143,163,164,179,188,191,192,199,200,188,219,227,]),'nexp':([56,81,107,129,130,131,150,154,156,157,180,181,203,213,223,],[71,71,71,71,71,166,71,71,71,71,71,71,71,71,71,]),'compexp':([56,81,107,129,130,131,132,150,154,156,157,180,181,203,213,223,],[72,72,72,72,72,72,167,72,72,72,72,72,72,72,72,72,]),'sumexp':([56,74,81,107,129,130,131,132,133,134,135,136,137,150,154,156,157,180,181,203,213,223,],[73,100,73,73,73,73,73,73,168,169,170,171,172,73,73,73,73,73,73,73,73,73,]),'compexp1':([56,81,107,129,130,131,132,150,154,156,157,180,181,203,213,223,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'mulexp':([56,74,81,107,129,130,131,132,133,134,135,136,137,138,139,150,154,156,157,180,181,203,213,223,],[75,75,75,75,75,75,75,75,75,75,75,75,75,173,174,75,75,75,75,75,75,75,75,75,]),'pexp':([56,74,81,107,129,130,131,132,133,134,135,136,137,138,139,140,141,150,154,156,157,180,181,203,213,223,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,175,176,76,76,76,76,76,76,76,76,76,]),'llamada':([56,74,81,83,107,109,129,130,131,132,133,134,135,136,137,138,139,140,141,150,154,156,157,180,181,203,209,210,212,213,214,215,223,232,],[80,80,80,112,80,112,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,112,112,112,80,112,112,80,112,]),'saveId':([61,88,127,128,],[87,126,160,161,]),'statement':([83,109,209,210,212,214,215,232,],[108,145,216,217,218,220,221,234,]),'statement1':([83,109,209,210,212,214,215,232,],[109,109,109,109,109,109,109,109,]),'asignacion':([83,109,190,209,210,212,214,215,232,],[111,111,205,111,111,111,111,111,111,]),'lectura':([83,109,209,210,212,214,215,232,],[113,113,113,113,113,113,113,113,]),'escritura':([83,109,209,210,212,214,215,232,],[114,114,114,114,114,114,114,114,]),'for':([83,109,209,210,212,214,215,232,],[115,115,115,115,115,115,115,115,]),'if':([83,109,209,210,212,214,215,232,],[116,116,116,116,116,116,116,116,]),'while':([83,109,209,210,212,214,215,232,],[117,117,117,117,117,117,117,117,]),'saveOperator':([93,94,95,96,97,98,99,102,103,104,105,],[131,132,133,134,135,136,137,138,139,140,141,]),'escritura1':([154,],[183,]),'escritura2':([154,203,],[184,211,]),'for1':([155,],[189,]),'else':([225,],[228,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID SEMICOLON addP programa1','programa',5,'p_programa','main.py',136),
  ('addP -> <empty>','addP',0,'p_addP','main.py',142),
  ('programa1 -> vars modules programa2','programa1',3,'p_programa1','main.py',160),
  ('programa1 -> vars modules','programa1',2,'p_programa1','main.py',161),
  ('programa1 -> programa2','programa1',1,'p_programa1','main.py',162),
  ('programa2 -> main','programa2',1,'p_programa2','main.py',167),
  ('main -> MAIN LPAREN param RPAREN LCURLY vars statement RCURLY END','main',9,'p_main','main.py',172),
  ('tipo -> INT guardaTipoVar','tipo',2,'p_tipo','main.py',188),
  ('tipo -> FLOAT guardaTipoVar','tipo',2,'p_tipo','main.py',189),
  ('tipo -> CHAR guardaTipoVar','tipo',2,'p_tipo','main.py',190),
  ('guardaTipoVar -> <empty>','guardaTipoVar',0,'p_guardaTipoVar','main.py',195),
  ('vars -> var','vars',1,'p_vars','main.py',202),
  ('vars -> empty','vars',1,'p_vars','main.py',203),
  ('var -> VAR var2','var',2,'p_var','main.py',208),
  ('var1 -> ID','var1',1,'p_var1','main.py',214),
  ('var1 -> ID COMMA var1 addV saveId','var1',5,'p_var1','main.py',215),
  ('var1 -> ID arr','var1',2,'p_var1','main.py',216),
  ('var1 -> ID arr COMMA var1 addV saveId','var1',6,'p_var1','main.py',217),
  ('var1 -> ID mat COMMA var1 addV saveId','var1',6,'p_var1','main.py',218),
  ('var1 -> ID mat','var1',2,'p_var1','main.py',219),
  ('var1 -> ID mat especial','var1',3,'p_var1','main.py',220),
  ('var1 -> empty','var1',1,'p_var1','main.py',221),
  ('addV -> <empty>','addV',0,'p_addV','main.py',230),
  ('var2 -> var2 tipo var1 SEMICOLON addV saveId','var2',6,'p_var2','main.py',250),
  ('var2 -> empty','var2',1,'p_var2','main.py',251),
  ('especial -> TRANSPUESTA','especial',1,'p_especial','main.py',257),
  ('especial -> INVERSA','especial',1,'p_especial','main.py',258),
  ('especial -> DETERMINANTE','especial',1,'p_especial','main.py',259),
  ('arr -> LBRACKET CTEI RBRACKET','arr',3,'p_arr','main.py',264),
  ('arr -> LBRACKET exp RBRACKET','arr',3,'p_arr','main.py',265),
  ('mat -> LBRACKET CTEI RBRACKET LBRACKET CTEI RBRACKET','mat',6,'p_mat','main.py',271),
  ('mat -> LBRACKET exp RBRACKET LBRACKET exp RBRACKET','mat',6,'p_mat','main.py',272),
  ('mat -> LBRACKET exp RBRACKET LBRACKET CTEI RBRACKET','mat',6,'p_mat','main.py',273),
  ('mat -> LBRACKET CTEI RBRACKET LBRACKET exp RBRACKET','mat',6,'p_mat','main.py',274),
  ('modules -> function modules','modules',2,'p_modules','main.py',280),
  ('modules -> empty','modules',1,'p_modules','main.py',281),
  ('save_fun -> <empty>','save_fun',0,'p_save_fun','main.py',286),
  ('function -> FUN VOID function1','function',3,'p_function','main.py',308),
  ('function -> FUN INT function2','function',3,'p_function','main.py',309),
  ('function -> FUN CHAR function2','function',3,'p_function','main.py',310),
  ('function -> FUN FLOAT function2','function',3,'p_function','main.py',311),
  ('function1 -> ID save_fun LPAREN param RPAREN SEMICOLON LCURLY vars statement RCURLY','function1',10,'p_function1','main.py',317),
  ('function2 -> ID save_fun LPAREN param RPAREN SEMICOLON LCURLY vars statement RETURN exp SEMICOLON RCURLY','function2',13,'p_function2','main.py',322),
  ('statement -> statement1 statement','statement',2,'p_statement','main.py',327),
  ('statement -> empty','statement',1,'p_statement','main.py',328),
  ('statement1 -> asignacion SEMICOLON','statement1',2,'p_statement1','main.py',334),
  ('statement1 -> llamada SEMICOLON','statement1',2,'p_statement1','main.py',335),
  ('statement1 -> lectura SEMICOLON','statement1',2,'p_statement1','main.py',336),
  ('statement1 -> escritura SEMICOLON','statement1',2,'p_statement1','main.py',337),
  ('statement1 -> for','statement1',1,'p_statement1','main.py',338),
  ('statement1 -> if','statement1',1,'p_statement1','main.py',339),
  ('statement1 -> while','statement1',1,'p_statement1','main.py',340),
  ('asignacion -> ID EQUALS exp','asignacion',3,'p_asignacion','main.py',347),
  ('asignacion -> ID arr EQUALS exp','asignacion',4,'p_asignacion','main.py',348),
  ('asignacion -> ID mat EQUALS exp','asignacion',4,'p_asignacion','main.py',349),
  ('param -> tipo param1','param',2,'p_param','main.py',355),
  ('param -> empty','param',1,'p_param','main.py',356),
  ('param1 -> ID','param1',1,'p_param1','main.py',362),
  ('param1 -> ID COMMA param1','param1',3,'p_param1','main.py',363),
  ('param1 -> empty','param1',1,'p_param1','main.py',364),
  ('llamada -> ID LPAREN exp RPAREN','llamada',4,'p_llamada','main.py',371),
  ('if -> IF LPAREN exp RPAREN LCURLY statement RCURLY','if',7,'p_if','main.py',376),
  ('if -> IF LPAREN exp RPAREN LCURLY statement RCURLY else','if',8,'p_if','main.py',377),
  ('else -> ELSE LCURLY statement RCURLY','else',4,'p_else','main.py',382),
  ('else -> empty','else',1,'p_else','main.py',383),
  ('for -> FOR LPAREN for1 RPAREN LCURLY statement RCURLY','for',7,'p_for','main.py',387),
  ('for1 -> FROM asignacion TO exp','for1',4,'p_for1','main.py',391),
  ('while -> WHILE LPAREN exp RPAREN LCURLY statement RCURLY','while',7,'p_while','main.py',395),
  ('escritura -> PRINT LPAREN escritura1 RPAREN','escritura',4,'p_escritura','main.py',400),
  ('escritura1 -> escritura2 COMMA escritura2','escritura1',3,'p_escritura1','main.py',404),
  ('escritura1 -> escritura2','escritura1',1,'p_escritura1','main.py',405),
  ('escritura2 -> CTESTRING','escritura2',1,'p_escritura2','main.py',409),
  ('escritura2 -> CTEI','escritura2',1,'p_escritura2','main.py',410),
  ('escritura2 -> CTEF','escritura2',1,'p_escritura2','main.py',411),
  ('escritura2 -> exp','escritura2',1,'p_escritura2','main.py',412),
  ('lectura -> READ LPAREN var1 RPAREN','lectura',4,'p_lectura','main.py',417),
  ('exp -> nexp','exp',1,'p_exp','main.py',423),
  ('exp -> nexp OR saveOperator nexp','exp',4,'p_exp','main.py',424),
  ('nexp -> compexp','nexp',1,'p_nexp','main.py',430),
  ('nexp -> compexp AND saveOperator compexp','nexp',4,'p_nexp','main.py',431),
  ('compexp -> sumexp','compexp',1,'p_compexp','main.py',437),
  ('compexp -> compexp1 sumexp','compexp',2,'p_compexp','main.py',438),
  ('compexp1 -> sumexp GT saveOperator sumexp','compexp1',4,'p_compexp1','main.py',445),
  ('compexp1 -> sumexp LT saveOperator sumexp','compexp1',4,'p_compexp1','main.py',446),
  ('compexp1 -> sumexp GTE saveOperator sumexp','compexp1',4,'p_compexp1','main.py',447),
  ('compexp1 -> sumexp LTE saveOperator sumexp','compexp1',4,'p_compexp1','main.py',448),
  ('compexp1 -> sumexp NE saveOperator sumexp','compexp1',4,'p_compexp1','main.py',449),
  ('sumexp -> mulexp','sumexp',1,'p_sumexp','main.py',457),
  ('sumexp -> mulexp PLUS saveOperator mulexp','sumexp',4,'p_sumexp','main.py',458),
  ('sumexp -> mulexp MINUS saveOperator mulexp','sumexp',4,'p_sumexp','main.py',459),
  ('mulexp -> pexp','mulexp',1,'p_mulexp','main.py',466),
  ('mulexp -> pexp MUL saveOperator pexp','mulexp',4,'p_mulexp','main.py',467),
  ('mulexp -> pexp DIV saveOperator pexp','mulexp',4,'p_mulexp','main.py',468),
  ('pexp -> var1','pexp',1,'p_pexp','main.py',474),
  ('pexp -> CTEI','pexp',1,'p_pexp','main.py',475),
  ('pexp -> CTEF','pexp',1,'p_pexp','main.py',476),
  ('pexp -> CTEC','pexp',1,'p_pexp','main.py',477),
  ('pexp -> llamada','pexp',1,'p_pexp','main.py',478),
  ('pexp -> LPAREN exp RPAREN','pexp',3,'p_pexp','main.py',479),
  ('empty -> <empty>','empty',0,'p_empty','main.py',485),
  ('saveId -> <empty>','saveId',0,'p_saveId','main.py',491),
  ('saveOperator -> <empty>','saveOperator',0,'p_saveOperator','main.py',512),
]
