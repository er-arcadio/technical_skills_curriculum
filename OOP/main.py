# Class definition
class Pet():
    def __init__(self, name, breed, energy=5):
        self.name = name
        self.breed = breed
        self.hunger_level = 0
        self.energy = energy

    def sleep(self, hours):
        new_energy = 2*hours + self.energy
        if new_energy > 10:
            new_energy = 10
        self.energy = new_energy


# Main Code
pet1 = Pet('Sir Fluffy III', 'Cat')     # 1 instance created
pet2 = Pet('Blue', 'Dog', energy=10)    # Another instance created


# 1. Predict as many outputs as you can before running the code
print(pet1.name)    #
print(pet1.energy)  #

pet1.sleep(2)
print(pet1.energy)  #
print(pet2.energy)  #

# 2. Add the functions `eat()` and `play()`. Change which ever variable(s) you think should be changed.

# 3. Create a new Pet, and have them eat, play, and sleep. Then, print out their attributes.