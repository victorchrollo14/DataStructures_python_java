

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLlist:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        # Reading the linked list
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
    
        


if __name__ == "__main__":
    # creating the node data / values
    
    dlist = DoubleLlist()
    dlist.head = Node(1)

    first = dlist.head
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    # Linking the nodes 
    dlist.head.prev = None
    first.next = second      # linking first to second 

    second.prev = first        # linking second to first
    second.next = third        # linking seond to third

    third.prev = second       # linking third to second
    third.next = fourth       # linking third to fourth

    fourth.prev = third       # linking fourth to third
    fourth.next = None      

    print("Initial Doubly linked list:")
    dlist.print_list()
    print("\n")

    # UPDATE OPERATION
    # Insertion at the beginning 
    new_node = Node("new")
    dlist.head.prev = new_node           # Link prev of current head to new node
    dlist.head = new_node                # assigning new node as head
    new_node.next = first                # linking next of new node to first


    print("Inserting new element at the head: ")
    dlist.print_list()
    print("\n")

    # Insertion at the middle
    mid_node = Node("mid")
    second.next = mid_node              # linking next of second to mid node
    mid_node.prev = second              # linking prev of mid_node to second
    mid_node.next = third               # linking next of mid_node to third
    third.prev = mid_node               # linking prev of third node to mid_node

    print("Inserting new element at the middle: ")
    dlist.print_list()
    print("\n")

    





