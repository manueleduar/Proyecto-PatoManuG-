import ply.lex as lex
import ply.yacc as yacc
from tablaFuncionesVariables import TabFun, TabVarG, FunGeneral, VarGeneral

#reserved
reserved = {
    'fun' : 'FUN',
    'var': 'VAR',
    'program': 'PROGRAM',
    'main':'MAIN',
    'void' : 'VOID',
    'int' : 'INT',
    'float': 'FLOAT',
    'char' : 'CHAR',
    'if' : 'IF',
    'else' : 'ELSE',
    'return': 'RETURN',
    'end' : 'END',
    'read': 'READ',
    'print': 'PRINT', 
    'for' : 'FOR',
    'from' : 'FROM',
    'while': 'WHILE',
    'to': 'TO'

}

#tokens
tokens =[
    'ID',
    'CTEI',#CONSTANTE ENTERA
    'CTEF', #CONSTANTE FLOTANTE
    'CTEC', #CONSTANTE CHAR
    'CTESTRING',#COSNTANTE STRING
    'EQUALS',
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'LT', #LESS THAN
    'GT', #GREATER THAN
    'LTE', #LESS THAN OR EQUAL
    'GTE', #GRETER THAN OR EQUAL
    'AND', 
    'OR', 
    'LPAREN',
    'RPAREN',
    'COMMA',
    'SEMICOLON',
    'NE', #NOT EQUAL
    'LBRACKET',
    'RBRACKET',
    'LCURLY',
    'RCURLY',
    'TRANSPUESTA',
    'INVERSA',
    'DETERMINANTE', 
    'COMILLA'
] + list(reserved.values())

  
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_EQUALS = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMILLA = r'\"'
t_MUL = r'\*'
t_DIV = r'\/'
t_GT = r'\>'
t_LT = r'\<'
t_GTE = r'\=>'
t_LTE = r'\<='
t_NE = r'\<>' 
t_AND = r'\&&'
t_OR = r'\|'
t_TRANSPUESTA = r'\¡'
t_DETERMINANTE = r'\$'
t_INVERSA = r'\?'
t_ignore = ' \t\n'

#Para identificar ids
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    #if t.value in reserved:
    #t.type = reserved[t.value]
    t.type = reserved.get(t.value, 'ID')
    return t

#Para identificar floats
def t_CTEF(t):
    #r'\d+\.\d+'
    r'[-+]?\d*\.\d+'
    t.value = float(t.value)
    return t

#Para identificar ints
def t_CTEI(t):
    #r'\d+'
    r'0|[-+]?[1-9][0-9]*'
    t.value = int(t.value)
    return t

#Para identificar strings
def t_CTESTRING(t):
    #r'[a-zA-Z_0-9]+'
    #t.value = string(t.value)
    r'\'[\w\d\s\,. ]*\'|\"[\w\d\s\,. ]*\"'
    return t


#Si sucede un error se despliega en que parte fue 
def t_error(t):
    print("ERROR at '%s'" % t.value)
    t.lexer.skip(1)

lexer = lex.lex()

global scope, current_tipo, is_Function
is_Function = False
tableG = TabFun()


def p_programa(p):
        '''
        programa : PROGRAM ID SEMICOLON programa1
        '''
        p[0] = 'PROGRAMA COMPILADO'

        #TABLA GLOBAL 

        # agrega funcion programa
        current_tipo = p[1]
        myprogram = FunGeneral(current_tipo, p[2])
        tableG.add(myprogram)
    
def p_programa1(p):
    '''
	programa1 : vars modules programa2
	programa1 : vars modules
	| programa2
	'''

def p_programa2(p):
    '''
	programa2 :  main
	''' 
def p_main(p):
    '''
	main : MAIN LPAREN param RPAREN LCURLY vars statement RCURLY END
	'''   
	
def p_tipo(p):
    '''
    tipo : INT 
         | FLOAT
         | CHAR
    '''    

def p_vars(p):
    '''
    vars : var 
         | empty
    '''

def p_var(p):
    '''
    var : VAR var2
    '''     

def p_var1(p):
    '''
        var1 : ID
        | ID COMMA var1
        | ID arr 
        | ID arr COMMA var1
        | ID mat COMMA var1
        | ID mat
        | ID mat especial
        | empty
    '''
    # inicializador de tabla general de variables
    tabVar = TabVarG()
    if not is_Function:
        scope = 'global'

    current_tipo = p[-1]

    iden = p[1]
    var = VarGeneral(current_tipo, iden, scope)
    if (tabVar.searchVarG(var.id)):
        print("la variable de nombre: ",  var .id, "ya existe")

    else:
        tabVar.add(var)
    tabVar.printVars()


def p_var2(p):
    # Recursividad para tener varios tipos de variables
    '''
        var2 : var2 tipo var1 SEMICOLON
             | var2 tipo arr SEMICOLON
             | var2 tipo mat SEMICOLON
             | empty
    ''' 
  
    
def p_especial(p):
    '''
    especial : TRANSPUESTA
             | INVERSA
             | DETERMINANTE
    ''' 
    
def p_arr(p):
    '''
    arr : LBRACKET CTEI RBRACKET
        | LBRACKET exp RBRACKET 
    
    '''  

def p_mat(p):
    '''
    mat : LBRACKET CTEI RBRACKET LBRACKET CTEI RBRACKET
        | LBRACKET exp RBRACKET LBRACKET exp RBRACKET
        | LBRACKET exp RBRACKET LBRACKET CTEI RBRACKET
        | LBRACKET CTEI RBRACKET LBRACKET exp RBRACKET
    ''' 
    
        
