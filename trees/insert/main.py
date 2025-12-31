class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
        


my_tree = BinarySearchTree()
my_tree.insert(1)
my_tree.insert(2)
my_tree.insert(3)
my_tree.insert(4)
my_tree.insert(5)
my_tree.insert(6)
my_tree.insert(7)
print(my_tree.root)
