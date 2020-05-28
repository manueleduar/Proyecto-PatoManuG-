import ply.lex as lex
import ply.yacc as yacc
from tablaFuncionesVariables import tabFun, tabVar
from avail import Avail
from cube import Cube
from stack import Stack
from mem import Memory
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
    'COMPARE',
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
t_COMPARE = r'\=='
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

# pilas para los cuadruplos
stackName = Stack()
stackTypes = Stack()
operadores = Stack()
quadruples = []

avail = Avail()

#instanciar Objetos de clases utilizadas
cubo = Cube()
saltos = Stack()
memoria = Memory()

def p_programa(p):
        '''
        programa :  PROGRAM ID SEMICOLON addP programa1 
        '''
        global programId
        programId = p[2]
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
	main : MAIN LPAREN param2 RPAREN LCURLY vars statement RCURLY END
	'''
    global actual_funTipo
    actual_funTipo = p[1]
    # asigna nombre del programa
    global fid
    fid = p[1]
    print('_________', fid)
    global tablaFun
    tablaFun.add_Fun(actual_funTipo, fid, 0, [], [], 0)
    print('\nFuncion que se añadio', fid, 'de tipo:', actual_funTipo)
	
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
            | ID arr COMMA var1 addV 
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
        #print('\tVariable:', varI         d, 'de tipo', actual_varTipo, 'agregada a la tabla de variables')
            
    else:
        SystemExit()

# def p_addVartoStack(p):
#     'addVartoStack : '
#     global stackName, operadores, fid
#     res = tablaFun.getVar_Tipo(p[-1], fid)

#     if res:
#         stackTypes.push(res)
#         stackName.push(p[-1])

#     else: 
#         print('NO SE PUDO')
#         sys.exit()
        
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

    # if actual_funTipo == 'void':
    actual_funTipo = p[-2]
    fid = p[-1]
    tablaFun.add_Fun(actual_funTipo, fid, 0, [], [], 0)
        
    # print('actual tipo', actual_funTipo)
    # print('\nFuncion que se añadio', fid, 'de tipo:', actual_funTipo)
    # else:
    #     actual_funTipo = p[-2]
    #     fid = p[-1]
    #     tablaFun.add_Fun(actual_funTipo, fid, 0, [], [], 0)
        # print('actual tipo', actual_funTipo)
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
    function1 : ID save_fun LPAREN param2 RPAREN SEMICOLON LCURLY vars statement RCURLY 
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
    asignacion : ID saveId2 EQUALS addOperadorName exp genera_quad_asignacion
               | ID saveId2 arr EQUALS addOperadorName exp genera_quad_asignacion
               | ID saveId2 mat EQUALS addOperadorName exp genera_quad_asignacion
    ''' 
def p_genera_quad_asignacion(p):
    'genera_quad_asignacion : '
    global stackTypes, stackName, operadores, quadruples
    
    if operadores.size() > 0:
        if operadores.top() == '=':
            operadores2 = operadores.pop()
            operando_derecho = stackName.pop()
            operando_derecho_tipo = stackTypes.pop()
            operando_izquierdo = stackName.pop()
            operando_izquierdo_tipo = stackTypes.pop()

            result = cubo.getTipo(operando_izquierdo_tipo, operando_derecho_tipo, operadores2)

            if result != 'ERROR':
                quad = (operadores2, operando_derecho, None, operando_izquierdo)
                print('quadruplo:', str(quad))
                quadruples.append(quad)
            
            else: 
                print('Type Dissmatch....')
                sys.exit()
    else: 
        print('Vacio....')
        return  


def p_addOperadorName(p):
    'addOperadorName : '
    global operadores
    aux = p[-1]
    operadores.push(aux)


    
def p_param(p):
    '''
    param : 
          | empty
    
    ''' 

def p_param1(p):
    '''
        param1 : ID
            | ID COMMA var1 addV
            | ID arr 
            | ID arr COMMA var1 addV 
            | ID mat COMMA var1 addV
            | ID mat 
            | ID mat especial 
            | empty 
    ''' 

