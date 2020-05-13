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
    def getQ(self):
        #obtiene el ultimo
        l = self.quad.pop()
        return l

class Operaciones():
    def __init__(self):
        self.cubo = Cube()
    def suma(self, operaodres:Stack, operando_name_and_types:Stack): 
        if operaodres.top() == '+' or '-':
            #es igual al ultimo añadido 
            right_operand = operando_name_and_types.pop()
            left_operand = operando_name_and_types.pop()
            operador = operaodres.pop()
            #verifica que los tipos concuerden accediendo al atributo de los operandos
            res_type = self.cubo.getTipo(right_operand.tipo, left_operand.tipo, operador)
            if (res_type != 'ERROR'):
                #crea un objeto cuadruplo #creo que este puede ser llamado en main para evitar crear vrios#
                quad = Quad()
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

print ("hi welcome to test")

s = Stack()
z = Stack()
from tablaFuncionesVariables import var

uno = 1
dos = 2
cubo = Cube()
a = var('float', uno)
b = var('float', dos)

print("a", a.tipo,"b", b.tipo)

s.push(a)
s.push(b)
z.push('+')

o = Operaciones()

o.suma(z,s)


