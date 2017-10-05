class Egg:

    def __init__(self, color, is_broken=False):
        self.color = color
        self.__is_broken = is_broken

    def drop(self):
        self.__is_broken = True

    def __repr__(self):
        return 'Egg <color: {}, is_broken: {}>'.format(self.color, self.__is_broken)


class EggCarton:

    def __init__(self, egg=[]):
        self.eggs = list()

    def add_egg(self, egg):
        self.eggs.append(egg)

    def drop_egg(self):
        last_egg = self.eggs.pop()
        last_egg.drop()

        return last_egg

if __name__ == '__main__':
    carton = EggCarton()
    for egg in range(3):
        carton.add_egg(Egg("blue"))
    for egg in range(4):
        carton.add_egg(Egg("yellow"))
    # carton.drop_egg(Egg(self.eggs.pop())

print(carton.eggs)
