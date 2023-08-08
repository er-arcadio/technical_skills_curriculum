# Linked Lists: Train Cars (No OOP)

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Extensions](#extensions)
- [Hints & Resources](#hints--resources)

## Intro

The train engineers have a chain of train cars that are represented here in code as a linked list. Complete the following challenges by creating functions that manipulate the train car linked list.

_Note: Linked lists are typically done with Object Oriented Programming. OOP has been omitted here to eliminate that prerequisite, but the concepts and techniques remain the same._

## The Lab

**Pre-Lab Walkthrough**

- This is an example dictionary view of the data you will be using in the challenges later on. A dictionary is a good way to visualize a linked list since we cant see the whole structure at once using OOP.

    ```py
    first_train = "33"
    train_cars = {
        "12" : {
            "color" : "black",
            "weight" : "9232",
            "material" : "coal",
            "next_train" : None  
        },
        "33" : {
            "color" : "red",
            "weight" : "3139",
            "material" : "gold",
            "next_train" : "12"
        }
    }

    print(train_cars[first_train]["next_train"])
    ```
    1. What's the "material" held in the first train?
    2. How do you know a train is the last one on the tracks? first one?
    3. What will be the output of the print statement?

- Use the code above to reference the following statements:
    ```py
    train_id = first_train

    while train_id != None:
        this_train = train_cars[train_id]
        print(this_train["color"])

        train_id = this_train["next_train"]

    print("no more trains")
    ```
    1. What is the meaning of the condition on line 3? `train_id != None`
    2. How many times will the while loop iterate?
    2. What is the end result of this code?


## Extensions

_See `main.py` for the challenges_

## Hints & Resources