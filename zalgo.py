# coding: utf-8
from random import randint, choice

def zalgo(text):
    """[--light] text
    ZALGO"""
    zalgo_threshold = 50
    zalgo_chars = [unichr(i) for i in range(0x0300, 0x036F + 1)]
    zalgo_chars.extend([u'\u0488', u'\u0489'])
    random_extras = [unichr(i) for i in range(0x0FBE, 0x0FD4 + 1)]
    random_extras.extend([unichr(i) for i in range(0x0F00, 0x0F17 + 1)])
    random_extras.extend([unichr(i) for i in range(0x1D023, 0x1D045 + 1)])
    def insert_randoms(text):
        newtext = []
        for char in text:
            newtext.append(char)
            if randint(1,5) == 1:
                newtext.append(choice(random_extras))
        return u''.join(newtext)
    source = insert_randoms(text.decode('utf8').upper())
    zalgoized = []
    for letter in source:
        zalgoized.append(letter)
        zalgo_num = randint(0, zalgo_threshold) + 1
        for _ in range(zalgo_num):
            zalgoized.append(choice(zalgo_chars))
    response = choice(zalgo_chars).join(zalgoized)
    return response.encode('utf8', 'ignore')
