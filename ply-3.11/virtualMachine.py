import sys
import time 
import mem as memoria

class VirtualMachine():
    def __init__(self):
        self.quads = []
        self.iterators = []
        self.memoria = memoria.Memory()
        self.start_time = 0
        self.tp = 0
        self.activation_record = []


    def rebuildCte(self):
        with open('constants.txt', 'r') as cteList:
            lines = []
            for line in cteList:
                lines.append(eval(line))
            
            for line in lines:
                self.memoria.value_to_memory(line[1], line[0])
            
              
    def clean_quad(self):
        with open('quadruples.txt', 'r') as quadsList:
            quads =[]
            for quad in quadsList:
                quads.append(eval(quad))
            return quads
            
           
    def reading (self, quads):
        for q in quads:
            if q[0] == self.memoria.get_operator_address('+'):
                self.plus(q)
                
            elif q[0] == self.memoria.get_operator_address('-'):
                self.minus(q)
                
            elif q[0] == self.memoria.get_operator_address('*'):
                self.mult(q)
                
            elif q[0] == self.memoria.get_operator_address('/'):
                self.division(q)
            
            elif q[0] == self.memoria.get_operator_address('<'):
                self.less_equal(q)
                    
            elif q[0] == self.memoria.get_operator_address('>'):
                self.greater_equal(q)   
                
            elif q[0] == self.memoria.get_operator_address('<='):
                self.lessThan_equal(q)
                
            elif q[0] == self.memoria.get_operator_address('>='):
                self.greaterThan_equal(q)
                
            elif q[0] == self.memoria.get_operator_address('=='):
                self.compare(q)   
                
            elif q[0] == self.memoria.get_operator_address('!='):
                self.Not_Equal(q)
                
            elif q[0] == self.memoria.get_operator_address('&&'):
                self.and_compare(q)

            elif q[0] == self.memoria.get_operator_address('|'):
                self.or_compare(q)
        
            elif q[0] == self.memoria.get_operator_address('='):
                self.asignacion(q)

            elif q[0] == self.memoria.get_operator_address('read'):
                self.inputOP(q) 

            elif q[0] == self.memoria.get_operator_address('print'):
                self.printing(q) 
    ####### OPERADORES LOGICOS DE COMPARACION #######

    def greater_equal(self, quad):
        if self.memoria.value_from_memory(quad[1]) > self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)

    def less_equal(self, quad):
        if self.memoria.value_from_memory(quad[1]) < self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)

    def greaterThan_equal(self, quad):
        if self.memoria.value_from_memory(quad[1]) >= self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)   
        else:
            self.memoria.value_to_memory(quad[3], False)

    def lessThan_equal(self, quad):
        if self.memoria.value_from_memory(quad[1]) <= self.memoria.value_from_memory(quad[2]):
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


    ####### PRINT OPERATOR and INPUT OPERATOR #######  
    def printing(self, quad):
        if isinstance(quad[1], str):
            print(quad[1])        
        else:
            print(self.memoria.value_from_memory(quad[3]))
    
    def inputOP(self, quad):
        inputVM = input()
        self.memoria.value_to_memory(quad[3], inputVM)
            
      ####### OPERADORES ARITMETICOS ####### 
        
    def mult (self, quad):
        temp = self.memoria.value_from_memory(quad[1]) * self.memoria.value_from_memory(quad[2])
        #print("multiplicando...", temp)
        self.memoria.value_to_memory(quad[3], temp)
        
    def division (self, quad):
        temp = self.memoria.value_from_memory(quad[1]) / self.memoria.value_from_memory(quad[2])
        self.memoria.value_to_memory(quad[3], temp)
        
    def plus (self, quad):
        temp = self.memoria.value_from_memory(quad[1]) + self.memoria.value_from_memory(quad[2])
        # print("sumando...", temp)
        self.memoria.value_to_memory(quad[3], temp)
        
    def minus (self, quad):
        temp = self.memoria.value_from_memory(quad[1]) - self.memoria.value_from_memory(quad[2])
        # print("Restando...", temp)
        self.memoria.value_to_memory(quad[3], temp)
 
    def asignacion(self, quad):
        self.memoria.value_to_memory(quad[3], self.memoria.value_from_memory(quad[1])) 
       
       
    
# vm = VirtualMachine()
# vm.rebuildCte()
# q = vm.clean_quad()

# vm.reading(q)
        
        
    

            


        


        