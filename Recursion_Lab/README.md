# Recursion Lab

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Extensions](#extensions)
- [Hints & Resources](#hints--resources)

## Intro

You may have heard of the **Fibonacci sequence**; the first 2 numbers are 0 and 1 and each number after is the sum of the previous two numbers: 0, 1, 1, 2, 3, 5, 8, 13, etc.

But, have you heard of **Collatz Conjecture**!? It's a famous unsolved problem in mathematics. The conjecture says that every integer, that follows these 2 rules, will eventually reach 1.
- Rule 1: if the current number is even, divide it by 2
- Rule 2: if the current number is odd, multiply it by 3 and add 1 (3x + 1)

With these 2 rules, you will always eventually reach 1! For example:
- **3**, 10, 5, 16, 8, 4, 2, **1**
- **7**, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, **1** 

## The Lab

- Write a function for **Collatz Conjecture** using a while loop. _It should take in any starting integer and print all the numbers in the sequence up until it hits 1._
    ```py
    # Here's a little bit of starter code
    def collatz_while(n):
        while n > 1:
            pass

    collatz_while(3)
    ``` 
- Now, try to redo this function recursively! That means it should have no while loop and instead the function should call itself if we haven't reached 1 yet.
    ```py
    # Here's a little bit of starter code
    def collatz_recurs(n):
        pass

    collatz_recurs(3)
    ```

- Nice! Now, if you run into an infinite loop, submit your starting number. You can disprove the conjecture and make millions of dollars!

## Extensions

Professor Curious has a whole bunch of other similar conjectures and sequences. For each write 2 functions. One that uses a loop and one that uses recursion.

_See the `recursion.py` for the extensions._

## Hints & Resources

- [Recursion video in Python](https://www.youtube.com/watch?v=ivl5-snqul8) - How to code using a loop vs using recursion.
- [Article on visualizing recursion](https://medium.com/swlh/visualizing-recursion-6a81d50d6c41).