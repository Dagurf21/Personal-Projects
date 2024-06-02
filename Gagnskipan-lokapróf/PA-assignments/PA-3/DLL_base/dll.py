
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self): #TODO -> Done
        self.head = Node("head") # Sentinel Node as head
        self.tail = Node("tail") # Sentinel Node as tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current = None

    def insert(self, data): # TODO -> Done
        new_node = Node(data)
        
        # If list is empty, head.next should be pointing to tail
        if self.head.next == self.tail and self.tail.prev == self.head:
            # Adjust pointers to insert the new node between head and tail
            new_node.prev = self.head
            new_node.next = self.tail
            self.head.next = new_node
            self.tail.prev = new_node
        else:
            # Insert the new node in front of the current node
            new_node.prev = self.current.prev
            new_node.next = self.current
            if self.current.prev is not None:
                self.current.prev.next = new_node
            self.current.prev = new_node
        
        # Move current to the new node
        self.current = new_node

    def remove(self): # TODO -> Done
        # Starting at some position
        if self.current and self.current != self.head and self.current != self.tail:
            # Set the prev pointer of the current node to the prev pointer of the next node
            prev_node = self.current.prev
            next_node = self.current.next

            prev_node.next = next_node
            next_node.prev = prev_node

            self.current = prev_node

    def get_value(self): # TODO -> Done
        if self.current:
            return self.current.data
        else:
            return None

    def move_to_next(self): # TODO -> Done
        # Base cases
        if self.is_empty():
            raise Exception("List is empty")
        elif self.current is None: 
            raise Exception("Current is not set")
        elif self.current.next == self.tail: # Current is at tail
            raise Exception("At tail")
        else:
            # Move the current to next
            self.current = self.current.next

    def move_to_prev(self): # TODO -> Done
        if self.is_empty():
            raise Exception ("List is empty")

        if self.current.prev == self.head:
            raise Exception ("Already at front of list")

    def move_to_pos(self, pos): # TODO -> Done
        length = len(self)
        
        self.current = self.head
        if (length) > pos and pos > 0:
            for _ in range(pos): 
                self.current = self.current.next

    def clear(self): # TODO -> Done
        if self.is_empty():
            return

        self.head = Node("head") # Sentinel Node as head
        self.tail = Node("tail") # Sentinel Node as tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current = None

    def get_first_node(self): #TODO -> Done
        return self.head.next.data

    def get_last_node(self): #TODO -> Done
        return self.tail.prev.data

    def partition(self, low, high):
        pass

    def is_empty(self): # TODO -> Done
        return self.head.next == self.tail

    def __len__(self): #TODO -> Done
        current = self.head.next
        length = 0
        while current != self.tail:
            length += 1
            current = current.next

        return length

    def __str__(self): #TODO -> Done
        ret_str = ""

        current = self.head.next # Start from the first actual node
        while current != self.tail: # Stop at the tail sentinel
            ret_str += str(current.data) + " "
            current = current.next
        
        return ret_str

if __name__ == "__main__":
    #create tests here if you want
    dll = DLL()

    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(4)
    dll.insert(5)
    dll.insert(6)
    dll.insert(7)
    dll.insert(8)
    dll.insert(9)

    print (dll)
    first = dll.get_first_node()
    last = dll.get_last_node()
    print ("First :", first)
    print ("Last : ", last)

    print (dll.get_value())
    dll.move_to_next()
    
    dll.move_to_pos(4)
    print (dll.get_value())

