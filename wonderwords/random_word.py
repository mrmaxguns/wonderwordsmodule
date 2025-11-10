"""
The ``random_word`` module houses all classes and functions relating to the
generation of single random words.
"""

from random import Random
import re
import enum
from types import ModuleType
from typing import (
    Union,
    Optional,
    List,
    Dict,
    Any,
    Type,
    TextIO,
    Tuple,
    IO,
    Iterable,
    Set,
    Iterator,
)

from . import assets
from . import _trie


WordList = List[str]


class NoWordsToChooseFrom(Exception):
    """NoWordsToChooseFrom is raised when there is an attempt to access more
    words than exist. This exception may be raised if the amount of random
    words to generate is larger than the amount of words that exist.
    """

    pass


class Defaults(enum.Enum):
    """This enum represents the default word lists. For example, if you want a
    random word generator with one category labeled 'adj' for adjectives, but
    want to use the default word list, you can do the following::

        >>> from wonderwords import RandomWord, Defaults
        >>> w = RandomWord(adj=Defaults.ADJECTIVES)
        >>> w.word()
        'red'

    Options available:

    * ``Defaults.NOUNS``: Represents a list of nouns
    * ``Defaults.VERBS``: Represents a list of verbs
    * ``Defaults.ADJECTIVES``: Represents a list of adjectives
    * ``Defaults.PROFANITIES``: Represents a list of curse words

    """

    NOUNS = "nounlist.txt"
    VERBS = "verblist.txt"
    ADJECTIVES = "adjectivelist.txt"
    PROFANITIES = "profanitylist.txt"


def _obtain_resource(
    package: Union[str, ModuleType], resource: str
) -> Union[IO[str], TextIO]:
    """Load a file object from a package, ensuring compatibility with supported Python versions."""
    try:
        # Introduced in Python 3.9
        from importlib.resources import files  # type: ignore

        return files(package).joinpath(resource).open("r")
    except ImportError:
        # Required for Python 3.8, but emits a DeprecationWarning on Python 3.11
        from importlib.resources import open_text

        return open_text(package, resource)


def _get_words_from_text_file(word_file: str) -> WordList:
    """Read a file found in static/ where each line has a word, and return
    all words as a list
    """
    with _obtain_resource(assets, word_file) as f:
        words = f.readlines()
    return [word.rstrip() for word in words]


def _load_default_categories(
    default_categories: Type[Defaults],
) -> Dict[Defaults, WordList]:
    """Load all the default word lists"""
    out: Dict[Defaults, WordList] = {}
    for category in default_categories:
        out[category] = _get_words_from_text_file(category.value)
    return out


# A dictionary where each key representing a category like 'nouns' corresponds to a list of words.
_DEFAULT_CATEGORIES: Dict[Defaults, WordList] = _load_default_categories(Defaults)


def is_profanity(word: str) -> bool:
    """See if a word matches one of the words in the profanity list.

    :param word: The word to check
    :return: Whether the word was found in the profanity list
    """
    return word.lower().strip() in _DEFAULT_CATEGORIES[Defaults.PROFANITIES]


def filter_profanity(words: Iterable[str]) -> Iterator[str]:
    """Attempt to filter out profane words from a list. This should be done in all user-facing applications if random
    words are generated to avoid anything that could possibly be offensive. Curse word filtering is currently not done
    by default on the :py:class:`RandomWord` class.

    Example::

        >>> from wonderwords import filter_profanity
        >>> list(filter_profanity(["hello", "aSS", "world"]))
        ["hello", "world"]

    :param words: Iterable of words to filter
    :return: An iterable of the filtered result
    """
    return filter(
        lambda w: not is_profanity(w),
        words,
    )


