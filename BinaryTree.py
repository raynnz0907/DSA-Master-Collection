from collections import deque

class BinaryTreeNode:
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
                self.left = BinaryTreeNode(data)
            
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

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

def bfstrav(root):
    if root is None:
        return
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        print(node.data, end=" ")

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


if __name__ == "__main__":
    # Constructing the binary tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6

    values = [31,51,61,7,14,46]

    root = BinaryTreeNode(values[0])

    for val in values[1:]:
        root.add_child(val)

    print("\nPreOrder")
    preordertrav(root)

    print("\nInOrder")
    inordertrav(root)

    print("\npostorder")
    postordertrav(root)

    print("\nBFS")
    bfstrav(root)