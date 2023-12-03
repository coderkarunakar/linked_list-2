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

#LOGIC:
#mainitaing 2 pointers mainptr and refptr and refptr moves till end of the linked list,using a count variable which is initialized to 0 and taking that as a reference ,and this time moving mainptr untill ref ptr reaches none


    def print_nth_from_last(self, n):
        main_ptr = self.head
        ref_ptr = self.head
        #count is for to keep track of no of nodes visited
        count = 0

#checks if the linked list is not empty
        if self.head is not None:
            #this moves ref_ptr forward n times
            while count < n:
                #checks ref_ptr reaches the end of the list before reaching the nth node,if so n>no.of nodes in list,and prints appropriate message
                if ref_ptr is None:
                    print(f"{n} is greater than the number of nodes in the list")
                    return

                ref_ptr = ref_ptr.next
                count += 1
#this moves both main_ptr and ref_ptr both simultaneously,until ref_ptr reaches end of the list
#here it takes the ref_ptr value as above what we get it
            while ref_ptr is not None:
                #this moves main_ptr one node ahead
                main_ptr = main_ptr.next
                #this moves ref_ptr one step ahead
                ref_ptr = ref_ptr.next
# Finally, prints the data of the node referenced by main_ptr, which is the nth node from the end of the linked list
            print(f"The {n}th node from the end is {main_ptr.data}")

# Example usage:
llist = LinkedList()

llist.append(20)
llist.append(4)
llist.append(15)
llist.append(35)

n = int(input("enter nth from last of the nodes"))
llist.print_nth_from_last(n)
