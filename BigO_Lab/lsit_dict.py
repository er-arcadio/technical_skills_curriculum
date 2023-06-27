key = "lime"        # For example


# 1 - find the count of...
sourP_dict = {
    'berry': 8, 
    'lemon': 13, 
    'lime': 8, 
    'orange': 9, 
    'raspberry': 12
}
count = sourP_dict[key]


# 2 - If order matters, 
sourP_list = ['raspberry', 'lime', 'berry', 'orange', 'lime', 'berry', 'lemon', 'berry', 'lemon', 'berry', 'lemon', 'lemon', 'orange', 'lime', 'lemon', 'lemon', 'lime', 'lemon', 'raspberry', 'lemon', 'raspberry', 'raspberry', 'orange', 'orange', 'orange', 'raspberry', 'raspberry', 'raspberry', 'orange', 'raspberry', 'lemon', 'lemon', 'lemon', 'raspberry', 'raspberry', 'lime', 'lemon', 'orange', 'lemon', 'orange', 'lime', 'orange', 'lime', 'raspberry', 'raspberry', 'berry', 'berry', 'berry', 'lime', 'berry']

count = 0
for sp in sourP_list:
    if sp == key:
        count += 1


# 3 - know all types, find average, 
sourP_types = ['berry', 'lemon', 'lime', 'orange', 'raspberry']
sourP_counts = [8, 13, 8, 9, 12]

count = -1
for idx, typ in enumerate(sourP_types):
    if typ == key:
        count = sourP_counts[idx]

    
# 4 - know if a type exists
sourP_exist = {'berry', 'lemon', 'lime', 'orange', 'raspberry'}

count = key in sourP_exist       # true or false value

