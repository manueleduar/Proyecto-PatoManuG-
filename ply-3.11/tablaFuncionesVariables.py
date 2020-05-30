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

    def get_dir_memoria(self, id):
        return self.var_list[id]["address"]
        

class tabFun():
    def __init__(self):
        self.funciones = {}

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
            print('\nFuncion añadida:', id)
            
        else:
            print('La funcion' , id , 'ya existe')

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
        if (self.funciones[fid]['vars'].search_vars(id) or self.funciones['programa']['vars'].search_vars(id)):
            print('La variable', id, 'ya existe')
        else:
            #m = Memory()
            #ad = m.set_var_direction(tipo, id, fid)
            self.funciones[fid]['vars'].add(tipo, id, -1)
           
            
    def print_fun_vars(self, fid):
        if fid in self.funciones:
            self.funciones[fid]['vars'].print_vars()


