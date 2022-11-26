""" 
What is max-heap?
max heap is a complete binary tree, where the value of parent node is less than that of the child node.
It is filled from left side.

for example:
(15 > 12 and 15 > 11 and 41 > 26 and 41 > 12)

Examples of min heap

           15                     100
          /   \                  /    \  
        12     11              51       41 
       /                      /  \     /  \
      6                     32   31   26  12

How is max heap is Implemented?
Max heap is also implemented using an Array.
where arr[0] is the root node.

we can access the left index of any node using:
arr[2*k + 1]

access right node:
arr[2*k + 2]

access parent node:
arr[k-1/2]

Operations on max heaps:
getmax() - getting maximum value of the heap . it takes O(1) Time complexity.
removemax() - removes the maximum element of the heap. Time complexity is O(log n).
insert(value) - Inserting a new element into the heap.Time complexity is O(log n).

"""


class MaxHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    # Helper functions.
    def parent_index(self, index):
        return (index - 1)//2
    
    def parent(self, index):
       return self.storage[self.parent_index(index)]
    
    def left_index(self, index):
        return 2 * index + 1
    
    def left_child(self, index):
        return self.storage[self.left_index(index)]
    
    def right_index(self, index):
        return 2 * index + 2

    def right_child(self, index):
        return self.storage[self.right_index(index)]

    def has_parent(self, index):
        return self.parent_index(index) >= 0
    
    def has_left(self, index):
        return self.storage[self.left_index(index)] is not None

    def has_right(self, index):
        return self.storage[self.right_index(index)] is not None

    def is_full(self):
        return self.capacity == self.size
    
    def swap(self, first, second):
        temp = self.storage[first]
        self.storage[first] = self.storage[second]
        self.storage[second] = temp

    # insertion 
    def insert(self, value):
        if self.is_full():
            raise("insufficent space")
        self.storage[self.size] = value
        self.size += 1
        self.heapify_up()
    
    def heapify_up(self):
        index = self.size - 1
        while (self.has_parent(index) and self.parent(index) < self.storage[index]):
            self.swap(self.parent_index(index), index)
            index = self.parent_index(index)

    def getmax(self):
        return self.storage[0]
    
    def delete_max(self):
        if (self.size == 0):
            raise("Empty heap") 
        root = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return root

    def heapify_down(self):
        index = 0
        print(self.left_child(index), self.storage[index])
        while (self.has_left(index) and self.left_child(index) > self.storage[index]):
            self.swap(self.left_index(index), index)
            index = self.left_index(index)
        
    def print_heap(self):
        for i in self.storage:
            print(i, end=" ")
    

if __name__ == "__main__":
    # creating a maxheap with a size of 10
    max_heap = MaxHeap(10)

    # insertion operations
    max_heap.insert(12)
    max_heap.insert(23)
    max_heap.insert(45)
    max_heap.insert(78)
    max_heap.insert(34)
    max_heap.insert(68)
    max_heap.insert(18)
    max_heap.insert(13)
    max_heap.insert(98)
    max_heap.insert(110)

    print("The initial max heap: ")
    max_heap.print_heap()

    print('\n')
    print(f"The maximum value:{max_heap.getmax()}")
    
    max_heap.delete_max()
    print('\n')
    print("max heap after deletion of max value:")

    max_heap.print_heap()

    












