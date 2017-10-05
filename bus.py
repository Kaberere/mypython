# # A school bus contains 10 children and 1 driver. The school bus cannot be
# # driven until there are a driver and 10 children. Make a school bus that
# # has two drivers and nine children. What happens when you try to drive
# # it?


# class SchoolBus:

#     def __init__(self, children=10, driver=1):
#         self.children = children
#         self.driver = driver

# def bus_move(self, children, driver):
#     if driver == 1 and children == 10:
#         print("Bus can be driven")
#     else:
#         print("Incorrect number of driver and children")


# class Children(SchoolBus):
#     children_created = 0

#     def __init__(self, driver, children=10):
#         if Children.children_created == 9:
#             raise Exception("Bus cannot be driven")
#         Children.children_created -= 1
#         self.children = children
#         self.driver = driver

#     def children(self):
#         return self.children

#     def driver(self):
#         return self.driver

#     def __repr__(self):
#         return "I am %s and on the bus;" % (self.children)


# class Driver(SchoolBus):
#     driver_added = 0

#     def __init__(self, children, driver=1):
#         if Driver.driver_added > 1:
#             raise Exception("{}, bus cannot be driven" .format(driver))
#         Driver.driver_added += 1
#         self.driver = driver
#         self.children = children

#     def driver(self):
#         return self.driver

#     def children(self):
#         return self.children

#     def __repr__(self):
#         return "I am %s, the driver;" % (self.driver)

# child1 = Children("Eve")
# print(child1)
# child2 = Children("Cave")
# print(child2)
# child3 = Children("Tumi")
# print(child3)
# child4 = Children("Eva")
# print(child4)
# child5 = Children("Lavet")
# print(child5)
# child6 = Children("Ely")
# print(child6)
# child7 = Children("Andrew")
# print(child7)
# child8 = Children("Francis")
# print(child8)
# child9 = Children("Tshepo")
# print(child9)
# child10 = Children("Amaka")
# print(child10)
# driver1 = Driver("Nana")
# print(driver1)
# driver2 = Driver("Kabz")
# print(driver2)

class Person:

    def __init__(self, name):
        self.name = name


class Driver(Person):
    pass


class Child(Person):
    pass


class SchoolBus:

    def __init__(self, drivers=[], children=[]):
        self.drivers = drivers
        self.children = children

    def add_driver(self, driver):
        if isinstance(driver, Driver):
            self.drivers.append(driver)
        else:
            print("Get out co-driver!")

    def add_child(self, child):
        self.children.append(child)

    def drive_bus(self):
        if len(self.drivers) == 1 and len(self.children) == 10:
            print("Bus can be driven")
        else:
            print("Bus can't drive")

if __name__ == '__main__':
    import random
    newbus = SchoolBus()
    newbus.add_driver(Driver("Nana"))
for values in range(10):
    kid = input("Enter the child's name: ")
    newbus.add_child(Child(kid))

newbus.drive_bus()
