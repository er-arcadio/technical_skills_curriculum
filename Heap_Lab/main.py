# Note: If you get stuck refer to the ReadMe.md

# Helper Functions
def head_idx():
    return 0

def left_of(idx):
    return 2*idx + 1

def right_of(idx):
    return 2*idx + 2

def parent_of(idx):
    return (idx-1) // 2 

# Data
min_heap = [2, 3, 6, 8, 10, 15, 18]


# Mild

# 1. The index for '6' is 2. Print the left and right child nodes of 6

# 2. Print the parent node of 6.

# 3. A new value has been added to the heap. (always at element 0)
# Write a loop; While 9 is bigger than either of its 2 children, swap it in the list with the smaller of the 2.

new_value = 9
min_heap.insert(0, new_value)
# YOUR WHILE LOOP HERE
# print(min_heap) # [2, 6, 3, 9, 8, 10, 15, 18]


# 4. Put your while loop in the `min_heapify` function below:
# Adjust the code so that the following does the same as before.

def min_heapify(heap):
    pass # Your code here

def push(value, heap):
    heap.insert(0, value)
    min_heapify(heap)


min_heap = [2, 3, 6, 8, 10, 15, 18]
push(9, min_heap)
print(min_heap)         # [2, 6, 3, 9, 8, 10, 15, 18]


# Medium

# 5. Finish the code and pop the head out of the list (remove the first value).
# Use your min_heapify function from before to make sure the smallest value is now at the head.

def pop_min_heap(heap):
    # your code here
    return 


print("Minimum Value:", pop_min_heap(min_heap)) # Minimum Value: 2
print(min_heap)                                 # [3, 6, 10, 9, 8, 18, 15]



# 6. Use a loop to pop all the values in the heap (and heapify each time)
# NOTE: this should print all the values in ascending order.


# 7. Write a function `max_heapify(heap)` that does the same as `min_heapify(heap)`, but keeps the greatest value at the head.
# Create your own max_heap and tests.



# Spicy

# 8. Write a function that returns the indexes of all the leaf nodes in a heap.


# 9. Write a function `build_max(heap)` that turns a list into a max heap.
# You will need to use functions you've built previously
# Check to see that your final answer has been turned into a Max Heap

data = [13, 17, 1, 5, 4, 9, 14, 10, 6]

def build_max(heap):
    pass

max_heap = build_max(data)
print(max_heap)


# 10. Given a list of unsorted values, write a function `heap_sort(data)` that sorts the values from least to greatest.

unsorted_list = [13, 17, 1, 5, 4, 9, 14, 10, 6]