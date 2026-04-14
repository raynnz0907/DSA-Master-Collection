class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1 
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level()
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("ASUS"))
        
    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("IPHONE"))
    cellphone.add_child(TreeNode("SAMSUNG"))
    cellphone.add_child(TreeNode("NOKIA"))


    tv = TreeNode("TV")
    tv.add_child(TreeNode("SAMSUNG"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(cellphone)

    return root 



if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass
