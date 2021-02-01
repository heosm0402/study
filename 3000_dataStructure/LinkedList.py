
# Node
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly linked list
class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    # Add new node at the end of the linked list
    def enqueue(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def dequque(self):
        if self.head == None:
            return -1
        
        v = self.head.data
        self.head = self.head.next

        if self.head == None:
            self.tail = None
        
        return v

    def print(self):
        curn = self.head
        string = ""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
            curn = curn.next
        
        print(string)


s = SinglyLinkedList()
print(f"s.head is {s.head}")
print(f"s.tail is {s.tail}")

s.enqueue(Node(1))
s.enqueue(Node(2))
s.enqueue(Node(3))
s.enqueue(Node(4))

s.print()

print(f"s.head is {s.head}")
print(f"s.tail is {s.tail}")

print(s.dequque())
print(s.dequque())
s.print()

