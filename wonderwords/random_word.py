"""
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
"""

import random
from . import assets

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources


class NoWordsToChoseFrom(Exception):
    pass


class RandomWord:
    def __init__(self, nouns=None, verbs=None, adjectives=None):
        self.nouns = self.read_words("nounlist.txt") or nouns
        self.verbs = self.read_words("verblist.txt" or verbs)
        self.adjectives = self.read_words("adjectivelist.txt" or adjectives)
        self.parts_of_speech = {
            "nouns": self.nouns,
            "verbs": self.verbs,
            "adjectives": self.adjectives,
        }

    def filter(
        self,
        starts_with="",
        ends_with="",
        include_parts_of_speech=None,
        word_min_length=None,
        word_max_length=None,
    ):
        word_min_length, word_max_length = self._validate_lengths(
            word_min_length, word_max_length
        )
        include_parts_of_speech = include_parts_of_speech or [
            "nouns",
            "verbs",
            "adjectives",
        ]

        # filter parts of speech
        words = []
        for part_of_speech in include_parts_of_speech:
            try:
                words.extend(self.parts_of_speech[part_of_speech])
            except KeyError:
                raise ValueError(f"{part_of_speech} is an invalid part of speech")

        for word in words[:]:
            if not word.startswith(starts_with):
                words.remove(word)
            elif not word.endswith(ends_with):
                words.remove(word)

        for word in words[:]:
            if word_min_length is not None and len(word) < word_min_length:
                words.remove(word)
            elif word_max_length is not None and len(word) > word_max_length:
                words.remove(word)

        return list(set(words))

    def random_words(
        self,
        amount=1,
        starts_with="",
        ends_with="",
        include_parts_of_speech=None,
        word_min_length=None,
        word_max_length=None,
        return_less_if_necessary=False,
    ):
        choose_from = self.filter(
            starts_with=starts_with,
            ends_with=ends_with,
            include_parts_of_speech=include_parts_of_speech,
            word_min_length=word_min_length,
            word_max_length=word_max_length,
        )

        if not return_less_if_necessary and len(choose_from) < amount:
            raise NoWordsToChoseFrom(
                f"There aren't enough words to choose from. Cannot generate {str(amount)} word(s)"
            )
        elif return_less_if_necessary:
            return choose_from

        words = []
        for _ in range(amount):
            new_word = random.choice(choose_from)
            choose_from.remove(new_word)
            words.append(new_word)

        return words

    def word(
        self,
        starts_with="",
        ends_with="",
        include_parts_of_speech=None,
        word_min_length=None,
        word_max_length=None,
    ):
        return self.random_words(
            amount=1,
            starts_with=starts_with,
            ends_with=ends_with,
            include_parts_of_speech=include_parts_of_speech,
            word_min_length=word_min_length,
            word_max_length=word_max_length,
        )[0]

    @staticmethod
    def read_words(word_file):
        words = pkg_resources.open_text(assets, word_file).readlines()
        return [word.rstrip() for word in words]

    def _validate_lengths(self, word_min_length, word_max_length):
        if not isinstance(word_min_length, (int, type(None))):
            raise TypeError("word_min_length must be type int or None")

        if not isinstance(word_max_length, (int, type(None))):
            raise TypeError("word_max_length must be type int or None")

        if word_min_length is not None and word_max_length is not None:
            if word_min_length > word_max_length and word_max_length != 0:
                raise ValueError(
                    "word_min_length cannot be greater than word_max_length"
                )

        if word_min_length is not None and word_min_length < 0:
            word_min_length = None

        if word_max_length is not None and word_max_length < 0:
            word_max_length = None

        return (word_min_length, word_max_length)
