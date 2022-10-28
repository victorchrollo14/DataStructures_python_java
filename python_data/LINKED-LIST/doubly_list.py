

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLlist:
    def __init__(self):
        self.head = None
    
    def print_list(self):
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
    dlist.head.next = second      # linking first to second 

    second.prev = first        # linking second to first
    second.next = third        # linking seond to third

    third.prev = second       # linking third to second
    third.next = fourth       # linking third to fourth

    fourth.prev = third       # linking fourth to third
    fourth.next = None      

    dlist.print_list()


