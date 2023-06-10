# Python Essentials Review

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Teacher Notes

### Goal & Sequence

The goal here is that students get a flash intro to essential Python syntax **up to but not** including OOP. 

### Teaching Tips

This lesson is designed for students with a strong programming background who will likely know or be familiar with Python already. Plan on moving quickly through this lesson spending little time on the lesson walkthrough and most of the time on the practice activities in `py_essentials.py`.

### Learning Objectives

Students will be able to:

- Use variables, strings, concatenation, and formatted output.
- Create and call return functions with parameters using operations, and conditional flow.
- Create, read, update and delete fundamental data structures such as lists and dictionaries
- Iterate through a list of literals and a list of dictionaries.
- [Stretch] Create filters and mappings of lists using list comprehension.

## Launch

Have students start by opening the lab and have them self-sort into three groups:
1. Ready to work with a partner as a navigator (I know python) 
2. Ready to work with a partner as a driver (I don't know python)
3. Want to go over the concepts first with a teacher.

Use the lesson walkthrough and challenges as a teacher guided experience, and use the lab as something more hands off. 

Reassure students that whatever they are bringing to the table is enough to do well here and get the ball rolling. After just a couple of examples, students will be coding in Python through exploration, trial and error, and some reading of documentation.

## Lesson Walkthrough

> Teacher Note: Present the following code snippets to the students in a way that they can easily refer back to them later for the independent practice. Key vocabulary that may trip up students have been bolded for your awareness. 

1. First, we look at some fundamental Python **data types** -- **integers** and **strings** -- and the **formatted string**.

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

2. Ask the students to predict the final output for both variables: `concat_sentence` and `formatted_sentence`. _Answer: Both variables will produce the same results "Today is Saturday and the temperature is 78". The values "Saturday" and 78 are saved in **variables**. Then, they are **concatenated** to other strings in order to produce a longer string which is then saved in a separate variable. In the first example, `temperature_f` is **cast** from an integer into a string, and in the second example, formatted string is being used to shortcut the concatenation._

3. In this next example, we see **conditional statements** inside functions.

    ```py
    # function definition
    def absolute_value(n):
        if n < 0:
            return n * -1
        else:
            return n
        
    # outputs using the function
    print(absolute_value(9))
    print(absolute_value(-3))
    ```

4. Ask students here to predict the output and give them a moment to discuss their thinking with their partner. _Answer: The first print will output 9 and the second will output 3. Both numbers will be positive as this function **returns** the absolute value of the input. (Note: this example is mostly for students to see the Python syntax. However, if you find that students don't really know why the results are what they are, spend a bit of time tracing the code. i.e. "If 'n', the inputted number, is less than 0 (negative) the function returns the positive version..." etc.)_ 

> Teacher Note: This may be a good time to pause and have students work on the first half of the challenges practicing these concepts. Consider the level of your specific group of students.


5. These next couple of examples get tricky. A **list** (similar to an array in other languages) is a way to hold multiple related values in one variable. Ask students to predict the two outputs. Most will either say 'John' or 'Jacob' for the first and 'John', 'Jacob', 'J', or 'o' for the second output. 
    ```py
    # list of names
    names = ['John', 'Jacob', 'Jingleheimer', 'Schmidt']

    # 1st output
    print(names[1])


    half_name = "John Jacob"

    print(half_name[1])
    ```

6. The first output prints the name _'Jacob'_, and the second prints the letter _'o'_. Notice the **zero indexing**, we count values starting at 0 instead of 1. A string can be indexed as well. We can think of a string as a list of **characters**: 'J', 'o', 'h', 'n', ' ', etc.

7. The following code uses a **for loop** to **iterate** through a string and list. It will apply the same action for each **element** in the list or character in the string. Ask students to predict the outputs and give them a moment to discuss their thinking with their partner. 
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
            j_names.append(word)     # append means to add to the end
    
    print(j_names)
    ```

8. Part 1 will print a '-' symbol after every letter 'J-', 'o-', 'h-', etc. Part 2 prints a new list only of the names that start with the letter _'J'_. Also, notice that there are 2 **methods** being used here: `.startswith()` which returns True if the strings starts with given letter, and `.append()` which adds the element to the end of the list. For more information and examples on how these methods and other string and list methods work, check out the resources below.

9. We can use a **dictionary** to label the elements in our list. We would then access the values using the label instead of the index number. For a dictionary, the label is called the **"key"** (for example 'name') and the elements are called the **"values"** (for example 'Mr. John Keating'). Ask students if they can predict the output here.
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

10. The sentence should read _"My English teacher is 32 years old."_ Notice the curly "mustache" brackets for the dictionary and the square brackets for the list of students.  

> Teacher note: At this point it makes sense to send students to complete the rest of the pair programming challenges in the `py_essentials.py`. If students make it to #7, they are ready for the corresponding Python Essentials Lab.

## Close

Consider adding one or both of these activities at the close of your lesson:

- **Discussion**: "Why might one decide to use a dictionary over a list? .. a list instead of a dictionary?" -- Lists are better when you have a lot of similar data that can be grouped together. Typically you will be iterating over a list. Dictionary's are best for specific access. The key here is the "key/value" pairing. Each value has a specific representation or label. 
- **Reflection**: With their partner, have students brainstorm a list of everything reviewed today. Then, on an easily collectable paper or index card, have them independently write down 2 topics they're really comfortable with and 2 topics they're still anxious about.


## Extra Help & Resources

- Python Lightning Intro [Slide Deck](https://drive.google.com/file/d/1gsuGKeb-Q8wp7tZafoEzIgQybpQj_UjO/view)
- [String Methods](https://www.w3schools.com/python/python_ref_string.asp)
- [List](https://www.w3schools.com/python/python_lists_loop.asp) and [String](https://www.w3schools.com/python/gloss_python_for_string.asp) Iteration Examples
- [List Methods](https://www.w3schools.com/python/python_ref_list.asp)
- [Dictionary Methods](https://www.w3schools.com/python/python_ref_dictionary.asp)
- [List comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) [Spicy]
