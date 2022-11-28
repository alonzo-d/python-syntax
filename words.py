# def print_upper_words(words):
#     """ convert each word to uppercase then print separately """
#     for word in words:
#         print(word.upper())


# print_upper_words(['boat', 'car', 'train', 'plane'])

def print_only_es(words):
    """ print only words that begin with 'e' """

    for word in words:
        if word.startswith('e'):
            print(word)


print_only_es(['apple', 'orange', 'elote'])
