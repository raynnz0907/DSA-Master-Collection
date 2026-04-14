
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