#we can create a node with this
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        #we can handle Linkedlist nodes with this
class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            return
        lastnode=self.head
        while lastnode.next:
            lastnode=lastnode.next
        lastnode.next=newNode

    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
        print()


#this is O(n2) algorithm
    def remove_duplicate(self):
        #current is initialized to first value
        current=self.head
        #works till end of all elements
        while current:
            #assigning current values to the runner
            runner=current
            #moving 1 step next 
            while runner.next:
                #checking both the values are mathching
                if runner.next.data==current.data:
                    #if mathed skip that and updatae next as next.next
                    runner.next=runner.next.next
                    #if doesnot match simply move 1step next
                else:
                    runner=runner.next
                    #and move current also 1 step next
            current=current.next

  
if __name__=="__main__":
    linked_list=LinkedList()

linked_list = LinkedList()
linked_list.append(2)
linked_list.append(3)
linked_list.append(2)
linked_list.append(4)
linked_list.append(3)
linked_list.append(5)

print("linked list before removing duplicates")
linked_list.display()
linked_list.remove_duplicate()
print("linkedlist after removing duplicates")
linked_list.display()


