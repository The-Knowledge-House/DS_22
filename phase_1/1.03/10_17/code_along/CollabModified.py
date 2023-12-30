import Person
# import Person as P


# this will error...
# how do we fix this?
class Collaborator(PersonClass):
    def print_email(self):
        print(f"{self.name}@gmail.com")


if __name__ == "__main__":
    collabA = Collaborator("Jazmin", "Tuna Sandwiches", [])
    collabA.print_email()
    collabA.fav_food()
