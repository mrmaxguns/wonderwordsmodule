import random


def word():
    word_file = open("words.txt", "r")
    words = word_file.readlines()

    words_newline_stripped = []
    for w in words:
        words_newline_stripped.append(w.rstrip())

    return random.choice(words_newline_stripped)


def words_list(amount):
    word_file = open("words.txt", "r")
    words = word_file.readlines()

    words_newline_stripped = []
    for w in words:
        words_newline_stripped.append(w.rstrip())

    list_of_words = []
    for w in range(amount):
        list_of_words.append(random.choice(words_newline_stripped))

    return list_of_words


def starts_with(letter):
    word_file = open("words.txt", "r")
    words = word_file.readlines()

    words_newline_stripped = []
    for w in words:
        words_newline_stripped.append(w.rstrip())

    list_of_words_that_start_with_letter = []

    for i in words_newline_stripped:
        if i[0] == letter:
            list_of_words_that_start_with_letter.append(i)

    return random.choice(list_of_words_that_start_with_letter)
