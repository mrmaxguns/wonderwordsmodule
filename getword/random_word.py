import random


# Class random_word is the class that contains all the random word functions
class random_word:
    # Initialize some important variables
    def __init__(self):
        # Open and read the file containing the words
        word_file = open('words.txt', "r")
        words = word_file.readlines()

        # Strip all newlines from the words
        words_newline_stripped = []
        for w in words:
            words_newline_stripped.append(w.rstrip())

        # Store the list of words in dict_words_list
        self.dict_words_list = words_newline_stripped

    # Word function chooses a random word from the dict_words_list
    def word(self):
        return random.choice(self.dict_words_list)

    # Words_list function chooses a certain amount of random word and returns them as a list
    def words_list(self, amount):
        list_of_words = []
        for w in range(amount):
            list_of_words.append(random.choice(self.dict_words_list))

        return list_of_words

    # Starts with chooses a random word from the words that start with a certain letter
    def starts_with(self, letter):
        list_of_words_that_start_with_letter = []

        for i in self.dict_words_list:
            if i[0] == letter:
                list_of_words_that_start_with_letter.append(i)

        return random.choice(list_of_words_that_start_with_letter)
