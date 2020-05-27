# from tablaFuncionesVariables import tabFun, tabVar, var

class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
         return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]



# stack = Stack()
# stack.push(1011)
# stack.push(101201201)

# stack.push(1133)
# stack.push(1454)
# stack.push(15454)

# print(stack.top())
# stack.pop()

# print(stack.top())
# stack.pop()

# print(stack.top())
# stack.pop()

# print(stack.top())
# stack.pop()

# print(stack.top())
# stack.pop()


