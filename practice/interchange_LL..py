# Python Program to Interchange two Elements of the List without touching the Key Field
# Node class to create individual nodes for the linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList class to manage the nodes and perform operations on the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a new node at the end of the linked list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Method to print the linked list
    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    # Method to interchange two elements without changing the key field
    def interchange_elements(self, index1, index2):
        #checks both are same ,if same there is nothing to swap
        if index1 == index2:
            #return empty i.e nothing
            return

        prev1 = None
        current1 = self.head
        count1 = 0
        while current1 and count1 != index1:
            prev1 = current1
            current1 = current1.next
            count1 += 1

        prev2 = None
        current2 = self.head
        count2 = 0
        while current2 and count2 != index2:
            prev2 = current2
            current2 = current2.next
            count2 += 1
#ikadiki ah index point ki reach avtai
#this means current1,current2 is None then return nothing
        if not current1 or not current2:
            return
#after reaching that particular index that value points to current2 value
#ah index point lodi current2 value ki point chestai
        if prev1:
            prev1.next = current2
            #if prev1 doesnot exist current1 is the head of the LL,self.head is updated to current2,making current2 is the new head of the LL
        else:
            self.head = current2

#if prev2 exist then at that value pointing to current1 value
#ah index point lodi current2 value ki point chestai

        if prev2:
            prev2.next = current1
            #if prev 2 does not exist then head points to current1
        else:
            self.head = current1
            
            #after pointing completing this swaping takes place inorder to point to next value
#here swaping is taking place curr1 with curr2 and curr2 with curr1
#finaly pointing chesin tarvata next unna values ni ila swap chesi point cheyachu
        current1.next, current2.next = current2.next, current1.next

# Example usage:
if __name__ == "__main__":
    # Creating a linked list
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    # Displaying the original linked list
    print("Original Linked List:")
    linked_list.display()

    # Interchanging elements at indices 1 and 3
    linked_list.interchange_elements(1, 3)

    # Displaying the modified linked list after interchanging elements
    print("\nLinked List after interchanging elements at indices 1 and 3:")
    linked_list.display()
