class Cat:
    pass


class Person:

    def __init__(self, complaint="no water, too much PHP"):
        self.__complaint = complaint  # encapsulation#

    def complain(self):
        print(self.__complaint)


class EIT(Person):
    pass


class Fellow(Person):
    pass

people = list()
people.append(Fellow())
for _ in range(27):
    people.append(EIT())
people.append(Cat())
for person in people:
    # check to make sure your person is a Person. If so, complain. If not,
    # "Not a person"
    if isinstance(person, Person):
        person.complain()
    else:
        print("Not a person")
