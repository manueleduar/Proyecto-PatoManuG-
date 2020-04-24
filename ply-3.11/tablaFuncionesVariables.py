class tabFun:
    def __init_(self):
        self.tab_funciones = {}
    def add(self, element:tuple):
        self.tab_funciones.update(element)

class tabVar:
    def __init__(self):
        self.tab_variables = {}
    def add(self, element: tuple):
        self.tab_variables.update(element)

# class element: 
#     def __init__(self, iden_elemento, tipo_elemento, scope_elemento):
#         self.iden_elemento = iden_elemento
#         self.tipo_elemento = tipo_elemento
#         self.scope_elemento = scope_elemento
    
#     # setters
#     def set_iden(self, iden):
#         self.iden = iden
    
#     def set_tipo(self, tipo):
#         self.tipo = tipo
    
#     def set_scope(self, scope):
#         self.scope = scope    
    
#     # getters
#     def get_tipoElement(self):
#         return self.tipo_elemento
    
#     def getIdenElemento(self):
#         return self.iden_elemento
    
#     def get_ScopeElemento(self):
#         return self.scope_elemento
