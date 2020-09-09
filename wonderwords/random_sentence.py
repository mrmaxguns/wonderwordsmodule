"""
Generate structured sentences in which every word is random.
"""

import random
from typing import Optional, List

from .random_word import RandomWord

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources


VOWELS = ["a", "e", "i", "o", "u"]


def _present_tense(verb):
    """Convert a verb in the form of "to ____" to the present tense 3rd person
    form"""
    verb = verb.strip()
    lowercase_verb = verb.lower()
    if lowercase_verb.endswith(("ss", "ch", "x", "tch", "sh", "zz")):
        verb = verb + "es"
    elif lowercase_verb.endswith("y") and not verb.endswith(
        tuple([vowel + "y" for vowel in VOWELS])
    ):
        verb = verb[:-1] + "ies"
    else:
        verb = verb + "s"
    return verb


# The main class containing all the data and functions
class RandomSentence:
    """The RandomSentence provides an easy interface to generate structured
    sentences where each word is randomly generated.

    Example::

        >>> s = RandomSentence(nouns=["car", "cat", "mouse"], verbs=["eat"])
        >>> s2 = RandomSentence()

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
        self.noun = nouns or RandomWord.read_words("nounlist.txt")
        self.verb = verbs or RandomWord.read_words("verblist.txt")
        self.adjective = adjectives or RandomWord.read_words("adjectivelist.txt")

    # Randomly generate bare bone sentences
    def bare_bone_sentence(self):
        """Generate a bare-bone sentence in the form of
        ``The [subject (noun)] [predicate (verb)].``. For example:
        ``The cat runs.``.

        Example::

            >>> s.bare_bone_sentence()

        :return: string in the form of a bare bone sentence where each word is
            randomly generated
        :rtype: str
        """
        the_noun = random.choice(self.noun)
        the_verb = _present_tense(random.choice(self.verb))

        return f"The {the_noun} {the_verb}."

    def simple_sentence(self):
        """Generate a simple sentence in the form of
        ``The [subject (noun)] [predicate (verb)] [direct object (noun)].``. For
        example: ``The cake plays golf``.

        Example::

            >>> s.simple_sentence()

        :return: a string in the form of a simple sentence where each word is
            randomly generated
        :rtype: str
        """
        the_direct_object = random.choice(self.noun)
        the_bare_bone_sentence = self.bare_bone_sentence()[:-1]

        return f"{the_bare_bone_sentence} {the_direct_object}."

    def bare_bone_with_adjective(self):
        """Generate a bare-bone sentence with an adjective in the form of:
        ``The [(adjective)] [subject (noun)] [predicate (verb)].``. For example:
        ``The skinny cat reads.``

        Example::

            >>> s.bare_bone_with_adjective()

        :return: a string in the form of a bare-bone sentence with an adjective
            where each word is randomly generated
        :rtype: str
        """
        the_noun = random.choice(self.noun)
        the_verb = _present_tense(random.choice(self.verb))
        the_adjective = random.choice(self.adjective)

        return f"The {the_adjective} {the_noun} {the_verb}."

    def sentence(self):
        """Generate a simple sentence with an adjective in the form of:
        ``The [(adjective)] [subject (noun)] [predicate (verb)] [direct object (noun)].``.
        For example: ``The green orange likes food.``

        Example::

            >>> s.sentence()

        :return: a string in the form of a simple sentence with an adjective
            where each word is randomly generated
        :rtype: str
        """
        the_bare_bone_with_adjective = self.bare_bone_with_adjective()[:-1]
        the_direct_object = random.choice(self.noun)

        return f"{the_bare_bone_with_adjective} {the_direct_object}."
