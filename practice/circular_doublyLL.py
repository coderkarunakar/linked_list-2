#implement circular doubly LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        #here extra one more in doubly
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        #creating an empty  Linkedlist
        self.head = None

    # Function to insert a node at the beginning of the circular doubly linked list
    def insert_beginning(self, data):
        #creating a new node
        new_node = Node(data)
        if self.head is None:
            #if the head is None (i.e LL is empty )creating a new node and making to point its next and prev points to itself
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node

        else:
            #since it is a circular doubly LL self.head.prev refers to last node which was created earlier
            last = self.head.prev
            #it sets next point of new node to point to the current head of the LL  (establishes link between new node and the node that was previously head of the LL)
            new_node.next = self.head
            #sets the prev pointer of new node to point to the node that was previously the last node in the LL
            new_node.prev = last
            #updates the next pointer of the  previously lastnode to point to the new node ,this links the last node to the new node,making the new node the head  of the list
            last.next = new_node
            #updates the prev pointer of current head node to point to the new node ,this maintains the circular list by linking the prev head pointer to the new head(the insertion node)
            self.head.prev = new_node
            # updates the  head pointer of the LL to point to the newnode,this makes newly inserted node the new head of circular doubly linkedlist
            self.head = new_node

    # Function to insert a node at the end of the circular doubly linked list
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            last.next = new_node
            self.head.prev = new_node

    # Function to display the circular doubly linked list
    def display(self):
        if self.head is None:
            print("The list is empty")
            return

        current = self.head
        print("Nodes of the circular doubly linked list:")
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

# Example usage:
circular_dll = CircularDoublyLinkedList()
circular_dll.insert_beginning(5)
circular_dll.insert_beginning(3)
circular_dll.insert_end(7)
circular_dll.display()
