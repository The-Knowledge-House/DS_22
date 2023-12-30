from Person import PersonClass
# from Person import PersonClass, giveTime
# from Person import *


class Collaborator(PersonClass):
    def print_email(self):
        print(f"{self.name}@gmail.com")


if __name__ == "__main__":
    collabA = Collaborator("Jazmin", "Tuna Sandwiches", [])
    collabA.print_email()
    collabA.fav_food()
