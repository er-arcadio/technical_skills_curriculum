# Linear and Binary Search

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Teacher Notes

### Goal & Sequence

NOTE: This Lab is Incomplete.

### Teaching Tips (optional)

### Representation (optional)

### Learning Objectives

Students will be able to:

_with advanced lense_
_3-5 objectives_
_0-2 stretch obj._

## Launch

- Open up the ["Design a Search" app](https://jolson615.github.io/createasearchalgorithm/index.html) and have students see if they can find 50 or prove its not there.

- Ask students what a sure fire strategy of always finding 50 is. One effective but slow way we can always find 50 or prove its not there is by clicking on every square and revealing their number. If we see 50 we know it is there, and if we do not we know it is not. However, there's a more efficient way. Any ideas?

- Give students some time to develop a strategy. Then ask them if they've noticed any patterns? 
    - _Hint1: The numbers are in order, and we can use that to our advantage when coming up with a strategy._ 
    - _Hint2: For example, if you click on a number too high then you can skip clicking on all the numbers to the right of that -- too low and you can skip the numbers to the left of that._

- Have a student be the driver as you navigate them through the binary search algorithm. If you click in the middle, whether or not you get 50, you can eliminate at least half of the squares, etc. 

- Questions to ask students:
    - What's better about this "binary" method vs the original "linear"?
    - What's the fewest and most click you'd need using linear search? What about using binary search?

## Lesson Walkthrough

Think of a number between 1 and 100, and I'm going to try to guess it. Tell me whether your number is higher or lower after each guess. Can you write this code?

**Linear Search**

- Share this piece of code with your students, but don't run it yet!
    ```py
    print("Think of a number between 1 and 100, and I'm going to try to guess it. Please respond with either 'yes', 'higher', or 'lower'.")

    guess = 0
    response = ''

    while response.lower() != 'yes':
        guess += 1
        response = input(f"Is it {guess}? ")

    print(f"Hurray! Your number is {guess}!")
    ```

- Have students turn and talk to their partner and explain to each other what is happening in this code. Have a student or pair lead walking through the above code. _It is guessing each number starting at 1 until we arrive at the number._

- Tell students you're thinking of a number 5 for example (be sure to pick one under 10). Then, demo the code. Notice

**Binary Search**

- Now ask a student to think of a number between 1 and 100, and guess their number using the binary search algorithm.
    - you: "Is it 50?"
    - student: "lower"
    - you: "Is it 25?"
    - student: "higher"
    - ...etc.

- Ask students to formulate an idea of how you may be arriving at the number. Repeat the game several times until they notice that you are using the same binary technique you used in the "Design a Search" app above.

- The linear search code above can be found in the `search.py`. Have students open this file and use it as a framework to try and code a binary search game solver. _NOTE: if students prefer, give them the option to watch YOU code it from scratch instead._ 
    ```py
    import math

    print("Think of a number between 1 and 100, and I'm going to try to guess it. Please respond with either 'yes', 'higher', or 'lower'.")

    lowest_num = 1
    highest_num = 100
    response = ''

    while response.lower() != 'yes':
        guess = math.floor( (lowest_num+highest_num) / 2 ) # guess will always be the average (middle) of the 2 numbers
        response = input(f"Is it {guess}? ")

        if response.lower() == 'higher':
            lowest_num = guess + 1
        elif response.lower() == 'lower':
            highest_num = guess - 1
        

    print(f"Hurray! Your number is {guess}!")
    ```

- When students return together, consider asking a few of them to share their work with the class.

## Close

Questions for Reflection

- What are the minimum and maximum amount of guesses for Linear Search? ...Binary Search?
- Which way do you prefer to write code to search for a value? Why?
- When would linear search make more sense to use? Why? Consider these lists ( ages, names, user profiles (dictionary format), IDs, passwords)
- There's linear (1) and binary (2). Is there a world where ternary (3) or quaternary (4) search would make sense?

## Extra Help & Resources

- ["Design a Search"](https://jolson615.github.io/createasearchalgorithm/index.html) app to help visualize
- [Binary Search Video Resource](https://youtu.be/KXJSjte_OAI?t=118)
- Interesting [Ternary Search Video](https://www.youtube.com/watch?v=WyWL1PBNvb8)