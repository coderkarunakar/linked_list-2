# Python Program to Check whether a Singly Linked List is a Palindrome
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

    def is_palindrome(self):
            # Create an empty list to store the values of the linked list nodes
        values = []
            # Set the current node to the head of the linked list
        current = self.head
            # Traverse the linked list and store the values of each node in the list
        while current:
                    # Append the value of the current node to the 'values' list
            values.append(current.value)
                    # Move to the next node in the linked list
            current = current.next
      # Check if the list of values is equal to its reverse
    # Return True if it is a palindrome, False otherwise
    # #this below line reverses the whole LL and compares      
        return values == values[::-1]

# Example usage:
# Create a linked list
linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(2)
linked_list.add(1)

print("Linked List:")
linked_list.print_list()

if linked_list.is_palindrome():
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
