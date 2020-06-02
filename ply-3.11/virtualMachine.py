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
        self.operators = {
            '+' : 1,
            '-' : 2,
             '*' : 3,
             '/' : 4,
             '<' : 5,
             '>' : 6,
             '<=' : 7,
             '>=' : 8,
             '==' : 9,
             '!=' : 10,
             '&&' : 11,
             '|' : 12,
             '=' : 13,
             'FOR' : 14,
             'WHILE' : 15,
             'READ' : 16,
             'PRINT' : 17,
             'GOTO' : 18,
             'GOTOF' : 19,
             'GOTOV' : 20,
             'ERA' : 21,
             'GOSUB' : 22,
             'RETURN': 23,
             'ENDPROC' : 24,
             'VER': 25,
             'END': 26,
            }


    def value_to_mem (self, address, value):
        if address < 23000 and address >= 13000:
            #globales int
            if address < 15000 and address >= 13000:
                #resto offset FALTA
                self.global_mem[address] = value
                #float
            elif address < 17000 and address >= 15000:
                self.global_mem[address] = value
                #char
            elif address < 19000 and address >= 17000:
                self.global_mem[address] = value
                #bool
            else:
                self.global_mem[address] = value
        else:
            if address <31000 and address >= 23000:
                # local entera
                if address < 25000 and address >= 23000:
                    self.func_memory[-1][address] = value
                    # local float
                elif address < 27000 and address >= 25000:
                    self.func_memory[-1][address] = value
                    # local char
                elif address < 29000 and address >= 27000:
                    self.func_memory[-1][address] = value
                else:
                    #local bool 
                     self.func_memory[-1][address] = value