# Mild

# 1. Write a function for the factorial of a number
# ex. 3! = 3*2*1 = 6 -- 5! = 5*4*3*2*1 = 120

def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product

def recursive_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
    
# 2. Write a function that computes the sum of the digits of a number.
# ex. 2148 => (2+1+4+8) = 15

def sum_digits(n):
    total = 0
    remainder = n
    while remainder > 0:
        total += remainder % 10
        remainder = remainder // 10
    return total

def recursive_sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + recursive_sum_digits(n//10)
    
# 3. Write a function that reverses the order of a list.
# ex. [1, 2, 3, 4, 5] => [5, 4, 3, 2, 1]

def reverse(l):
    reversed_l = []
    idx = len(l) - 1
    while idx >= 0:
        reversed_l.append(l[idx])
    return reversed_l

def recursive_reverse(l):
    if len(l) <= 1:
        return l
    else:
        return [l[-1]] + recursive_reverse(l[:-1])

# Medium

# 4. Every number can be represented as a "single digit". Write a function that converts any number to it's "single digit" form
# ex. 7 => 7 -- 57 (5+7) => 12 (1+2) => 3 -- 159 => 15 => 6

def single_digit(n):
    digits = [int(x) for x in str(n)]
    while len(digits) > 1:
        digits = [int(x) for x in str(sum(digits))]
    return digits[0]

def recursive_single(n):
    digits = [int(x) for x in str(n)]
    if len(digits) > 1:
        return recursive_single(sum(digits))
    else:
        return n
    

# 5. Would you rather have a million dollars or a penny that doubles in size for a month (30 days)?
# Write a function that finds how much a penny doubled for 30 days is.

def penny_doubled(days=30):
    days_passed = 1
    total = 0.01
    while days_passed < days:
        total *= 2
        days_passed += 1
    return total


def recursive_penny_doubled(days_left=30, payment=0.01):
    if days_left == 1:
        return payment
    else:
        return recursive_penny_doubled(days_left-1, payment*2)

# 6. Is the number prime? Can it only be divided by itself and 1?
# ex. 7 is prime (factors: 1, 7) but 10 is not (factors: 1, 2, 5, 10)
# Hint: Check 2 first (by default) and work your way up until you hit the original number.

def is_prime(n):
    next_number = 2
    while next_number < n:
        if n % next_number == 0:
            return False
        next_number += 1
    return True

def recursive_prime(n, next_number=2):
    if n == next_number:
        return True
    elif n % next_number == 0:
        return False
    else:
        return recursive_prime(n, next_number + 1)

# Spicy
# NOTE: These are much easier as recursion than as a loop. Feel free to skip non-recursive version.

# 7. A few chess players have made it to the finals fighting for 1st - 4th place.
# Write a function that will return all the ways the players can get placed.
# ex.   ['Sherman', 'Rosemary', 'Lucero', 'Yareli']
#       ['Sherman', 'Rosemary', 'Yareli', 'Lucero']
#       ['Sherman', 'Lucero', 'Rosemary', 'Yareli']

finalists = ['Sherman', 'Rosemary', 'Lucero', 'Yareli']


# 8. Here's a list of all the chess students before the finals.
# Write a function that finds all the combinations of last 4 finalists that could have ocurred. 
# ex.   ['Raven', 'Dorian', 'Santiago', 'Marisol']
#       ['Raven', 'Dorian', 'Santiago', 'Stephanie']
# NOTE: order doesn't matter here!
# ex.   ['Raven', 'Dorian', 'Santiago', 'Marisol'] making it to the finals is the same as
#       ['Marisol', 'Raven', 'Santiago', 'Dorian']. It's the same 4 people.

all_students = ['Raven', 'Dorian', 'Santiago', 'Marisol', 'Stephanie', 'Roland', 'Sherman', 'Rosemary', 'Lucero', 'Yareli']


# 9. Raven has caught wind of a pop quiz coming up and wants to let everyone in the class know about it.
#   She only has the number of her 2 best friends: Stephanie and Rosemary. They have some other people's phone numbers, and so on.
#   If each student can only text one other person, what would be the chain of communication that get's everyone the information?

# Here's a dictionary of the lines of communication
communications = {
    'Raven': ['Stephanie', 'Rosemary'], 
    'Dorian': ['Santiago', 'Yareli'], 
    'Santiago': ['Dorian', 'Roland'], 
    'Marisol': ['Roland', 'Sherman', 'Yareli'], 
    'Stephanie': ['Raven', 'Rosemary'], 
    'Roland': ['Santiago','Marisol', 'Lucero'], 
    'Sherman': ['Marisol'], 
    'Rosemary': ['Raven', 'Stephanie', 'Lucero'], 
    'Lucero': ['Roland', 'Rosemary'], 
    'Yareli': ['Dorian', 'Marisol']
}