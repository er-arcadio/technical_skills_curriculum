from data import train_cars

first_train = "2779"

print(train_cars[first_train])


# Challenges
# For each challenge, do not use dictionary or list methods 


# -- Mild --

# Print the first train's data

# What color is the second train in sequence? (without peaking at the data)

# Write a function `print_trains(train_cars, first_train)` that prints all the train cars in sequence order


# -- Medium --

new_train = {
    "id": 777,
    "color": "red",
    "weight": 9112,
    "material": "titanium",
}

# Write a function `append(train)` that adds a new train to the end of the linked list.
# Be sure to check your results

# Write a function `pop()` that removes the last item of the linked list

# Write a function `insert(idx, train)` that inserts the new_train at a specified index and returns the ID of the first_train

# Write a function `remove(idx)` that removes a train from the chain (but not the dictionary) and returns the ID of the first_train


# -- Spicy --

# Write a function `reverse(train_cars, first_train)` that makes the last train car first and the first train car last.
# The function should return the new first_train

# Write a function sort_trains(train_cars, first_train). Use your favorite sorting algorithm to sort the trains by weight.
# The heaviest should be at the front and lightest at the back.

# [Super Spicy] Convert the linked list using object oriented programming.
# - Create a new file `Link.py` that defines 2 classes: "Train" and "Car"
# - Train should have the `first_train` variable and a methods to append a new train
# - Car should have all the attributes in the dictionary above -- include "next_train" and "id"

# [Super Spicy] Add and adjust `print_trains()` and the rest of the functions from the Medium challenges in your "Train" class
# the print for each train should display the color, material, and weight.