class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
    
    def push_front(self, data): # TODO -> DONE
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
        
    def pop_front(self):
        if self.head is None:
            return
        
        self.head = self.head.next
    
    def push_back(self, data): # TODO -> DONE
        new_node = Node(data)
        curr = self.head
        
        if self.head is None:
            self.head = new_node
            return

        # Walk to end of list
        while (curr.next):
            curr = curr.next

        curr.next = new_node

    def pop_back(self):
        if self.head is None:
            return
        
        curr = self.head
        while (curr.next.next):
            curr = curr.next

        curr.next = None
        

    def get_size(self): # TODO -> DONE
        curr = self.head
        counter = 0
    
        while curr is not None:
            counter += 1
            curr = curr.next

        return counter
    
    def __str__(self): # TODO -> DONE
        ret_str = ""
        curr = self.head
        while curr:
            ret_str += (f"{str(curr.data)} ")
            curr = curr.next

        return ret_str
    


ll = LinkedList()
ll.push_back(1)
ll.push_back(2)
ll.push_back(3)
ll.push_back(4)
ll.push_back(5)
ll.push_back(6)
print(ll)

size = ll.get_size()
print(size)
ll.pop_front()
print(ll)

ll.pop_back()
print(ll)