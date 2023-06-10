# Complete the following challenges
"""Part 1"""

#1. Complete the function by making it return the square of the provided number.
def find_the_square(n):
  return n**2

print(find_the_square(5)) # should be 25

#2. Complete the function by making it return "Did you know NAME is AGE years old?"
def get_bio(name, age):
  return f"Did you know {name} is {age} years old?"

print(get_bio('John Jacob Jingleheimer Schmidt', 33))

#3. Complete the function by making it return "Welcome Queen B" if "Beyonce" is the name. Otherwise, it should return "VIP access denied"
def vip_entrance(name):
  if name == "Beyonce":
    return "Welcome Queen B"
  else:
    return "VIP access denied"

print(vip_entrance('Beyonce'))

#4. Go back to all 3 functions and add an extra test case, a function call to see that different inputs work.
## Solutions may vary!


"""Part 2"""
#5. Given a list of strings, write a function to count the number of strings that start with a specific character.
# NOTE: Your return should be an integer (a count) not a list or string.
def strings_with_character(strings, character):
  new_list = []
  for string in strings:
    if string.startswith(character):
      new_list.append(string)
  return len(new_list)

print(strings_with_character(['Marco', 'Alberto', 'Manny', 'Melissa', 'Stephanie'], 'M'))  # should return 3


#6. Given a word and a letter, write a function that returns True if the word contains the letter, otherwise False.
def word_has_letter(word, letter):
  for let in word:
    if let == letter:
      return True
  return False

print(word_has_letter('happy', 'y')) # returns True


#7. Given a list of words, write a function to return a new list containing only the words that have more than five characters.
# HINT: look up the len() function
def long_words(words):
  new_list = []
  for word in words:
    if len(word) > 5:
      new_list.append(word)
  return new_list

print(long_words(['Marco', 'Alberto', 'Manny', 'Melissa', 'Stephanie']))


# Spicy Challenges

#8. Complete the function by making it return the sum of the even numbers of the provided list
# HINT: look up the % operator
def sum_of_evens(seq):
  # return sum([i for i in seq if i%2==0])
  total_sum = 0
  for num in seq:
    if num%2 == 0:
      total_sum += num
  return total_sum


print(sum_of_evens([5, 14, 6, -2, 0, 45, 66]))


#9. In the code block below complete each of the functions used by Twitter
def truncate_tweet(tweet):
  """
  This function should take a tweet, and check to see 
  if it is longer than 140 characters. If it is, only 
  return the first 140 characters of the tweet. Otherwise
  return the whole tweet
  """
  if len(tweet) > 140:
    return tweet[:140]
  else:
    return tweet


print(truncate_tweet('What did we do to deserve dogs?'))
print(truncate_tweet('@NYCTSubway The New York City #subway is literally the best and worst version of #transportation that has ever existed in the history of the #world. If I had had an apple for every time the train was late and the subway tunnel was hot, then I would be able to cure world hunger. #facts #periodt Get at me @WldHungerRelief!'))

#10. Look into "list comprehension". If you haven't already, try using this Python specific technique to turn your functions into 1 liners.