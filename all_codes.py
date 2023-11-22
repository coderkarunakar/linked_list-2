# 1.Reverse a LL
# Reverese a linked List

#given a linked list


# 1->2->3->4->5->None   ,here 1 is our head part

#we need to reverse the given Linked List and we will be getting like 
# 5->4->3->2->1->None  ,here we  will be getting new head of LL i.e 5


#3.Reversing a linked list code

class Node:
    def __init__(self,data):

        self.data=data
        self.next=None
def printLL(head):
     #performs on head is not none
   while head is not None:
   #here we are converting it to string since it head is an int and we need output in the form of
   #-> arrow function and the printLL is an string and head is an integer so we can not do like that so we are simply converting it to string ...
      print(str(head.data) + "->",end="")
      # inorder to get the next value
      head =head.next
      #by the above the loop was done and finally we need to print None and simply return empty
   print("None")
   return 

def takeInput():
    inputList = [int(ele)for ele in input().split()]
    head =None
    tail=None
    for currData in inputList:
        if currData == -1:
            break
        newNode =Node(currData)
        if head is None:
            head =newNode
            tail =newNode
        else:
            tail.next =newNode
            tail= newNode
    return head
        





        #our target
        #we have a linked list 1->2->3->4->5->None
        #then we need to get like 5->4->3->2->1->None
    #here we will be calling like 1->2->3->4->5->None as 2->3->4->5->None from here u will be getting like 5->4->3->2->None here small head is pointing to 5 and a reference is maintained to it.(i.e curr) it works till it is curr.next is not None ,if it is none it will get stopped 

        #now trying to implement  the function
def reverse1(head):

    #if our head.next is none then we need to return head only ,if any of the statement is true it will not check other.even if any one is correct then it will go 
    #here order of statement is important
    if head is None or  head.next is None:
        return head
#here we used head.next since we are actually trying to call the next part of head since first part is our head and storing 
#we cannot loose the reference of the small head so we are storing it in the curr                     
    smallHead =reverse1(head.next)
    curr=smallHead
    while curr.next is not None: 
        curr =curr.next
        #this line is to make 2's next to be 1 i.e begining head and our curr is pointing to last node
    curr.next = head
    #till now we made like 2's next is 1 ,but still 1's next is pointing to 2 only so inorder to make it none we are making this step
    head.next = None
    return smallHead 


head = takeInput()
printLL(head)

#lets call a linked list reverse function(pass the head i.e we pass the linked list) and after reversing we store in head only
head=reverse1(head)
#after that print linked list
printLL(head)



    #small ex:
    #1->2->3  this will call
    # we will call on 
    # 2->3 to get reversed this will call on
    # 3->None to get reversed 
    #now this linked list is same as the reversed linked list
    #now finally we will get like 3->2->1->None as our expected output

    #dry run for the reverse function
    # 1->2->3->4->->None,here initially head is 1 
    #it checks for the if condition,it gets fails
    #now it will call on 2->3-4->None (here head is 2)
    #again it checks the condition and it gets fails
    #we will go to reverse
    # and we will  get like 3->4->None
    #4->None
    #Now in 3->4 we got like in small head we got referece of 4,now put curr head to be small head i.e 4
    #4s next we need is 3
    # 4-3->None since our small head is 4  then it will return .small head has been return 4 to 2
    #now u have called for 2->3->4 ,in the small head   we got like 4->3->2->None
    #finally we will get like 4->3->2->None as our output


    #first please add to github after bug solving

    #please take a note there is a bug in this code and and i am commiting this please refer you tube for this and please take a time complexity analysis as well
