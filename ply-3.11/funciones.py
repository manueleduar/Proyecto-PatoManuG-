class FuncionesID:
    def __init__(self, address, id):
        self.address = address
        self.id = id

class Direccion_Funcion:
    def __init__(self):
        self.directory = dict()

    def set(self, address, id):
        self.directory[address] = id

    def get_fun_address(self, address):
        return self.directory[address]

    def contains(self, key):
        return key in self.directory