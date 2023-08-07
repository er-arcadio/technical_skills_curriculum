# Reading and Writing Algorithms

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Hints & Resources](#hints--resources)
- [Extensions](#extensions)

## Intro

If you haven't already, take a couple of minutes to familiarize yourself with the ["Sort the Cards" app](https://sortinggame.emmanuelrodri23.repl.co/).

In this lab we look at different algorithms that have been created to sort a list. Algorithmic thinking is an essential part of coding complex projects. 

## The Lab

- Look at the following code:
    ```py
    def sort(nums):
        n = len(nums)
        for i in range(n-1):    # main for loop
            for j in range(n-i-1):  # nested for loop
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    nums = [64, 34, 25, 12, 22, 11, 90]
    sort(nums)
    ```
    - How many times will the main for loop run?
    - How many times will the nested for loop run?
    - On the first iteration, when `j=0`, what will happen?
    - Write the pseudo code for the algorithm above. What are the steps in words?
    - (Optional) use the Sort the Cards app to visualize.

- The algorithm above is actually called **Bubble Sort**! Not the best algorithm, but one of the simpler ones to code.

## Extensions

**Mild**

1. Bogo Sort: Write the pseudo code for the following python code. 
    ```py
    import random

    def is_ordered(nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False

    def bogo_sort(nums):
        while not is_ordered(nums):
            random.shuffle(nums)

    nums = [3, 5, 2, 1, 4]
    bodo_sort(nums)
    print(nums)
    ```
    _Note this is not a good sorting algorithm. It's for instructional purposes only!_

2. Use this pseudo code for **Insertion Sort** to write the code in Python:
    ```markdown
    ** Insertion Sort **

    1. Look at the first 2 numbers. If they're out of order, swap them.
    2. For the next number if it's the greatest so far, skip it.
    3. Otherwise...
        a. put it in storage.
        b. shift the numbers on the left over to the right until you reach a number that is smaller than the storage number.
        b. Finally, put the storage number back in the new empty space.
    4. Repeat steps 2 and 3 until you've done the last number.
    ```

**Medium**

3. Write the pseudo code for the following python code. Then, change all the variables to be more descriptive ones. [Bonus] See if you can name the sorting algorithm
    ```py
    def sort(n, s):
        for i in range(s):
            m = i
            for j in range(i + 1, s):
                if n[j] < n[m]:
                    m = j
            (n[i], n[m]) = (n[m], n[i])
    
    n = [-2, 45, 0, 11, -9,88,-97,-202,747]
    sort(n, len(n))
    print(n)
    ```

4. Use this pseudo code for **Radix Sort** to write the code in Python: 
    ```markdown
    ** Radix Sort **

    1. Using a dictionary, sort the numbers into lists by their 1s place value.
    2. In order from 0-9, combine the lists into 1 big one.
    3. Repeat steps 1 and 2 for how ever many digits your largest number has. Each time moving over the place value used to group (ie. 10s, then 100s, etc.)
    ```
    _HINT: look up a video of Radix sort if you need to._

**Spicy**

5. Use this pseudo code for **Merge Sort** to write the code in Python:
    ```markdown
    ** Merge Sort **

    1. [Base Case 1] If your list is size 1 or lower, return it
    2. [Base Case 2] If your list is size 2, check if the two values are in order. Swap if they aren't. Return the list
    3. If your list is greater than 2 values, split your list in half, and repeat steps 1, 2, or 3 on both halves depending on their new size. If you do step 3, do step 4 as well.
    4. Merge the 2 halves back together:
        A. Create a new list.
        B. Check the first value of both halves.
        C. Add the smaller value to the new list
        D. Repeat steps B and C. If one of the halves run out of values, just append the rest of the other half.
        E. Return the new list.
    ```

6. Look up the code for **Quick Sort** in Python. Try writing the algorithm yourself before checking it with another online source.


## Hints & Resources

- Use the [Sort the Cards](https://sortinggame.emmanuelrodri23.repl.co/) app to help visualize things when they get too hard to conceptualize.