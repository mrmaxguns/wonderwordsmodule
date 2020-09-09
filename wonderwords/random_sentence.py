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
        the_verb = random.choice(self.verb)

        # Check for exceptions in english
        if the_verb[-1] == "h" and (the_verb[-2] == "s" or the_verb[-2] == "c"):
            return "The %s %ses." % (the_noun, the_verb)

        elif the_verb[-1] == "y":
            the_verb_list = list(the_verb)
            del the_verb_list[-1]
            the_new_verb = "".join(the_verb_list)
            return "The %s %sies." % (the_noun, the_new_verb)

        elif the_verb[-1] == "s" and the_verb[-2] == "s":
            return "The %s %ses." % (the_noun, the_verb)

        else:
            return "The %s %ss." % (the_noun, the_verb)

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

        the_bare_bone_sentence = self.bare_bone_sentence()
        the_bare_bone_list = list(the_bare_bone_sentence)
        del the_bare_bone_list[-1]
        the_simple_sentence = "".join(the_bare_bone_list)
        return "%s %s." % (the_simple_sentence, the_direct_object)

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
        the_verb = random.choice(self.verb)
        the_adjective = random.choice(self.adjective)

        # Check for exceptions in english
        if the_verb[-1] == "h" and (the_verb[-2] == "s" or the_verb[-2] == "c"):
            return "The %s %s %ses." % (the_adjective, the_noun, the_verb)

        elif the_verb[-1] == "y":
            the_verb_list = list(the_verb)
            del the_verb_list[-1]
            the_new_verb = "".join(the_verb_list)
            return "The %s %s %sies." % (the_adjective, the_noun, the_new_verb)

        elif the_verb[-1] == "s" and the_verb[-2] == "s":
            return "The %s %s %ses." % (the_adjective, the_noun, the_verb)

        else:
            return "The %s %s %ss." % (the_adjective, the_noun, the_verb)

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
        the_noun = random.choice(self.noun)
        the_verb = random.choice(self.verb)
        the_adjective = random.choice(self.adjective)
        the_direct_object = random.choice(self.noun)

        # Check for exceptions in english
        if the_verb[-1] == "h" and (the_verb[-2] == "s" or the_verb[-2] == "c"):
            return "The %s %s %ses %s." % (
                the_adjective,
                the_noun,
                the_verb,
                the_direct_object,
            )

        elif the_verb[-1] == "y":
            the_verb_list = list(the_verb)
            del the_verb_list[-1]
            the_new_verb = "".join(the_verb_list)
            return "The %s %s %sies %s." % (
                the_adjective,
                the_noun,
                the_new_verb,
                the_direct_object,
            )

        elif the_verb[-1] == "s" and the_verb[-2] == "s":
            return "The %s %s %ses %s." % (
                the_adjective,
                the_noun,
                the_verb,
                the_direct_object,
            )

        else:
            return "The %s %s %ss %s." % (
                the_adjective,
                the_noun,
                the_verb,
                the_direct_object,
            )
