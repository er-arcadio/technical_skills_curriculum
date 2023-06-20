# Sorting Algorithms

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Teacher Notes

### Goal & Sequence

The goal of this lesson is to have students explore algorithms and sorting techniques through a ["Sort the Cards" game app](https://sortinggame.emmanuelrodri23.repl.co/). The focus mostly consists of trial and error, formulating and documenting ideas and strategies, and demoing and articulating those ideas with fellow classmates.

Towards the end of the lesson, students will have the opportunity to put some algorithms into code and introduce some vocabulary.

### Teaching Tips

Students learn best when they internalize through exploration and discussion. This lesson is designed intentionally to avoid vocabulary and code for the first half. As students begin to feel confident articulating their own algorithms, consider only then introducing the fundamental algorithms and allowing them to bring it to code on their own. 

Note: The most advanced sorting interview questions have students not memorizing algorithms, but being able to understand and bend them to optimize for a specific problem. This exploration is meant to facilitate that type of thinking.

### Representation

Consider asking students, "In what context have you heard the term 'algorithm' used?". Some examples that may come up include: Rubik's Cube Algorithm, Youtube (or other social media) algorithm, Computer Science algorithms, or the Google Search algorithm.

Here are some other algorithms you can use to start a discussion having students formulate their own definition of an algorithm.
- Tying your shoes
- Grouping M&Ms or Skittles into  their colors
- Following a recipe (or driving directions)
- Bedtime or Morning routine.
- Facial Recognition

### Learning Objectives

Students will be able to:

- Formulate and articulate their own sorting algorithms. 
- Compare different algorithms explaining the benefits and drawbacks.
- Bring their algorithmic thinking to code.

## Launch

Start up the "Sort Cards" game and demo how it works -- the goal is to sort the cards in order from least to greatest. Have the students just play for now, and allow them to get familiar with how the app works.

Once most of them have finished, ask if any of them had a repeatable strategy that they can explain to the class. Disregard vocabulary for now and commend each volunteer.

Have them play again, this time focussing on a specific repeatable strategy. Be sure they ignore the counts (observations, cycles, etc.) for now.

Finish off by giving several students the time and space to clearly articulate the strategy they came up with. Consider demoing a preview on your screen or allowing them to share theirs with the class. 

## Lesson Walkthrough

> Note: The following lesson uses Insertion Sort and Selection Sort. However, Bubble, Selection, or Insertion Sort can each be interchanged at any point. 

**Unplugged / No Code**
- Use a student's algorithm, or the insertion sort algorithm to demo how students should now articulate their strategy on a document, paper, or other means. For example:
    ```markdown
    ** Manny's Sort ** (really just Insertion Sort)

    1. Look at the first 2 numbers. If they're out of order, swap them.
    2. For every other number if it's the greatest so far, skip it. Otherwise, put it in storage.
    3. Shift numbers on the left over until you reach a number that is smaller than the storage number.
    4. Finally, put the storage number back in the new empty space.
    ```
    _Note: the goal is not to have it align to code, but to think algorithmically or in clear repeatable steps._

- After demoing this algorithm, ask students to now notice the 4 counts, observations, cycles, moves, and storage, and predict what they're counting. 
    - Observations: number of times your are looking at a card
    - Moves: moving a card from one spot to another
    - Storage: number of empty slots available
    - Cycles: (tricky) max number of times you've observed the same number.

- Have students try again to sort the cards while keeping these counts low. They should focus on creating a repeatable strategy and articulating it to their partner.

- When students return, allow them to share their algorithms with you and the class navigating as you drive to demo for all to see. 

**Incorporating Code**

- Now, flip the script and have another student drive as you navigate them through Selection Sort. For Selection Sort, look for the smallest number and place it in the first slot. Then, look for the next smallest and put it in the second slot, and so on until the list is sorted. _You can have them share their screen if on virtual or come up to the front of the class._ _NOTE: this is not going to be a low scoring algorithm, but it is a guaranteed simpler one to code out._

- Ask students to try to code this algorithm in Python. Consider pairing off the students that are ready to go, and demoing the steps once more using the app, for students who would like to see it again. 

- Once students return, have a couple of them explain their code to the class. Here's one way to do it:
    ```python
    def selection_sort(sample_list):
        sorted_list = []

        for i in range( len(sample_list) ):
            smallest = sample_list[0]
            for element in sample_list:
                if element < smallest:
                    smallest = element
            sorted_list.append( sample_list.pop(smallest) )
        
        return sorted_list

    print(selection_sort([5, 2, 1, 3, 4]))
    ```

## Extensions

- Try Selection sort without creating a new list!

    HINT: You can use the following piece of code to swap two variables' values:

    ```py
    num1 = 4
    num2 = 10
    (num1, num2) = (num2, num1)
    # num1 = 10
    # num2 = 4
    ```

- Check out the algorithm for [Insertion Sort](https://www.youtube.com/watch?v=JU767SDMDvA), and try to code it!  

## Extra Help & Resources

- [Algorithm for tying shoes](https://madice99.wordpress.com/2016/09/07/algorithm-for-tying-your-shoes/)
- [Selection Sort](https://www.youtube.com/watch?v=g-PGLbMth_g)