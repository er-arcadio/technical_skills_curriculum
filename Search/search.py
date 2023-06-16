
# Linear Search
def linearSearch():
    print("Think of a number between 1 and 100, and I'm going to try to guess it. Please respond with either 'yes', 'higher', or 'lower'.")

    guess = 0
    response = ''

    while response.lower() != 'yes':
        guess += 1
        response = input(f"Is it {guess}? ")

    print(f"Hurray! Your number is {guess}!")

linearSearch()


#Binary Search
def binarySearch():
    pass