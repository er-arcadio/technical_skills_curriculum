# 4. Stretch: Is there an optimal cost of power transfer?
# 5. Stretch: Are there any single points of failure?

# Use any or all 4 grids in sample_data to test your functions

from sample_data import grid1, grid2, grid3, grid4

# 1. Write a function that checks if all power plants have power.
# HINT: Another way of saying this is check that all nodes are visited.

def full_power(power_grid):
    pass

full_power(grid1)


# 2. Write a function that checks if there is a loop in your power grid.
# HINT: Check for a cycle from every node.

def has_cycle(power_grid):
    pass

has_cycle(grid1) #False
has_cycle(grid2) #True


#[Spicy]
# 3. Write a function that finds all the unique paths from one plant to another.

def get_path(power_grid, start, end):
    pass

get_path(grid1, 0, 4) # [[0, 1, 4]]
get_path(grid1, 4, 5) # [[4, 6, 5], [4, 3, 5], [4, 3, 2, 5], [4, 3, 6, 5]]


from sample_data import grid5, grid6

# 4. Write a function that takes in a weighted directional graph, a start node, and an end node:
# It find the paths from start to end (or return an empty list), and the cost of that path.
# See the ReadMe for more context.

def cheapest_path(power_grid, start, end):
    pass


cheapest_path(grid5, 1, 2)  # [{'path':[1, 2], 'cost':1}, {'path':[1, 4, 2], 'cost':6}]
cheapest_path(grid6, 0, 6)  # []


# 5. Re-write the function from number 5 to return the most cost efficient path.


# (Optional) BONUS

# 6. In the maze.py there's a graph of a maze (a bidirectional graph).
# If 0 is the start node and the index with the value 'exit' is the destination node, find the path that gets you out of the maze.
