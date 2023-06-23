# For these extensions, write your own tests and create your own
# keys to ensure your functions work


# 1. Given a list of words in alphabetical order, write a function to find a given word.
words = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-ray', 'Yankee', 'Zulu']

def find_word(alpha_list, key):
    pass




# 2. Given k, the number of rotations, create a function that searches a rotated list for a number. HINT: 'k' is also the index of the lowest value.
rotated_list = [343, 362, 379, 380, 387, 388, 401, 410, 412, 418, 432, 456, 484, 488, 492, 493, 23, 30, 44, 58, 63, 70, 72, 73, 74, 91, 98, 109, 129, 139, 140, 143, 150, 160, 164, 179, 195, 221, 253, 258, 260, 262, 264, 275, 289, 290, 292, 326, 335, 341]
k = 16

def find_rotated(rot_list, k, key):
    pass




# 3. Create a function that uses binary search to first find the 'k' value in a rotated list. Then, use the function from #2 to search for a value in the list. HINT: the 'k' index value is the only number that has a larger number to the left.
def find_k_rot(rot_list):
    pass




# 4. Given the peak value 'k', create a function that searches a bitonic list for a number.
bitonic_list = [9, 67, 72, 83, 86, 95, 110, 114, 136, 156, 171, 176, 187, 193, 214, 224, 248, 261, 271, 278, 302, 337, 364, 392, 406, 480, 489, 495, 498, 491, 431, 417, 344, 307, 299, 293, 282, 255, 230, 229, 151, 140, 133, 80, 73, 57, 44, 32, 29, 2]
k = 28

def find_bitonic(bit_list, k, key):
    pass




# 5. Create a function that uses binary search to first find the 'k' value in a bitonic list. Then, use the function above to search for a value in the list.
def find_k_bit(bit_list):
    pass




# 6. Ternary search function
sorted_list = [23, 30, 44, 58, 63, 70, 72, 73, 74, 91, 98, 109, 129, 139, 140, 143, 150, 160, 164, 179, 195, 221, 253, 258, 260, 262, 264, 275, 289, 290, 292, 326, 335, 341, 343, 362, 379, 380, 387, 388, 401, 410, 412, 418, 432, 456, 484, 488, 492, 493]




# 7. Find the indexes of the 2 numbers that add to a given sum.
sorted_list = [4, 5, 6, 8, 11, 16, 24, 33, 42, 56, 77, 98, 131, 155, 185, 215, 261, 319, 377, 416, 479, 534, 549, 611, 720, 801, 865, 968, 1063, 1164]
sum_key = 742



# 7b. Try to reduce your loops to just 1. Then, incorporating recursion.