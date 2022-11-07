"""
Implementation of a Binary Search Tree.

"""

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    # Performing operations using recursion
    def insert(self, value):
        if (value < self.value):
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        if (value > self.value):
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    
    def In_order_traversal(self):
        if (self.left):
            self.left.In_order_traversal()
        print(self.value, end=" ")
        if (self.right):
            self.right.In_order_traversal()
    
    def pre_order_traversal(self):
        print(self.value, end=" ")
        if (self.left):
            self.left.pre_order_traversal()
        if (self.right):
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if (self.left):
            self.left.post_order_traversal()
        if (self.right):
            self.right.post_order_traversal()
        print(self.value, end=" ")

    def find(self, value):
       if value < self.value:
           if (self.left is None):
               return False
           else:
               return self.left.find(value)

       elif value > self.value:
           if (self.right is None):
               return False
           else: 
               return self.right.find(value)
       
       else:
           return True
        

tree = TreeNode(25)
tree.insert(50)
tree.insert(15)
tree.insert(10)
tree.insert(20)
tree.insert(4)
tree.insert(12)
tree.insert(45)
tree.insert(55)

print("\nPre order Traversal: ")
tree.pre_order_traversal()

print("\nIn order Traversal: ")
tree.In_order_traversal()

print("\nPost Order Traversal: ")
tree.post_order_traversal()

val = int(input("\nEnter the value to search: "))
print(tree.find(val))


