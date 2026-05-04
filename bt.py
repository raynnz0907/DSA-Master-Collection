from collections import deque

def bfstrav(root):
    if root.self is None:
        return
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print(node.data,end="")

        if node.left is not None:
            q.append(node.left)
        elif node.right is not None:
            q.append(node.right)



class BST:
    def __init__ (self,data):
        self.data = data
        self.left= None 
        self.right = None

    def insert(self,data):
        if self.data == data:
            return

        if data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
        
        elif data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)

    def search(self,val):
        if self.data is None:
            return False

        if val == self.data:
            return True
        elif val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
    