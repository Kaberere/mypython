import random


class StringHelper:

    @staticmethod
    def randomCase(string):
        tempstr = ""
        for char in string:
            tempstr += char.upper() if random.randint(0, 1) else char.lower()

        return tempstr


class StringCount:

    @staticmethod
    def abbreviate(string, num):
        if (num < len(string)):
            return string[0:num] + "...."
        else:
            return string

        # abbreviation_str = string[0:num] + "....."
        # return abbreviation_str

text = "Hello this is a test"
print(StringHelper.randomCase(text))

sentence = "Hello my name is"
print(StringCount.abbreviate(sentence, 5))

text2 = "I am late for class because I hate programming"
print(StringCount.abbreviate(text2, 9))

text3 = "Everlyne"
print(StringCount.abbreviate(text3, 5))
