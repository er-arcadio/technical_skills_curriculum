import random

students = [
    {
        "name":"Tanya",
        "age": 26,
        "occupation": "Lawyer"
    },
    {
        "name":"Bradley",
        "age": 37,
        "occupation": "Astrologer"
    },
    {
        "name":"Zakir",
        "age": 20,
        "occupation": "Builder"
    },
    {
        "name":"Velma",
        "age": 41,
        "occupation": "Teacher"
    },
    {
        "name":"Reggie",
        "age": 25,
        "occupation": "Stockbroker"
    },
    {
        "name":"Abubakar",
        "age": 30,
        "occupation": "Marketing Director"
    },
    {
        "name":"Elijah",
        "age": 48,
        "occupation": "Nutritionist"
    },
    {
        "name":"Cole",
        "age": 31,
        "occupation": "Dental Nurse"
    },
    {
        "name":"Ellen",
        "age": 40,
        "occupation": "Entrepreneur"
    },
    {
        "name":"Sonia",
        "age": 36,
        "occupation": "Musician"
    }
]

train_cars = [{
    "id":random.randint(100000, 999999),
    "weight":random.randint(100000, 350000),
    "color": random.choice(["black", "silver", "grey", "bronze", "brown"])
} for i in range(20)]