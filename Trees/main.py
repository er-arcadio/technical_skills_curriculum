from tree import tree

# Test
def get_value(t):
    current_node = t
    while current_node['right']:
        current_node = current_node['right']
    return current_node['value']

print(get_value(tree))

# Mild

# 1. Write a function to get the minimum value in a tree.

def get_min(tree):
    pass


# 2. Write a function that searches for a given value n in a tree.
# Should return true if the value exists

def find(n, tree):
    pass

# Medium

# 3. Modify the function find() from #2 to return the list of visited nodes if the value exists.

# 4. Write a function called get_parent(n, tree) that returns the parent of a given value or -1.
# For example, get_parent(6, tree) => 8, and get_parent(5, tree) => -1 since there is no parent for 5.


# Spicy

# 5. Write a function called youngest_relative(x, y, tree) that finds the closest common ancestor of a node or -1.
# For example, youngest_relative(6, 10, tree) => 8, youngest_relative(4, 9, tree) => 5