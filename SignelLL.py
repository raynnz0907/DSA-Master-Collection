class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_bigging(self,data):
        new_node = Node(data,self.head)
        self.head = new_node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current:
            current = current.next
        current.next = Node(data)

    def insert_at_pos(self,index,data):
        new_node = Node(data)
        if index < 0:
            print("Index cannot be negative")
        else:
            current = self.head
            count = 0
            while current is not None and count < index -1:
                current = current.next
                count += 1
            
            new_node.next = current.next
            current.next = new_node
    
    def search(self,val):
        current = self.head
        while current is not None:
            if current == val:

                return True
            current = current.next
            return False

                



        