

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLlist:
    # constructor to create an empty circular linked list
    def __init__(self):
        self.head = None

    def prepend(self, value):
        node = Node(value)
        temp = self.head
        node.next = self.head
        
        # If Linkedlist is not None then set the
        # next of last node
        if (self.head is not None):
            while (temp.next != self.head):
                temp = temp.next
            temp.next = node
        else:
            node.next = node
        
        self.head = node    

    def append(self, value):
        new_node = Node(value)
        temp = self.head

        if (self.head is None):
            self.head = new_node
            new_node.next = new_node
        else:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def delete(self, value):
        temp = self.head  
        n1 = temp.next                     # to keep track two consecutive elements

        if (temp is None):
            return 
        
        if (str(temp.data) == value):
            while (temp):
                if (temp.next == self.head):
                    temp.next = self.head.next
                    self.head = n1
                    break
                temp = temp.next

        else: 
            while (temp.next != self.head):
                if (str(n1.data) == value):
                    temp.next = n1.next
                    break
                temp = temp.next   
                n1 = temp.next                    



    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
            if (temp == self.head):
                break
            

# creating the list and nodes
clist = CircularLlist()
clist.prepend(3)
clist.prepend(4)
clist.prepend(5)
clist.prepend("hi")
clist.append("hello")
clist.print_list()
print("\n")
key = input("enter the element to delete: ")
clist.delete(key)
clist.print_list()








