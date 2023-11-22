# Merge two sorted LinkedList
#Please look classNotes for better logic understanding
# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(head1, head2):
    dummy = ListNode()
    current = dummy

    while head1 is not None and head2 is not None:
        if head1.value < head2.value:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    # If one list is shorter than the other, add the remaining elements.
    if head1 is not None:
        current.next = head1
    else:
        current.next = head2

    return dummy.next

def print_linked_list(head):
    while head:
        print(head.value, end=" ")
        head = head.next
    print()

# Main function to handle multiple test cases
def main():
    t = int(input("Enter the number of test cases: "))
    
    for _ in range(t):
        values1 = list(map(int, input().split()))
        values2 = list(map(int, input().split()))

        head1 = None
        head2 = None

        for value in reversed(values1):
            if value != -1:
                head1 = ListNode(value, head1)

        for value in reversed(values2):
            if value != -1:
                head2 = ListNode(value, head2)

        merged_head = merge_sorted_lists(head1, head2)
        print_linked_list(merged_head)

if __name__ == "__main__":
    main()


#just please look the above code carefully....
 