def p_param2(p):
      '''
        param2 : param2 tipo var1  addV
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
    escritura : PRINT LPAREN operadorPrint escritura1 operatorPrintQuad RPAREN 
    ''' 
def p_escritura1(p):
     '''
    escritura1 : escritura2 COMMA escritura2
               | escritura2
    ''' 
def p_escritura2(p):
     '''
    escritura2 : COMILLA CTESTRING COMILLA
               | CTEI saveCTE operatorPrintQuad
               | CTEF saveCTE operatorPrintQuad
               | exp 
    ''' 

def p_lectura(p):
    '''
    lectura : READ operatorRead LPAREN var1 operatorReadQuad RPAREN
    ''' 

#EXPRESIONES
def p_exp(p):
    '''
    exp : nexp genera_quad_or
        | nexp genera_quad_or OR addOperadorName  nexp 
    ''' 

def genera_cuadruplo():
    global operadores, stackName, stackTypes, quadruples
    
    if operadores.size() > 0:
        # if operadores.top() == 'print' or operadores.top() == 'read':
        #     operando2 = operadores.pop()
        #     valor = stackName.pop()
        #     stackTypes.pop()
        #     quad = (operando2, None, None, valor)
        #     print('quad de print:', str(quad))
        #     quadruples.append(quad)
        
        # if operadores.top() != '=':
        operando2 = operadores.pop()
        operando_derecho = stackName.pop()
        operando_derecho_tipo = stackTypes.pop()
        operando_izquierdo = stackName.pop()
        operando_izquierdo_tipo = stackTypes.pop()

        result_type = cubo.getTipo(operando_izquierdo_tipo, operando_derecho_tipo, operando2)

        if result_type != 'ERROR':
            result = avail.next()
            quad = (operando2, operando_izquierdo, operando_derecho, result)

            print('quad: ' + str(quad))

            quadruples.append(quad)
            stackName.push(result)
            stackTypes.push(result_type)

        else: 
            print('Type dismatch...')
            sys.exit()
    else:
        print('PILA DE OPERANDOS VACIA....')


def p_genera_quad_or(p):
    'genera_quad_or : '
    global operadores
    if operadores.size() > 0:
        if operadores.top() == '|':
            genera_cuadruplo()
     

def p_genera_quad_and(p):
    'genera_quad_and : '
    global operadores
    if operadores.size() > 0:
        if operadores.top() == '&&':
            genera_cuadruplo()


def p_compare_quad(p):
    'compare_quad : '
    global operadores
    if operadores.size() > 0:
        if operadores.top() == '<' or operadores.top() == '>' or operadores.top() == '<=' or operadores.top() == '>=' or operadores.top() == '==' or operadores.top() == '!=':
            genera_cuadruplo()  


def p_if_quad(p):
    'if_quad : '
    global stackName, stackTypes, quadruples, saltos
    result_type = stackTypes.pop()
    if result_type == 'bool':
        valor = stackName.pop()
        quad = ('GotoF', valor, None, -1)
        quadruples.append(quad)
        saltos.push(len(quadruples)-1)

    else: 
        print('Type Dissmatch....')
        return


def p_nexp(p):
    '''
    nexp : compexp genera_quad_and
         | compexp genera_quad_and AND addOperadorName compexp 
    ''' 
    

def p_compexp(p):
    '''
    compexp : sumexp
            | compexp1 sumexp
    ''' 


def p_compexp1(p):
    '''
    compexp1 : sumexp GT addOperadorName sumexp compare_quad
             | sumexp LT addOperadorName sumexp compare_quad
             | sumexp GTE addOperadorName sumexp compare_quad
             | sumexp LTE addOperadorName sumexp compare_quad
             | sumexp NE addOperadorName sumexp compare_quad
             | sumexp COMPARE addOperadorName sumexp compare_quad
    ''' 


