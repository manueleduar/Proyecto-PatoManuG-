import ply.lex as lex
import ply.yacc as yacc
from avail import Avail
from tablaFuncionesVariables import tabFun, tabVar
from cube import Cube
from virtualMachine import *
from stack import Stack
from mem import Memory
import sys
import json

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
t_GTE = r'\>='
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
array = []

avail = Avail()

#instanciar Objetos de clases utilizadas
cubo = Cube()
saltos = Stack()

def p_programa(p):
        '''
        programa :  PROGRAM ID SEMICOLON addP programa1 
        '''
        global programId
        programId = p[2]
        # print ("Nombre programa es ––––––––––––––––––––", programId)
        p[0] = 'PROGRAMA COMPILADO'
      


def p_addP(p):
    'addP :'
    #tipo de programa
    global actual_funTipo, fid
    actual_funTipo = 'programa'
    fid = 'programa'
    tablaFun.add_Fun(actual_funTipo, fid, 0, [], [], 0)
    # asigna nombre del programa
    # global fid
    # fid = p[-2]
    # global tablaFun
    # if tablaFun.search_tabFun(fid):
    #     print("funcion ya existe")
    # else:
    #     tablaFun.add_Fun(actual_funTipo, fid, 0, [], [], 0)
    #     print('\nFuncion que se añadio', fid, 'de tipo:', actual_funTipo)


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
	main : MAIN save_fun LPAREN param2 RPAREN LCURLY vars statement RCURLY END
	'''
    global actual_funTipo
    actual_funTipo = p[1]
    # asigna nombre del programa
    global fid
    fid = p[1]
    #print('_________', fid)
    global tablaFun
    tablaFun.add_Fun(actual_funTipo, fid, 0, [], [], 0)
    #print('\nFuncion que se añadio', fid, 'de tipo:', actual_funTipo)
	
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
   
   
    # print ("var que está almacenando", varId)
    
    
#-----------Anadir variable a la tabla de variables----------------#

def p_addV(p):
    'addV :'
    global tablaFun
    global varId
    global actual_varTipo
    if not varId == None:
        if tablaFun.search_tabFun(fid):
          tablaFun.addVar(fid, actual_varTipo, varId)    
        else:
          SystemExit()
    # else:
    #     print("no se puede añadir none")


        
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

    if p[-1] == 'main':
        actual_funTipo = 'main'
        fid = p[-1]
        tablaFun.add_Fun(actual_funTipo, fid, 0, [], [], 0)
    else:    
        actual_funTipo = p[-2]
        fid = p[-1]
        tablaFun.add_Fun(actual_funTipo, fid, 0, [], [], 0)
        


    
def p_function(p):
    '''
    function : FUN VOID function1 end_func
             | FUN INT function2 end_func
             | FUN CHAR function2 end_func
             | FUN FLOAT function2 end_func
    ''' 

def p_function1(p):
    '''
    function1 : ID save_fun LPAREN param2 RPAREN SEMICOLON LCURLY vars statement RCURLY 
    '''
    
def p_function2(p):
    '''
    function2 : ID save_fun LPAREN param2 RPAREN SEMICOLON LCURLY vars statement RETURN operadorReturn exp quad_return SEMICOLON RCURLY
    '''
  

def p_end_func(p):
    'end_func : '
    global quadruples, tablaFun
    quad = ('ENDFUNC', None, None, -1)
    quadruples.append(quad)
    tablaFun.reset_temp_add()
    print("END FUNC")

    
    

def p_operadorReturn(p):
    'operadorReturn : '
    global operadores
    operadores.push('return')



def p_quad_return(p):
    'quad_return : '
    global quadruples, stackName, stackTypes, operadores, actual_funTipo
    if operadores.size() > 0:
        if operadores.top() == 'return':
            operadores2 = operadores.pop()
            result = stackName.pop()
            #result_type = stackTypes.pop()

            quad = (operadores2, -1, -1, result)
            # print('QUAD RETURN:', str(quad))
            quadruples.append(quad)
            
        else: 
            print('Type dissmatch')
            sys.exit()




    
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
        # if operadores.top() == '=':
        # sacar la direccion de memoria del operador antes que nada
        op = tablaFun.get_op_mem(operadores.top())
        operadores2 = operadores.pop()
        operando_derecho = stackName.pop()
        operando_derecho_tipo = stackTypes.pop()
        operando_izquierdo = stackName.pop()
        operando_izquierdo_tipo = stackTypes.pop()
        result = cubo.getTipo(operando_izquierdo_tipo, operando_derecho_tipo, operadores2)
        # print("result CUBO--------", operando_izquierdo_tipo, operando_derecho_tipo, result)

        if result != 'ERROR':
            quad = (op, operando_derecho, None, operando_izquierdo)
            quadruples.append(quad)
            
    else: 
        print('Vacio....')
        sys.exit()  


def p_addOperadorName(p):
    'addOperadorName : '
    global operadores
    aux = p[-1]
    #op = tablaFun.get_op_mem(aux)
    #print('MEMORY OPERATOR', op, 'de', aux)
    #meter a la pila de operadores el op, este asocia el operador a la direccion de memoria asignada SE DEBE ARREGLAR CUADRUPLOS PARA QUE 
    # DEBE QUEDAR operadores.push(op)
    operadores.push(aux)


    
# def p_param(p):
#     '''
#     param : 
#           | empty
    
    # ''' 

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

