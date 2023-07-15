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


# Challenges

# 1. Finish the code by writing the min_heapify function

min_heap = [2, 3, 6, 8, 10, 15, 18]

def min_heapify(heap):
    pass # Your code here

def push(value, heap):
    heap = [value] + heap
    min_heapify(heap)

push(9, min_heap)
print(min_heap)         # [2, 6, 3, 9, 8, 10, 15, 18]



# 2. Finish the code and pop the head out of the list. Use your min_heapify function from before.

min_heap = [2, 3, 6, 8, 10, 15, 18]

def pop_min_heap(heap):
    # your code here
    return 

print("Minimum Value:", pop_min_heap(min_heap))  # 2
print(min_heap)             # [3, 6, 10, 9, 8, 18, 15]



# 3. Write a function that returns the indexes of all the leaf nodes in a heap.



# 4. Write a function `max_heapify(heap)` that does the same as `min_heapify(heap)`, but keeps the greatest value at the head.



# 5. Write a function `build_max(heap)` that turns a list into a max heap.
# You will need to use functions you've built previously
# Check to see that your final answer has been turned into a Max Heap

data = [13, 17, 1, 5, 4, 9, 14, 10, 6]

def build_max(heap):
    pass

max_heap = build_max(data)
print(max_heap)



# 6. Given a list of unsorted values, write a function `heap_sort(data)` that sorts the values from least to greatest.

unsorted_list = [13, 17, 1, 5, 4, 9, 14, 10, 6]