#DOUBT IN THIS CODE:

#creating a node class 
class Node:
    #constructor with self,data parameters ,data and none as there attributes
    def __init__(self, data):
        self.data = data
        self.next = None
#it serves the structure  of implementation of a linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
#append method adds a new node to the end of the Linked List 
    def append(self, data):
        new_node = Node(data)
        #if the list is empty,it sets both head and tail to the new node
        #otherwise,it adds new node to the end of the list and updtes the tail pointer.
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
#sorts the linked list using merge sort algorithm
#it recursively divides the linked list into smaller halves untill individual nodes are reached
#it uses the merge method to merge and sort  the divided halves
    def merge_sort(self, head):
        #there is one element or the list is already sorted
        if not head or not head.next:
            #returns the head
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.merge(left, right)
        return sorted_list
        #merge method merges two sorted linkedlist(left and right) returns a single sorted linked list
        #it compares the data of the nodes in the left and right and merges them in ascending order
        #recursively merges the list untill all elements are sorted

    def merge(self, left, right):
        result = None
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)

        return result

#get middle method finds the midddle node of the linked list using the slow and fast pointer approach
    def get_middle(self, head):
        #linked list is empty or it contains only one element in linked list
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow
#print list method  prints  the elemnts of the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

#this below method means that it allows the main method only in script format and it does not allow you to the other elements as  module in this file 
#it has only this script have to run and allow ,other files are not allowed 


if __name__ == "__main__":
    linked_list = LinkedList()

    n = int(input("Enter the number of elements: "))
    print("Enter the elements:")
    for _ in range(n):
        data = int(input())
        linked_list.append(data)


# Printing the original linked list
    print("\nOriginal Linked List:")
    linked_list.print_list()
# Sorting the linked list using merge sort
    linked_list.head = linked_list.merge_sort(linked_list.head)

    print("\nSorted Linked List:")
    linked_list.print_list()
#first take no of elements like 5 or any
#then enter those 5 or any elements one after another by clicking enter button.     