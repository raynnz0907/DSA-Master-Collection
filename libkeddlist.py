class Node:
    def __init__(self,data,prev = None,next = None):
        self.data = data
        self.prev = prev
        self.next = next
    
class doublelinkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_bg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head 
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        
    def insterinbetween(self,data,position):
        new_node = Node(data)
        if position < 0 :
            raise IndexError
        if position == 1:
            self.insert_at_bg(data)
            return

        current = self.head
        count = 0 

        while current.next is not None and count < position - 1:
            current = current.next
            count += 1
    
        if current is None:
            print("Position out of bounds")
            return
        
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        current.next = new_node 



        
