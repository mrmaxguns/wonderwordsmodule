import random


class random_sentence:
    def __init__(self):
        noun_file = open('nounlist.txt', 'r')
        adjective_file = open('adjectivelist.txt', 'r')
        verb_file = open('verblist.txt', 'r')

        nouns = noun_file.readlines()
        adjectives = adjective_file.readlines()
        verbs = verb_file.readlines()

        def strip_newline(words):
            words_newline_stripped = []
            for w in words:
                words_newline_stripped.append(w.rstrip())
            return words_newline_stripped

        self.noun = strip_newline(nouns)
        self.verb = strip_newline(verbs)
        self.adjective = strip_newline(adjectives)

    def bare_bone_sentence(self):
        thenoun = random.choice(self.noun)
        theverb = random.choice(self.verb)
        return 'The %s %ss' % (thenoun, theverb)
