class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child("Mac")
    laptop.add_child("HP")
    laptop.add_child("ASUS")\
    
    cellphone = TreeNode("Cellphone")
    cellphone.add_child("IPHONE")
    cellphone.add_child("SAMSUNG")
    cellphone.add_child("NOKIA")

    tv = TreeNode("TV")
    tv.add_child("SAMSUNG")
    tv.add_child("LG")

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(cellphone)



if __name__ == '__main__':
    root = build_product_tree()
    pass
