import TKH.functions as tkh

# import EasterEgg package here along with draw module

from Person import PersonClass


personM = PersonClass("Mo", "Hummus", ["Farukh", "Tim"])
personT = PersonClass("Tim", "Hummus", ["Farukh", "Mo"])

mutuals = tkh.mutual_friends(personM, personT)

print("Mo & Tim both know", mutuals)

# TODO: uncomment this line of code when your import is complete
# draw.mystery_func()
