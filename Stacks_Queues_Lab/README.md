# TITLE

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Extensions](#extensions)
- [Hints & Resources](#hints--resources)

## Intro

A Queue uses FIFO - first element in the queue is the first to be pulled out. "first in, first out"

A Stack uses LIFO - last element added to the queue is the first one to be removed. "last in, first out"

Use the idea of a Stack or Queue to keep track of data as you work through it.

## The Lab

**Queues**

The following list of logs has been turned into a list of dictionaries. Use a queue to complete the following challenges. 
```py
# Log of activity:
#     Enter 900 - Jeff
#     Enter 902 - Manny
#     Exit 905
#     Enter 910 - Ileini
#     Exit 911
#     Exit 916 
#     Enter 918 - Betty
#     Enter 919 - Danny
#     Exit 923
# NOTE: 900 = 9:00am ; 1400 = 2:00pm

activity_log = [
    {'action':'Enter', 'time':900, 'name':'Jeff'},
    {'action':'Enter', 'time':902, 'name':'Manny'},
    {'action':'Exit', 'time':905},
    ... # see the main.py for the rest
]
```
1. Write a function called `print_queue()` that takes in the `activity_log` and prints the queue after each value has been added or removed. _HINT: 'Enter' means add to the queue, and 'Exit' means pop from the queue_

2. Write a function called `print_times()` that takes in the `activity_log` and prints the total time for each person after they exit. 
    ```
    # output
    Jeff - 5 minutes
    Manny - 9 minutes
    Ileini - 6 minutes
    etc.
    ```
3. Write a function called `lost_crawlers()` that takes in the `activity_log` and prints anybody who is still in the tunnel.


**Stacks**

The following list of logs has been turned into a list of strings. Use a stack to complete the following challenges. 
```py
# Log of activity:
#     Submitted 900 - Jeff
#     Submitted 902 - Manny
#     Grade_Test 905
#     Submitted 910 - Ileini
#     Grade_Test 911
#     Grade_Test 916 
#     Submitted 918 - Betty
#     Submitted 919 - Danny
#     Grade_Test 923
# NOTE: 900 = 9:00am ; 1400 = 2:00pm

grading_log = [
    'Submitted 900 - Jeff',
    'Submitted 902 - Manny',
    'Grade_Test 905',
    ... # see the main.py for the rest
]
```
_Hint: Look up and use the `Str.split()` method to read the parts of each log_

4. Write a function called `print_stack()` that takes in the `grading_log` and prints the stack after each value has been added or removed. _HINT: 'Submitted' means add to the stack, and 'Grade_Test' means pop from the queue_

5. Write a function called `print_stack_times()` that takes in the `grading_log` and prints the total time it takes for each test to be graded. 
    ```
    # output
    Manny - 3 minutes
    Ileini - 1 minutes
    Jeff - 16 minutes
    etc.
    ```
6. Write a function called `not_graded()` that takes in the `grading_log` and prints anybody who still hasn't had their test graded.

## Extensions

`print( myFunc( len(myList) )`
- The line above is missing a closing parenthesis. Write a function that takes in a string like the one above and checks if any closed parenthesis are missing.
    _Hint: You'll need to use a stack!_
    ```py
    # For example:

    str1 = 'print( "Hello" )'
    str2 = 'print( myFunc( len(myList) )'

    count_par(str1) # "All brackets complete"
    count_par(str2) # “1 Closed Bracket(s) missing”
    ```

- Modify the previous function to also check for open parenthesis!
     ```py
    # For example:

    str1 = 'print( "Hello" )'
    str2 = 'print( myFunc( len(myList) )'
    str3 = 'if n == 1) and j ==2)'

    count_par(str1) # "All parenthesis complete"
    count_par(str2) # “1 Closed parenthesis missing”
    count_par(str3) # “2 Open parenthesis missing”
    ```

- (Spicy!) Encryption - Write a function `encrypt()` that encrypts any given string by converting the chosen characters using this `encrypt_mapping`:

    ```py
    encrypt_mapping = {
        'e':7,
        'a':'te',
        'r':'??',
        't':25,
        '?':'oa'
    }

    # For example:
    str1 = 'jeff'
    str2 = 'jane'
    str3 = 'earth'

    encrypt(str1) # jeff => j7ff
    encrypt(str2) # jane => jten7 => j257n7
    encrypt(str3) # earth => 7te??25h => 7257oaoa25h => 7257oteote25h => 7257o257o25725h
    ```
    _Hint: can be done with a queue or recursion_

- (Super Spicy) Create a function `decode()` that takes the result from above and decodes it back to the original string.


## Hints & Resources