def p_addParam(p):
    'addParam : '
    tablaFun.add_parametros_tabFun(fid, varId, actual_varTipo)
    print('ADD PARAM:', fid, varId, actual_varTipo)


def p_param2(p):
      '''
        param2 : param2 tipo param1 addV addParam
             | empty 
    ''' 
    
def p_verifica_parametros(p):
    'verifica_parametros : '
    global countParams
    checkParams = tablaFun.getNumeroParametros(p[-4])
    if not countParams == checkParams:
        print('Numero de parametros incorrectos en', p[-4])
        print('COUNT PARAMS = ', countParams, checkParams, p[-4])
        sys.exit()

    # else de prueba
    else:
        print('Numero de parametros ACEPTADO')


def p_cuenta_parametros(p):
    '''cuenta_parametros : '''
    global countParams
    countParams = countParams + 1
    print('PARAMS ACTUALIZADO', countParams)


def p_llamada(p): 
    '''
    llamada : ID era_call LPAREN aux_exp verifica_parametros RPAREN gosub_quad
    
    ''' 
def p_aux_exp(p):
    '''
    aux_exp : exp 
            | exp quad_param COMMA cuenta_parametros aux_exp 
            | empty
    '''  

def p_ZeroParameters(p):
    '''ZeroParameters : '''
    global countParams
    countParams = 0


def p_era_call(p):
    'era_call : '
    global quadruples, countParams
    nameV = p[-1]
    quad = ('ERA', None, None, nameV)
    quadruples.append(quad)
    countParams = 1
    print ("ERA CALL _________", nameV )
   


def p_quad_param(p):
    '''quad_param : '''
    global quadruples 
    val = stackName.pop()
    stackTypes.pop()
    quad = ('PARAM', val, None, -1)
    quadruples.append(quad)


def p_gosub_quad(p):
    'gosub_quad : '
    global quadruples
    gosub_call = p[-6]
    quad = ('GOSUB', None, None, gosub_call) 
    quadruples.append(quad)
    print("gosub-----------------", p[-6], str(quad))
    
    
  


def p_if(p):
    '''
    if : IF LPAREN exp RPAREN if_quad LCURLY statement RCURLY else end_if   
    ''' 

def p_else(p):
    '''
    else : ELSE else_quad LCURLY statement RCURLY
         | empty
    ''' 

def p_for_op(p):
    'for_op :'
    global operadores, quadruples, saltos
    
    op = tablaFun.get_op_mem('for')
    operadores.push(op)
    saltos.push(len(quadruples))

