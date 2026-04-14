class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None  # Initializes an empty doubly linked list

    def insert_at_head(self, data):  # Inserts a node at the beginning
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, data):  # Inserts a node at the end
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        new_node.prev = current

    def insert_at(self, data, position):  # Inserts a node at a specific position
        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.insert_at_head(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0

        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds")
            return

        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node  # FIXED

        current.next = new_node

    def display(self):  # Prints the list from head to end
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("None")

    def reverse(self):  # Reverses the doubly linked list
        current = self.head
        temp = None

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp:
            self.head = temp.prev  # FIXED head update

    def search(self, value):  # Searches for a value in the list
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    dl = DoubleLinkedList()

    print("Insert at head:")
    dl.insert_at_head(10)
    dl.insert_at_head(5)
    dl.display()

    print("\nAppend at end:")
    dl.append(20)
    dl.append(30)
    dl.display()

    print("\nInsert at position (index 2):")
    dl.insert_at(15, 2)
    dl.display()

    print("\nSearch for 20:")
    print("Found?", dl.search(20))

    print("\nReverse the list:")
    dl.reverse()
    dl.display()