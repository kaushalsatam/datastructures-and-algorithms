class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None

class LinkedList:
    # Linked List constructor
    def __init__(self, value) :
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # method to print Linked List
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # method to append a Node in the Linked List(Last)
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # method to pop a Node from the Linked List(Last)
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None

            self.length -= 1
            return temp.value
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            pre.next = None
            self.length -= 1
            return temp.value

    # method to prepend a Node to the Linked List(First)
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # method to Pop First Node from the Linked List(First)
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        if self.length == 0:
            self.tail = None
        self.length -= 1
        return temp

    # method to get value of the Node from a particular index
    def get(self, index):
        if index >= self.length or index < 0:
            return None
        temp = self.head
        # count = 0
        # while count != index:
        #     temp = temp.next
        #     count += 1
        # underscore _ is used because the value is not going to be used in the loop
        for _ in range(index):
            temp = temp.next
        return temp

    # method to set value of the Node at a particular index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp.value == None:
            return False
        temp.value = value
        return True

    # method to insert a Node into the Linked List at a particular index
    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        temp = self.get(index - 1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    # method to remove Node at a particular index from the Linked List
    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # method to reverse the Linked List
    def reverse(self):
        # reverse the head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linked_list = LinkedList(11)
my_linked_list.append(12)
my_linked_list.append(13)
my_linked_list.append(14)
my_linked_list.append(15)
my_linked_list.print_list()
print("Linked List after prepend")
my_linked_list.prepend(10)
my_linked_list.prepend(9)
my_linked_list.print_list()
print("Linked List after pop first")
my_linked_list.pop_first()
my_linked_list.pop_first()
my_linked_list.print_list()
print(f"Node at index 3: {my_linked_list.get(3)}")
print("Linked List after set value at position (3)")
my_linked_list.set_value(3, 69)
my_linked_list.print_list()
print("Linked List after inserting node at position (3)")
my_linked_list.insert(3, 18)
my_linked_list.print_list()
print("Linked List after removing node at position (3)")
my_linked_list.remove(3)
my_linked_list.print_list()
print("Reversed Linked List")
my_linked_list.reverse()
my_linked_list.print_list()
