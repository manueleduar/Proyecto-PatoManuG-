class TablaGlobal:
    def __init_(self):
        self.tab_global = {}

    def add(self, objeto):
        if not self.search(objeto.id):
            self.tab_global.update(objeto.tipo, objeto.id)
        
    def search(self, id):
        if (id in self.tab_global.keys()):
            return True
        return False
                

    def print_elements(self):
        print(*self.tab_global)
                
        
        
        
class TablaFun:
    def __init_(self):
        self.tab_funciones = {}



class TablaVar:
    def __init__(self):
        self.tab_variables = {}

        
class Objeto ():
    def __init__(self, tipo, id):
        self.id = id
        self.tipo = tipo
        
    # setters
    def set_ID(self, id): 
        self.id = id
        
    def set_Tipo(self, tipo):
        self.tipo = tipo
    
    # getters
    def get_ID(self):
        return self.id

    def get_Tipo(self):
        return self.tipo
        
        
        
        



