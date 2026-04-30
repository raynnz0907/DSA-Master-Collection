class BinarySearchTreeNode:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None

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

    subtree = BinarySearchTreeNode(1)
    subtree.left = BinarySearchTreeNode(2)
    subtree.right = BinarySearchTreeNode(3)
    subtree.left.left = BinarySearchTreeNode(4)
    subtree.left.right = BinarySearchTreeNode(5)
    subtree.right.right = BinarySearchTreeNode(6)

    print("\nPreOrder")
    preordertrav(subtree)

    print("\nInOrder")
    inordertrav(subtree)

    print("\npostorder")
    postordertrav(subtree)