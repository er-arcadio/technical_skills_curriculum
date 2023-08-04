from sample_data import courses, instructors


class Student():
    def __init__(self, name):
        self.name = name
        self.current_courses = []


manny = Student('Manny')
print(manny.name)     # Manny
print(manny.current_courses)  # []



# Create an instance of Student with your name, and print the name.


# Include major in the Student class. The default should be 'Undeclared'

# student1 = Student('Jack')                            
# student2 = Student('Jill', major='Computer Science')
# print(student1.major) # 'Undeclared'
# print(student2.major) # 'Computer Science'


# Look in the sample_data.py and add 2 courses from that dictionary to your instance of Student. 