import Person


class Instructor(PersonClass):
    def task(self):
        makeSlides()


if __name__ == "__main__":
    personA = Instructor("Farukh", "Hummus", ["Mo", "Tim"])
    personA.fav_food()
    personA.task()
