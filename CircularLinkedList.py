class Node: # Creating a Node
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initializes an empty circular linked list

    def append(self, data):  # Adds a node at the end of the circular list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        
        current = self.head
        while current.next != self.head:  # FIXED condition
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def print_list(self):  # Prints all elements of the circular linked list
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        while True:
            print(current.data, end=" --> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

    def insert_at_front(self, data):  # Inserts a node at the beginning
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def search(self, value):  # Searches for a value in the circular list
        if not self.head:
            return False
        
        current = self.head
        while True:
            if current.data == value:
                return True
            current = current.next
            if current == self.head:
                break
        return False


if __name__ == "__main__":
    cl = CircularLinkedList()

    print("Appending elements:")
    cl.append(16)
    cl.append(25)
    cl.append(35)
    cl.print_list()

    print("\nInsert at front:")
    cl.insert_at_front(5)
    cl.print_list()

    print("\nSearch for 25:")
    print("Found?", cl.search(25))