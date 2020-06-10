from mem import Memory

class tabVar:
    def __init__(self):
        self.var_list ={}
             
    def add(self, tipo, id, address):
        self.var_list[id] ={
            'tipo': tipo,
            'address': address
        }
        
    def search_vars(self, id):
        return id in self.var_list.keys()
    
    def print_vars(self):
        print(self.var_list.items())

    def get_Tipo(self, id):
        return self.var_list[id]['tipo']

    # def get_dir_memoria(self, id):
    #     return self.var_list[id]["address"]
        

class tabFun():
    
    def __init__(self):
        self.funciones = {}
        self.m = Memory()

    def add_Fun(self, tipo, id, nParams, tParams, idParams, nvars):
        if self.funciones.get(id) == None:
            self.funciones[id] = {
                'tipo' : tipo, # tipo de funcion
                'nParams' : nParams, # numero de parametros
                'tParams' : tParams, # tipo de parametros
                'idParams' : idParams, # nombre de parametros
                'vars' : tabVar(),
                'nvars' : nvars # numero de variables
            }
            
        # else:
        #     print('La funcion' , id , 'ya existe')

    def search_tabFun(self, id):
        return id in self.funciones


    def searchVar_tabFun(self, fid, id):
        if self.funciones[fid]['vars'].search_vars(id) or self.funciones['programa']['vars'].search_vars(id):
            return True
        else: 
            print('La variable', id, 'no existe...')
            

    def getVar_Tipo(self, id, fid):
        if self.funciones[fid]['vars'].search_vars(id):
            return self.funciones[fid]['vars'].get_Tipo(id)
        else:
            print('La variable', id, 'no existe...')



    
    def addVar(self, fid, tipo, id):
        #si ya existe en local no lo agrega 
        if self.funciones[fid]['vars'].search_vars(id):
            print('La variable', id, 'ya existe en el scope', fid)


        # si no existe en el local aun lo agrego
        elif not self.funciones[fid]['vars'].search_vars(id):
            ad = self.m.set_var_direction(tipo, id, fid)
            self.funciones[fid]['vars'].add(tipo, id, ad)
            self.funciones[fid]['nvars'] = self.funciones[fid]['nvars'] + 1
            #print("no existe en local aun se va a agregar")


        # si existe como global no lo agrego
        elif self.funciones['programa']['vars'].search_vars(id):
            print('La variable', id, 'ya existe en el programa como global')
        

        # si no existe como global lo agrego como global
        elif self.funciones['programa']['vars'].search_vars(id):
            ad = self.m.set_var_direction('programa', id, fid)
            self.funciones['programa']['vars'].add(tipo, id, ad)
            self.funciones['programa']['nvars'] = self.funciones[fid]['nvars'] + 1

  
            
    
   
    def add_var_mem(self, tipo, vid, funId):
        self.m.set_var_address(tipo, vid, funId)    
        

    def get_var_mem(self, var):
        return self.m.get_var_address(var)


    def getNumeroParametros(self, fid):
        return self.funciones[fid]['nParams']

    def add_parametros_tabFun(self, fid, nameVar, varTipo):
        self.funciones[fid]['nParams'] = self.funciones[fid]['nParams'] + 1
        self.funciones[fid]['idParams'].append(nameVar)
        self.funciones[fid]['tParams'].append(varTipo)
    
    
    def add_temp_mem(self, tipo, vid, funId):
       self.m.set_temp_address(tipo, vid, funId)    
        

    def get_temp_mem(self, temp):
        return self.m.get_temp_address(temp)
        

    def add_cte_mem(self, val):
        self.m.set_cte_address(val)
        

    def get_cte_mem(self, val):
        return self.m.get_cte_address(val) 
    

    def get_op_mem(self, op):
        return self.m.get_operator_address(op)
          
    def reset_temp_add(self):
        self.m.reset_temp_vals()
            
    def print_fun_vars(self, fid):
        if fid in self.funciones:
            self.funciones[fid]['vars'].print_vars()
            



