class Cat:
    cats_created = 0

    def __init__(self, name):
        self.name = name
        Cat.cats_created += 1

print(Cat.cats_created)
for i in range(10):
    Cat("Joseph")
print(Cat.cats_created)