def p_for_quad(p):
    'for_quad : '
    global stackName, stackTypes, quadruples, saltos
    result_type = stackTypes.pop()

    if result_type == 'bool':
        valor = stackName.pop()
        quad = ('GOTOV', valor, None, -1)
        # print('quad:', str(quad))
        quadruples.append(quad)
        saltos.push(len(quadruples)-1)
    else: 
        print('Error for quad....')
        sys.exit()

def p_for(p):
    '''
    for : FOR for_op LPAREN for1 RPAREN for_quad LCURLY statement RCURLY for_end
    '''
def p_for1(p):
    '''
    for1 : FROM asignacion TO exp
    '''

        
def p_loop_end(p):
    'loop_end : '
    global stackName, stackTypes, quadruples, saltos
    end = saltos.pop()
    retroceso = saltos.pop()
    quad = ('GOTO', None, None, retroceso)
    quadruples.append(quad)
    llenar_quad(end, retroceso)

def p_for_end(p):
    'for_end : '
    global stackName, stackTypes, quadruples, saltos
    end = saltos.pop()
    retroceso = saltos.pop()
    retroceso = int(retroceso) +1
    quad = ('GOTO', None, None, retroceso)
    quadruples.append(quad)
    llenar_quad(end, retroceso)

def p_while_quad(p):
    'while_quad : '
    global stackName, stackTypes, quadruples, saltos
    result_type = stackTypes.pop()

    if result_type == 'bool':
        valor = stackName.pop()
        quad = ('GOTOF', valor, None, -1)
        print('quad:', str(quad))
        quadruples.append(quad)
        saltos.push(len(quadruples)-1)

    else: 
        print('Error while quad....')
        sys.exit()
    
def p_while_op(p):
    'while_op :'
    global operadores, quadruples, saltos
    op = tablaFun.get_op_mem('while')
    # print('OPERATOR WHILE MEMORY', op)
    operadores.push(op)
    saltos.push(len(quadruples))   

def p_while(p):
    '''
    while : WHILE while_op LPAREN exp RPAREN while_quad LCURLY statement RCURLY loop_end
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
    lectura : READ operatorRead LPAREN exp operatorReadQuad RPAREN
    ''' 

#EXPRESIONES
def p_exp(p):
    '''
    exp : nexp 
        | nexp OR addOperadorName nexp genera_quad_or
    ''' 


def genera_cuadruplo():
    global operadores, stackName, stackTypes, quadruples
    
    if operadores.size() > 0:
        # Sacar direccion de   al operador antes que nada
        op = tablaFun.get_op_mem(operadores.top())
        operando2 = operadores.pop()
        operando_derecho = stackName.pop()
        operando_derecho_tipo = stackTypes.pop()
        operando_izquierdo = stackName.pop()
        operando_izquierdo_tipo = stackTypes.pop()
      
        result_type = cubo.getTipo(operando_izquierdo_tipo, operando_derecho_tipo, operando2)
        if result_type != 'ERROR':
            result = avail.next()

            ##### ASIGNAR MEMORIA A TEMPORAL (result en este caso) ########
            tablaFun.add_temp_mem(result_type, result, fid)
            var_temp = tablaFun.get_temp_mem(result)
            # print(result, 'result temporal-----------------------------------', var_temp, result_type, fid)
            
            # quad = (op, operando_izquierdo, operando_derecho, result)
            quad = (op, operando_izquierdo, operando_derecho, var_temp)
           # print('Cuadruplo: ' + str(quad))

            quadruples.append(quad)
            # stackName.push(result)
            # stackTypes.push(result_type)

            ### agregar a la pila de nombres, la direccion en vez de nombre ######
            stackName.push(var_temp)
            stackTypes.push(result_type)

        else: 
            print('No se ha generado quad')
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
        quad = ('GOTOF', valor, None, -1)
        # print('quad:', str(quad))
        quadruples.append(quad)
        saltos.push(len(quadruples)-1)

    else: 
        print('Error if quad....')
        sys.exit()
    
def p_end_if(p):
    'end_if : '
    global saltos
    end = saltos.pop()
    # print("el end que debe guardar en F:", end, '\n')
    llenar_quad(end, -1)           

