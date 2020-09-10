"""
The ``random_word`` module houses all classes and functions relating to the
generation of single random words.
"""

import random
from typing import Optional, List

from . import assets

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources


class NoWordsToChoseFrom(Exception):
    """NoWordsToChoseFrom is raised when there is an attempt to access more
    words than exist. This exception may be raised if the amount of random
    words to generate is larger than the amount of words that exist.
    """

    pass


class RandomWord:
    """The RandomWord class encapsulates multiple methods dealing with the
    generation of random words and lists of random words.

    Example::

        >>> r = RandomWord(nouns=["apple", "orange"])
        >>> r2 = RandomWord()

    :param nouns: a list of nouns that will be used to generate random nouns.
        Defaults to None.
    :type nouns: list, optional
    :param verbs: a list of verbs that will be used to generate random verbs.
        Defaults to None.
    :type verbs: list, optional
    :param adjectives: a list of adjectives that will be used to generate random
        adjectives. Defaults to None.
    :type adjectives: list, optional
    """

    def __init__(
        self,
        nouns: Optional[List[str]] = None,
        verbs: Optional[List[str]] = None,
        adjectives: Optional[List[str]] = None,
    ):
        self.nouns = nouns or self.read_words("nounlist.txt")
        self.verbs = verbs or self.read_words("verblist.txt")
        self.adjectives = adjectives or self.read_words("adjectivelist.txt")
        self.parts_of_speech = {
            "nouns": self.nouns,
            "verbs": self.verbs,
            "adjectives": self.adjectives,
        }

    def filter(
        self,
        starts_with: str = "",
        ends_with: str = "",
        include_parts_of_speech: Optional[List[str]] = None,
        word_min_length: Optional[int] = None,
        word_max_length: Optional[int] = None,
    ):
        """Return all existing words that match the criteria specified by the
        arguments.

        Example::

            >>> # Filter all nouns that start with a:
            >>> r.filter(starts_with="a", include_parts_of_speech=["noun"])

        :param starts_with: the string each word should start with. Defaults to
            "".
        :type starts_with: str, optional
        :param ends_with: the string each word should end with. Defaults to "".
        :type ends_with: str, optional
        :param include_parts_of_speech: a list of strings denoting a part of
            speech. Each word returned will be in the category of at least one
            part of speech. By default, all parts of speech are enabled.
            Defaults to None.
        :type include_parts_of_speech: list of strings, optional
        :param word_min_length: the minimum length of each word. Defaults to
            None.
        :type word_min_length: int, optional
        :param word_max_length: the maximum length of each word. Defaults to
            None.
        :type word_max_length: int, optional

        :return: a list of unique words that match each of the criteria
            specified
        :rtype: list of strings
        """
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
        amount: int = 1,
        starts_with: str = "",
        ends_with: str = "",
        include_parts_of_speech: Optional[List[str]] = None,
        word_min_length: Optional[int] = None,
        word_max_length: Optional[int] = None,
        return_less_if_necessary: bool = False,
    ):
        """Generate a list of n random words specified by the ``amount``
        parameter and fit the criteria specified.

        Example::

            >>> # Generate a list of 3 adjectives or nouns which start with "at"
            >>> # and are at least 2 letters long
            >>> r.random_words(
            ...     3,
            ...     starts_with="at",
            ...     include_parts_of_speech=["adjectives", "nouns"],
            ...     word_min_length=2
            ... )

        :param amount: the amount of words to generate. Defaults to 1.
        :type amount: int, optional
        :param starts_with: the string each word should start with. Defaults to
            "".
        :type starts_with: str, optional
        :param ends_with: the string each word should end with. Defaults to "".
        :type ends_with: str, optional
        :param include_parts_of_speech: a list of strings denoting a part of
            speech. Each word returned will be in the category of at least one
            part of speech. By default, all parts of speech are enabled.
            Defaults to None.
        :type include_parts_of_speech: list of strings, optional
        :param word_min_length: the minimum length of each word. Defaults to
            None.
        :type word_min_length: int, optional
        :param word_max_length: the maximum length of each word. Defaults to
            None.
        :type word_max_length: int, optional
        :param return_less_if_necessary: if set to True, if there aren't enough
            words to statisfy the amount, instead of raising a
            NoWordsToChoseFrom exception, return all words that did statisfy
            the original query.
        :type return_less_if_necessary: bool, optional

        :raises NoWordsToChoseFrom: if there are less words to choose from than
            the amount that was requested, a NoWordsToChoseFrom exception is
            raised, **unless** return_less_if_necessary is set to True.

        :return: a list of the words
        :rtype: list of strings
        """
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
            random.shuffle(choose_from)
            return choose_from

        words = []
        for _ in range(amount):
            new_word = random.choice(choose_from)
            choose_from.remove(new_word)
            words.append(new_word)

        return words

    def word(
        self,
        starts_with: str = "",
        ends_with: str = "",
        include_parts_of_speech: Optional[List[str]] = None,
        word_min_length: Optional[int] = None,
        word_max_length: Optional[int] = None,
    ):
        """Returns a random word that fits the criteria specified by the
        arguments.

        Example::

            >>> # Select a random noun that starts with y
            >>> r.word(ends_with="y", include_parts_of_speech=["nouns"])

        :param starts_with: the string each word should start with. Defaults to
            "".
        :type starts_with: str, optional
        :param ends_with: the string the word should end with. Defaults to "".
        :type ends_with: str, optional
        :param include_parts_of_speech: a list of strings denoting a part of
            speech. The returned will be in the category of at least one
            part of speech. By default, all parts of speech are enabled.
            Defaults to None.
        :type include_parts_of_speech: list of strings, optional
        :param word_min_length: the minimum length of the word. Defaults to
            None.
        :type word_min_length: int, optional
        :param word_max_length: the maximum length of the word. Defaults to
            None.
        :type word_max_length: int, optional

        :raises NoWordsToChoseFrom: if a word fitting the criteria doesn't
            exist

        :return: a word
        :rtype: str
        """
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
        """Read a file found in static/ where each line has a word, and return
        all words as a list
        """
        words = pkg_resources.open_text(assets, word_file).readlines()
        return [word.rstrip() for word in words]

    def _validate_lengths(self, word_min_length, word_max_length):
        """Validate the values and types of word_min_length and word_max_length"""
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
