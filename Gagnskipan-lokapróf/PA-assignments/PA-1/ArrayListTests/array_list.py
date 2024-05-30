class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self): # TODO: DONE
        # TODO: remove 'pass' and implement functionality
        self.size = 0
        self.capacity = 2
        self.arr = [0] * self.capacity
        self.ordered = True

    #Time complexity: O(n) - linear time in size of list
    def __str__(self): # TODO: DONE
        return_string = ""
        
        if self.size == 0:
            return return_string

        for x in range(self.size):
            if (self.size - 1) == x:
                return_string += f"{self.arr[x]}"
            else:
                return_string += f"{self.arr[x]}, "

        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value): # TODO: DONE
        if self.size == self.capacity:
            self.resize()

        for x in range(self.size, 0, -1):
            self.arr[x] = self.arr[x - 1]

        self.arr[0] = value
        self.size += 1
        self.ordered = False
        #self.is_ordered()

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index): # TODO: DONE
        if 0 < index > self.size:
            raise IndexOutOfBounds
        
        if self.size == self.capacity:
            self.resize()

        """ Place all values from old arr to new_arr until the specified index """
        new_arr = [0] * (self.capacity + 1)
        for i in range(index):
            new_arr[i] = self.arr[i]

        new_arr[index] = value
        for i in range(index, self.size):
            new_arr[i + 1] = self.arr[i]

        self.arr = new_arr
        self.size += 1

    #Time complexity: O(1) - constant time
    def append(self, value): # TODO: DONE
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index): # TODO: DONE
        if 0 > index < (self.size - 1):
            raise IndexOutOfBounds
        if self.size == 0:
            raise Empty
        
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self): # TODO: DONE
        if self.size == 0:
            raise Empty
        
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index): # TODO: DONE
        if self.size == 0:
            raise Empty
        if index < 0 or index > (self.size - 1):
            raise IndexOutOfBounds
        
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_last(self): # TODO: DONE
        if self.size == 0:
            return Empty

        return self.arr[self.size - 1]
    
    #Time complexity: O(n) - linear time in size of list
    def resize(self): # TODO: DONE
        new_cap = self.capacity * 2
        new_arr = [0] * new_cap

        for index in range(self.size):
            new_arr[index] = self.arr[index]

        self.capacity = new_cap
        self.arr = new_arr

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index): # TODO: DONE
        if index < 0 or index >= self.size:
            raise IndexOutOfBounds

        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]

        self.size -= 1

    #Time complexity: O(1) - constant time
    def clear(self): # TODO: DONE
        if self.size == 0:
            pass
        else:
            self.arr = [0] * 2
            self.capacity = 2
            self.size = 0
            self.ordered = True

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value): # TODO: DONE
        self.is_ordered()
        if not self.ordered:
            raise NotOrdered
        
        index = 0
        while index < self.size and self.arr[index] < value:
            index += 1

        self.insert(value, index)

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value): # TODO: DONE
        for index in range(self.size):
            if self.arr[index] == value:
                return index
        raise NotFound

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value): # TODO: DONE
        index = self.find(value)
        self.remove_at(index)

    
    def is_ordered(self): # TODO: DONE
        for index in range(1, self.size):
            if self.arr[index - 1] > self.arr[index]:
                self.ordered = False
                return False
            self.ordered = True
            return True



if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    arr_lis.prepend(8)
    arr_lis.prepend(7)
    arr_lis.prepend(6)
    arr_lis.prepend(5)
    arr_lis.prepend(4)
    arr_lis.prepend(3)
    arr_lis.prepend(2)
    arr_lis.prepend(1)
    print(arr_lis)  
    get_last = arr_lis.get_last()
    get_first = arr_lis.get_first()
    get_index_zero = arr_lis.get_at(0)
    print("Get Last:", get_last)
    print("Get First", get_first)
    print("Index Zero:", get_index_zero)

    arr_lis.set_at(1000, 0)
    get_first = arr_lis.get_first()
    print("Expect 1000 -> got:", get_first)

    arr_lis.clear()
    arr_lis.prepend(8)
    arr_lis.prepend(7)
    arr_lis.prepend(6)
    arr_lis.prepend(5)
    arr_lis.prepend(4)
    arr_lis.prepend(3)
    arr_lis.prepend(2)
    arr_lis.prepend(1)

    arr_lis.insert_ordered(5)
    print(arr_lis)

    arr_lis.append(1000)
    print("Append 1000:", arr_lis)

    arr_lis.remove_at(5)
    print("remove at 5:", arr_lis)

    index_find = arr_lis.find(1000)
    print(index_find)

    arr_lis.remove_value(1000)
    print(arr_lis)