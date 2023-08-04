# Introduction to Classes

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Teacher Notes

### Goal & Sequence

This lesson gives students an introduction to classes and a rationale as to why they are useful. The lesson covers mostly abstraction and a bit of encapsulation. There is no polymorphism or inheritance here.

A python template in which students can work from has been attached with a copy of the code. 

- [Launch](#launch)
- [Lesson Walkthrough](#lesson-walkthrough)
- [Extensions](#extensions)
- [Close](#close)

### Learning Objectives

Students will be able to:

- Distinguish data from actions in a class
- Compare the use of classes with that of dictionaries in Python
- Read `__init__()` functions and create and read other functions in classes using the `self` identifier.
- Create multiple instances of classes. 

## Launch

**Data and Actions**

We're building a program where we need to save multiple pets in variables. All pets have similar attributes, for example `name`, `hunger_level`, and so on. Let's brain storm a couple more:

- Open up a doc or sketch pad and create the heading `Attributes`. Come up with as many _pet_ attributes you can think of. For example:
    ```
    Attributes (aka Data)
    - name
    - hunger_level
    ...
    ```

- Now create a new heading `Actions`. Come up with as many actions that a pet may do, and in parenthesis, include the attribute that may become affected. Here are some examples to get you started:
    ```
    Actions
    - eat (lowers hunger_level)
    ...
    ```
    _Note: if you think of an action that changes an attribute you didn't include yet, add it to Attributes!_

- What data type might you use to create and store a pet in python?

**Mini Challenge**

- Using only the few attributes in this example, create as many unique pets you can think of in just 1 minute:
    ```py
    pet1 = {
        'name': 'Sir Fluffy III',
        'breed': 'Cat',
        'hunger_level': 7,  # 0 = starving; 10 = full
        'energy': 2,        # 0 = no energy; 10 = charged/playful
    }
    ```
    - What was the most challenging part about this challenge?
    - [Spicy] How would you incorporate the action `sleep()`? What would be the input? What data would be change?

## Lesson Walkthrough

- A **Class** allows us to create a new customized data structure with attributes (aka **Data**) and **Actions** written as functions. Most classes have an `__init__()` function that activates once as soon as a new variable of the class is created. This variable is called an **instance**.
    ```py
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

    print(pet1.name)
    print(pet1.energy)

    pet1.sleep(2)
    print(pet1.energy)
    print(pet2.energy)
    ```

    - Predict as many outputs as you can before running the code
    - Add the functions `eat()` and `play()`. Change which ever variable(s) you think should be changed.
    - Create a new Pet, and have them eat, play, and sleep. Then, print out their attributes.

## Extra Help & Resources