def p_sumexp(p):
    '''
    sumexp : mulexp 
           | mulexp PLUS addOperadorName mulexp genera_sum_quad
           | mulexp MINUS addOperadorName mulexp genera_sum_quad
    '''    
    
def p_genera_sum_quad(p):
    'genera_sum_quad : '
    global operadores
    if operadores.size() > 0:
        if operadores.top() == '+' or operadores.top() == '-':
            genera_cuadruplo()


def p_genera_quad_mul(p):
    'genera_mul_quad : '
    global operadores
    if operadores.size() > 0:
        if operadores.top() == '*' or operadores.top() == '/':
            genera_cuadruplo()


# Leer operador print y generar quadruplo
def p_operadorPrint(p):
	'operadorPrint : '
	global operadores
	operadores.push('print')


def p_operatorPrintQuad(p):
    'operatorPrintQuad : '
    global operadores
    if operadores.size() > 0:
        if operadores.top() == 'print':
            operator_aux = operadores.pop()
            valor = stackName.pop()
            stackTypes.pop()
            quad = (operator_aux, None, None, valor)
            print('quad:', str(quad))
            quadruples.append(quad)


# Leer operador read y generar quadruplo
def p_operatorRead(p):
    'operatorRead : '
    global operadores
    operadores.push('read')

def p_operatorReadQuad(p):
    'operatorReadQuad : '
    global operadores
    if operadores.size() > 0:
        if operadores.top() == 'read':
            operator_aux = operadores.pop()
            valor = stackName.pop()
            stackTypes.pop()
            quad = (operator_aux, None, None, valor)
            print('Quadruplo de read:', str(quad))
            quadruples.append(quad)


def p_mulexp(p):
    '''
    mulexp : pexp 
           | pexp MUL addOperadorName pexp genera_mul_quad
           | pexp DIV addOperadorName pexp genera_mul_quad
    '''


def p_pexp(p):
    '''
    pexp : var1 saveId 
         | CTEI saveCTE
         | CTEF saveCTE
         | CTEC saveCTE
         | CTESTRING saveCTE  
         | llamada
         | LPAREN exp RPAREN
    '''


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None
    
# guarda en pila variables      
def p_saveId(p):
    '''saveId : '''
    global varId, tablaFun, fid, stackName, stackTypes 
    if tablaFun.searchVar_tabFun(fid, varId):
        tipos = tablaFun.getVar_Tipo(varId, fid)
        # memoria.set_var_direction(tipos, varId,actual_funTipo,fid)
        if tipos:
            stackTypes.push(tipos)
            stackName.push(varId)
        # print('\t OPERANDO AÑADIDO ----> tipo y nombre: ', stackTypes.top(), stackName.top())

    else:
        SystemExit()   


def p_saveId2(p):
    '''saveId2 : '''
    global varId, tablaFun, fid, stackName, stackTypes

    varId = p[-1]
    if tablaFun.searchVar_tabFun(fid, varId):
        tipos = tablaFun.getVar_Tipo(varId, fid)
        stackTypes.push(tipos)
        stackName.push(varId)
        # print('\t OPERANDO_asignacion AÑADIDO ----> tipo y nombre: ', stackTypes.top(), stackName.top())

    else:
        SystemExit()   



def p_saveCTE(p):
    '''saveCTE : '''
    global cte, t
    cte = p[-1]
    t = type(cte)
    
    memoria.set_cte(cte)
    
    if (t == int):
        stackTypes.push('int')
        stackName.push(cte)
        
    elif (t == float):
        stackTypes.push('float')
        stackName.push(cte)
        
    elif (t == str):
        stackTypes.push('string')
        stackName.push(cte)

    else:
        stackTypes.push('char')
        stackName.push(cte)

    # print('\t OPERANDO AÑADIDO ----> CTE ', stackTypes.top(), stackName.top())


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
        # nombreArchivo = 'prueba2.txt'
        nombreArchivo = 'prueba4.txt'
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

