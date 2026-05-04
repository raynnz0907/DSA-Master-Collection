class CategoryNode:
    def __init__(self, name):
        self.name = name
        self.children = []


class CategoryTree:
    def __init__(self):
        self.root = None

    def add_root(self, name):
        self.root = CategoryNode(name)

    def add_subcategory(self, parent, child_name):
        new_node = CategoryNode(child_name)
        parent.children.append(new_node)
        return new_node

    def display(self, node, level=0):
        if node:
            print(" " * level + "- " + node.name)
            for child in node.children:
                self.display(child, level + 2)


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root)

        # LL Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


# -----------------------------
# Main Program (Integration)
# -----------------------------
if __name__ == "__main__":

    # Create Category Hierarchy
    tree = CategoryTree()
    tree.add_root("Products")

    electronics = tree.add_subcategory(tree.root, "Electronics")
    clothing = tree.add_subcategory(tree.root, "Clothing")

    tree.add_subcategory(electronics, "Mobiles")
    tree.add_subcategory(electronics, "Laptops")
    tree.add_subcategory(clothing, "Men")
    tree.add_subcategory(clothing, "Women")

    print("Category Hierarchy:")
    tree.display(tree.root)

    # Create AVL Tree for Fast Search
    avl = AVLTree()
    root = None

    categories = [
        "Electronics", "Mobiles", "Laptops",
        "Clothing", "Men", "Women"
    ]

    for cat in categories:
        root = avl.insert(root, cat)

    print("\nSorted Categories (AVL Tree):")
    avl.inorder(root)

    # -----------------------------
    # User Input Search
    # -----------------------------
    print("\n")
    search_key = input("Enter category to search: ")
    result = avl.search(root, search_key)

    print("\nSearch Result:")
    if result:
        print(f"{search_key} found in category system")
    else:
        print(f"{search_key} not found")