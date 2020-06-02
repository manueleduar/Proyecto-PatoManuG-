class Memory:
    def __init__(self):
        #DICCIONARIOS PARA VARIABLES
        self.constants = {}
        self.variables ={}
        self.temporal = {}
        self.operators = {
            '+':1,
            '-':2,
             '*':3,
             '/':4,
             '<':5,
             '>':6,
             '<=':7,
             '>=':8,
             '==':9,
             '!=':10,
             '&&':11,
             '|':12,
             '=':13,
             'for': 14,
             'while': 15,
             'read': 16,
             'print': 17
            }
              
        #GLOBALES 
        self.gi = 1000 #lower 1000 upper 2999
        self.gf = 3000 #lower 3000 upper 5999
        self.gc = 5000 #lower 5000 upper 6999
        self.gb = 7000 #lower 7000 upper 8999

        #GLOBALES TEMPORALES
        self.gLi = 11000 #lower 1000 upper 12999
        self.gLf = 13000 #lower 3000 upper 15999
        self.gLc = 15000 #lower 5000 upper 16999
        self.gLb = 17000 #lower 7000 upper 18999
                
        # LOCALES TEMPORALES 
        self.li = 19000 #lower 19000 upper 19999
        self.lf = 20000 #lower 20000 upper 29999
        self.lc = 21000 #lower 29000 upper 21999
        self.lb = 22000 #lower 41000 upper 22999
        
        # LOCALES 
        self.li = 23000 #lower 23000 upper 25999
        self.lf = 26000 #lower 26000 upper 28999
        self.lc = 29000 #lower 29000 upper 30999
        self.lb = 31000 #lower 31000 upper 32999
        
        # CONSTANTES
        self.ctei = 45000 #lower 45000 upper 45999
        self.ctef = 46000 #lower 46000 upper 46999
        self.ctec = 47000 #lower 47000 upper 47999
        self.cteString = 48000 #lower 48000 upper 48999
        
    def set_var_direction(self, tipo, id, funId):
        #VARIABLES GLOBALES
        if funId == 'programa':
            if tipo == 'int':
                if self.gi <3000:
                    address = self.gi
                    # print("se ha configurado la var", id, "global, la direccion es:", address)
                    self.gi += 1
                    #print("address actualizada a ", self.gi)
                else:
                    print("index out of range")
                    
            elif tipo == 'float':
                if self.gf < 5000:
                    address = self.gf
                    #print("se ha configurado la var", id, "global, la direccion es:", address)
                    self.gf += 1
                    #print("address actualizada a ", self.gf)

                else:
                    print("index out of range")

            elif tipo == 'char':
                if self.gc < 7000:
                    address = self.gc
                    self.gc += 1
                else:
                    print("index out of range")

            else:
                if self.gb < 9000:
                    address = self.gb
                    self.gb += 1
         
        
        else:
            if tipo == 'int':

                if self.li <26000:
                    address = self.li
                    #print("adress", address)
                    #print("se ha configurado la var", id, "Local, la direccion es:", address)
                    self.li += 1
                    #print("address actualizada a ", self.li)
                else:
                    print("index out of range")

            elif tipo == 'float':
                if self.lf < 29000:
                    address = self.lf
                    #print("se ha configurado la var", id, "local, la direccion es:", address)
                    self.lf += 1
                    #print("address actualizada a ", self.lf)

                else:
                    print("index out of range")
                    
            elif tipo == 'char':
                if self.lc < 31000:
                    address = self.lc
                    #print("se ha configurado la var", id, "local, la direccion es:", address)                   
                    self.lc += 1
                    #print("address actualizada a ", self.lc)
                    
                else:
                    print("index out of range")
            
            else:
                if self.lb < 33000:
                    address = self.lb
                    #print("se ha configurado la var", id, "local, la direccion es:", address)
                    self.lb += 1
                    #print("address actualizada a ", self.lb)

        return address
    
    
    
    
    def set_temp_direction(self, tipo, id, funId):
        if tipo == 'int':
            if self.gLi <13000:
                address = self.gLi
                #print("adress", address)
                #print("se ha configurado la var", id, "Local, la direccion es:", address)
                self.gLi += 1
                #print("address actualizada a ", self.li)
            else:
                    print("index out of range")

        elif tipo == 'float':
           if self.gLf < 15000:                
               address = self.gLf
               self.gLf += 1
           else:
                print("index out of range")
                    
        elif tipo == 'char':
            if self.gLc < 17000:
                address = self.gLc
                #print("se ha configurado la var", id, "local, la direccion es:", address)                   
                self.gLc += 1
                #print("address actualizada a ", self.lc)            
            else:
                print("index out of range")
            
        else:
            if self.gLb < 20000:                   
                address = self.gLb
                #print("se ha configurado la var", id, "local, la direccion es:", address)
                self.gLb += 1
                #print("address actualizada a ", self.lb)
        return address
  
            
     # CONSTANTES          
       
    def set_cte(self, val):
        if isinstance(val, int):
            if(self.ctei < 46000):
                address = self.ctei
                #print("constante entera se ha configurado con dir ",val, address)
                self.ctei += 1
                #print("constante entera updated ", self.ctei)
        
        elif isinstance(val, float):
            if self.ctef < 47000:
                address = self.ctef
                #print("constante flotante se ha configurado con dir",val, address)
                self.ctef += 1
                #print("constante flotante updated ", self.ctef)
        
        elif isinstance(val, str):
            if len(val)<2:
                if self.ctec < 48000:
                    address = self.cteString
                    #print("constante char se ha configurado con dir ",val ,address)
                    self.ctec += 1
                    #print("constante char updated ", self.ctec)
            else:
                if self.cteString < 49000:
                    address = self.cteString
                    #print("constante string se ha configurado con dir ",val, address)
                    self.cteString += 1
                    #print("constante string updated ", self.cteString)
        return address 
    
    def set_var_address(self, tipo, vid, funId):
        ad = self.set_var_direction(tipo, vid, funId)
        self.variables[vid]={
            'address': ad
        }
    def get_var_address(self, temp):
        if temp in self.variables.keys():
            return self.variables[temp]['address']
        
    def set_temp_address(self, tipo, vid, funId):
        ad = self.set_temp_direction(tipo, vid, funId)
        self.temporal[vid]={
            'address': ad
        }
    def get_temp_address(self, temp):
        if temp in self.temporal.keys():
            return self.temporal[temp]['address']
    

    def set_cte_address(self, val):
        #asigna una direccion de memoria para agregar al diccionario de ctes
        if self.get_cte_address(val) == -1:
            ad = self.set_cte(val)
            print("\tLa CONSTANTE", val, "ahora se ha guardado en ", ad)
            self.constants[val] = {
            'address': ad
            }
        
        
    def get_cte_address (self, val):
        if val in self.constants.keys():
            return self.constants[val]["address"]
        
        else:
            return -1
    
    def get_operator_address(self, op):
        if op in self.operators.keys():
            return self.operators[op]

        
    def reset_temp_vals(self):
        self.gLi = 19000
        self.gLf = 20000
        self.gLc = 21000
        self.gLb = 22000
        


# x = Memory()
# x.set_temp_address("int", "a", "Hola")
# x.set_temp_address("float", "b", "programa")
# print(x.get_temporal_address("a"))
# print(x.get_temporal_address("b"))

# print(x.get_cte_address(3.14))

# print(x.get_operator_address('+')