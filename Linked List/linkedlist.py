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