def p_else_quad(p):
    'else_quad : '
    global quadruples, saltos
    quad = ('GOTO', None, None, -1)
    quadruples.append(quad)
    fAux = saltos.pop()
    saltos.push(len(quadruples)-1)
    llenar_quad(fAux, -1)
    # print('quad:', str(quad))

def llenar_quad(end, cont):
    global quadruples
    temp = list(quadruples[end])
    temp[3] = len(quadruples)
    quadruples[end] = tuple(temp)


def p_nexp(p):
    '''
    nexp : compexp 
         | compexp AND addOperadorName compexp genera_quad_and
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
    #print('PRINT OPERATOR',)   
    operadores.push('print')


def p_operatorPrintQuad(p):
    'operatorPrintQuad : '
    global operadores
    if operadores.size() > 0:
        if operadores.top() == 'print':
            op = tablaFun.get_op_mem('print')
            operator_aux = operadores.pop()
            valor = stackName.pop()
            stackTypes.pop()
            quad = (op, None, None, valor)
            # print('Cuadruplo:', str(quad))
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
            op = tablaFun.get_op_mem('read')
            operator_aux = operadores.pop()
            valor = stackName.pop()
            stackTypes.pop()
            quad = (op, None, None, valor)
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
    if not varId == None:
        if tablaFun.searchVar_tabFun(fid, varId):
            tipos = tablaFun.getVar_Tipo(varId, fid)
            
            tablaFun.add_var_mem(tipos, varId, fid)
            varMem = tablaFun.get_var_mem(varId)
            # print("variable", varId, varMem)
       
            if tipos:
                stackTypes.push(tipos)
                stackName.push(varMem)
                # print('Direccion de', varId, 'es', varmem)

            else:
                 SystemExit()  
    # else:
    #     print("no se puede añadir variable none") 


def p_saveId2(p):
    '''saveId2 : '''
    global varId, tablaFun, fid, stackName, stackTypes
    
    varId = p[-1]

    if tablaFun.searchVar_tabFun(fid, varId):
        tipos = tablaFun.getVar_Tipo(varId, fid)
        tablaFun.add_var_mem(tipos, varId, fid)
        memVar = tablaFun.get_var_mem(varId)
        
        stackTypes.push(tipos)
        stackName.push(memVar)

    else:
        SystemExit()   



def p_saveCTE(p):
    '''saveCTE : '''
    global cte, t, cteA, array
    cte = p[-1]
    t = type(cte)
    
    tablaFun.add_cte_mem(cte)
    
    cte_address = tablaFun.get_cte_mem(cte)
    cteA = (cte, cte_address)
    
    if not cteA in array:
        array.append(cteA)
    else:
        "cte existe ya"
   
    
    if (t == int):
        stackTypes.push('int')
        stackName.push(cte_address)
        #print("tipo y nombre que se ven", cte)

    elif (t == float):
        stackTypes.push('float')
        stackName.push(cte_address)


    else:
        stackTypes.push('char')
        stackName.push(cte_address)
     

def p_error(p):
    if p is not None:
        # Esto evita que se meta en un ciclo infinito al encontrar errores de sintaxis
        parser.errok()
        print('Syntax Error in input!', p)
        sys.exit()

    else: 
        print('Unexpected end of input....')

    
parser = yacc.yacc()


if __name__ == '__main__':
    try:
        nombreArchivo = 'factorial.txt'
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
            print("Correct Syntax")

            ###### archivo-salida.py ######
            f = open ('quadruples.txt','w')
            for i in quadruples:
                f.write(str(i) + '\n')
                #f.write('\n')
            f.close()
            ##### archivo de salida de constantes #######
            c = open("constants.txt", 'w')
            for i in array:
                c.write(str(i) + '\n')
            c.close()  
            
            # Maquina virtual        
            vm = VirtualMachine()
            vm = VirtualMachine()
            vm.rebuildCte()
            q = vm.clean_quad()

            vm.reading(q)
        else: 
            print("Syntax error")
            
    except EOFError:
        # print("ERROREOF")
        print(EOFError)

