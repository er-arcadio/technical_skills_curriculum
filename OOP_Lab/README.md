# The Bursar's Office

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Extensions](#extensions)
- [Hints & Resources](#hints--resources)

## Intro

The bursar's office has gone digital! You've been hired to put together their system. You'll need to create Classes for different objects throughout the university.

## The Lab

- We start with a class `Student` with only 2 attributes, and will slowly build on top of that. Use the `main.py` to code along:
    ```py
    class Student():
        def __init__(self, name):
            self.name = name
            self.current_courses = []
    ```

- Create an instance of the class Student with your name:
    ```py
    student = Student('Manny')

    print(student.name)             # Manny
    print(student.current_courses)  # []
    ```

- Look for 2 or 3 courses in the `sample_data.py` that interest you, and add their name to `current_courses`:
    ```py
    new_courses = ['Philosophy', 'Statistics']

    for course in new_courses:
        student.current_courses.append(course)
    ```

- Programmers that have access to this class wont be able to see the `sample_data.py`. Create a function `add_course()` that adds the course name if its in the courses dictionary in `sample_data.py`. Otherwise, it should print that the course is not available. Finish the following code:
    ```py
    class Student():
        def __init__(self, name):
            self.name = name
            self.current_courses = []

        def add_course(self, course):
            # Your code here!


    new_courses = ['Philosophy', 'Statistics', 'Japanese']

    for course in new_courses:
        student.add_course(course)

    # Should print "Japanese course not avaialble"
    ```

- Lastly, change the `current_courses` variable to **private**, and add a `get_current_courses()` function that returns the list of current courses. Turning the variable private will ensure that someone doesn't manually add a course that doesn't actually exist.

    ```py
    class Student():
        def __init__(self, name):
            self.name = name
            self.__current_courses = [] # 2 underscores before the variable makes it private

        def add_course(self, course):
            if course in courses:
                self.__current_courses.append(course)
            else:
                print(course, "course not available.")

        def get_current_courses(self):
            return self.__current_courses 


    print(student.get_current_courses()) # ['Philosophy', 'Statistics'] for me
    # print(student.__current_courses)  # this should now give an error!
    ```

## Extensions

**Mild**

1. Create a new instance of Student with another name, and print the name.

2. Include a `major` in the Student class. The default should be 'Undeclared'
    ```py
    # Tests
    student1 = Student('Jack')                            
    student2 = Student('Jill', major='Computer Science')

    print(student1.major) # 'Undeclared'
    print(student2.major) # 'Computer Science'
    ```
3. Include a private variable `__completed_courses` in the Student class. The initial value should always be an empty dictionary.

4. Create a function `complete_course()` that takes in a course name and a GPA, and does the following:
    - If the course is not in `__current_courses`, it prints that the course is not being taken.
    - Otherwise, the course is added to the dictionary with value as the GPA. For example:
        ```py
        student.complete_course('Anthropology', 3.7)  # 'Manny is not currently taking Anthropology'
        student.complete_course('Statistics', 3.8)    # __completed_courses = [{'Statistics': 3.8}]
        ```

    Be sure to create a `get_completed_courses()` to read the variable.

**Medium**

5. Create a function `get_gpa()` that takes the average gpa from the private `__completed_courses` dictionary.

6. Create a function `get_credits()` that adds the credits for each class in the private `__completed_courses` dictionary according to the number of credits in the `courses` variable.

7. Create a function `get_grade()` that returns the grade level of the student according to the following chart:
    ```
    'Freshman'  - if the credits are < 32
    'Sophomore' - if the credits are 32 <= c < 64
    'Junior'    - if the credits are 64 <= c < 96
    'Senior'    - if the credits are 96 <= c < 128
    'Graduate'  - if the credits are > 128
    ```

8. Create a function `get_transcript()` that prints the students name, major, grade (from #7), completed_courses (and their individual GPAs), Avg GPA (from #5), and total credits (from #6)

**Spicy**

9. When using the get functions for the private variables, you send the list itself instead of the copy of the list! This is bad, because someone can still then edit the list. Instead of returning this list itself, return a [deepcopy](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/) of the list.

10. Create a new class `Instructor` with the following data and the following actions.
    ```
    Data
    - name
    - __courses (private)

    Action
    - join_course()     - If course exists in `courses`, add this instructor's name to `instructors` list, and add the course to __courses variable here; Otherwise, say that course is not available. If name is already in list, say so as well.
    - drop_course()     - Remove's name from `instructors` list in `courses` and removes course from __courses here.
    - get_courses()     - Returns a copy of the list of courses this instructor is in.
    ```

11. Create a list of `Instructors` one for every instructor in the `instructors` list in `sample_data.py`. Be sure each Instructor class also joins the courses using their `join_course()` function. Then, print out all the Instructor classes and their courses.

## Hints & Resources

