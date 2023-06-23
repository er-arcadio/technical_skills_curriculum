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
    
    while idx == -1 and left_idx <= right_idx:
        middle_idx = math.floor((right_idx+left_idx)/2)
        if sorted_list[middle_idx] < n:
            left_idx = middle_idx + 1
        elif sorted_list[middle_idx] > n:
            right_idx = middle_idx - 1
        else: # it's the middle value
            idx = middle_idx
    
    return idx

# recursive binary
def recurs_idx_of(n, sorted_list):
    left_idx = 0
    right_idx = len(sorted_list) - 1
    middle_idx = math.floor((right_idx+left_idx)/2)

    if left_idx > right_idx:
        return -1
    elif n > sorted_list[middle_idx]:
        return recurs_idx_of(n, sorted_list[middle_idx+1:])
    elif n < sorted_list[middle_idx]:
        return recurs_idx_of(n, sorted_list[:middle_idx])
    else: # it's the middle value
        return middle_idx


print("List: ", data)
print(f"Index of {N}: ", linear_idx_of(N, data))