class BinarySearchTreeNode:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
            
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

def preordertrav(subtree):
    if subtree is None:
        return
    print(subtree.data, end=" ")
    preordertrav(subtree.left)
    preordertrav(subtree.right)

    
def inordertrav(subtree):
    if subtree is None:
        return
    inordertrav(subtree.left)
    print(subtree.data, end= " ")
    inordertrav(subtree.right)

def postordertrav(subtree):
    if subtree is None:
        return
    postordertrav(subtree.left)
    postordertrav(subtree.right)
    print(subtree.data, end=" ")




if __name__ == "__main__":
    # Constructing the binary tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6

    values = [31,51,61,7,14,46]

    root = BinarySearchTreeNode(values[0])

    for val in values[1:]:
        root.add_child(val)

    print("\nPreOrder")
    preordertrav(root)

    print("\nInOrder")
    inordertrav(root)

    print("\npostorder")
    postordertrav(root)