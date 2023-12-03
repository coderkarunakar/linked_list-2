#doubt


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def remove(self, node):
        if self.head == self.head.next:
            self.head = None
        else:
            temp = self.head
            while temp.next != node:
                temp = temp.next
            temp.next = node.next
            if node == self.head:
                self.head = node.next

    def josephus(self, step):
        if not self.head:
            return None
        current = self.head
        while current.next != current:
            count = 1
            while count != step:
                current = current.next
                count += 1
            self.remove(current)
            current = current.next
        return current.data

# Example usage
if __name__ == "__main__":
    n = 7  # Number of people
    k = 3  # Step
    people = CircularLinkedList()
    for i in range(1, n + 1):
        people.insert(i)

    survivor = people.josephus(k)
    print(f"The survivor in the Josephus problem with {n} people and step {k} is person {survivor}")
