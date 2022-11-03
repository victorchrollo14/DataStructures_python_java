
# Creating a node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating a Linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to push the element on top of the stack
    def push(self, value):
        item = Node(value)
        if (self.head is None):
            self.head = item
        else:
            item.next = self.head
            self.head = item

    # Function to remove and return the top element of the stack
    def pop(self):
        temp = self.head
        assert temp is not None, f"The Stack is empty"
        self.head = self.head.next         # changing the head from current head to next element
        return temp.data
    
    
    # Fuction to return the elements in a stacks
    def print_stack(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def is_empty(self):
        if (self.head is None):
            return True
        else:
            return False

    def peek(self):
        temp = self.head
        assert temp is not None, "The stack is empty"
        return temp.data
        

if __name__ == "__main__":
    # Creating an empty stack
    stack = LinkedList()
    
    # Pushing elements into the stack
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # stack.push(4)
    # stack.push(78)
    
    # Printing all the elements of a stack
    stack.print_stack()
    
    # Removing and returning the head of the stack
    print(stack.pop())
    print()

    # return True if stack is empty else False
    print(stack.is_empty())

    # return the top element of the stack
    print(stack.peek())
    


