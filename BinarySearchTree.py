class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self,data):
            if data == self.data:
                return
            
            if data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = BinarySearchTreeNode(data)
            
            elif data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = BinarySearchTreeNode(data)

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
    
def preordertrav(root):
        if root is None:
            return
        print(root.data, end=" ")
        preordertrav(root.left)
        preordertrav(root.right)

def inordertrav(root):
     if root is None:
          return
     inordertrav(root.left)
     print(root.data, end=" ")
     inordertrav(root.right)
    
def postordeertrav(root):
     if root is None:
          return
     postordeertrav(root.left)
     postordeertrav(root.right)
     print(root.data, end=" ")


            

if __name__ == "__main__":
    values = [41,61,4,62,7,1,5,17]
    root = BinarySearchTreeNode(values[0])
    for val in values[1:]:
        root.insert(val)

    print("\n Preorder")
    preordertrav(root)

    print("\nInOrder")
    inordertrav(root)

    print("\npostorder")
    postordeertrav(root)