





#Merge two sorted Linked List

class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def mergeTwoLists(l1, l2):
    #creating a dummy node with value 0 facilitate merging,creating new node with value of 0
    dummy = ListNode(0)
    #initializing pointer current to the dummy node
    current = dummy
#enters the loop and iterates untill both the l1 and l2 have elements
    while l1 and l2:
        #compares both the values of both loops and merge them in ascending order
        if l1.val < l2.val:
            #assign smaller node as next of the merged list
            current.next = l1
            l1 = l1.next
        else:
#assign smaller node as next of the merged list
            current.next = l2
            l2 = l2.next
            #moves the current pointer to next node in merged list
        current = current.next
#connects the left over nodes from l1 and l2 to the merged Linked list
    current.next = l1 if l1 else l2
#returns the next of the dummy which is the head of the merged List
    return dummy.next

# Function to print the linked list for testing purposes
def printLinkedList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Reading inputs and merging the lists
t = int(input())
for _ in range(t):
    values1 = list(map(int, input().split()))
    values2 = list(map(int, input().split()))

    head1 = ListNode(values1[0])
    current1 = head1
    for val in values1[1:]:
        if val != -1:
            current1.next = ListNode(val)
            current1 = current1.next

    head2 = ListNode(values2[0])
    current2 = head2
    for val in values2[1:]:
        if val != -1:
            current2.next = ListNode(val)
            current2 = current2.next

    result = mergeTwoLists(head1, head2)
    printLinkedList(result)
