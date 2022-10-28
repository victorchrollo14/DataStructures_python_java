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
    
    def Delete_list(self):
        pass


if __name__ == "__main__":
    # Creating an instance of LinkedList class
    llist = LinkedList()
    llist.head = Node(1)

    first =  llist.head
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
    print("elements of linkedlist: ")
    llist.PrintList()
    print('\n')
    

    # INSERTION OPERATION
    # Insertion at the beginning of node
    new_node = Node("new")                    # Create a new node
    new_node.next = llist.head                # point the address of new node to current head
    llist.head = new_node                     # assign new_node as the head
    
    print("New linkedlist after Insertion of new node at the head:")
    llist.PrintList()

    # Insertion at the middle
    middle_node = Node("mid")                 # create a new node
    middle_node.next = second                 # point the address towards the next node
    first.next = middle_node                  # point the address of previous node to middle_node
     
    print('\n')
    print("Linked list after insertion at the middle: ")
    llist.PrintList()

    # Insertion at the end
    end_node = Node("end")
    end_node.next = None
    third.next = end_node

    print("\n")
    print("The linked list after insertion at the end: ")
    llist.PrintList()


    # Deletion Operation
    # Deletion at the head  (by moving the head form node1 to node2 , node1 gets deleted)
    llist.head = llist.head.next        # shifting the head from node1(new_node) -----> node2(first)
    
    print("\n")
    llist.PrintList()

    

    
    




    
