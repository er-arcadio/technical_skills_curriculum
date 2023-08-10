from boss_files import home

# class Folder():
#     def __init__(self, name):
#         self.name = name
#         self.folders = []
#         self.files = []


## Mild

# 1. Print the name of the folder saved in 'home'

# 2. Print the name of folders and files saved in 'home'

# 3. Recursively print all the folders in the tree. For every level deep it is, add '-->' before it.
## For example
# Home
# --> Applications
# --> --> Utilities
# --> Desktop
# ... 


# 4. Write a function that takes a folder node and prints a list of file names in that folder.

def print_files(folder):
    pass

print_files(home) # []
print_files(home.folders[0]) # ['Chrome', 'Mail', 'Notes', 'Photos']


# 5. Write a function that takes a folder node and prints the list of folder names in that3 folder.
# Test it out with the 'Home' folder, then with another nested folder. Note: remember to pass the Folder() Node not a String.

def print_folders(folder):
    pass

print_folders(home) # ['Applications', 'Desktop', 'Documents', 'Downloads']
print_folders(home.folders[0]) # []


## Medium

# 6. Write a function that takes a folder node and uses recursion to print all the files and folders below it.
# Use an indent, '\t', or --> symbol to show nested folders and files.

def print_all(folder):
    pass

print_all(home)

# 7. Write a function that uses recursion to print the tree as a dictionary

def to_dict(tree):
    pass

print(to_dict(home))

# 8. Write a function that uses recursion to find a file by name.
# It should return True if it exists or False if not.
test_inputs = ['chocolate.png', 'vanilla.png', 'write_offs.pdf', 'procedure.txt', 'recall.txt']
test_answers = [True, False, True, True, False]

def find(file_name):
    pass

find('chocolate.png') # True

# 9. Modify the above function to return the file path if true or "File does not exist" if false.
# For example: find('procedure.txt') => 'Home/Desktop/Projects/Weddings/procedure.txt'


# 10. Write a function that finds a folder by name and returns the node if found. Otherwise, it should return None.

def goTo(folder):
    pass

weddings = goTo('Weddings')
print(weddings.name) # 'Weddings'


## Spicy

# 11. Find the 'color_palette_templates' folder and move it to the Passion_Projects folder
# Check that the color_palette_templates's parent folder no longer holds it and that Passion_Projects does
## Hint: you'll need to use functions above that you have already created to do this.



# 12. Write a function that finds the lowest common ancestor folder that holds the 2 inputted files
# For example: common_ancestor('ny_invoice.pdf', 'la_invoice.pdf) => 'Finances'
# For example: common_ancestor('roster_screenshot.jpg', 'New_Years2023') => 'Desktop'