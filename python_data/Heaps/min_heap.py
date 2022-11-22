"""
What is a min heap?
Min heap is a complete binary tree where the value of the parent node is smaller than or equal to the value of the child node.

from example below:
(5 < 10 and 5 < 15) or (13 < 16 and 13 < 21) or (31 < 100 and 31 < 41)

Examples of min heap

            5                      13
          /   \                  /    \  
        10     15              16      31 
       /                      /  \     /  \
     30                     41    51  100  41


How is a min heap represented?
Min heap is typically represented as an array.
where Arr[0] is the root node.

we can access the left child of node at index 'k' using:
Arr[2*k + 1]

right child of node using 
Arr[2*k + 2]

Parent node using 
Arr[k-1/2]


Operations on min heap:
getMin() - it gets the root element of the min heap, Time complexity is O(1) constant.
extractMin() - it removes the minimum element of the min heap. Time complexity is O(log n) logarithmic, as this operation 
needs to main heap property after removing the root.

"""

class MinHeap:
    
    def __init__(self, capacity):
        self.storage = [0] * capacity
        """ 
        storage = []
        for i in xrange(capacity):
            storage.append(0) 

        """
        self.capacity = capacity
        self.size = 0
        "size of array"
        
    
    def parent_index(self, index):
        return (index - 1)//2
    
    def parent(self, index):
        return self.storage[self.parent_index(index)]
    
    def left_child_index(self, index):
        return (2 * index) + 1

    def has_left(self, index):
        return self.storage[(2*index) + 1] is not None
    
    def right_child_index(self, index):
        return (2 * index) + 2

    def has_right(self, index):
        return self.storage[(2*index) + 1] is not None

    def has_parent(self, index):
        return self.parent_index(index) >= 0

    def is_full(self):
        return self.size == self.capacity

    def swap(self, first, second):
        temp = self.storage[first]
        self.storage[first]  = self.storage[second]
        self.storage[second] = temp 
    
    def insert(self, data):
        if self.is_full():
            raise("insufficient capacity")
        self.storage[self.size] = data
        self.size += 1
        self. heapify_up()
    
    def  heapify_up(self):
        index = self.size - 1
        while (self.has_parent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.parent_index(index), index)
            index = self.parent_index(index)

    def print_heap(self):
        for i in self.storage:
            print(i, end=" ")
    
    def removeMin(self):
        if (self.size == 0):
            raise("Empty heap")
        root = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return root


    def heapify_down(self):
        index = 0
        while (self.has_left(index) and self.storage[index] > self.storage[self.left_child_index(index)]):
            self.swap(self.left_child_index(index), index)
            index = self.left_child_index(index)

    def getMin(self):
        return self.storage[0]


            



if __name__ == "__main__":
    min_heap = MinHeap(10)
    min_heap.insert(23)
    min_heap.insert(24)
    min_heap.insert(36)
    min_heap.insert(67)
    min_heap.insert(12)
    min_heap.insert(15)
    min_heap.insert(45)
    min_heap.insert(6)
    min_heap.insert(17)
      
    print("initial minheap: ")
    min_heap.print_heap()

    min_heap.removeMin()
    
    print("\n")
    print("min heap after deleting root: ")
    min_heap.print_heap()










        



    



















