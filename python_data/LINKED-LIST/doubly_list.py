

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
    
    def search(self, key):
        temp = self.head
        i = 0
        while (temp):
            if(str(temp.data) == key):
                print(f"{key} found at index {i}")
            temp = temp.next
            i += 1
        
        


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

    # Insertion at the end
    end_node = Node("end")
    fourth.next = end_node            # linking next of fourth to end_node
    end_node.prev = fourth            # Linking prev of end_node to fourth
    end_node.next = None              # Linking next of end_node to None

    print("Inserting new element at the end: ")
    dlist.print_list()
    print("\n")
    
    # SEARCH OPERATION
    key = input("Enter the element to search: ")
    dlist.search(key)
    print("\n")


    # DELETE OPERATION
    # Deleting at the beginning 
    dlist.head = first                # Changing the head new_node to first

    print("Deleting at the beginning: ")
    dlist.print_list()
    print("\n")

    # Deleting at the middle
    second.next = third                     # linking the next of second to third
    third.prev = second                     # Linking the prev of third to next (mid_node gets deleted)

    print("Deleting at the middle: ")
    dlist.print_list()
    print("\n")

    # Deleting at the End
    fourth.next = end_node.next           # Linking next of fourth to None
    end_node.prev = None                  # Linking prev of end_node to none

    print("Deleting at the end: ")
    dlist.print_list()
    print("\n")

    




    





