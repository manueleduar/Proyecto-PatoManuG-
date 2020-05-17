import ply.lex as lex
import ply.yacc as yacc
from cube import Cube
from tablaFuncionesVariables import tabFun, tabVar, var
from operaciones import Quad, Operaciones
from stack import Stack
import sys


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
tokens = [
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
t_NE = r'\!=' 
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


tablaFun = tabFun()
actualFunType = ''
fid = ''
operando_name_and_types = Stack()
operadores = Stack()
saltos = Stack()
quad = Quad()
cubo = Cube()
quad_generator = Operaciones()

def p_programa(p):
        '''
        programa :  PROGRAM ID SEMICOLON addP programa1 
        '''
        p[0] = 'PROGRAMA COMPILADO'


def p_addP(p):
    'addP :'
    #tipo de programa
    global actual_funTipo
    actual_funTipo = 'programa'
    # asigna nombre del programa
    global fid
    fid = p[-2]
    print('---------',fid)
    global tablaFun
    if tablaFun.search_tabFun(fid):
        print("funcion ya existe")
    else:
        tablaFun.add_Fun(actual_funTipo, fid, 0, [], [], 0)
        print('\nFuncion que se añadio', fid, 'de tipo:', actual_funTipo)


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
    global actual_funTipo
    actual_funTipo = p[1]
    # asigna nombre del programa
    global fid
    fid = p[1]
    print('_________', fid)
    global tablaFun
    tablaFun.add_Fun(actual_funTipo, fid, 0, [], [], 0)
    # print('\nFuncion que se añadio', fid, 'de tipo:', actual_funTipo)
	
#---------------Tipos de variables aceptadas-------------------#

def p_tipo(p):
    '''
    tipo : INT guardaTipoVar
         | FLOAT guardaTipoVar
         | CHAR guardaTipoVar 
    ''' 
#--------------Funcion para guardar los tipos de vairbles encontrados-------------------#

def p_guardaTipoVar(p): 
    'guardaTipoVar : '
    global actual_varTipo
    actual_varTipo = p[-1]
    # print('Tipo de VAR en TABLA de variables:', actual_varTipo)
    
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
            | ID COMMA var1 addV
            | ID arr
            | ID arr COMMA var1  addV
            | ID mat COMMA var1 addV
            | ID mat 
            | ID mat especial 
            | empty 
    '''
    global varId
    varId = p[1]
    
    
#-----------Anadir variable a la tabla de variables----------------#

def p_addV(p):
    'addV :'
    global tablaFun
    global varId
    global actual_varTipo
    if tablaFun.search_tabFun(fid):
        tablaFun.addVar(fid, actual_varTipo, varId)
        # tablaFun.print_fun_vars(fid)
        # print('\tVariable:', varId, 'de tipo', actual_varTipo, 'agregada a la tabla de variables')
        
        # agregando nombre y tipo a la pila
        varDatos = var(actual_varTipo, varId)
        operando_name_and_types.push(varDatos)
              
    else:
        SystemExit()


        
def p_var2(p):
    # Recursividad para tener varios tipos de variables
    '''
        var2 : var2 tipo var1 SEMICOLON addV
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

def p_save_fun(p):   
    ' save_fun : '
    global actual_funTipo
    global fid
    global tablaFun

    if actual_funTipo == 'void':
        actual_funTipo = p[-2]
        fid = p[-1]
        tablaFun.add_Fun(actual_funTipo, fid, 0, [], [], 0)
        
    # print('actual tipo', actual_funTipo)
    # print('\nFuncion que se añadio', fid, 'de tipo:', actual_funTipo)
    else:
        actual_funTipo = p[-2]
        fid = p[-1]
        tablaFun.add_Fun(actual_funTipo, fid, 0, [], [], 0)
        print('actual tipo', actual_funTipo)
        # print('\nFuncion que se añadio', fid, 'de tipo:', actual_funTipo)

    
def p_function(p):
    '''
    function : FUN VOID function1 
             | FUN INT function2 
             | FUN CHAR function2 
             | FUN FLOAT function2 
    ''' 


def p_function1(p):
    '''
    function1 : ID save_fun LPAREN param RPAREN SEMICOLON LCURLY vars statement RCURLY 
    '''
    
def p_function2(p):
    '''
    function2 : ID save_fun LPAREN param RPAREN SEMICOLON LCURLY vars statement RETURN exp SEMICOLON RCURLY 
    '''
    
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
    asignacion : ID add_id EQUALS saveOperator exp
               | ID add_id arr EQUALS saveOperator exp
               | ID add_id mat EQUALS saveOperator exp
    ''' 


def p_add_id(p):
    '''add_id : '''
    global varId, tablaFun, fid
    varId = p[-1]
    if tablaFun.searchVar_tabFun(fid, varId):
        t = tablaFun.getVar_Tipo(varId, fid)
        variable = var(t, varId)
        operando_name_and_types.push(variable)
    else:
        sys.exit()


def genera_quad_asignacion(p): 
    'genera_quad_asignacion : '
    global operando_name_and_types, operadores, quad
    if len(operadores.pop() > 0):
        if operadores.top() == '=':
            op = operadores.pop()
            der = operando_name_and_types.pop()
            izq = operando_name_and_types.pop()
            res = cubo.getTipo(izq.tipo, der.tipo, op)
            if res != 'ERROR':
                quad.addQ(izq.id, der.id, op, None)
            else:
                print("Type mismatch")
                SystemExit()


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
         | compexp AND saveOperator compexp
    ''' 
    

def p_compexp(p):
    '''
    compexp : sumexp 
            | compexp1 sumexp
    ''' 



def p_compexp1(p):
    '''
    compexp1 : sumexp GT saveOperator sumexp
             | sumexp LT saveOperator sumexp
             | sumexp GTE saveOperator sumexp
             | sumexp LTE saveOperator sumexp
             | sumexp NE saveOperator sumexp 
    ''' 




def p_sumexp(p):
    '''
    sumexp : mulexp  
           | mulexp PLUS saveOperator mulexp
           | mulexp MINUS saveOperator mulexp
    ''' 
    
def p_saveOperator(p):
    'saveOperator : '
    global actual_operator
    actual_operator = p[-1]
    operadores.push(actual_operator)
    print(operadores.top())


def p_mulexp(p):
    '''
    mulexp : pexp  
           | pexp MUL saveOperator pexp
           | pexp DIV saveOperator pexp
    '''


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
    if p is not None:
        # Esto evita que se meta en un ciclo infinito al encontrar errores de sintaxis
        parser.errok()
        print('Syntax Error in input!', p)
    else: 
        print('Unexpected end of input....')

    
parser = yacc.yacc()


if __name__ == '__main__':
    try:
        #nombreArchivo = 'test1.txt'
        nombreArchivo = 'prueba2.txt'
        # nombreArchivo = 'prueba4.txt'
        # nombreArchivo = 'prueba3.txt'
        arch = open(nombreArchivo, 'r')
        print("El archivo a leer es: " + nombreArchivo)
        informacion = arch.read()
        arch.close()
        lexer.input(informacion)
        while True:
            tok = lexer.token()
            if not tok:
                break
            # print(tok)
        if (parser.parse(informacion, tracking = True) == 'PROGRAMA COMPILADO'):
            print ("Correct Syntax")
        else: 
            print("Syntax error")
    except EOFError:
        # print("ERROREOF")
        print(EOFError)

