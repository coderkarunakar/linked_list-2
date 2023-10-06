# #This was the best Approach among all
# #we had a LL 1->2->3->4->5->None
# #stand at 1 and reverse the LL 5->4->3->2->None here head in small head i.e 5 and tail in small tail i.e 2
# #in order to get like above step we need  to make like 
# #small tail.next=head
# #head.next=None


# #1->2->3->4->5
# #2->3->4->5 call this part to get reverse only 3,4,5 ,here 2 as head
# #we get 5->4->3->None


# #Facebook interview question pls use chatgpt and understand each line
# #MAIN CODING LOGIC
# def reverse3(head):

#     #basecase
#     if head is None or head.next is None:
#         return head
#     smallHead=reverse3(head.next )
#     tail=head.next
#     tail.next=head
#     head.next=None
#     return smallHead


# head=takeInput()
# printLl(head)
# head=reverse3(head)
# printLL(head)


# #output like
# # 1 2 3 4 5 -1
# #1->2->3->4->5->None
# #5->4->3->2->1->None