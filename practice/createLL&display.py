# Python Program to Create a Linked List & Display the Elements in the List
#to create individual nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#to manage that individual nodes
#note:LinkedList spell is must imp
class LinkedList:
    def __init__(self):
        
        self.head=None

    def append(self,data):
        #creating a new node (carefull)
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            return
        
        lastnode=self.head
        #this loop traverse till end of the LL
        while lastnode.next:
            #here updating the lastnode.next value as lastnode
            lastnode=lastnode.next
        lastnode.next=newNode


    def display(self):
        current=self.head
        while current:
            print(current.data, end=" ")
            current=current.next

if __name__=="__main__":
    linked_list=LinkedList()
    
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(16)


    print("Elements in the linked list:")
    linked_list.display()


