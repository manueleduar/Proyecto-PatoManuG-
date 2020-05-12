from cube import Cube
from stack import Stack

class Operaciones():
    def __init__(self):
        self.cubo = Cube()
    def suma(self, operaodres:Stack, operando_name_and_types:Stack): 
        if operaodres.top() == '+' or '-':
            right_operand = operando_name_and_types.pop()
            left_operand = operando_name_and_types.pop()
            operador = operaodres.pop()
            res_type = self.cubo.getTipo(right_operand, left_operand, operador)
            if (res_type != 'error'):
                quad = "hello"
            else:
                print("Type mismatch")
    def factores(self, operaodres:Stack, operando_name_and_types:Stack):
        if operaodres.top() == '*' or '/':
            right_operand = operando_name_and_types.pop()
            left_operand = operando_name_and_types.pop()
            operador = operaodres.pop()
            res_type = self.cubo.getTipo(right_operand, left_operand, operador)
            if (res_type != 'error'):
                quad = "hello"
            else:
                print("Type mismatch")