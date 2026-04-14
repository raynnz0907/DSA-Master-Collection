class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None  # Initializes an empty linked list

    def intsertion_at_begginng(self, data):  # Inserts a node at the beginning
        new_node = Node(data, self.head)
        self.head = new_node

    def inster_at_end(self, data):  # Inserts a node at the end
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at_postion(self, index, data):  # Inserts a node at a specific index
        if index < 0:
            raise IndexError("Index cannot be negative")
        
        if index == 0:
            self.intsertion_at_begginng(data)
            return
        
        current = self.head
        count = 0
        while current is not None and count < index - 1:
            current = current.next
            count += 1
        
        if current is None:
            raise IndexError("Index beyond the list")

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def reverse(self):  # Reverses the linked list
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def search(self, value):  # Searches for a value in the list
        current = self.head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    def transverse(self):  # Prints the linked list elements
        current = self.head
        while current is not None:
            print(current.data, end=" --> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    ll = SingleLinkedList()

    print("Insert at beginning:")
    ll.intsertion_at_begginng(80)
    ll.intsertion_at_begginng(35)
    ll.intsertion_at_begginng(5)
    ll.transverse()

    print("\nInsert at end:")
    ll.inster_at_end(78)
    ll.transverse()

    print("\nInsert at position (index 2):")
    ll.insert_at_postion(2, 15)
    ll.transverse()

    print("\nSearch for 35:")
    print("Found?" , ll.search(35))

    print("\nReverse the list:")
    ll.reverse()
    ll.transverse()