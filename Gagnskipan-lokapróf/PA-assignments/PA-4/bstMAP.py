class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Node:
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"Node(key={self.key}, data={self.data})"

class BSTMap:
    
    def __init__(self) -> None:
        self.root = None

    def insert(self, key, data):
        if self.root is None:
            self.root = Node(key, data)
        else:
            self._insert(self.root, key, data)

    def _insert(self, current_node, key, data):
        if key < current_node.key:  # To the left
            if current_node.left is None:
                current_node.left = Node(key, data)
            else:
                self._insert(current_node.left, key, data)
        elif key > current_node.key:  # To the right
            if current_node.right is None:
                current_node.right = Node(key, data)
            else:
                self._insert(current_node.right, key, data)
        else:  # If the key already exists update the value
            raise ItemExistsException

    def update(self, key, data):
        if self.root is None:
            raise NotFoundException
        else:
            self._update(self.root, key, data)

    def _update(self, current_node, key, data):
        if key < current_node.key:  # To the left
            if current_node.left is None:
                raise NotFoundException
            else:
                self._update(current_node.left, key, data)
        elif key > current_node.key:  # To the right
            if current_node.right is None:
                raise NotFoundException
            else:
                self._update(current_node.right, key, data)
        elif key == current_node.key:  # Key found
            current_node.data = data
        else:
            raise NotFoundException

    def find(self, key):
        if self.root is None:
            raise NotFoundException
        else:
            return self._find(self.root, key)
            
    def _find(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None: 
                raise NotFoundException
            else:
                return self._find(current_node.left, key)
        
        elif key > current_node.key:
            if current_node.right is None:
                raise NotFoundException
            else:
                return self._find(current_node.right, key)
        
        elif key == current_node.key:
            return current_node.data
        
        else:
            raise NotFoundException

    def contains(self, key):
        if self.root is None:
            return False
        else:
            return self._contains(self.root, key)

    def _contains(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                return False
            else:
                return self._contains(current_node.left, key)
        
        if key > current_node.key:
            if current_node.right is None:
                return False
            else:
                return self._contains(current_node.right, key)

        if key == current_node.key:
            return True
    
        else:
            raise NotFoundException

    def __str__(self) -> str:
        elements = []
        self._in_order_traversal(self.root, elements)
        return " ".join(f"{{{key}:{data}}}" for key, data in elements)

    def _in_order_traversal(self, node, elements):
        if node:
            self._in_order_traversal(node.left, elements)
            elements.append((node.key, node.data))
            self._in_order_traversal(node.right, elements)

    def __setitem__(self, key, data):
        if self.contains(key): 
            self.update(key, data)
        else:
            self.insert(key, data)
    
    def __getitem__(self, key):
        if self.contains(key):
            return self.find(key)
        else:
            raise NotFoundException

    def __len__(self):
        elements = []
        self._in_order_traversal(self.root, elements)
        return len(elements)
        

# Usage Example
bst_map = BSTMap()
bst_map.insert(10, 'ten')
bst_map.insert(5, 'five')
bst_map.insert(15, 'fifteen')
bst_map.insert(3, 'three')
bst_map.insert(7, 'seven')

print("output: " + str(bst_map))  # Output: {3:three} {5:five} {7:seven} {10:ten} {15:fifteen}


