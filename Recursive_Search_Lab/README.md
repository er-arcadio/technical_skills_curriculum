# Recursive Search

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Hints & Resources](#hints--resources)
- [Extensions](#extensions)

## Intro

Binary search is a powerful tool because of it's ability to continuously split the data in half, minimizing the number of observations that need to be made. Recursion is an iterative tool that is best used with some data structures and makes some problems easier to visualize.

This lab is a chance to practice the two concepts, binary search and recursion, in combination.

## The Lab

> This lab is for students that understand what recursion and binary search is, but can use more practice coding the concepts together. If you need a more granular, hands-on walk through of what recursion or binary search is please refer to the lessons prior.

- In the lesson prior, we looked at a way to use binary search to guess the user's number (between 1 and 100). Open the `recursive_search.py` and explain the code and what it's doing with your partner. 
- When students return, have a volunteer explain to the class. _The code is using linear search to find the index of N in the list._
- Ask the students: "For any given number, what's the least and most number of checks the computer will make before finding the number or realizing it's not there?"

**Binary Search**

- Binary search is the idea of looking for a value by repeatedly eliminating the half of the data in which the number cannot be in. _Open up the ["Design a Search" app](https://jolson615.github.io/createasearchalgorithm/index.html), and demo what this binary search algorithm looks like._

- In the app, we can naively search each card one at a time looking for 50. That could take at least 1 and at most 21 searches. **What is the least and most number of searches using the binary search method?** _(At least 1 and at most 4!)_

- In the `recursive_search.py`, have students try to complete the binary search code or code it along with them. There are 3 steps to look out for:
    1. Is the middle number higher than the search number?
    2. Is the middle number lower than the search number?
    3. Is the middle number the search number?

**Binary Recursion**

- Recursion works similar to a loop. In both situations, you will say in pseudocode "in this situation, repeat". There is a key difference:
    - In a loop, you use a condition to determine wether you repeat a block of code.
    - In recursion, you call the function itself, ideally with a smaller form of the data.

- Now, have students attempt to covert the binary search done in a while loop into one that is done recursively.

**Summary**

- How would you compare the recursive and non recursive functions?
    - They're about the same length
    - One uses a while loop, one doesn't
- ?

## Extensions

For each of these problems, code the solution without recursion before attempting it with recursion

**Mild**
- Given a list of words in alphabetical order, find a given word.
    ```py
    words = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-ray', 'Yankee', 'Zulu']

    # write your own tests to ensure this works
    ```
- You can rotate a list to the right by moving the last number to the beginning of the list. For example `[1, 3, 6, 10]` can rotate once to `[10, 1, 3, 6]` (k=1), twice to `[6, 10, 1, 3]` (k=2), and so on. Note: 'k' represents the number of rotations.
    - Given the number of rotations, create a function that searches a rotated list for a number.
    ```py
    rotated_list = [343, 362, 379, 380, 387, 388, 401, 410, 412, 418, 432, 456, 484, 488, 492, 493, 23, 30, 44, 58, 63, 70, 72, 73, 74, 91, 98, 109, 129, 139, 140, 143, 150, 160, 164, 179, 195, 221, 253, 258, 260, 262, 264, 275, 289, 290, 292, 326, 335, 341]
    k = 16
    # write your own tests
    ```
    _HINT: 'k' is the index in which the list dips down to its lowest value._

**Medium**
- Create a function that uses binary search to first find the 'k' value in a rotated list. Then, use the function above to search for a value in the list. HINT: the 'k' number is the only number that is smaller than the number before it. 
- A Bitonic List is a list that increases in value, then decreases in value. For example, `[1, 3, 5, 7, 6, 4, 2]` (k=3). In this case, 'k' is the peak of the array, the highest value, or the value that is larger than both values left and right of it.
    - Given the peak value 'k', create a function that searches a bitonic list for a number.
    ```py
    bitonic_list = [9, 67, 72, 83, 86, 95, 110, 114, 136, 156, 171, 176, 187, 193, 214, 224, 248, 261, 271, 278, 302, 337, 364, 392, 406, 480, 489, 495, 498, 491, 431, 417, 344, 307, 299, 293, 282, 255, 230, 229, 151, 140, 133, 80, 73, 57, 44, 32, 29, 2]
    k = 28
    # write your own tests
    ```
- Create a function that uses binary search to first find the 'k' value in a **bitonic** list. Then, use the function above to search for a value in the list.

**Spicy**

- multi-way (m-way / 3-way / ternary) tree
- Sorted Matrix
- Indexes of the Addends to a Sum

## Hints & Resources