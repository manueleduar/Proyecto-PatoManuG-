class Cube:
    def __init__(self):
        self.operators ={
            1:'+',
            2:'-',
            3:'*',
            4:'/',
            5:'<',
            6:'>',
            7:'<=',
            8:'>=',
            9:'==',
            10: '!=',
            11:'&&',
            12:'|' 
            }
        self.types= {
            1:'int',
            2:'float',
            3:'char',
            4:'bool',
            5:'CTEI',
            6:'CTEF',
            7:'CTEC',
            8:'CTESTRING',
            9:'ERROR',
            } 
        
    def cuboSemantico(self):
        self.compat={
            #int
            self.types[1]:{
                #int-int compatibility
                self.types[1]:{
                    self.operators[1]:self.types[1],
                    self.operators[2]:self.types[1],
                    self.operators[3]:self.types[1],
                    self.operators[4]:self.types[1],
                    self.operators[5]:self.types[4],
                    self.operators[6]:self.types[4],
                    self.operators[7]:self.types[4],
                    self.operators[8]:self.types[4],
                    self.operators[9]:self.types[4],
                    self.operators[10]:self.types[4],
                    self.operators[11]:self.types[4],
                    self.operators[12]:self.types[4],
                },
                #int-float compatibility
                self.types[2]:{
                    self.operators[1]:self.types[2],
                    self.operators[2]:self.types[2],
                    self.operators[3]:self.types[2],
                    self.operators[4]:self.types[2],
                    self.operators[5]:self.types[4],
                    self.operators[6]:self.types[4],
                    self.operators[7]:self.types[4],
                    self.operators[8]:self.types[4],
                    self.operators[9]:self.types[4],
                    self.operators[10]:self.types[4],
                    self.operators[11]:self.types[4],
                    self.operators[12]:self.types[4],
                    
                },
                #int-char compatibility
                self.types[3]:{
                    self.operators[1]:self.types[9],
                    self.operators[2]:self.types[9],
                    self.operators[3]:self.types[9],
                    self.operators[4]:self.types[9],
                    self.operators[5]:self.types[9],
                    self.operators[6]:self.types[9],
                    self.operators[7]:self.types[9],
                    self.operators[8]:self.types[9],
                    self.operators[9]:self.types[9],
                    self.operators[10]:self.types[9],
                    self.operators[11]:self.types[9],
                    self.operators[12]:self.types[9],
                },
            },
            #float
            self.types[2]:{
                    #float-int compatibility
                self.types[1]:{
                    self.operators[1]:self.types[9],
                    self.operators[2]:self.types[9],
                    self.operators[3]:self.types[9],
                    self.operators[4]:self.types[9],
                    self.operators[5]:self.types[9],
                    self.operators[6]:self.types[9],
                    self.operators[7]:self.types[9],
                    self.operators[8]:self.types[9],
                    self.operators[9]:self.types[4],
                    self.operators[10]:self.types[4],
                    self.operators[11]:self.types[4],
                    self.operators[12]:self.types[4],
                
                },
                #float-char compatibility
                self.types[2]:{
                    self.operators[1]:self.types[2],
                    self.operators[2]:self.types[2],
                    self.operators[3]:self.types[2],
                    self.operators[4]:self.types[2],
                    self.operators[5]:self.types[4],
                    self.operators[6]:self.types[4],
                    self.operators[7]:self.types[4],
                    self.operators[8]:self.types[4],
                    self.operators[9]:self.types[4],
                    self.operators[10]:self.types[4],
                    self.operators[11]:self.types[4],
                    self.operators[12]:self.types[4],
                    
                },
                #float-char compatibility
                self.types[3]:{
                    self.operators[1]:self.types[9],
                    self.operators[2]:self.types[9],
                    self.operators[3]:self.types[9],
                    self.operators[4]:self.types[9],
                    self.operators[5]:self.types[9],
                    self.operators[6]:self.types[9],
                    self.operators[7]:self.types[9],
                    self.operators[8]:self.types[9],
                    self.operators[9]:self.types[9],
                    self.operators[10]:self.types[9],
                    self.operators[11]:self.types[9],
                    self.operators[12]:self.types[9],
                },
                
            },
            #char
            self.types[3]:{
                    #char-int compatibility
                self.types[1]:{
                    self.operators[1]:self.types[9],
                    self.operators[2]:self.types[9],
                    self.operators[3]:self.types[9],
                    self.operators[4]:self.types[9],
                    self.operators[5]:self.types[9],
                    self.operators[6]:self.types[9],
                    self.operators[7]:self.types[9],
                    self.operators[8]:self.types[9],
                    self.operators[9]:self.types[9],
                    self.operators[10]:self.types[9],
                    self.operators[11]:self.types[9],
                    self.operators[12]:self.types[9],
                },
                #char-float compatibility
                self.types[2]:{
                    self.operators[1]:self.types[9],
                    self.operators[2]:self.types[9],
                    self.operators[3]:self.types[9],
                    self.operators[4]:self.types[9],
                    self.operators[5]:self.types[9],
                    self.operators[6]:self.types[9],
                    self.operators[7]:self.types[9],
                    self.operators[8]:self.types[9],
                    self.operators[9]:self.types[9],
                    self.operators[10]:self.types[9],
                    self.operators[11]:self.types[9],
                    self.operators[12]:self.types[9],
                    
                },
                #int-char compatibility
                self.types[3]:{
                    self.operators[1]:self.types[9],
                    self.operators[2]:self.types[9],
                    self.operators[3]:self.types[9],
                    self.operators[4]:self.types[9],
                    self.operators[5]:self.types[9],
                    self.operators[6]:self.types[9],
                    self.operators[7]:self.types[9],
                    self.operators[8]:self.types[9],
                    self.operators[9]:self.types[4],
                    self.operators[10]:self.types[4],
                    self.operators[11]:self.types[4],
                    self.operators[12]:self.types[4],
                },
                
            },

        }    
    
    def printO(self):
        print(self.operators[1])
        print(self.types[1])
        
x = Cube()
x.printO()