class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_data(self,data):
        if self.data == data:
            return
        elif self.data < data:
            if self.right:
                self.right.add_data(data)
            else:
                self.right = BinarySearchTreeNode(data)
        
        else:
            if self.left:
                self.left.add_data(data)
            else:
                self.left = BinarySearchTreeNode(data)
            

        