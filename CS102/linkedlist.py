
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_next_node(self, next_node):
        self.next_node = next_node
    

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def insert(self, new_node):
        if self.head_node.value is None:
            self.head_node = new_node
            return
        
        current_node = self.head_node
        while current_node.next_node != None:
            current_node = current_node.next_node

        current_node.set_next_node(new_node)

    def __iter__(self):
        iter_node = self.head_node
        if iter_node.value is None:
            return StopIteration
        else:
            yield iter_node.get_value()
            iter_node = iter_node.next_node   
    
#myList = LinkedList([1,2])
#myList.insert(Node([3,4]))
#myList.insert(Node([5,6]))
#myList.insert(Node([7,8]))
#myList.insert(Node([9,10]))
