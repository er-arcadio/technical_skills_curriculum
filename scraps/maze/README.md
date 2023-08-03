# Searching for the Exit

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Extensions](#extensions)
- [Hints & Resources](#hints--resources)

## Intro

Have you ever gotten lost trying to find your way out of a maze? Check this one out.

![hard maze!](./assets/hard_maze.png)

- What general strategy would you go about doing to get yourself out of this maze? _Note: don't worry about actually getting through, what's most important is your strategy._

## The Lab

- Okay, that was tough! Let's see if we can bring it to code and we'll use a much simpler maze. If we think of a maze as a grid where each cell can be connected to other neighboring cells we get something that looks like this: 

    ![Simple maze as grid](./assets/simple_maze_numbered.png)

- This is what some of the code will look like. Open `maze.py` to see the whole thing:

    ```py
    maze = [
        [1, 6],
        [0, 2],
        [1, 8],
        [4, 9],
        [3, 5],
        # and so on...
    ]
    ```
    - Looking at the maze list, what cell can you go to from cell-2?
    - Looking at the maze graph, what cells can you go to from cell-27?
    - (Stretch) Find the full path from start to end. Travel by saying the numbers out loud.

- 

**The Maze - DFS with Stacks**
What strategy do you use to solve a maze puzzle?
Write pseudocode for your strategy




## Extensions

## Hints & Resources