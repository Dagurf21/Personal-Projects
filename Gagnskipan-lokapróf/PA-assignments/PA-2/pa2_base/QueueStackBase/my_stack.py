from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self):        
        self.container = ArrayDeque()

    def push(self, data):
        self.container.push_front(data)
    
    def pop(self):
        self.container.pop_front()
    
    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return str(self.container)
    

a = Stack()

a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)

print(a)
a.pop()
print(a)
