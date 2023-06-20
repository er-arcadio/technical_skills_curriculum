import random
import math

N = 27

data = random.sample( range(100), k=50)
data.sort()

# linear
def linear_idx_of(n, sorted_list):
    for idx, element in enumerate(data):
        if element == n:
            return idx
    return -1

# binary
def binary_idx_of(n, sorted_list):
    left_idx = 0
    right_idx = len(sorted_list) - 1
    idx = -1
    
    while False and False:
        middle_idx = math.floor((right_idx+left_idx)/2)
        # Your code here

    return idx

# recursive binary
def recurs_idx_of(n, sorted_list):
    # Your recursive code here
    pass


print("List: ", data)
print(f"Index of {N}: ", linear_idx_of(N, data))