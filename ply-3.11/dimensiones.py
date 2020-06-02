class Node ():
    def __init__(self, superior, o):
        self. superior = superior
        self.o = o
        self.next = None

class Dims (Node):
    def __init__(self):
        self.head = None
        self.prev = None
    
    def push (self, superior, o):
        nuevo = Node(superior, o)
        
        if self.head is None:
            self.head = nuevo
            return
        last = self.head
        while(last.next):
            last = last.next
            
        last.next = nuevo
        
   



