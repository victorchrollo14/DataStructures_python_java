""" 
Breadth first Search in binary Search tree.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BTree:
    # creates an empty binary search tree.
    def __init__(self):
        self.root = None

    def insert(self, value):
        temp = self.root
        while (temp):
            if (value < temp.data):
                if (temp.left is None):
                    temp.left = Node(value)
                    break
                else:
                    temp = temp.left
            if (value > temp.data):
                if (temp.right is None):
                    temp.right = Node(value)
                    break
                else:
                    temp = temp.right

    def traverse(self):
        current = self.root

        stack = []
        while (1):
            if current is not None:
                stack.append(current)
                current = current.left
            
            elif(stack):
                current = stack.pop()
                print(current.data, end=" ")
                
                current = current.right

            else:
                break
        print()

    def level_order_traversal(self):
        current = self.root
        if current is None:
            return
        
        queue = []
        queue.append(current)
        while (len(queue) > 0):
            print(queue[0].data)
            current = queue.pop(0)

            if (current.left is not None):
                queue.append(current.left)
            if (current.right is not None):
                queue.append(current.right)
            

      
if __name__ == "__main__":
    tree = BTree()
    tree.root = Node(5)
    tree.insert(4)
    tree.insert(6)
    tree.insert(3)
    tree.insert(2)
    tree.insert(8)
    tree.insert(7)
    tree.insert(10)

    tree.traverse()
    tree.level_order_traversal()


