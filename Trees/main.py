from tree import tree

# Test 
def get_value(t):
    current_node = t
    while current_node['right']:
        current_node = current_node['right']
    return current_node['value']

print(get_value(tree))



## Mild

# 1. Print the head of the tree. (The first, top most value)

# 2. Print the left and right node of the head. (5 and 8)

# 3. Recursively (easier) or through a loop (harder) print all the values in the tree

# Medium

# 4. Write a function to get the minimum value in a tree.

def get_min(tree):
    pass

# 5. Find the BigO of problem 1-4. Rationalize your thinking.

# 6. Write a function that searches for a given value n in a tree.
# It should return the dictionary at that spot if the value exists and None if it doesn't

def find(n, tree):
    pass

find(4, tree) # {"value":4, "left":None, "right":{...} }


# 7. Duplicate the function find() from #5, but have it return the list of visited nodes if the value exists.
def find2(n, tree):
    pass

find2(4, tree) # 7 => 5 => 4


# Spicy

# 8. Write a function called get_parent(n, tree) that returns the parent of a given value or -1.
# For example, get_parent(3, tree) => 5, and get_parent(7, tree) => -1 since there is no parent for 5.


# 9. Write a function called youngest_relative(x, y, tree) that finds the closest common ancestor of a node or -1.
# For example, youngest_relative(6, 10, tree) => 8, youngest_relative(4, 9, tree) => 5