class RandomWord:
    """The RandomWord class encapsulates multiple methods dealing with the
    generation of random words and lists of random words.

    Example::

        >>> from wonderwords import RandomWord, Defaults
        >>>
        >>> r = RandomWord(noun=["apple", "orange"]) # Category 'noun' with
        ...     # the words 'apple' and 'orange'
        >>> r2 = RandomWord() # Use the default word lists
        >>> r3 = RandomWord(noun=Defaults.NOUNS) # Set the category 'noun' to
        ...     # the default list of nouns

    .. important::

       Wonderwords version ``2.0`` does not have custom
       categories. In fact there are only three categories: nouns, verbs, and
       adjectives. However, wonderwords will remain backwards compatible until
       version ``3``. Please note that the ``parts_of_speech`` attribute will
       soon be deprecated, along with other method-specific features.

    :param enhanced_prefixes: whether to internally use a trie data
        structure to speed up ``starts_with`` and ``ends_with``. If enabled,
        the class takes longer to instantiate, but calls to the generation
        functions will be significantly (up to 4x) faster when using the
        ``starts_with`` and ``ends_with`` arguments. Defaults to True.
    :type enhanced_prefixes: bool, optional
    :param rng: an instance of a ``random.Random`` used for randomization
    :type rng: random.Random, optional
    :param kwargs: keyword arguments where each key is a category of words
        and value is a list of words in that category. You can also use a
        default list of words by using a value from the `Default` enum instead.
    :type kwargs: list, optional

    """

    def __init__(
        self, enhanced_prefixes: bool = True, rng: Optional[Random] = None, **kwargs: Union[WordList, Defaults]
    ):
        # A dictionary where lists of words organized into named categories
        self._categories: Dict[str, WordList]
        # If enhanced prefixes are enabled, these tries represent all the words known to the generator in forward and
        # reverse. If disabled, this is just None.
        self._tries: Union[Tuple[_trie.Trie, _trie.Trie], None]
        # Random number generator.
        self._generator: Random = rng or Random()
        # Kept for backwards compatibility. Same as self._categories
        self.parts_of_speech: Dict[str, WordList]

        if kwargs:
            self._categories = self._get_word_lists_by_category(kwargs)
        else:
            self._categories = self._get_word_lists_by_category(
                {
                    "noun": Defaults.NOUNS,
                    "verb": Defaults.VERBS,
                    "adjective": Defaults.ADJECTIVES,
                    # The following was added for backwards compatibility
                    # reasons. The plural categories will be deleted in
                    # wonderwords version 3. See issue #9.
                    "nouns": Defaults.NOUNS,
                    "verbs": Defaults.VERBS,
                    "adjectives": Defaults.ADJECTIVES,
                }
            )

        if enhanced_prefixes:
            # Two tries. One trie data structure is generated from
            # the words, while the second one is generated from the
            # words in reverse to deal with starts_with and ends_with
            # respectively.
            self._tries = (_trie.Trie(), _trie.Trie())
            for _, category in self._categories.items():
                for word in category:
                    self._tries[0].insert(word)
                    self._tries[1].insert(word[::-1])
        else:
            self._tries = None

        self.parts_of_speech = self._categories

    def filter(  # noqa: C901
        self,
        starts_with: str = "",
        ends_with: str = "",
        include_categories: Optional[Iterable[str]] = None,
        include_parts_of_speech: Optional[Iterable[str]] = None,
        word_min_length: Optional[int] = None,
        word_max_length: Optional[int] = None,
        regex: Optional[str] = None,
        exclude_with_spaces: bool = False,
    ) -> WordList:
        """Return a sorted list of all existing words that match the criteria
        specified by the arguments.

        Example::

            >>> # Filter all nouns that start with a:
            >>> r.filter(starts_with="a", include_categories=["noun"])

        .. important:: The ``include_parts_of_speech`` argument will soon be
            deprecated. Use ``include_categories`` which performs the exact
            same role.

        :param starts_with: the string each word should start with. Defaults to
            "".
        :type starts_with: str, optional
        :param ends_with: the string each word should end with. Defaults to "".
        :type ends_with: str, optional
        :param include_categories: a list of strings denoting a part of
            speech. Each word returned will be in the category of at least one
            part of speech. By default, all parts of speech are enabled.
            Defaults to None.
        :type include_categories: list of strings, optional
        :param include_parts_of_speech: Same as include_categories, but will
            soon be deprecated.
        :type include_parts_of_speech: list of strings, optional
        :param word_min_length: the minimum length of each word. Defaults to
            None.
        :type word_min_length: int, optional
        :param word_max_length: the maximum length of each word. Defaults to
            None.
        :type word_max_length: int, optional
        :param regex: a custom regular expression which each word must fully
            match (re.fullmatch). Defaults to None.
        :type regex: str, optional
        :param exclude_with_spaces: exclude words that may have spaces in them
        :type exclude_with_spaces: bool, optional

        :return: a list of unique words that match each of the criteria
            specified
        :rtype: list of strings
        """
        word_min_length, word_max_length = self._validate_lengths(
            word_min_length, word_max_length
        )

        # include_parts_of_speech will be deprecated in a future release
        if not include_categories:
            if include_parts_of_speech:
                include_categories = include_parts_of_speech
            else:
                include_categories = list(self._categories.keys())

        # Filter by part of speech and length. Both of these things
        # are done at once since categories are specifically ordered
        # in order to make filtering by length an efficient process.
        # See issue #14 for details.
        words: Set[str] = set()

        for category in include_categories:
            try:
                words_in_category = self._categories[category]
            except KeyError:
                raise ValueError(f"'{category}' is an invalid category") from None

            words_to_add = self._get_words_of_length(
                words_in_category, word_min_length, word_max_length
            )
            words.update(words_to_add)

        if self._tries is not None:
            if starts_with:
                words = words & self._tries[0].get_words_that_start_with(starts_with)
            if ends_with:
                # Since the ends_with trie is in reverse, the
                # ends_with variable must also be reversed.
                # Example (apple):
                # - Backwards: elppa
                # - ends_with: el
                # Currently this is very clunky, since all words
                # that match then need to be reversed to their
                # original forms. Currently, I have no idea how
                # to improve this. But, even with the extra overhead
                # of iteration, this system still significantly
                # shortens the amount of time to filter the words.
                ends_with = ends_with[::-1]
                words = words & set(
                    [
                        i[::-1]
                        for i in self._tries[1].get_words_that_start_with(ends_with)
                    ]
                )

        # Long operations that require looping over every word
        # (O(n)). Since they are so time-consuming, the arguments
        # passed to the function are first checked if the user
        # actually specified any time-consuming arguments. If they
        # are, all long filters are checked at once for every word.
        long_operations: Dict[str, Any] = {}

        if regex is not None:
            long_operations["regex"] = re.compile(regex)
        if exclude_with_spaces:
            long_operations["exclude_with_spaces"] = None
        if self._tries is None:
            if starts_with:
                long_operations["starts_with"] = starts_with
            if ends_with:
                long_operations["ends_with"] = ends_with

        if long_operations:
            words -= self._perform_long_operations(words, long_operations)

        return sorted(list(words))

    def random_words(
        self,
        amount: int = 1,
        starts_with: str = "",
        ends_with: str = "",
        include_categories: Optional[Iterable[str]] = None,
        include_parts_of_speech: Optional[Iterable[str]] = None,
        word_min_length: Optional[int] = None,
        word_max_length: Optional[int] = None,
        regex: Optional[str] = None,
        return_less_if_necessary: bool = False,
        exclude_with_spaces: bool = False,
    ) -> WordList:
        """Generate a list of n random words specified by the ``amount``
        parameter and fit the criteria specified.

        Example::

            >>> # Generate a list of 3 adjectives or nouns which start with
            ...     # "at"
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
        :param include_categories: a list of strings denoting a part of
            speech. Each word returned will be in the category of at least one
            part of speech. By default, all parts of speech are enabled.
            Defaults to None.
        :type include_categories: list of strings, optional
        :param include_parts_of_speech: Same as include_categories, but will
            soon be deprecated.
        :type include_parts_of_speech: list of strings, optional
        :param word_min_length: the minimum length of each word. Defaults to
            None.
        :type word_min_length: int, optional
        :param word_max_length: the maximum length of each word. Defaults to
            None.
        :type word_max_length: int, optional
        :param regex: a custom regular expression which each word must fully
            match (re.fullmatch). Defaults to None.
        :type regex: str, optional
        :param return_less_if_necessary: if set to True, if there aren't enough
            words to statisfy the amount, instead of raising a
            NoWordsToChoseFrom exception, return all words that did statisfy
            the original query.
        :type return_less_if_necessary: bool, optional
        :param exclude_with_spaces: exclude words that may have spaces in them
        :type exclude_with_spaces: bool, optional

        :raises NoWordsToChoseFrom: if there are fewer words to choose from than
            the amount that was requested, a NoWordsToChoseFrom exception is
            raised, **unless** return_less_if_necessary is set to True.

        :return: a list of the words
        :rtype: list of strings
        """
        choose_from = self.filter(
            starts_with=starts_with,
            ends_with=ends_with,
            include_categories=include_categories,
            include_parts_of_speech=include_parts_of_speech,
            word_min_length=word_min_length,
            word_max_length=word_max_length,
            regex=regex,
            exclude_with_spaces=exclude_with_spaces,
        )

        if len(choose_from) < amount:
            if return_less_if_necessary:
                self._generator.shuffle(choose_from)
                return choose_from
            else:
                raise NoWordsToChooseFrom(
                    "There aren't enough words to choose from. Cannot generate "
                    f"{str(amount)} word(s)"
                )

        words: WordList = []
        for _ in range(amount):
            new_word = self._generator.choice(choose_from)
            choose_from.remove(new_word)
            words.append(new_word)

        return words

    def word(
        self,
        starts_with: str = "",
        ends_with: str = "",
        include_categories: Optional[Iterable[str]] = None,
        include_parts_of_speech: Optional[Iterable[str]] = None,
        word_min_length: Optional[int] = None,
        word_max_length: Optional[int] = None,
        regex: Optional[str] = None,
        exclude_with_spaces: bool = False,
    ) -> str:
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
        :param include_categories: a list of strings denoting a part of
            speech. Each word returned will be in the category of at least one
            part of speech. By default, all parts of speech are enabled.
            Defaults to None.
        :type include_categories: list of strings, optional
        :param include_parts_of_speech: Same as include_categories, but will
            soon be deprecated.
        :type include_parts_of_speech: list of strings, optional
        :param word_min_length: the minimum length of the word. Defaults to
            None.
        :type word_min_length: int, optional
        :param word_max_length: the maximum length of the word. Defaults to
            None.
        :type word_max_length: int, optional
        :param regex: a custom regular expression which each word must fully
            match (re.fullmatch). Defaults to None.
        :type regex: str, optional
        :param exclude_with_spaces: exclude words that may have spaces in them
        :type exclude_with_spaces: bool, optional

        :raises NoWordsToChoseFrom: if a word fitting the criteria doesn't
            exist

        :return: a word
        :rtype: str
        """
        return self.random_words(
            amount=1,
            starts_with=starts_with,
            ends_with=ends_with,
            include_categories=include_categories,
            include_parts_of_speech=include_parts_of_speech,
            word_min_length=word_min_length,
            word_max_length=word_max_length,
            regex=regex,
            exclude_with_spaces=exclude_with_spaces,
        )[0]

    @staticmethod
    def read_words(word_file: str) -> WordList:
        """Will soon be deprecated. This method isn't meant to be public, but
        will remain for backwards compatibility. Developers: use
        _get_words_from_text_file internally instead.
        """
        return _get_words_from_text_file(word_file)

    def _validate_lengths(
        self, word_min_length: Any, word_max_length: Any
    ) -> Tuple[Union[int, None], Union[int, None]]:
        """Validate the values and types of word_min_length and word_max_length"""
        if not isinstance(word_min_length, (int, type(None))):
            raise TypeError("word_min_length must be type int or None")

        if not isinstance(word_max_length, (int, type(None))):
            raise TypeError("word_max_length must be type int or None")

        if word_min_length is not None and word_max_length is not None:
            if word_min_length > word_max_length != 0:
                raise ValueError(
                    "word_min_length cannot be greater than word_max_length"
                )

        if word_min_length is not None and word_min_length < 0:
            word_min_length = None

        if word_max_length is not None and word_max_length < 0:
            word_max_length = None

        return word_min_length, word_max_length

    def _get_word_lists_by_category(
        self, custom_categories: Dict[str, Any]
    ) -> Dict[str, WordList]:
        """Add custom categories of words"""
        out: dict[str, WordList] = {}
        for name, words in custom_categories.items():
            if isinstance(words, Defaults):
                word_list = _DEFAULT_CATEGORIES[words]
            else:
                word_list = words

            # All the words in each category are sorted. This is so
            # that they can be bisected by length later on for more
            # efficient word length retrieval. See issue #14 for
            # details.
            word_list.sort(key=len)
            out[name] = word_list

        return out

    def _get_words_of_length(
        self,
        word_list: WordList,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
    ) -> WordList:
        """Given ``word_list``, get all words that are at least
        ``min_length`` long and at most ``max_length`` long.
        """

        if min_length is None:
            left_index = 0
        else:
            left_index = self._bisect_by_length(word_list, min_length)

        if max_length is None:
            right_index = None
        else:
            right_index = self._bisect_by_length(word_list, max_length + 1)

        return word_list[left_index:right_index]

    def _bisect_by_length(self, words: WordList, target_length: int) -> int:
        """Given a list of sorted words by length, get the index of the
        first word that's of the ``target_length``.
        """

        left = 0
        right = len(words) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if len(words[middle]) < target_length:
                left = middle + 1
            else:
                right = middle - 1

        return left

    def _perform_long_operations(
        self, words: Set[str], long_operations: Dict[str, Any]
    ) -> Set[str]:
        """Return a set of words that do not meet the criteria specified by the long operations."""
        remove_words: Set[str] = set()
        for word in words:
            if "regex" in long_operations:
                if not long_operations["regex"].fullmatch(word):
                    remove_words.add(word)
            if "exclude_with_spaces" in long_operations:
                if " " in word:
                    remove_words.add(word)
            if "starts_with" in long_operations:
                if not word.startswith(long_operations["starts_with"]):
                    remove_words.add(word)
            if "ends_with" in long_operations:
                if not word.endswith(long_operations["ends_with"]):
                    remove_words.add(word)
        return remove_words
