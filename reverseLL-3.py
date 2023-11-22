#This was the best Approach among all
#we had a LL 1->2->3->4->5->None
#stand at 1 and reverse the LL 5->4->3->2->None here head in small head i.e 5 and tail in small tail i.e 2
#in order to get like above step we need  to make like 
#small tail.next=head
#head.next=None


#1->2->3->4->5
#2->3->4->5 call this part to get reverse only 3,4,5 ,here 2 as head
#we get 5->4->3->None




class Node:
    def __init__(self,data):
        #actually a node consist of data and next value i.e ref of next value so here we are storing next
        #value as None..
        self.data=data
        self.next=None
def takeInput():
    inputList = [int(ele)for ele in input("enter elements").split()]
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

        #for getting head purpose

def printLL(head):
    #performs on head is not none
    while head is not None:
    #here we are converting it to string since it head is an int and we need output in the form of
    #-> arrow function and the printLL is an string and head is an integer so we can not do like that so we are simply converting it to string ...
        print(str(head.data) + "->",end="")
        head =head.next
        #by the above the loop was done and finally we need to print None and simply return 
    print("None")
    return 

def reverse1(head):
#base case:if head.next element is none we reached end so return head(i.e element)
#special case:if no elements in LL then return None i.e head
    if head is None or head.next is None  :
        #it returns None if head is none or head.next is none
        return head
#in order to traverse to end of the LL below step is..
    smallHead =reverse1(head.next)
    #by till above we will get like 1->5->4->3->2->None here smallhead is pointing to 5
    #and head is pointing to 1

#in order to traverse to end of LL we made reverse from second call and first element remains in same position(1st)    in order to make it end and to put none after it we are following this steps
    #initialize:we cannot loose reference of smallhead because in the end we need to return this as head so assigning into something and traversing
    curr=smallHead                    
    #condition:it goes till end of LL i.e 1 step less than None(it traverse till its next step becomes None)
    while curr.next is not None: 
        curr=curr.next
#here curr is like a tail(end point )making our first element(head)to point after end point (like 1 after 2) and here only we are able to reverse making next point as a head main imp logic reversing is done here only  
    curr.next=head
    #in this head is 1 which points to 2 in order to make it None which is after end of the LL
    head.next=None
    return smallHead



#the above solution is O(n2)
 
                        #OUR MAIN LOGIC PART
def reverse2(head):

    #a special case and a base case
    if head is None or head.next is None:
        #in this case head,will be head, and tail also will be head
        return head,head


# 1->2->3->4->5
#1 ->5->4->3->2->None here smaill tail is 2
    #need to return 2 things so 
    smallHead,smallTail=reverse2(head.next)
    #here making 5s next as 4,4s next as 3 and so on....
    smallTail.next=head
    #1s next to be none
    head.next=None


#and after complete reversing we will get like 5->4->3->2->1 here small head is 5 and tail is head i.e 1
#here your tail is your head 
#here returning smallHead since actual head reamins same and with this process head only making changes
    return smallHead,head
#Facebook interview question pls use chatgpt and understand each line
#MAIN CODING LOGIC
def reverse3(head):

    #basecase
    if head is None or head.next is None:
        return head
    smallHead=reverse3(head.next )
    #because already 1's next is 2 so we can make after reversing 
    #1->2->3->4->5->None
    # ex:1->5->4->3->2->NOne to 5->4->3->2->1->none since alredy 1's next is 2(head.next=tail(end point(here 2)),tail.next=head means endpoint next is head)head.next to none (after  putting our head ,its next to be none ) 
    
    #Note:here onwards .next means to backward direction not forward
    #this makes backward call
    tail=head.next
    #this is used to connect in reverse (next means backward)
    tail.next=head
    #this is used to disconnect 4->5 (note:None means end of the LL ,it is not a part )
    head.next=None
    return smallHead



head=takeInput()
printLL(head)
head=reverse3(head)
printLL(head)




# head,tail=reverse2(head)
# printLL(head)

#output like
# 1 2 3 4 5 -1
#1->2->3->4->5->None
#5->4->3->2->1->None