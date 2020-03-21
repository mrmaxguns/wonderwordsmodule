'''
MIT License

Copyright (c) 2020 mrmaxguns

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import random


# Class random_word is the class that contains all the random word functions
class random_word:
    # Initialize some important variables
    def __init__(self):
        # Import importlib (will help gather resources)
        try:
            import importlib.resources as pkg_resources
        except ImportError:
            import importlib_resources as pkg_resources

        # Read words.txt
        words = pkg_resources.open_text('wonderwords', 'words.txt').readlines()

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
