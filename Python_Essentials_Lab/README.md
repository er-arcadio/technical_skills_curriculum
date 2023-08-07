# TITLE

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/les-mis-python-essentials)](https://repl.it/github/upperlinecode/les-mis-python-essentials)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Hints & Resources](#hints--resources)
- [Extensions](#extensions)

## Intro

_**Les Misérables** is a French historical novel by Victor Hugo, first published in 1862, that is considered one of the greatest novels of the 19th century. The novel is divided into 5 volumes, each volume divided into several books, and subdivided into chapters, for a total of 48 books and 365 chapters. Each chapter is relatively short, commonly no longer than a few pages._

In this 3 part lab, you will have 3 variables to work with. 
- `word_counts` - a list of integers that represent the number of words in each of the 48 books
- `glossary` - A list of 5 dictionaries representing the 5 volumes. Each dictionary contains the volume number, volume title, and a list of book titles that belong to the volume.
- `caption` - A large string that is a caption or paragraph taken out from the novel.

## The Labs

### Python Essentials Lab 1 - Lists

```py
my_list = [1, 2, 3]

for num in my_list:
    print(num)

# 1
# 2
# 3
```

**Mild**

1. Use `word_counts` to print a list of the first 8 books' word counts.
2. How many words are there in the whole novel?
3. How many books have at least 1200 words? 


**Medium**

4. How many words are in the book with the most words?
5. Write a function that returns the indexes of the books that have a multiple of 5 word count. (eg. 1225, 100, 1430)

**Spicy**

6. Which 2 Books add up to a total of 17059 words? Write a function to find the two numbers that add up to a specific target. Return the indexes of the two numbers in the list. You can assume there is only one solution.
7. Which 2 back-to-back books have the most most words combined? (For example, [2, 3] for the 2nd and 3rd index would be a valid answer, but [4, 9] would not.)

### Python Essentials Lab 2 - String Iteration

```py
my_string = 'Hello World'

for character in my_string:
    print(character)

# H
# e
# l
# ...
```

**Mild**

1. How many characters are in the `caption` string?
2. Use `.split(' ')` to find how many words are in the string.
3. Use `splice(a, b)` to print the sentence, _"She concealed her gray hair under a frizzed wig known as the baby wig."_

**Medium**

4. Using the `caption` string, write a function that returns a list of the words in the caption, but eliminate any duplicates. 
5. Which word is used most in the caption? Write a function to count the occurrences of each word in the string `caption` and return the counts in a dictionary. _Bonus: Which letter is most used? (Hint: you don't have to change your function for this)_

**Spicy**

6. Which word is the first word to repeat? Write a function to find the first repeated word in a list of words **without using a nested for loop**. _This is known as O(n)._
7. A "scrambled subset" is when you take random words from a string to make a new string. For example. if caption was "Away we go!", "Go away." would be a scrambled subset because 'go' and 'away' can be found in "Away we go". However, "Here we go" wouldn't because of 'here', and "Go away, go!" wouldn't because 'go' only exists once in "Away we go!"._
Write a function to test if these 3 use case sentences are a "scrambled subset" of the `caption` string?
    - "Picture a memory with long hair. A gentle, intelligent picture." 
    - "Take one picture of that wig, but cut the hair short to her neck."
    - "Her long hair was longer than she had hoped."
    <details>
    <summary>Answers to test case sentences:</summary>

    - "Picture a memory with..." -- **False**: "picture" only appears once in caption.
    - "Take one picture of..." -- **True**
    - "Her long hair was longer..." -- **False**: "longer" is not in the caption.
    </details>

    _Hint: Use `.replace()` to eliminate periods and commas, and use `.lower()` to turn both strings into all lower case words before splitting._
    
### Python Essentials Lab 3 - Dictionary and Nested Lists

```py
my_json = [
    {"name":"Jack", "relationship":"brother"},
    {"name":"Jill", "relationship":"sister"}
]
for sibling in my_json:
    print(sibling["name"])

# Jack
# Jill
```

**Mild**

1. Use `glossary` to print the list of books from volume 1
2. How many books are there in volume 5?
3. How many books are in each volume? Save these numbers in a list.


**Medium**
For #4-6, use `glossary` **and** `word_counts`.

4. Which volume is the shortest read? (ie. has the least amount of words)
5. Write a function that takes in a volume and a book number and returns the number of words in that book. (eg. `words_in(2, 4)` should return `6505`, the total number of words in Volume 2 Book 4)
6. Write a function that takes in a word count and prints the corresponding book name. (eg. `print_book(6505)` should print `"The Gorbeau Hovel"`)
string

**Spicy**

7. Create a matrix, a list of lists, of the book word counts by volume. Insert 0s so that the length of each list is the same. 
```py
wc_matrix = [ 
    [ "volume1book1", "volume1book2", ...],
    [ "volume2book1", ...],
    ...
 ]
```

8. Write a function that will rotate that matrix 90 degrees clockwise.
    For example, this matrix...
    ```py
    m = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    ```
    ...would rotate and turn into this matrix:
    ```py
    m90 = [
        [4, 1],
        [5, 2],
        [6, 3]
    ] 
    ```

## Hints & Resources

- Available [list methods](https://www.w3schools.com/python/python_ref_list.asp) in Python
- Available [string methods](https://www.w3schools.com/python/python_ref_string.asp) in Python.
- Creating [functions](https://www.w3schools.com/python/python_functions.asp) in Python
- Examples of [reading a list of dictionaries](https://pythonexamples.org/python-list-of-dictionaries/)