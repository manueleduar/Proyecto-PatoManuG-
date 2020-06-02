import sys
import time

class VirtualMachine():
    def __init__(self):
        self.quads = []
        self.iterators = []
        self.global_mem = { } #13000 - 20999
        self.func_memory = [{}] # 23000- 30999
        self.start_time = 0
        self.end = 0
        self.activation_record = []
        


    # def value_to_mem (self, address, value):
    #     if address < 23000 and address >= 13000:
    #         #globales int
    #         if address < 15000 and address >= 13000:
    #             #resto offset FALTA
    #             self.global_mem[address] = value
    #             #float
    #         elif address < 17000 and address >= 15000:
    #             self.global_mem[address] = value
    #             #char
    #         elif address < 19000 and address >= 17000:
    #             self.global_mem[address] = value
    #             #bool
    #         else:
    #             self.global_mem[address] = value
    #     else:
    #         if address <31000 and address >= 23000:
    #             # local entera
    #             if address < 25000 and address >= 23000:
    #                 self.func_memory[-1][address] = value
    #                 # local float
    #             elif address < 27000 and address >= 25000:
    #                 self.func_memory[-1][address] = value
    #                 # local char
    #             elif address < 29000 and address >= 27000:
    #                 self.func_memory[-1][address] = value
    #             else:
    #                 #local bool 
    #                  self.func_memory[-1][address] = value
                     
    
    # def value_from_memory(self, x):
    #     # print (x)
    #     print(1)
