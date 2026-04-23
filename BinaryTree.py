class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_data(self,data):
        if self.data == data:
            return
        
        elif self.data > data:
            if self.left:
                self.left.add_data(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        else:
            if self.right:
                self.right.add_data(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def print_in_order_traversal(self):
        elements = []

        #Visiting the left tree
        if self.left:
            elements += self.left.print_in_order_traversal()
        
        #The root node
        elements.append(self.data)

        if self.right:
            elements += self.right.print_in_order_traversal()

        return elements
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(0,len(elements)):
        root.add_data(elements[i])

    return root


if __name__ == '__main__':
    elements = [14,16,413,67,15,13]


