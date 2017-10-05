import string


def is_isogram(word):

    # loop through word
    # keep track of character and their count
    # check if count is greater than 1
    # return true/false
    word = word.lower()

    for character in word:
        if character.isalpha() and word.count(character) > 1:
            return False
    return True

if __name__ == '__main__':
    print(is_isogram('background'))
    print(is_isogram('downstream'))
    print(is_isogram('lumberjacks'))
