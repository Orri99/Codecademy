from linkedlist import Node, LinkedList

class Hashmap:
    def __init__(self, array_size):
        self.size = array_size
        self.array = [LinkedList() for index in range(self.size)]
    
    def hash_and_compress(self, key):
        hash = sum(key.encode())
        return hash % self.size
    
    def assign(self, key, value):
        array_index = self.hash_and_compress(key)
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        
        for item in list_at_array:
            if item[0] == key:
                item[1] = value
                return
        
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.hash_and_compress(key)
        list_at_index = self.array[array_index]

        for item in list_at_index:
            if item[0] == key:
                return item[1]


testMap = Hashmap(10)
testMap.assign("Title","Text")
print(testMap.retrieve("title"))