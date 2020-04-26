class VarGeneral: 
    def __init__(self, tipo, id, scope):
        self.tipo = tipo
        self.id = id
        self.scope = scope
        
        
class FunGeneral: 
    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id
    
        
class TabVarG():
    def __init__(self):
        self.tabVG = [VarGeneral]

    def add(self, VarGeneral):
        if not self.searchVarG(VarGeneral.id):
            self.tabVG.append(VarGeneral)
    
    def searchVarG(self, id): 
        if id in self.tabVG:
            return True
        return False

    def printVars(self):
        for i in self.tabVG:
            print (self.tabVG)


class TabFun():
    def __init__(self):
        self.tab_fun = []
        
    def add(self, FunGeneral):
        if not self.searchVarG(FunGeneral.id):
            self.tab_fun.append(FunGeneral)
    
    def searchVarG(self, id): 
        if id in self.tab_fun:
            return True
        return False
    
x= VarGeneral('int', 'a', 'global')
y = VarGeneral('char', 'v', 'local')

a = FunGeneral('void', 'MarcaBien')

tablaGen = TabVarG()
tablaGen.add(x)
tablaGen.add(y)

x1 = TabFun()
x1.add(a)

tablaGen.printVars()

