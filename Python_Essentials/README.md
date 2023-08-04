# Python Essentials Review

## CONTEXT & PURPOSE

The goal here is that students get a flash intro to essential Python syntax **up to but not** including OOP. This lesson is designed for students with a strong programming background who will likely know or be familiar with Python already. Plan on moving quickly through the lesson spending little time on the lesson walkthrough and most of the time on the practice activities in the Replit.

#### Sequence

1. [Getting Started](#getting-started)
3. [Lesson Walkthrough](#lesson-walkthrough)
4. [Content Header 2, etc](#etc)
5. [Close](#close)

## <a href="getting-started"></a>GETTING STARTED

Include both technical setup and launch (in whichever order makes the most sense)

### Setup

Have the students fork a copy of the lab before launching into the lesson.

### Launch

Have students self-sort into three groups according to how they view the lab:
1. **(I know python)** Ready to work with a partner as a navigator 
2. **(I mostly know python)** Ready to work with a partner as a driver 
3. **(I'm not too confident with python)** Ready to go over the concepts first with a teacher.

[These slides](./Python%20Lightning%20Intro.pdf) are a good resource and/or alternative to the walkthrough. [This link](https://drive.google.com/file/d/1gsuGKeb-Q8wp7tZafoEzIgQybpQj_UjO/view) will take you to an online version


## <a href="lesson-walkthrough"></a>Lesson Walkthrough

### Data Types and Conditional Flow

1. Here are some fundamental Python _data types_: **integers** and **strings**.

    ```py
    # declaring variables
    day_of_week = "Saturday"
    temperature_f = 78

    # concatenation and formatted strings
    concat_sentence = "Today is " + day_of_week + " and the temperature is " + str(temperature_f)
    formatted_sentence = f"Today is {day_of_week} and the temperature is {temperature_f}"

    # output
    print(concat_sentence)
    print(formatted_sentence)
    ```
    > ###### Helpful questions
    > - Why isn't 78 in double quotes like Saturday?
    > - Predict the output for both variables.
    

2. Here are some **conditional statements** inside functions.

    ```py
    # function definition
    def my_function(n):
        if n < 0:
            return n * -1
        else:
            return n
        
    # outputs using the function
    print(my_function(9))
    print(my_function(-3))
    ```
    > ###### Helpful questions
    > - Can you predict either of the two outputs?
    > - What's a better name for this function?
    

### Lists, Loops, and Dictionaries

3. A **list** (similar to an array in other languages) is a way to hold multiple related values in one variable.
    ```py
    # 1. list of names
    names = ['John', 'Jacob', 'Jingleheimer', 'Schmidt']

    print(names[1])


    # 2. string of characters
    half_name = "John Jacob"

    print(half_name[1])
    ```
    > ###### Helpful questions
    > - Predict the two outputs.
    > - [Spicy] What are some ways we can make the two outputs print the same thing?
    


4. The following code uses a **for loop** to **iterate** through a string and list. It will apply the same action for each **element** in the list or character in the string:
    ```py
    # Part 1
    half_name = 'John Jacob'

    for let in half_name:
        print(let + '-')


    # Part 2
    names = ['John', 'Jacob', 'Jingleheimer', 'Schmidt']

    j_names = []
    for name in names:
        if word.startswith('J'):
            j_names.append(word)     # append means to add to the end of list
    
    print(j_names)
    ```
    > ###### Helpful questions
    > - What data type will `print(let + '-')` print?
    > - What data type will `print(j_names)` print?
    > - Write down your prediction to the two outputs, and be ready to share your reasoning.

5. We can use a **dictionary** to label the elements in our list. The label is called the **"key"** (for example 'name') and the elements are called the **"values"** (for example 'Mr. John Keating'):
    ```py
    my_teacher = {
        'name': 'Mr. John Keating',
        'subject':'English',
        'age':32,
        'alumni':True,
        'students': ['Neil', 'Charlie', 'Knox']
    }

    print(f"My {my_teacher['subject']} teacher is {my_teacher['age']} years old.")
    ```
    > ###### Helpful questions
    > - How many students does Mr. Keating have?
    > - What do you think "English represents in this dictionary?
    > - Can you predict what the output will be? 


## <a href="close"></a>CLOSE

**Discussion**: Why might one decide to use a dictionary over a list? .. a list instead of a dictionary?

**Reflection**: With a partner, brainstorm a list of all the topics reviewed today. Then, on an easily collectable paper or index card, write down 2 topics you're really comfortable with and 2 topics you're still anxious about.


_The best way to see if you've mastered these skills is to try the lab(s) associated with this lesson. As a reminder, the expectation with labs is slightly different from what most students and teachers are used to during the school year. If you can complete the first 50-75% of the activities in a lab, you're ready to move on to the next concept._
