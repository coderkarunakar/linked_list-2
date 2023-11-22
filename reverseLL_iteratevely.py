# 1->2->3->4->5->None
#after reversing we should get like
# 5->4->3->2->1->None
#use chatgpt or 9th video in LL part 2 get iterative reverseLL approach 

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next  # Save the next node
        current.next = prev      # Reverse the link

        # Move prev and current one step forward
        prev = current
        current = next_node

    # Update the head of the reversed list
    head = prev

    return head

# Function to create a linked list from user input
def create_linked_list():
    input_values = input("Enter space-separated values for the linked list: ").split()
    head = None
    prev = None

    for value in input_values:
        node = ListNode(int(value))
        if head is None:
            head = node
        else:
            prev.next = node
        prev = node

    return head

# Main program
if __name__ == "__main__":
    # Create a linked list from user input
    head = create_linked_list()

    # Reverse the linked list
    head = reverse_linked_list(head)

    # Print the reversed linked list
    current = head
    while current is not None:
        print(current.value, end=" ")
        current = current.next

# Original linked list: 1 -> 2 -> 3 -> 4 -> 5

# Initialize: prev = None, current = 1, next = None
# In the loop:
# next = 2, current.next = None, prev = 1, current = 2
# next = 3, current.next = 1, prev = 2, current = 3
# next = 4, current.next = 2, prev = 3, current = 4
# next = 5, current.next = 3, prev = 4, current = 5
# next = None, current.next = 4, prev = 5, current = None
# Exit the loop, and prev points to the new head: 5 -> 4 -> 3 -> 2 -> 1
# The linked list has been successfully reversed iteratively.