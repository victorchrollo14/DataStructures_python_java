# CRUD OPERATIONS ON LINKED LIST
# SEARCH OPERATION

''' Construction of a simple linked list with three nodes '''


# Node class
class Node:

    # Function to initialize a node object
    def __init__(self, data):
        self.data = data          # Assign data
        self.next = None          # Initialize next as null


# LinkedList contains the node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Funcion to traverse the list
    def PrintList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+

    '''

    llist.head.next = second  # link first node with second

    '''
    Now next of first Node refers to second.  So they
    both are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''

    second.next = third  # linking the second node with third

    '''
    Now next of first Node refers to second.  So they
    both are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |   o------->|  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''

    llist.PrintList()
    print()
    

    # INSERTION OPERATION
    # Insertion at the beginning of node
    new_node = Node("new")                    # Create a new node
    new_node.next = llist.head                # point the address of new node to current head
    llist.head = new_node                     # assign new_node as the head

    llist.PrintList()



    
