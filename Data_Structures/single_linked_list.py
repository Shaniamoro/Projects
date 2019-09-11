class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    # Appending to the end of the list O(n) complexity
    def end_sert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        cur_node = self.head
        if self.head is not None:
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node

    # Appending to the beginning of the list O(1) complexity
    def front_sert(self, data):
        self.head.data = data

        if self.head.data is not None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # Appending to the middle of the list
    def middle_sert(self,data):
        new_node = Node(data)
        len = self.length()
        cur_node = self.head

        if cur_node.data is None:
            self.head = new_node

        if len % 2 == 0:
            middle_index = len / 2
        else:
            middle_index = (len + 1)/2
        while middle_index > 1:
            middle_index -= 1
            cur_node = cur_node.next

        new_node.next = cur_node.next
        cur_node.next = new_node

    # Insert into a given index of the list
    def insert(self, val, index):
        if index > self.length():
            print('ERROR: Index is not within bounds ')
            return None
        new_node = Node(val)
        cur_node = self.head
        while index > 1:
            index -= 1
            cur_node = cur_node.next

        new_node.next = cur_node.next
        cur_node.next = new_node

    # Insert integer values from lowest to highest
    def sorted_insert(self, val):
        new_node = Node(val)
        cur_node = self.head
        if cur_node.data is None:
            cur_node.data = val
        while cur_node.data > new_node.data and cur_node.next is not None:
            cur_node = cur_node.next

        new_node.next = cur_node.next
        cur_node.next = new_node

    # Getting the size of our list
    def length(self):
        cur_node = self.head
        len = 0
        while cur_node.next is not None:
            len += 1
            cur_node = cur_node.next
        return len

    # Displaying the content of our list
    def print(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    # Search for data in a node based on it's index in the list
    def get_data(self, index):
        if index >=self.length() or index < 0:
            print ("ERROR : Index is not within bounds ")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index: return cur_node.data
            cur_index += 1

    # Search for a Node based on its value
    def delete(self, index):
        if index >= self.length():
            print("ERROR : Index is not within bounds ")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                prev_node.next = cur_node.next
                return
            cur_index += 1

    # Delete all nodes in the list
    def delete(self):
        cur_node = self.head
        while cur_node:
            prev = cur_node.next
            del cur_node.data
            cur_node = prev
        print('Linked List has been deleted')

    # Prints the list in linked list format
    def printlist(self):
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            if cur_node is None:
                print(None)
            else:
                print(cur_node.data, end='->')

    # Gets the last element in the linked list
    def get_tail(self):
        cur_node = self.head
        while cur_node:
            if cur_node.next is None:
                return cur_node
            cur_node = cur_node.next


myList = LinkedList()
for i in range(1, 10):
    myList.end_sert(i)
myList.printlist()



