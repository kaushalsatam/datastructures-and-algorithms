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


my_linked_list = LinkedList(11)
my_linked_list.append(12)
my_linked_list.append(13)
my_linked_list.append(14)
my_linked_list.append(15)
print("Linked List before Popping")
my_linked_list.print_list()
print("Linked List after Popping")
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
my_linked_list.print_list()
