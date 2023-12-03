class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            #below one points to itself
            #Result: head -> 1 -> (points to itself)
            new_node.next = self.head
        else:
# Start from the head of the list
            temp = self.head
            # Traverse the list until reaching the node whose next pointer points back to the head
            while temp.next != self.head:
                # Result: head -> 1 -> 2 -> (points back to 1)
                 # Move to the next node in the list
                temp = temp.next
             # Set the next pointer of the last node to the new node 
            temp.next = new_node
            # Make the new node's next pointer point back to the head, completing the circular structure
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            #since we made a connection at last points to first(self.head) so break no need to 1 again
            
            if temp == self.head:
                break
        print()

if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3) 
    cll.append(4)

    print("Circular Linked List:")
    cll.display()
