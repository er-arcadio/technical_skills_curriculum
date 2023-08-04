from collections import defaultdict

# Data
courses = {
    'Biology': {'instructors': ['Yasin Lopez', 'Ollie Bowers'], 'credits': 3},
    'Chemistry': {'instructors': ['Yasin Lopez', 'Alexander Moses', 'Tomas Landry'], 'credits': 3},
    'Physics': {'instructors': ['Alexander Moses', 'Tomas Landry'], 'credits': 3},
    'Algebraic Geometry': {'instructors': ['Ollie Bowers', 'Ralph Hull', 'Alexandre Torres'], 'credits': 3},
    'Statistics': {'instructors': ['Ralph Hull', 'Cormac Barry'], 'credits': 3},
    'Calculus': {'instructors': ['Tomas Landry', 'Ralph Hull'], 'credits': 3},
    'Spanish': {'instructors': ['Darcy Valenzuela', 'Kingsley Barrera'], 'credits': 3},
    'French': {'instructors': ['Darcy Valenzuela', 'Thalia Clark'], 'credits': 3},
    'American Sign Language': {'instructors': ['Louise Noble', 'Thalia Clark'], 'credits': 3},
    'Western Civilization': {'instructors': ['Ernest Hooper', 'Umar Jackson'], 'credits': 3},
    'Humanities': {'instructors': ['Candice Maddox', 'Ernest Hooper'], 'credits': 3},
    'Anthropology': {'instructors': ['Candice Maddox', 'Umar Jackson'], 'credits': 3},
    'Philosophy': {'instructors': ['Nabil Rivas', 'Ophelia Robbins', 'Arron Mcdaniel'], 'credits': 3},
    'Psychology': {'instructors': ['Louise Noble', 'Claude Turner'], 'credits': 3},
    'Sociology': {'instructors': ['Claude Turner', 'Teresa Daniel'], 'credits': 3},
    'English Literature': {'instructors': ['Savannah Woodard', 'Juliet Duran'], 'credits': 3},
    'Creative Writing': {'instructors': ['Casper Le', 'Kristian Mcknight', 'Arron Mcdaniel'], 'credits': 3},
    'Music': {'instructors': ['Casper Le', 'Kristian Mcknight'], 'credits': 3},
    'Art': {'instructors': ['Juliet Duran', 'Kadie Gordon'], 'credits': 3},
    'Architecture': {'instructors': ['Alexandre Torres', 'Maggie Franklin'], 'credits': 3},
    'Micro Economics': {'instructors': ['Cormac Barry', 'Tallulah Chen'], 'credits': 3},
    'Macro Economics': {'instructors': ['Tallulah Chen', 'Muhammad Gentry'], 'credits': 3},
    'Personal Economics': {'instructors': ['Muhammad Gentry', 'Haleema Green', 'Safa Parker'], 'credits': 3},
    'Study Abroad': {'instructors': ['Haleema Green'], 'credits': 3},
    'Capstone': {'instructors': ['Teresa Daniel', 'Nabil Rivas'], 'credits': 4},
}


instructors = defaultdict(list)
for course in courses:
    for instructor in courses[course]['instructors']:
        instructors[instructor].append(course)