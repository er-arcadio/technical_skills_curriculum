# Linked Lists: Train Cars

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Extensions](#extensions)
- [Hints & Resources](#hints--resources)

## Intro

The train engineers have a chain of train cars that are represented here in code as a linked list. Complete the following challenges by creating functions that manipulate the train car linked list.

_Note: Linked lists are typically done with Object Oriented Programming. The default has been saved as such. Use `data.py` instead of `oop_data.py` if you'd like to learn linked lists without OOP._

## The Lab

**Pre-Lab Walkthrough**

- This is an example dictionary view of the data you will be using in the challenges later on. A dictionary is a good way to visualize a linked list since we cant see the whole structure at once using OOP.

    ```py
    class Monkey():
        def __init__(self, name):
            self.name = name
            self.next_monkey = None

    first_monkey # set to first monkey in linked list
    ```
    ```py
    # first_monkey = monkeys[0]
    # monkeys = [
    #    {'name':'alpha', 'next_monkey':monkeys[1]},
    #    {'name':'beta', 'next_monkey':monkeys[2]},
    #    {'name':'charlie', 'next_monkey':monkeys[3]},
    #    {'name':'delta', 'next_monkey':None},
    #]

    print(first_monkey.next_monkey.name)
    ```
    
    1. What's the "name" of the first monkey?
    2. How do you know that a monkey is last on the linked list?
    3. What will be the output of the print statement?

- Use the code above to reference the following statements:
    ```py
    current_monkey = first_monkey

    while current_monkey != None:
        print(current_monkey.name)
        current_monkey = current_monkey.next_monkey

    print("no more monkeys")
    ```
    1. What does it mean when `current_monkey` **is** `None`
    2. How many times will the while loop iterate?
    2. What is the end result of this code?


## Extensions

_See `main.py` for the challenges_

## Hints & Resources