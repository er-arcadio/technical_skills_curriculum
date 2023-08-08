# Stacks and Queues

## Teacher Notes

### Goal & Sequence

Stacks and Queues may be a foreign topic for students. This lesson mostly unplugged. Toward the end there is some code with lists to illustrate a practical use. For something more hands on and coding intensive, refer to the lab.

- [Launch](#launch)
- [Lesson Walkthrough](#lesson-walkthrough)
- [Extensions](#extensions)
- [Close](#close)

### Representation

The lesson also uses the example of the Touch Tunnel from the Liberty Science Center exhibit to demonstrate queues. Consider going to the [website](https://lsc.org/explore/exhibitions/touch-tunnel) or Google images to show pictures so students are familiar with the experience. Otherwise if that is not something that resinates with your or your students, feel free to change this analogy to a line at the post office or something else.

### Learning Objectives

Students will be able to:

- Articulate the difference between stacks and queues
- Use a series of timestamps to define the state of a stack or queue
- Use terms like **push** and **pop** see them in code.
- Read stacks and queues code and differentiate the data structure.

## Launch

Some card games like [the one in this video (Egyptian Ratscrew)](https://youtu.be/7h99zClpN0M?t=13) have player draw from the top of their deck, but add cards to the bottom. In this case, your deck of cards is a **Queue**. Cards move up the queue until they are drawn.
- What are some other examples of a **queue** in real life?

Other games like _Gin Rummy_ have a discard pile. On your turn when you draw, you can pull from the top of the discard pile. Then, you discard by adding cards to the top of the discard pile. In this case, the discard pile is a **Stack**. Only the top card of the stack can be drawn.
- What are some other examples of a **stack** in real life?

## Lesson Walkthrough

**The Queue**

At the Liberty Science Center in NJ, there's an activity called the Touch Tunnel. It's an 80 foot long tunnel that is so pitch black dark you have to "touch" the walls and crawl your way through. 

- Before you enter, you sign your name in the kiosk, and when you leave, the sensors log an exit. This way, we always know if someone is still left inside. Below is the log from a class field trip.

    ```
    Log of activity:

    Enter 900 - Jeff
    Enter 902 - Manny
    Exit 905
    Enter 910 - Ileini
    Exit 911
    Exit 916 
    Enter 918 - Betty
    Enter 919 - Danny
    Exit 923


    NOTE: 900 = 9:00am ; 1400 = 2:00pm
    ```
    _Sketch a **queue** to keep track of the activity._
    - How long did it take Jeff to go through the Touch Tunnel experience?
    - How long did it take Manny to go through the Touch Tunnel experience?
    - At 9:23 is there anyone still in the tunnel?
    - Who took the longest to get through? (Ignore anyone still in the tunnel if any)

**The Stack**

The example above follows the rule _First In, First Out_ (FIFO). The first person in the tunnel will be the first to leave. But watch how the same time log can be used for the rule _Last In, First Out_ (LIFO).
- Below is a time log of when tests were submitted and graded. When they're done, students place there test in a pile, in a shallow basket on the teacher's desk, and when the teacher is ready, they grab the top most test to grade.
    ```
    Log of activity:

    Submitted 900 - Jeff
    Submitted 902 - Manny
    Grade_Test 905
    Submitted 910 - Ileini
    Grade_Test 911
    Grade_Test 916 
    Submitted 918 - Betty
    Submitted 919 - Danny
    Grade_Test 923


    NOTE: 900 = 9:00am ; 1400 = 2:00pm
    ```
    _Sketch a **stack** to keep track of the activity._
    - In what order did the teacher grade the tests? (Whose was graded first, second, etc.)
    - How long did it take for Jeff’s test to be pulled for grading?
    - At 9:23, whose test is still in the basket?
    
**The Code**

> Teacher Note: This can alternatively be done as a pair programming activity if you prefer. 

- How would you summarize the difference between a stack and a queue based on the examples above?

- Both data structures have 2 main functions: **Push** and **Pop**. Push adds the number to the data structure, and Pop removes the number.
    ```py
    numbers = [1, 2, 3]

    def push(arr, num):
        arr.append(num)

    def pop1(arr):
        return arr.pop(0)

    def pop2(arr):
        return arr.pop(-1)


    print(pop1(numbers))
    push(numbers, 4)
    print(pop2(numbers))    # Note: always stick to either a queue or stack pop, don't mix your pops
    ```
    - Which `pop()` function is the `queue_pop` and the `stack_pop`? Explain.
    - What do you predict is the output of the above code?

## Extra Help & Resources