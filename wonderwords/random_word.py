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

# Import the random module
import random


# Class random_word is the class that contains all the random word functions
class random_word:
    # Initialize some important variables
    def __init__(self):
        # Import importlib (will help gather the text files containing the words)
        try:
            import importlib.resources as pkg_resources
        except ImportError:
            # For older versions of python:
            import importlib_resources as pkg_resources

        # Read the files
        nouns = pkg_resources.open_text('wonderwords', 'nounlist.txt').readlines()
        adjectives = pkg_resources.open_text('wonderwords', 'adjectivelist.txt').readlines()
        verbs = pkg_resources.open_text('wonderwords', 'verblist.txt').readlines()

        # Strip newlines from all the files
        def strip_newline(file):
            words_newline_stripped = []
            for w in file:
                words_newline_stripped.append(w.rstrip())
            return words_newline_stripped

        # Create variables that contain lists of all the words
        self.noun = strip_newline(nouns)
        self.verb = strip_newline(verbs)
        self.adjective = strip_newline(adjectives)

    def check_for_errors(self, word_min_length, word_max_length):
        standard_error_message = '\nPlease visit our documentation for more info:\n' \
                                 'https://github.com/mrmaxguns/wonderwordsmodule/wiki/Wonderwords-Documentation'

        # Check for any mistakes in parameters
        if not isinstance(word_min_length, int):
            raise TypeError('word_min_length must be int' + standard_error_message)

        if not isinstance(word_max_length, int):
            raise TypeError('word_max_length must be int' + standard_error_message)

        if word_min_length > word_max_length and word_max_length != 0:
            raise Exception('word_min_length cannot be greater than word_max_length' + standard_error_message)

        if word_min_length < 0 or word_max_length < 0:
            raise Exception('word_max_length and/or word_min_length cannot be negative' + standard_error_message)

    # Word function chooses a random word from the lists
    def word(self, include_parts_of_speech='', word_min_length=0, word_max_length=0):
        self.check_for_errors(word_min_length, word_max_length)

        # create a function that filters words based on their length
        def filter_by_length(words_list, word_min_length_, word_max_length_):
            if word_min_length_ != 0:
                for i in words_list.copy():
                    if len(i) < word_min_length_:
                        words_list.remove(i)

            if word_max_length_ != 0:
                for i in words_list.copy():
                    if len(i) > word_max_length_:
                        words_list.remove(i)

        # List of words a random word will be picked from
        list_of_words_to_choose_from = []
        something_chosen = False

        # Check which parts of speech to include
        if 'noun' in include_parts_of_speech:
            filter_by_length(self.noun, word_min_length, word_max_length)
            list_of_words_to_choose_from.extend(self.noun)
            something_chosen = True
        if 'verb' in include_parts_of_speech:
            filter_by_length(self.verb, word_min_length, word_max_length)
            list_of_words_to_choose_from.extend(self.verb)
            something_chosen = True
        if 'adjective' in include_parts_of_speech:
            filter_by_length(self.adjective, word_min_length, word_max_length)
            list_of_words_to_choose_from.extend(self.adjective)
            something_chosen = True
        if not something_chosen:
            filter_by_length(self.noun, word_min_length, word_max_length)
            filter_by_length(self.verb, word_min_length, word_max_length)
            filter_by_length(self.adjective, word_min_length, word_max_length)
            list_of_words_to_choose_from = self.noun + self.verb + self.adjective

        # Return the random word
        return random.choice(list_of_words_to_choose_from)

    # Words_list function chooses a certain amount of random word and returns them as a list
    def words_list(self, amount, include_parts_of_speech='', word_min_length=0, word_max_length=0):
        self.check_for_errors(word_min_length, word_max_length)
        list_of_words = []

        # Loop through the amount of words passed as a parameter
        for every_word in range(amount):
            # Append a random word to the list
            list_of_words.append(self.word(include_parts_of_speech, word_min_length, word_max_length))

        # Return the list
        return list_of_words

    # Starts with chooses a random word from the words that start with a certain letter
    def starts_with(self, letter, include_parts_of_speech='', word_min_length=0, word_max_length=0):
        self.check_for_errors(word_min_length, word_max_length)

        # create a function that filters words based on their length
        def filter_by_length(words_list, word_min_length_, word_max_length_):
            if word_min_length_ != 0:
                for i in words_list.copy():
                    if len(i) < word_min_length_:
                        words_list.remove(i)

            if word_max_length_ != 0:
                for i in words_list.copy():
                    if len(i) > word_max_length_:
                        words_list.remove(i)

        list_of_words_to_choose_from = []
        something_chosen = False

        # Include certain parts of speech
        if 'noun' in include_parts_of_speech:
            filter_by_length(self.noun, word_min_length, word_max_length)
            list_of_words_to_choose_from.extend(self.noun)
            something_chosen = True
        if 'verb' in include_parts_of_speech:
            filter_by_length(self.verb, word_min_length, word_max_length)
            list_of_words_to_choose_from.extend(self.verb)
            something_chosen = True
        if 'adjective' in include_parts_of_speech:
            filter_by_length(self.adjective, word_min_length, word_max_length)
            list_of_words_to_choose_from.extend(self.adjective)
            something_chosen = True
        if not something_chosen:
            filter_by_length(self.noun, word_min_length, word_max_length)
            filter_by_length(self.verb, word_min_length, word_max_length)
            filter_by_length(self.adjective, word_min_length, word_max_length)
            list_of_words_to_choose_from = self.noun + self.verb + self.adjective

        list_of_words_that_start_with_letter = []

        # Choose only those words which start with the passed letter
        for i in list_of_words_to_choose_from:
            if i[0] == letter:
                list_of_words_that_start_with_letter.append(i)

        # Return the word
        return random.choice(list_of_words_that_start_with_letter)
