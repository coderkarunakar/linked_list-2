# #APPROACH

# #in this we are going to discuss a better version of reversing the LL(a better optimize approach)
# #Note:for every solution we need a  head and a tail i.e first and last node
# #A better Approach


# #1->2->3->4->5->None
# #5->4->3->2->None (this call will reverse you the linked list)(here small head is 5 and small tail is 2)

# #our function will be reverse(head)
# #Small head ,small Tail=reverse(head.next) (This call will reverse the linked list and gives small head,tail)

# #small tail.next =1(i.e head)
# #head.next=None
# #it returns 2 Things (i.e head,tail) Small head,and tail had become head
# #in this case our T.c will be O(n)

# #Clear Approach
# # 1->2->3->4->None
# #Call a reverse LL so Call  to get the reverse LL and get Small head,Tail 2->3->4->None
# #Now call 3->4-None
# #Now call 4->None(base case)

# #Our base case is head.next is None (if head becomes none both head and tail are none)
# #then return head,  head(since head is same and tail is same so we can return 4,4 to above call)
# #then in the 3->4-None call 4(small head)->None (small Tail)

# #Now we got Small head,Small Tail by calling on reverse LL
# #Small head,Small Tail =reverse(head.next)
# #Small Tail.next=head  (4->3)here 3 next is pointing to  4 we need to remove it
# #do head.next = None (now 3 next is None)

# #return small head,head 
# #Now we are able to do it in the order of n
# #just get the head and tail and you will be able to solve this question





# #CODING PART:REVERSE A LINKED LIST BUT IN THE OPTIMIZED WAY
# #IF WE GET BOTH HEAD AND TAIL OF NEXT PART WE DONT NEED TO TRAVERSE TILL LAST NODE SINCE WE ALREADY HAVE LAST NODE IN THE HEAD AND FIRST NODE IN THE FORM OF TAIL
# #FOR example if we have 1->2->3->4->5->None do it like
# #2->3->4->5 simply reverse it then we will get like
# #5->4->3->2->None here small head is 5 and small tail is 2

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

#reverse 1 is also a logic which is previous one
def reverse1(head):
    if head is None or head.next is None:
        return head
    smallHead =reverse1(head.next)
    curr=smallHead
    while curr.next is not None:
        curr=curr.next
    curr.next=head
    head.next=None
    return smallHead


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
    #here making 2s next to be 1
    smallTail.next=head
    #1s next to be none
    head.next=None


#and after complete reversing we will get like 5->4->3->2->1 here small head is 5 and tail is head i.e 1
    return smallHead,head


head=takeInput()
printLL(head)
head,tail=reverse2(head)
printLL(head)
#first approach is o(n2) and second approach is O(n) Times