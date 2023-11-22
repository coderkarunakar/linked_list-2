class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        #it means initially the head is none then create a new node
        #Note:self.head is an some existing value so not is used
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse_iterative(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            #this line finally points to end of the LL and which makes reverse and points to all the values of prev and we get reverse of the Linked list
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
# Create a linked list and add nodes based on user input
linked_list = LinkedList()

# Taking user input for linked list elements
values = input("Enter the elements of the linked list separated by space: ").split()

for value in values:
    linked_list.add_node(value)

print("Original Linked List:")
linked_list.display()

# Reverse the linked list
linked_list.reverse_iterative()

print("Reversed Linked List:")
linked_list.display()
 