# TITLE

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Teacher Notes

### Goal & Sequence

The goal of this lesson is to have students explore algorithms and sorting techniques through a ["Sort the Cards" game app](https://sortinggame.emmanuelrodri23.repl.co/). There will be **no** coding in this session. It mostly consists of trial and error, formulating and documenting ideas and strategies, and demoing and articulating those ideas with fellow classmates. In addition, this lesson works best with little to no vocabulary or use of complex algorithms. See "Teaching Tips"

Once students begin to feel comfortable with creating and using an algorithm, a series of repeatable steps to get to a conclusion, they should attempt the Sort Lab which has them put their ideas into code and introduces more vocabulary.

### Teaching Tips

Students learn best when they internalize through exploration and discussion. Use this lesson as a map for how to guide students along this journey. This lesson works best with no coding and a minimal use of vocabulary. We prefer to use vocabulary to label a student's idea or to group together similarly brought up ideas. 

The rationale behind no code is that (A) the coding is much easier once the algorithm is internalized, and proof of this internalization can usually be seen when students start to articulate their thoughts out loud. (B) The most advanced sorting interview questions have students not memorizing algorithms, but being able to understand and bend them to optimize for a specific problem. This exploration is meant to facilitate that type of thinking. 

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

- Generate sorting algorithms from scratch. 
- Articulate how both their unorthodox and orthodox algorithms operate. 
- Compare different algorithms explaining the benefits and drawbacks.
- Create a plan to optimize and adjust algorithms to meet certain constraints.

## Launch

Start up the "Sort Cards" game and demo how it works -- the goal is to sort the cards in order from least to greatest. Have the students just play for now, and allow them to get familiar with how the app works.

Once most of them have finished, ask if any of them had a repeatable strategy that they can explain to the class. Disregard vocabulary for now and commend each volunteer.

Have them play again, this time focussing on a specific repeatable strategy. Be sure they ignore the numbers (observations, cycles, final grade, etc.) for now.

Finish off by giving several students the time and space to clearly articulate the strategy they came up with. Consider demoing a preview on your screen or allowing them to share theirs with the class. 

## Lesson Walkthrough

> Note: the following lesson uses Insertion Sort, but Bubble or Selection Sort could work just as well. 

- Use a student's algorithm, or the insertion sort algorithm to demo how students should now articulate their strategy on a document, paper, or other means. For example:
    ```markdown
    ** Manny's Sort ** (really just Insertion Sort)

    1. Look at the first 2 numbers. If they're out of order, swap them.
    2. For every other number if it's the greatest so far, skip it. Otherwise, put it in storage.
    3. Shift numbers on the left over until you reach a number that is smaller than the storage number.
    4. Finally, put the storage number back in the new empty space.
    ```
    _Note: the goal is not to have it align to code, but to think algorithmically or in clear repeatable steps._

- Demo how this would work and ask students to now pay attention to the 4 measurements: observations, cycles, etc. The new goal is to have these numbers be as low as possible, because these numbers represent a cost. 

- Have students try again to sort the cards creating a strategy and articulating it to their partner. This time they should focus on 3 things.
    1. What are the measurements counting?
    2. What's a good strategy if the goal is to keep the left 2 numbers, observations and cycles, as low as possible?
    3. Whats a good strategy if the goal is to keep "moves" as low as possible?

    _Note: at this point, students should **not** be focussed on sorting completely every time, but instead coming up with a sound strategy_

- Bring students back and facilitate a discussion on the 3 focus points above:
    1. Observations count the number of times you look at a card, cycles, is number of times you need to double check a card 1 check of all cards is 1 cycle, 2 checks is 2 cycles, etc. Moves is number of times you move a card.
    2. Keeping a low cycle/observation count will require some memorization or relative organizing before sorting (as in the merge sort algorithm)
    3. Keeping a low move count will require lots of observations. You can find the lowest number and put it in the right place, then the next lowest, etc. (Selection sort)

- Last, if the students had come up with an algorithm that already exists. Expose the vocabulary term for it. Here are ones that likely will come up from most to least likely: insertion, selection, bubble, radix, merge, or quick sort.

> Note: At this point, if students feel comfortable articulating an algorithm, they should be ready to go right into the lab. Otherwise, use the extensions as more opportunities to get at bats at thinking algorithmically before doing so.

## Extensions

- You may have noticed that "observations" and "cycles" are the most costly contributors to the "Final Grade". Come up with a strategy that minimizes these two measurements, write it down, and see if your partner can use it to come up with a low score.
- Check the box "More Storage" at the top of the page. What strategy can you employ with this new resource to keep your measurements low?
- [Spicy] Try to get a score below 100!

## Extra Help & Resources

- [Algorithm for tying shoes](https://madice99.wordpress.com/2016/09/07/algorithm-for-tying-your-shoes/)
- [Algorithm for cleaning a pool](https://www.wikihow.com/Clean-Your-Own-Pool). Feel free to skim through this to get an idea of how verbose it can get.
- [Bubble Sort](https://www.studytonight.com/data-structures/bubble-sort). Ignore the code for now. Notice the steps they outline.