def p_modules(p):
    '''
    modules : function modules
            | empty
    
    '''     

    
def p_function(p):
    '''
    function : FUN VOID function1 
             | FUN tipo function2 
    ''' 
   
def p_function1(p):
    '''
    function1 : ID LPAREN param RPAREN SEMICOLON LCURLY vars statement RCURLY
    '''
    tipo = p[-1]
    name = p[1]  
    scope = name
    func = FunGeneral(tipo, name)
    tableG.add(func)

def p_function2(p):
    '''
    function2 : ID LPAREN param RPAREN SEMICOLON LCURLY vars statement RETURN exp SEMICOLON RCURLY   
    ''' 
    tipo = p[-1]
    name = p[1]
    scope = name
    func = FunGeneral(tipo, name)
    tableG.add(func)
    tableG.printFuns()

def p_statement(p):
    '''
    statement :  statement1 statement
              | empty
    ''' 


def p_statement1(p):
    '''
    statement1 : asignacion SEMICOLON
                | llamada SEMICOLON
                | lectura SEMICOLON
                | escritura SEMICOLON
                | for
                | if
                | while
    ''' 



def p_asignacion(p):
     '''
    asignacion : ID EQUALS exp
               | ID arr EQUALS exp
               | ID mat EQUALS exp
    ''' 
    

def p_param(p):
    '''
    param : tipo param1  
          | empty
    
    ''' 

def p_param1(p):
    '''
    param1 : ID
           | ID COMMA param1
           | empty 
    ''' 
    

def p_llamada(p): 
    '''
    llamada : ID LPAREN exp RPAREN
    ''' 

def p_if(p):
    '''
    if : IF LPAREN exp RPAREN LCURLY statement RCURLY
        | IF LPAREN exp RPAREN LCURLY statement RCURLY else
    ''' 

def p_else(p):
    '''
    else : ELSE LCURLY statement RCURLY
        | empty
    ''' 
def p_for(p):
    '''
    for : FOR LPAREN for1 RPAREN LCURLY statement RCURLY
    '''
def p_for1(p):
    '''
    for1 : FROM asignacion TO exp
    '''
def p_while(p):
    '''
    while : WHILE LPAREN exp RPAREN LCURLY statement RCURLY
    ''' 

def p_escritura(p):
     '''
    escritura : PRINT LPAREN escritura1 RPAREN
    ''' 
def p_escritura1(p):
     '''
    escritura1 : escritura2 COMMA escritura2
               | escritura2
    ''' 
def p_escritura2(p):
     '''
    escritura2 : CTESTRING  
               | CTEI
               | CTEF 
               | exp
    ''' 

def p_lectura(p):
    '''
    lectura : READ LPAREN var1 RPAREN
    ''' 

#EXPRESIONES
def p_exp(p):
    '''
    exp : nexp  
        | nexp OR nexp
    ''' 
def p_nexp(p):
    '''
    nexp : compexp
         | compexp AND compexp
    ''' 
    # if p[2]=='||':
    #     p[0] = p[1] | p[3]
    # else:
    #     p[0] = p[1]
    

def p_compexp(p):
    '''
    compexp : sumexp 
            | compexp1 sumexp
    ''' 

    # if p[2]=='&&':
    #     p[0] = p[1] | p[3]
    # else:
    #     p[0] = p[1]


def p_compexp1(p):
    '''
    compexp1 : sumexp GT sumexp
             | sumexp LT sumexp
             | sumexp GTE sumexp
             | sumexp LTE sumexp
             | sumexp NE sumexp 
    ''' 


    # def switch (option):
    #     options ={
    #         1: p[0] = p[1] > p[3]
    #         2: p[0] = p[1] < p[3]
    #         3: p[0] = p[1] >= p[3]
    #         4: p[0] = p[1] <= p[3]
    #         3: p[0] = p[1] != p[3]
    #     }
    #     print options.get(option, "Invalid comparison")


def p_sumexp(p):
    '''
    sumexp : mulexp  
           | mulexp PLUS mulexp
           | mulexp MINUS mulexp
    ''' 

    # if p[2] == '+':
    #     p[0] = p[1] + p[3]
    # elif p[2] == '-':
    #     p[0] = p[1] - p[3]
    # else:
    #     p[0] = p[1]

def p_mulexp(p):
    '''
    mulexp : pexp  
           | pexp MUL pexp
           | pexp DIV pexp
    '''

    # if p[2] == '*':
    #     p[0] = p[1] * p[3]
    # elif p[2] == '/':
    #     p[0] = p[1] / p[3]
    # else:
    #     p[0] = p[1]

def p_pexp(p):
    '''
    pexp : var1  
         | CTEI
         | CTEF
         | CTEC
         | llamada
         | LPAREN exp RPAREN
    '''


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
    #print("Syntax error at '%s'" % p.value)
    print("Syntax Error in input!", p)
    
parser = yacc.yacc()

def main():
    try:
        #nombreArchivo = 'test1.txt'
        nombreArchivo = 'prueba2.txt'
        arch = open(nombreArchivo, 'r')
        print("El archivo a leer es: " + nombreArchivo)
        informacion = arch.read()
        arch.close()
        lexer.input(informacion)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
        if (parser.parse(informacion, tracking = True) == 'PROGRAMA COMPILADO'):
            print ("Correct Syntax")
        else: 
            print("Syntax error")
    except EOFError:
        print("ERROREOF")

main()
