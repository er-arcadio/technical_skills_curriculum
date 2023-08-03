from ancestry_tree import luis, naya

# class Hispanic():
#     def __init__(self, percent):
#         self.percent = percent
#         self.mom = None
#         self.dad = None

print(luis.mom.percent)
print(luis.dad.mom.percent)



# 1. What percent hispanic are Luis's 2 great grandmothers on his father's side?

# 2. Write a function that returns all the percents in "level order" as a list (ie. [31, 60, 44, 82, 94, etc.])

# 3. Write a function that takes the average percent of all the women (left nodes)

# 4. Write a function that returns the most genetically hispanic person at each generation (level).

# 5. Write a function that returns the average drop for each leaf parent.
# For example, from 85 > 82 > 60 > 31 the percentage dropped 3, then 12, then 29 for an average drop of 14.7 (3+12+29 / 3 = 14.7).
