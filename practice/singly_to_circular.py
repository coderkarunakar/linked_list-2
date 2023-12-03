class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def convert_to_circular(self):
        if not self.head:
            print("Empty list, cannot convert to circular.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.head  # Connect last node to the head to make it circular

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break  # Exit loop if the circular link is reached
        print()

# Example Usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    print("Singly Linked List:")
    linked_list.display()

    linked_list.convert_to_circular()

    print("\nCircular Linked List:")
    linked_list.display()
