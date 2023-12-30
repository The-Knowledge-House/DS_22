"""
Some functions inside a package
"""


def mutual_friends(personA, personB):
    mutuals = set(personA.aff).intersection(set(personB.aff))
    return mutuals


def make_fav_food_hummus(person):
    person.food = "hummus"
