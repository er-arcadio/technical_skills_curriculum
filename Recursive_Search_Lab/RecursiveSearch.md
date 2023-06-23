# Recursion & Binary Search

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Hints & Resources](#hints--resources)
- [Extensions](#extensions)

## Intro

This lab is a chance to practice the two concepts, binary search and recursion, in combination.

**Binary Search** - Split the data in half. Is the value higher or lower? Get rid of the wrong side. Repeat until you find the data point.
**Recursion** - Function does something with a piece of data. If it's too big, **function calls itself** again with a smaller form of the data.

## The Lab

1. Open up the `recursiveSearch.py`. There, you will see a sorted list (`data`) of random values. You're also given a `key` which is a number that may or may not be in that list. Run the code a couple of times and see for your self.

2. Write a function that returns the index of where 27, the key, is located or -1 if the value isn't in the list. (Don't worry about efficiency for now)

3. Now, use binary search to write a new function that does the same thing. It may help to say the steps out loud to your partner or write them down in pseudo-code before coding out the solution. (Note: Skip this step if you did it this way in #3)

4. Finally, create a third function that uses binary search to look for the key, but this time it should use recursion instead of a loop. Here's the pseudo-code if you need it:
    - If the (middle) number is equal to the key, return the number's index.
    - If the key is greater, run this function again with the right half of the list.
    - If the key is lesser, run this function again with the left half of the list.

5. Congrats! Because your function calls itself, you are using recursion!

## Extensions

For each of these problems, code the solution **without** recursion before attempting it **with** recursion. The starter code can be found in the `extension.py`.

**Mild**

1. Given a list of words in alphabetical order, write a function to find a given word.
    
2. You can rotate a list to the right by moving the last number to the beginning of the list. For example `[1, 3, 6, 10]` can rotate once to `[10, 1, 3, 6]` (k=1), twice to `[6, 10, 1, 3]` (k=2), and so on. Note: 'k' represents the number of rotations.
    - Given the number of rotations, create a function that searches a rotated list for a number. _HINT: 'k' is also the index of the lowest value._

**Medium**

3. Create a function that uses binary search to first find the 'k' value in a rotated list. Then, use the function from #2 to search for a value in the list. HINT: the 'k' index value is the only number that has a larger number to the left. 

4. A Bitonic List is a list that increases in value, then decreases in value. For example, `[1, 3, 5, 7, 6, 4, 2]` (k=3). In this case, 'k' is the peak of the array, the highest value, or the value that is larger than both values left and right of it.
    - Given the peak value 'k', create a function that searches a bitonic list for a number.

5. Create a function that uses binary search to first find the 'k' value in a **bitonic** list. Then, use the function above to search for a value in the list.

**Spicy**

6. In ternary search, pick 2 random values and check if the value is less than both, greater than both, or in between the 2. Check out this [video on ternary search](https://www.youtube.com/watch?v=o3HPRpbGlbI), or do some research on your own. Then, write a function that applies this technique to a normally sorted list. 

7. Given a sorted list, find the indexes of the 2 numbers that add to a given sum. I can think of 3 ways to do this, but there are plenty! First, write any working program, then try to reduce your loops to just 1! Last, find a different way incorporating recursion.

## Hints & Resources

- [Recursion video in Python](https://www.youtube.com/watch?v=ivl5-snqul8) - How to code using a loop vs using recursion.
- [Article on visualizing recursion](https://medium.com/swlh/visualizing-recursion-6a81d50d6c41).
- ["Design a Search"](https://jolson615.github.io/createasearchalgorithm/index.html) app to help visualize
- [Binary Search Video Resource](https://youtu.be/KXJSjte_OAI?t=118)
- Interesting [Ternary Search Video](https://www.youtube.com/watch?v=WyWL1PBNvb8)