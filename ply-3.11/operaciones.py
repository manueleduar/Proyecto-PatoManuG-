from tablaFuncionesVariables import var
from cube import Cube
from stack import Stack
from avail import Avail


class Quad():
    def __init__(self):
        self.quad = []
        self.cont = 0

    def addQ(self, left, right, op, result):
        # añade un set de operador y operando derecho e izq
        q = {op, right, left, result}
        self.quad.append(q)
        # añade el contador
        self.cont += 1
        # anadir saltos

    def add_logic(self, goto, result, place, other):
        q = {goto, result, place, other}
        self.quad.append(q)

    def getQ(self):
        # obtiene el ultimo
        l = self.quad[-1]
        return l
        
    def fill_Quad(self, index):
        temp = self.quad[index]
        temp[3]= len(self.quad)
        self.quad[index] = tuple(temp)
        print ("cuadruplo", self.quad[index])

class Operaciones():
    def __init__(self):
        self.cubo = Cube()
        self.avail = Avail()
        
    def operations(self, operaodres: Stack, operando_name_and_types: Stack, quad: Quad):
        operador = operaodres.pop()
        right_operand = operando_name_and_types.pop()
        left_operand = operando_name_and_types.pop()
         # verifica que los tipos concuerden accediendo al atributo de los operandos
        
        res_type = self.cubo.getTipo(left_operand.tipo, right_operand.tipo, operador)
        
        if (res_type != 'ERROR'):
            result = self.avail.next()
            quad.addQ(right_operand.id,left_operand,operador.id, result)
            operando_name_and_types.push(result)
        else:
            print("type mismatch")
            SystemExit()
            
    def operations_min(self, operaodres: Stack, operando_name_and_types: Stack, quad: Quad):
        operator = operaodres.pop()
        operand = operando_name_and_types.pop()
        quad.addQ(None, None, operator, operand)
        operando_name_and_types.push(operand)
        

    def logic(self, operadores: Stack, operando_name_and_types: Stack, saltos: Stack, quad: Quad, goto):
        tipx = operadores.pop().tipo
        if tipx =='bool':
            result = operando_name_and_types.pop()
            quad.add_logic(goto, result, None, -1)
            saltos.push(len(quad)-1)
            print("tipo cuad " , result.id)
        else:
            print("type mismatch")
            SystemExit()
  


print("hi welcome to test")

s = Stack()
z = Stack()

uno = 1
dos = 2
cubo = Cube()
a = var('float', uno)
b = var('float', dos)


s.push(a)
s.push(b)
z.push('+')

print(s.pop().tipo, s.pop().tipo, z.pop())

# o = Operaciones()
# q = Quad()


