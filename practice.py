from collections import deque

def linearsearch(arr,val):
    for i in range (len(arr)):
        if arr[i] == val:
            print(f"Value found at index f{i}")
        else:
            print("Value not found")

def binarysearch(arr,val):
    flag = 0
    low = 0
    high = len(arr) - 1 

    while high >= low:
        mid = (high + low) // 2

        if arr[mid] == val:
            print("element found")
            flag = 1
        elif arr[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
        
class BT:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None 
    
    def add_child(self,data):
        if self.data == data:
            return

        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BT(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BT(data)

    def preordertrav(self):
        if self.data is None:
            return
        print(self.data, end="")
        if self.left:
            self.left.preordertrav()
        if self.right:
            self.right.preordertrav()
    
    def inordertrav(self):
        if self.data is None:
            return
        if self.left:
            self.left.inordertrav()
        print(self.data,end=" ")

        if self.right:
            self.right.inordertrav()

    def bfs(self):
        q = deque()
        q.append(self)

        while q:
            node = q.popleft()

            print(node.data, end=" ")

            if self.left is not None:
                q.append(node.left)
            elif self.right is not None:
                q.append(node.right)
                




        


