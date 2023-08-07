# Sorting Algorithms

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

Open up the ["Sort the Cards" game app](https://sortinggame.emmanuelrodri23.repl.co/). The goal is to sort the cards in order from least to greatest. Play once or twice, and get familiar with how the app works.

- What are some things you notice about how the game works?
- What's a repeatable strategy to get these sorted? Can you show and 

## Lesson Walkthrough 

**Unplugged / No Code**
- What we talked through in the Launch was an **algorithm**, a sorting algorithm. Here are the steps (pseudo code) to the **Insertion Sort** algorithm.  
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
- Try the steps above on your own using the app, and answer the following questions:
    - What are the 4 counters counting? (ie. observations, cycles, moves, and storage)
    - How might you try to improve this algorithm? 

**Incorporating Code**

- Now, let's look at the **Selection Sort** algorithm. 
    ```
    1. Look for the smallest number.
    2. Swap it with the card in the 1st slot.
    3. Repeat steps 1 and 2 until it's sorted, but replace '1st' with the next one (2nd, then 3rd, etc.)
    ```
    _NOTE: this is not going to be a low scoring algorithm, but it is a guaranteed simpler one to code out._

- Try this algorithm out with the app.
    - In what ways is this algorithm better than Insertion sort?
    - In what ways is it worse?

- Now, try coding these steps in a function.
    HINT: You can use the following piece of code to swap two variables' values:

    ```py
    num1 = 4
    num2 = 10
    (num1, num2) = (num2, num1)
    # num1 = 10
    # num2 = 4
    ```

## Extensions

- Try Selection sort without creating a new list!
    
- Check out the algorithm for [Insertion Sort](https://www.youtube.com/watch?v=JU767SDMDvA), and try to code it!

## Extra Help & Resources

- [Algorithm for tying shoes](https://madice99.wordpress.com/2016/09/07/algorithm-for-tying-your-shoes/)
- [Selection Sort](https://www.youtube.com/watch?v=g-PGLbMth_g)