from collections import deque

# Implementation of  QUEQUE using list
def queue_list():
    # creating an empty list
    queue = []           

    # adding Elements to the queue (Enqueue)
    queue.append('a')
    queue.append('b')
    queue.append('c')

    print(f"The elements of queue are: {queue}")

    # Removing Elements elements from the queue (Dequeue)
    print("\nElements dequeued from queue")
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))

    print(f"queue after deletion:\n{queue}")

# queue_list()

def queue_using_deque():
    queue = deque()

    # adding Elements to the queue (Enqueue)
    queue.append('a')
    queue.append('b')
    queue.append('c')

    print(f"Initial queue:\n{queue}")

    # Removing Elements from a queue (Dequeue)
    print("\nElements dequeued from the queue ")
    print(queue.popleft())
    print(queue.popleft())
    print(queue.popleft())

    print(f"queue after deletion:\n{queue}")

queue_using_deque()
