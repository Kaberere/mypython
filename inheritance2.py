import time


class ToothBrush:

    def __init__(self, color, toothpaste=None):
        self.color = color

    def add_toothpaste(self, toothpaste):
        self.toothpaste = toothpaste

    def brush(self, teeth, seconds):
        time.sleep(seconds)
        print("Finished brushing!")


class ElectricBrush(ToothBrush):

    def __init__(self, color):
        super(ElectricBrush, self).__init__(color)
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

        def brush(self, teeth, time):
            if not self.__is_on:
                raise MemoryError("Forgot to turn toothbrush on")
                super().brush(teeth, time)

    def __str__(self):
        return "Eyram is brushing using a %s ToothBrush" % (self.color)

electric_brush1 = ElectricBrush("yellow")
print(electric_brush1)

electric_brush2 = ElectricBrush("Purple")
electric_brush2.brush("Eyram", 7)
print(electric_brush2)
