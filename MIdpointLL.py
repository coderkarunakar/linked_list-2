

#Finding a Midpoint of Linked List



#Note:please look  our class notes as well
#Example:1->2->3->4->5
#in this case LL is 3
#we can find it by using a (length -1/2)=(5-1)/2=2 is index no i.e 3
#1->2->3->4->5->6
#in the above example the midpoint of the linked list is 3, (length-1)/2=(6-1)/2=2index (try to take a lesser no)

#instead of this we can use another approach as well okay let us maintain  2 points i.e x and 2x as 2 points(name this as slow and fast )
#where as x reaches mid of the linked list and 2x will reach end of the linked list

#the terminology will be like slow=slow.next,fast=fast.next.next(which will be 2 times faster than the slow)
#and we need to stop this at fast.next==null
#for another approach to stop is like fast.next.next==1 which means there is only 1 point at the last
#if any of the condition will work i need to stop


# Define the ListNode class and the find_midpoint function (as previously shown).
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_midpoint(head):
    if not head:
        return None

    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

# Function to create a linked list from user input.
def create_linked_list():
    values = input("Enter space-separated values for the linked list: ").split()
    if not values:
        return None

    # Initialize the head of the linked list.
    head = ListNode(int(values[0]))
    current = head

    # Create nodes for the linked list.
    for value in values[1:]:
        current.next = ListNode(int(value))
        current = current.next

    return head

# Main program
head = create_linked_list()

if head:
    midpoint_node = find_midpoint(head)

    if midpoint_node:
        print("Midpoint value:", midpoint_node.value)
    else:
        print("The linked list is empty.")
else:
    print("No input provided for the linked list.")

    #Question
# Code: Midpoint of LL

# Send Feedback

# For a given singly linked list of integers, find and return the node present at the middle of the list.

# Note :

# If the length of the singly linked list is even, then return the first middle node.

# Example: Consider, 10 -> 20 -> 30 -> 40 is the given list, then the nodes present at the middle with respective data values are, 20 and 30. We return the first node with data 20.

#  Input format :

# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space. 

# Remember/Consider :

# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

#  Output Format :

# For each test case/query, print the data value of the node at the middle of the given list.

# Output for every test case will be printed in a seperate line.

# Constraints :

# 1 <= t <= 10^2

# 0 <= M <= 10^5 

# Where M is the size of the singly linked list.

# Time Limit: 1sec

# Sample Input 1 :

# 1

# 1 2 3 4 5 -1

# Sample Output 1 :

# 3

# Sample Input 2 :

# 2 

# -1

# 1 2 3 4 -1

# Sample Output 2 :

# 2
# Definition for a singly linked list node
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    if not head:
        return None
    
    slow_ptr = head
    fast_ptr = head
    
    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    
    return slow_ptr

# Function to create a linked list from a list of integers
def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for item in arr[1:]:
        current.next = ListNode(item)
        current = current.next
    
    return head

# Function to print the data value of the middle node
def print_middle_node(head):
    middle_node = find_middle(head)
    if middle_node:
        print(middle_node.data)

# Input handling
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    head = create_linked_list(arr)
    print_middle_node(head)
