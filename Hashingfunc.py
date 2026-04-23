class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    # Hash Function
    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    # Insert (with rehashing - linear probing)
    def insert(self, key, value):
        index = self.hash_function(key)

        original_index = index
        while self.table[index] is not None:
            # If same key, update value
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            
            # Rehash (move to next slot)
            index = (index + 1) % self.size

            # Table full condition
            if index == original_index:
                print("Hash Table is full!")
                return
        
        self.table[index] = (key, value)
    
     # Search for a product
    def search(self, key):
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]

            index = (index + 1) % self.size

            if index == original_index:
                return None
        
        return None

    # Display the hash table
    def display(self):
        print("\nHash Table Contents:")
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")
    
ht = HashTable(5)

# Adding products
ht.insert("Laptop", 50000)
ht.insert("Phone", 20000)
ht.insert("Tablet", 15000)
ht.insert("Watch", 5000)
ht.insert("Camera", 30000)

# Display table
ht.display()

# Searching products
print("\nSearch Results:")
print("Phone:", ht.search("Phone"))
print("Camera:", ht.search("Camera"))
print("TV:", ht.search("TV"))