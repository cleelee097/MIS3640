def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True


def avoids(word,forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True
    print(avoid('Babson','abcde'))


