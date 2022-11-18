

"""     
        Time and Space Complexity:  

For open addressing:

ACTIVITY	        BEST CASE COMPLEXITY	AVERAGE CASE COMPLEXITY  	WORST CASE COMPLEXITY
Searching	            O(1)	            O(1)	                    O(n)
Insertion	            O(1)	            O(1)	                    O(n)
Deletion	            O(1)	            O(1)	                    O(n)
Space Complexity	    O(n)	            O(n)	                    O(n)     

for close addressing(chaining):

ACTIVITY	        BEST CASE COMPLEXITY	AVERAGE CASE COMPLEXITY	    WORST CASE COMPLEXITY
Searching	            O(1)	            O(1)	                    O(n)
Insertion	            O(1)	            O(1)	                    O(n)
Deletion	            O(1)	            O(1)	                    O(n)
Space Complexity	    O(m+n)	            O(m+n)	                    O(m+n)

"""

# Hash table can be implemented using dictionaries in python

def dictionary_implementation():
    # Creating an hash map or dictionary
    hash_table = {
        "Orange": 6,
        "Banana": 5,
        "Mango": 10,
        "pineapple": 20
    }

    # Reading the dictionary
    print(hash_table, "\n")

    # Update 
    hash_table["guava"] = 12
    # or
    hash_table.update({"apple": 34})
    print("Dictionary  After added element: ")
    print(hash_table, "\n")

    # Access
    value = hash_table.get("apple")
    print(f"value of apple: {value}\n")

    # Search 
    inp = input("enter a key to search: ")
    if inp in hash_table:
        print(f"{inp} is present in the dictionary\n")


    # Remove 
    # The following methods can be used to remove items or the whole dictionary .
    # pop(), popitem(), del , clear()

    # removes Orange from dictionary
    hash_table.pop("Orange")    

    # removes the last item in the dictionary
    hash_table.popitem()                     
    
    # deletes banana
    del hash_table["Banana"]

    # deletes the whole dictionary 
    # del hash_table    
    # Removes all the items in the dictionary  
    # hash_table.clear()                     

    print("dictionary after deletion: ")
    print(hash_table)

dictionary_implementation()
    
