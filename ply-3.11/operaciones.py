from cube import Cube
from stack import Stack
#Clase cuadruplo 
class Quad():
    def __init__(self):
        self.quad = []
        self.cont = 0
        
    def addQ(self, right, left, op):
        #añade un set de operador y operando derecho e izq
        q = {op, right, left}
        self.quad.append(q)
        #añade el contador
        self.cont += 1
        #anadir saltos
    def addJ(self, goto, result, place):
        q ={goto, result, place}
        self.quad.append(q)
    def getQ(self):
        #obtiene el ultimo
        l = self.quad.pop()
        return l

class Operaciones():
    def __init__(self):
        self.cubo = Cube()
    def suma(self, operaodres:Stack, operando_name_and_types:Stack, quad:Quad): 
        if operaodres.top() == '+' or '-':
            #es igual al ultimo añadido 
            right_operand = operando_name_and_types.pop()
            left_operand = operando_name_and_types.pop()
            operador = operaodres.pop()
            #verifica que los tipos concuerden accediendo al atributo de los operandos
            res_type = self.cubo.getTipo(right_operand.tipo, left_operand.tipo, operador)
            if (res_type != 'ERROR'):
                
                #añade los operandos y operador para crear cuadruplo 
                quad.addQ(right_operand, left_operand,operador)
                var_temp =  quad.getQ()
                print("se creo el nuevo quad")
                # #añade el cuadruplo creado en stack de operadores
                operando_name_and_types.push(var_temp)
                print("se ha añadido a la pila de operandos")
                #FALTA SI ALGUN OPERANDO FUERA TEMPORAL RETORNARLO A AVAIL#
            else:
                print("Type mismatch")
    
    def if_salto(self, operadores:Stack, operando_name_and_types:Stack, saltos:Stack, quad:Quad):
        #si el ultimo operador metido a la cola fue uno de los siguientes
         if operadores.top() == '>' or '<' or'<=' or '>=' or '==' or '!=':
             #saca el ultimo operando metido a operandos
             res_type = operando_name_and_types.pop()
             #si el ultimo tipo no es de tipo booleano 
             if (res_type.tipo != 'bool'):
                print("Type mismatch")
             else:
                 #genera el cuadruplo con un pointer vacio, el resultado y el operador es un goto
                quad.addQ("pointer", res_type, "goTo")
                #se pone el salto
                saltos.push(quad)
               
            

# print ("hi welcome to test")

# s = Stack()
# z = Stack()
# from tablaFuncionesVariables import var

# uno = 1
# dos = 2
# cubo = Cube()
# a = var('float', uno)
# b = var('float', dos)

# print("a", a.tipo,"b", b.tipo)

# s.push(a)
# s.push(b)
# z.push('+')

# o = Operaciones()

# o.suma(z,s)


