class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        #initially head is none
        self.head = None



    def insert_at_end(self, data):
        new_node = Node(data)
        #if head is empty
        if self.head is None:
            self.head = new_node
            #return nothing
            return
            #if it has elements then it is inserting next elements by creating new node
            #initializing the last value as the 1st head
        last = self.head
        #it finds last node by traversing the list until last.next becomes none
        while last.next:
            #this below line makes traverse to the last node that is end of the node ,if it reaches end of the  node then it can insert the new node at end point
            last = last.next
            #and then sets next pointer to the new node
        last.next = new_node


#here key means which value you want to delete
    def delete_node(self, key):
        #initializing first value i.e head as temp
        temp = self.head

        #THIS IS FOR CATCHING THE HEAD VALUE
        #if value exist in temp then continues
        if temp:
            #checks the first value as a key(which you want to delete)
            if temp.data == key:
                #if head is the delete value then update the head to the next value effectively removing head
                self.head = temp.next
                #setting original head to none to delete it temp =None,with the help of this None only we can make that value as none,and above head pointer got changed
                temp = None
                #return empty from the method
                return

#THIS IS FOR IF CATCHING DELETE VALUE IN THE GROUP OF ELEMENTS 
#temp exist i.e head value(first value) exist
        while temp:
            #if current data matches to the delete value then break
            if temp.data == key:
                break
            #storing the temp value inside the prev variable
            prev = temp
            #moving next value as the temp simply updating
            temp = temp.next


#THIS IS FOR IF THERE IS NO KEY(DELETE VALUE)
        if temp == None:
            #then returns empty
            return
#if key was found,updating the temp.next as a prev.next and skipping temp value by None
        prev.next = temp.next
        #here simply setting current value as None ,it means simply skip that value
        temp = None



    def display(self):
        #current is pointing to the 1st value in the linked list
        current = self.head
        #it iterates till elements exists in Linked List ,
        while current:
            #printing data
            print(current.data, end=" -> ")
            #currrent is updating till last
            current = current.next
        print("None")

    def is_empty(self):
        return self.head is None

    def get_length(self):
        count = 0
        current = self.head
        #iterates till elements exist in the linked list
        while current:
            count += 1
            current = current.next
        return count

#key means which value you want to search
    def search(self, key):
        current = self.head
        position = 1
        while current:
            if current.data == key:
                return f"Element {key} found at position {position}"
            position += 1
            current = current.next
        return f"Element {key} not found"


#reversing the elements
    def  reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            #all the values were stored in prev and finally making head to point as a prev so that all it get reveresed 
        self.head = prev

#removing the all duplicates
    def remove_duplicates(self):
        current = self.head
        prev = None
        #creating an empty set 
        elements = set()
        #iterates in all the elements of the Linked list 
        while current:

            #HERE CHECKING THE DUPLICATE VALUE IS PRESENT OR NOT,AND JUST UPDATING THE PREV AND CURRENT
            #checks that value is found in empty (set)
            if current.data in elements:
                #updating the next value to the prev value and and skipping the current value
                prev.next = current.next
                #current value got skipped by putting it as None
                current = None
                
                #when the current.data is not found in the elements then,it is encountered for the first time and it is considered as unique value then that value value is added into elements which is a set ,which maintains the unique value

                #HERE ADDING INTO SET TAKES PLACE 
            else:
                #this line is for adding into elements set 
                elements.add(current.data)
                #this line updates the prev pointer to the current node,this is necessary to keep track of the prev node before moving to next node
                prev = current
                #this pointer moves the current pointer to the next node in linked list,this is essential for checking duplicates
            current = prev.next


#simple slow moves one step and fast moves two steps forward0

    def find_middle(self):
        slow = self.head
        fast = self.head
        #while loop continues till fast and fast.next is not none
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #this means if slow element is there then return slow if not there then return None 
        return slow.data if slow else None

#with the help of this only we can make our code like it will be executed only in this code not as other code when it is imported as a module
if __name__ == "__main__":
    #creating an instance of the class linkedList,with the help of this only we can perform some methods like traversal,insertion,deletion,searching etc...
    linked_list = LinkedList()

#a call for inserting node after a node 
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(7)
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(8)

#displaying the nodes 
    print("Initial linked list:")
    linked_list.display()

 
    print("\nLength of the linked list:", linked_list.get_length())

    linked_list.delete_node(3)
    print("\nLinked list after deletion of node with value 3:")
    linked_list.display()

    print("\nSearching for element 7:", linked_list.search(7))
    print("Searching for element 10:", linked_list.search(10))

    linked_list.reverse()
    print("\nReversed linked list:")
    linked_list.display()

    linked_list.remove_duplicates()
    print("\nLinked list after removing duplicates:")
    linked_list.display()

    print("\nMiddle element of the linked list:", linked_list.find_middle())
