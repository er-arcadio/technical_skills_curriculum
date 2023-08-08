## If using the Dictionary Data
# from data import train_cars
# first_train_id = "277"
# print(train_cars[first_train_id])
# For each challenge, do not use dictionary or list methods 

## If using the OOP data
from oop_data import first_train
# class Car():
#     def __init__(self, ID, color, weight, material):
#         self.ID = ID
#         self.color = color
#         self.weight = weight
#         self.material = material
#         self.next_train = None




# -- Mild --

# 1. Print the first train's data

# 2. What color is the second train in sequence? (without peaking at the data)

# 3. Write a function `print_trains()` that takes in the first train and prints all the train car IDs in sequence order


# -- Medium --

new_train = {
    "id": 777,
    "color": "red",
    "weight": 9112,
    "material": "titanium",
}

# 4. Write a function `append(first_train, train)` that adds a new train to the end of the linked list.
# Be sure to check your results

# 5. Write a function `pop()` that removes the last item of the linked list

# 6. Write a function `insert(idx, train)` that inserts the new_train at a specified index and returns the ID of the first_train

# 7. Write a function `remove(idx)` that removes a train from the chain and returns the first train


# -- Spicy --

# 8. Write a function `reverse()` that takes in the linked list and reverses it.
# The function should return the new first_train

# 9. Write a function sort_trains(). Use your favorite sorting algorithm to sort the trains by weight.
# The heaviest should be at the front and lightest at the back.

# 10. [Super Spicy] Use object oriented programming to create a Train class.
# - Train should have the `first_train` variable and a function to append a new train

# 11. [Super Spicy] Finish adding the following functions to your Train class:
# - `print_trains()` 
# - `pop()`
# - `insert()`
# - `remove()`