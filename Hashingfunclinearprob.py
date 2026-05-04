class HashTable:
    def __init__(self,size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self,key):
        return hash(key) % self.size 
    
    def next_index(self,index):
        return (index + 1) % self.size
    
    def insert(self,key,value):
        index = self.next_index(key)

        while self.index[key] is not None:
            index = self.next_index(index)
        
        self.keys[index] = key 
        self.values[index] = value
    
    def search(self,key):
        index = self.hash_function(key)
        original_index = index

        while self.keys[index]!= key:
            index = self.next_index(index)
            if original_index == index or self.keys[index] is None:
                return None
        
        return self.values[index]
        