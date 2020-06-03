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


   # def equals(self, quad):
    def multiplication (self, quad):
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
    
    def goto (self, quad):
        self.iterators[-1] = quad[3]
    
    def gotoF (self, quad):
        if not self.memoria.value_from_memory(quad[1]):
            self.iterators[-1] = quad[3]
            
    
        
      
    
    
    
    

            
        


        