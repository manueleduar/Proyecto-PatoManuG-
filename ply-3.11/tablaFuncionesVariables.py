class tabVar:
    def __init__(self):
        self.var_list ={}
        
    def add(self, tipo, id):
        self.var_list[id] ={
            'tipo': tipo
        }
    def search_vars(self, id):
        return id in self.var_list
    
    def print_vars(self):
        for i in self.var_list:
            print('Variable', i, 'se encuentra en la tabla de variables')
        

class tabFun():
    def __init__(self):
        self.funciones = {}

    def add_Fun(self, tipo, id, nParams, tParams, idParams, nvars):
        if id not in self.funciones.keys():
            self.funciones[id] = {
                'tipo' : tipo, # tipo de funcion
                'nParams' : nParams, # numero de parametros
                'tParams' : tParams, # tipo de parametros
                'idParams' : idParams, # nombre de parametros
                'vars' : tabVar(),
                'nvars' : nvars # numero de variables
            }
            print('\nFuncion añadida:', id)
        else:
            print('La funcion' , id , 'ya existe')

    def search_tabFun(self, id):
        return id in self.funciones 
        
    def addVar(self, fid, tipo, id):
        if (self.funciones[fid]['vars'].search_vars(id)):
            print('La variable', id, 'ya existe')
        else:
            self.funciones[fid]['vars'].add(tipo, id)
            print('Variable', id, 'fue añadida exitosamente')
            
    def print_fun_vars(self, fid):
        if id in self.funciones:
            self.funciones[fid]['vars'].print_vars()