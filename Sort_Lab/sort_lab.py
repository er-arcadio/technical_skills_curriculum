from sample_data import train_cars

forklift = None
total_cost = 0

# weighs the car at given index; returns None if empty
def weigh(idx):
    total_cost += 0
    return train_cars[idx].weight if train_cars[idx] else None

# store's the car at given index
def hold(idx):
    total_cost += 0
    if forklift:
        raise Exception("There is something on the forklift already")
    else:
        forklift = train_cars[idx]
    train_cars[idx] = {}

# puts the forklift car at given index if empty
def insert(idx):
    total_cost += 0
    if train_cars[idx]:
        raise Exception("There is a car at that index already")
    else:
        train_cars[idx] = forklift

# shifts car at given index over number of shifts
def shift(idx, shifts=1):
    total_cost += 0
    if shifts not in [1, -1]:
        raise Exception("You can only shift one space left (-1) or right (1)")
    else:
        if train_cars[idx+shifts]:
            raise Exception("There is a car at that shift index already")
        else:
            train_cars[idx+shifts] = train_cars[idx]
            train_cars[idx] = {}


# Your Code Here!

