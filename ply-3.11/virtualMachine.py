import sys
import time

error_message = '\033[91m' + "ERROR: " + '\033[0m' 

class VirtualMachine():
    def __init__(self):
        self.var = 0