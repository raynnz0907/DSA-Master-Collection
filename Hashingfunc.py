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