from heapq import heapify, heappush, heappop


# creating an empty heap
heap = []
heapify(heap)


# Insertion using heappush
heappush(heap, 23)
heappush(heap, 24)
heappush(heap, 36)
heappush(heap, 67)
heappush(heap, 12)
heappush(heap, 15)
heappush(heap, 45)
heappush(heap, 6)
heappush(heap, 35)

# printing the root node or minimum value
print(f"The minimum value: {heap[0]}")

# Accessing the heap values
print("The initial heap: ")
for i in heap:
    print(i, end=" ")
print('\n')

# deleting from the heap
element = heappop(heap)

# Accessing heap values
print("The New values of heap: ")
for i in heap:
    print(i, end=" ")



