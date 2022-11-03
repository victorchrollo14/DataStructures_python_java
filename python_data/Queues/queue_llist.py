

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
    
    # method to add elements to the queue
    def enqueue(self, value):
        item = Node(value)

        # Linking the nodes 
        if (self.head is None):
            self.head = item

        else:
            item.next = self.head
            self.head = item
    
    # method to remove elements from the queue
    def dequeue(self):
        temp = self.head 
        head = self.head
        try:
            while (temp):
                nxt_temp = temp.next
                if (self.head.next is None):
                    self.head = None
                    return head.data

                elif (nxt_temp.next is None):
                    temp.next = None
                    return nxt_temp.data
                    
                temp = temp.next
        except Exception as e:
            print(e)

    # Function to print all the elements of the queue
    def print_queue(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def front(self):
        temp = self.head 
        return temp.data
    
    def rear(self):
        temp = self.head
        while (temp):
            if (temp.next is None):
                return temp.data
            temp = temp.next
        
        
if __name__ == "__main__":
    que = Queue()

    # adding elements to the queue
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)

    print("The Initial queue: ")
    que.print_queue()

    print(f"accessing the front element of queue: {que.front()}")
    print(f"accessing the rear element of the queue: {que.rear()}")

    print("\nelements dequeued from queue: ")
    print(que.dequeue())
    print(que.dequeue())
    print(que.dequeue())
    print(que.dequeue())

    print("\nQueue after Dequeue: ")
    que.print_queue()


        