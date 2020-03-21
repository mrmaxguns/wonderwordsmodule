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

        # Read the files
        nouns = pkg_resources.open_text('wonderwords', 'nounlist.txt').readlines()
        adjectives = pkg_resources.open_text('wonderwords', 'adjectivelist.txt').readlines()
        verbs = pkg_resources.open_text('wonderwords', 'verblist.txt').readlines()
        words = pkg_resources.open_text('wonderwords', 'words.txt').readlines()

        # Strip newlines
        def strip_newline(file):
            words_newline_stripped = []
            for w in file:
                words_newline_stripped.append(w.rstrip())
            return words_newline_stripped

        self.noun = strip_newline(nouns)
        self.verb = strip_newline(verbs)
        self.adjective = strip_newline(adjectives)
        self.dict_words_list = strip_newline(words)

    # Word function chooses a random word from the dict_words_list
    def word(self, include_parts_of_speech=''):
        list_of_words_to_choose_from = []
        something_chosen = False

        if 'noun' in include_parts_of_speech:
            list_of_words_to_choose_from.extend(self.noun)
            something_chosen = True
        if 'verb' in include_parts_of_speech:
            list_of_words_to_choose_from.extend(self.verb)
            something_chosen = True
        if 'adjective' in include_parts_of_speech:
            list_of_words_to_choose_from.extend(self.adjective)
            something_chosen = True
        if not something_chosen:
            list_of_words_to_choose_from = self.noun + self.verb + self.adjective

        return random.choice(list_of_words_to_choose_from)

    # Words_list function chooses a certain amount of random word and returns them as a list
    def words_list(self, amount, include_parts_of_speech=''):
        list_of_words = []
        for every_word in range(amount):
            list_of_words.append(self.word(include_parts_of_speech))

        return list_of_words

    # Starts with chooses a random word from the words that start with a certain letter
    def starts_with(self, letter, include_parts_of_speech=''):
        list_of_words_to_choose_from = []
        something_chosen = False

        if 'noun' in include_parts_of_speech:
            list_of_words_to_choose_from.extend(self.noun)
            something_chosen = True
        if 'verb' in include_parts_of_speech:
            list_of_words_to_choose_from.extend(self.verb)
            something_chosen = True
        if 'adjective' in include_parts_of_speech:
            list_of_words_to_choose_from.extend(self.adjective)
            something_chosen = True
        if not something_chosen:
            list_of_words_to_choose_from = self.noun + self.verb + self.adjective

        list_of_words_that_start_with_letter = []

        for i in list_of_words_to_choose_from:
            if i[0] == letter:
                list_of_words_that_start_with_letter.append(i)

        return random.choice(list_of_words_that_start_with_letter)
