import sys
import time 
import mem as memoria

class VirtualMachine():
    def __init__(self):
        self.quads = []
        self.iterators = []
        self.memoria = memoria.Memory()
        self.start_time = 0
        self.activation_record = []


    def readtxt(self):
        quadTxt = open('holamundo.txt', 'r')
        count = 0
        myList = []
        for line in quadTxt:
            count += 1
            myList.append(eval(line))
            print("Quad{}: {}".format(count, line.strip())) 

        quadTxt.close() 
        return myList

        #imprimiendo tuplas
        # for i in myList:
        #     print(i)

        # close line
    
    
        
    def clean_aux(self, myList):
        for i in myList:
            if i[0] == self.memoria.get_operator_address('='):
                print("es un igual")


    ####### OPERADORES LOGICOS DE COMPARACION #######

    def greater_than(self, quad):
        if self.memoria.value_from_memory(quad[1]) > self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)

    def less_equal(self, quad):
        if self.memoria.value_from_memory(quad[1]) <= self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)

    def greater_equal(self, quad):
        if self.memoria.value_from_memory(quad[1]) >= self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)   
        else:
            self.memoria.value_to_memory(quad[3], False)

    def Not_Equal(self, quad):
        if self.memoria.value_from_memory(quad[1]) != self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)

    def compare(self, quad):
        if self.memoria.value_from_memory(quad[1]) == self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)
    
    def and_compare(self, quad):
        if self.memoria.value_from_memory(quad[1]) and self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)

    def or_compare(self, quad):
        if self.memoria.value_from_memory(quad[1]) or self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)


    ####### PRINT OPERATOR #######
    
    def printing(self, quad):
        if isinstance(quad[1], str):
            print(quad[1])        
        else:
            print(self.memoria.value_from_memory(quad[1]))
        

        
      ####### READ OPERATOR #######  
    
    # def input(self, quad):
    #     user_input = input()

    #     if quad[3].__class__.__name__ in ('tuple'):
    #         if quad[1] == "Bool":
    #             if user_input.lower() == "true"


        


    

      ####### OPERADORES ARITMETICOS ####### 
        
    def mult (self, quad):
        temp = self.memoria.value_from_memory(quad[1]) * self.memoria.value_from_memory(quad[2])
        self.memoria.value_to_memory(quad[3], temp)
        
    def division (self, quad):
        temp = self.memoria.value_from_memory(quad[1]) / self.memoria.value_from_memory(quad[2])
        self.memoria.value_to_memory(quad[3], temp)
        
    def plus (self, quad):
        temp = self.memoria.value_from_memory(quad[1]) + self.memoria.value_from_memory(quad[2])
        self.memoria.value_to_memory(quad[3], temp)
    
    def minus (self, quad):
        temp = self.memoria.value_from_memory(quad[1]) - self.memoria.value_from_memory(quad[2])
        self.memoria.value_to_memory(quad[3], temp)
        
    def return_val(self, quad):
        self.memoria.value_to_memory(quad[3], self.memoria.value_from_memory(quad[1]))
        
    
        
    

            

    
# vm = VirtualMachine()

# x = vm.readtxt()

# vm.clean_aux(x)


        


        