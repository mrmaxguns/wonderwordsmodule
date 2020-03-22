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

# The main class containing all the data and functions
class random_sentence:
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

        # Strip newlines
        def strip_newline(words):
            words_newline_stripped = []
            for w in words:
                words_newline_stripped.append(w.rstrip())
            return words_newline_stripped

        # Variables store lists of words
        self.noun = strip_newline(nouns)
        self.verb = strip_newline(verbs)
        self.adjective = strip_newline(adjectives)

    # Randomly generate bare bone sentences
    def bare_bone_sentence(self):
        the_noun = random.choice(self.noun)
        the_verb = random.choice(self.verb)

        # Check for exceptions in english
        if the_verb[-1] == 'h' and (the_verb[-2] == 's' or the_verb[-2] == 'c'):
            return 'The %s %ses.' % (the_noun, the_verb)

        elif the_verb[-1] == 'y':
            the_verb_list = list(the_verb)
            del the_verb_list[-1]
            the_new_verb = ''.join(the_verb_list)
            return 'The %s %sies.' % (the_noun, the_new_verb)

        elif the_verb[-1] == 's' and the_verb[-2] == 's':
            return 'The %s %ses.' % (the_noun, the_verb)

        else:
            return 'The %s %ss.' % (the_noun, the_verb)

    def simple_sentence(self):
        the_direct_object = random.choice(self.noun)

        the_bare_bone_sentence = self.bare_bone_sentence()
        the_bare_bone_list = list(the_bare_bone_sentence)
        del the_bare_bone_list[-1]
        the_simple_sentence = ''.join(the_bare_bone_list)
        return '%s %s.' % (the_simple_sentence, the_direct_object)

    def bare_bone_with_adjective(self):
        the_noun = random.choice(self.noun)
        the_verb = random.choice(self.verb)
        the_adjective = random.choice(self.adjective)

        # Check for exceptions in english
        if the_verb[-1] == 'h' and (the_verb[-2] == 's' or the_verb[-2] == 'c'):
            return 'The %s %s %ses.' % (the_adjective, the_noun, the_verb)

        elif the_verb[-1] == 'y':
            the_verb_list = list(the_verb)
            del the_verb_list[-1]
            the_new_verb = ''.join(the_verb_list)
            return 'The %s %s %sies.' % (the_adjective, the_noun, the_new_verb)

        elif the_verb[-1] == 's' and the_verb[-2] == 's':
            return 'The %s %s %ses.' % (the_adjective, the_noun, the_verb)

        else:
            return 'The %s %s %ss.' % (the_adjective, the_noun, the_verb)

    def sentence(self):
        the_noun = random.choice(self.noun)
        the_verb = random.choice(self.verb)
        the_adjective = random.choice(self.adjective)
        the_direct_object = random.choice(self.noun)

        # Check for exceptions in english
        if the_verb[-1] == 'h' and (the_verb[-2] == 's' or the_verb[-2] == 'c'):
            return 'The %s %s %ses %s.' % (the_adjective, the_noun, the_verb, the_direct_object)

        elif the_verb[-1] == 'y':
            the_verb_list = list(the_verb)
            del the_verb_list[-1]
            the_new_verb = ''.join(the_verb_list)
            return 'The %s %s %sies %s.' % (the_adjective, the_noun, the_new_verb, the_direct_object)

        elif the_verb[-1] == 's' and the_verb[-2] == 's':
            return 'The %s %s %ses %s.' % (the_adjective, the_noun, the_verb, the_direct_object)

        else:
            return 'The %s %s %ss %s.' % (the_adjective, the_noun, the_verb, the_direct_object)
