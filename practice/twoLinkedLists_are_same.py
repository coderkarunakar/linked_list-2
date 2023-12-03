# Python Program to Check whether 2 Lists are Same
#Easy problem
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        lastnode=self.head
        while lastnode.next:
            lastnode=lastnode.next
        lastnode.next=newNode
def compareLL(List1,List2):
    temp1=List1.head
    temp2=List2.head
    while temp1 and temp2:
        if temp1.data!=temp2.data:
            return False
        temp1=temp1.next
        temp2=temp2.next
    return temp1 is None and temp2 is None

def createLL():
    Linked_List=LinkedList()
    elements=int(input("enter the no of elements in you Linked List"))

    for _ in range(elements):
        element=int(input("enter all elements one by one"))
        Linked_List.append(element)
    return Linked_List

print("create LL 1")
List1=createLL()
print("create LL 2")
List2=createLL()
if compareLL(List1,List2):
    print("both the LL are same")
else:
    print("both the LL are different")

