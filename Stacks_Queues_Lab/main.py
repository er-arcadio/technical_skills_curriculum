activity_log = [
    {'action':'Enter', 'time':900, 'name':'Jeff'},
    {'action':'Enter', 'time':902, 'name':'Manny'},
    {'action':'Exit', 'time':905},
    {'action':'Enter', 'time':910, 'name':'Ileini'},
    {'action':'Exit', 'time':911},
    {'action':'Exit', 'time':916},
    {'action':'Enter', 'time':918, 'name':'Betty'},
    {'action':'Enter', 'time':919, 'name':'Danny'},
    {'action':'Exit', 'time':923},
]

# 1. Write a function called `print_queue()` that takes in the `activity_log` and prints the queue after each value has been added or removed. _HINT: 'Enter' means add to the queue, and 'Exit' means pop from the queue_

# 2. Write a function called `print_times()` that takes in the `activity_log` and prints the total time for each person after they exit. 

# 3. Write a function called `lost_crawlers()` that takes in the `activity_log` and prints anybody who is still in the tunnel.



grading_log = [
    'Submitted 900 - Jeff',
    'Submitted 902 - Manny',
    'Grade_Test 905',
    'Submitted 910 - Ileini',
    'Grade_Test 911',
    'Grade_Test 916',
    'Submitted 918 - Betty',
    'Submitted 919 - Danny',
    'Grade_Test 923'
]

# 4. Write a function called `print_stack()` that takes in the `grading_log` and prints the stack after each value has been added or removed. _HINT: 'Submitted' means add to the stack, and 'Grade_Test' means pop from the queue_

# 5. Write a function called `print_stack_times()` that takes in the `grading_log` and prints the total time it takes for each test to be graded. 

# 6. Write a function called `not_graded()` that takes in the `grading_log` and prints anybody who still hasn't had their test graded.


# Extensions
# Write your own tests for each function!


# 7. Write a function that takes in a string like the one below and checks if any closed parenthesis are missing.
# 'print( myFunc( len(myList) )'


# 8. Modify the previous function to also check for open parenthesis!


# 9. (Spicy!) Encryption - Write a function `encrypt()` that encrypts any given string by converting the chosen characters using this `encrypt_mapping`:
encrypt_mapping = {
    'e':7,
    'a':'te',
    'r':'??',
    't':25,
    '?':'oa'
}


# 10. (Super Spicy!) Create a function `decode()` that takes the result from above and decodes it back to the original string.