class HashTalbe:
    def __init__ (self, size):
        self.size = size
        self.key = [None] * size
        self.value = [None] * size
    
    def hash_function(self,key):
        return hash(key) % self.size
    
    def next_index(self,index,attempt):
        return (index + attempt**2) % self.size
    
    def insert(self,key,value):
        index = self.hash_function(key)
        attempt = 0

        while self.key[index] is not None:
            attempt += 1
            index = self.next_index(index,attempt)

        self.key[index] = key
        self.value[index] = value