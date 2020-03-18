import random


class RandomWord:
    def __init__(self):
        word_file = open('words.txt', "r")
        words = word_file.readlines()

        words_newline_stripped = []
        for w in words:
            words_newline_stripped.append(w.rstrip())

        self.dict_words_list = words_newline_stripped

    def word(self):
        return random.choice(self.dict_words_list)

    def words_list(self, amount):
        list_of_words = []
        for w in range(amount):
            list_of_words.append(random.choice(self.dict_words_list))

        return list_of_words

    def starts_with(self, letter):
        list_of_words_that_start_with_letter = []

        for i in self.dict_words_list:
            if i[0] == letter:
                list_of_words_that_start_with_letter.append(i)

        return random.choice(list_of_words_that_start_with_letter)
