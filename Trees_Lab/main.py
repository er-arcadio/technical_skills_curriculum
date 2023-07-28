from boss_files import home

# class Folder():
#     def __init__(self, name):
#         self.name = name
#         self.folders = []
#         self.files = []


## Mild

# 1. Write a function that prints the array of file names in the current folder.

def print_files(folder):
    pass

print_files(home)


# 2. Write a function that prints the array of folder names in the current folder.
# Test it out with the 'Home' folder, then with another nested folder. Note: remember to pass the Folder() Node not a String.

def print_folders(folder):
    pass

print_folders(home)


# 3. Write a function that uses recursion to print all the files and folders.
# Use an indent or --> symbol to show nested folders and files.

def print_all(folder):
    pass

print_all(home)


## Medium

# 4. Write a function that uses recursion to print the tree as a dictionary

def to_dict(tree):
    pass

print(to_dict(home))


# 5. Write a function that uses recursion to find a file by name.
# It should return True if it exists or False if not.
test_inputs = ['chocolate.png', 'vanilla.png', 'write_offs.pdf', 'procedure.txt', 'recall.txt']
test_answers = [True, False, True, True, False]

def find(file_name):
    pass


# 6. Modify the above function to return the file path.
# For example: find('procedure.txt') => 'Home/Desktop/Projects/Weddings/procedure.txt'


# 7. Write a function that finds a folder by name and returns the node if found. Otherwise, it should return None.

def goTo(folder):
    pass

weddings = goTo('Weddings')


## Spicy

# 8. Find the 'color_palette_templates' folder and move it to the Passion_Projects folder
# Check that the color_palette_templates's parent folder no longer holds it and that Passion_Projects does



# 9. Write a function that finds the lowest common ancestor folder that holds the 2 inputted files
# For example: common_ancestor('ny_invoice.pdf', 'la_invoice.pdf) => 'Finances'
# For example: common_ancestor('roster_screenshot.jpg', 'New_Years2023') => 'Desktop'