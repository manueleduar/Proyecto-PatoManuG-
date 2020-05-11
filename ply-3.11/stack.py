from tablaFuncionesVariables import tabFun, tabVar, var

class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
         return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]


s = Stack()

s.push(1)
s.push(2)
s.push(10)
s.push(120)

print("Top = ", s.top())


print("Eliminando...", s.pop())
print("Eliminando...", s.pop())
print("Eliminando...", s.pop())
# print(s.pop())


print("Esta vacia la pila??", s.is_empty())

