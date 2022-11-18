"""
Time complexity of various operations on arrays.

ARRAY OPERATION	            REAL TIME COMPLEXITY	|   ASSUMED TIME COMPLEXITY
Access i-th element	            O(√N)	            |       O(1)
Traverse all elements	        O(N + √N)	        |       O(N)
Override element at i-th index	O(√N)	            |       O(1)
Insert element E	            O(N + √N)           |       O(N)
Delete element E	            O(N + √N)           |       O(N)

"""







import array


# array CRUD
# initializing array with values
arr = array.array('i', [1, 2, 3])          # creating array

# printing the original array
print(f'The newly created array: ', end=" ")          # reading the array
for i in arr:
    print(i, end=" ")


# UPDATE OPERATION
# append() - it is used to append an element at the end of an array
# insert(index, value) - it is used insert an element at a given index.

# using append
arr.append(4)                                                # updating array

print(f"\n\nthe array after appending: ", end=" ")
for i in arr:
    print(i, end=" ")

# using insert()
# inserting 8 at 3rd position
arr.insert(3, 8)                                               # updating array

print("\n\nThe array after inserting value: ", end=" ")
for i in arr:
    print(i, end=" ")


# Delete Operation
# pop() - It removes the element of the postion mentioned in its parameters and returns it.
# remove() - It removes the first occurance of the element mentioned in its parameter.

# using pop()
arr.pop(1)                                                               # delete operation 

print("\n\nThe array after pop operaion: ", end=" ")
for i in arr:
    print(i, end=" ")

# using remove()
arr.append(1)
# removes the first occurance of 1
arr.remove(1)                                                               # DELETE OPERATION

print("\n\nThe array after remove operation: ", end=" ")
for i in arr:
    print(i, end=" ")

# index() - It returns the index of the first occurance of the mention value.
# reverse() - It reverses the array

print(f"\n\nindex of 1: {arr.index(1)}")                                           # SEARCH OPERATION

arr.reverse()
print(f"\nThe array after reversing: ", end=" ")
for i in arr:
    print(i, end=" ")




