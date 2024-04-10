import argparse
import sys

from .random_word import RandomWord, NoWordsToChoseFrom
from .random_sentence import RandomSentence
from . import cmdline


def main():
    parser = argparse.ArgumentParser(
        prog="wonderwords",
        description="""Generate random words and sentences from the command line.
        Here is a full list of available commands. To learn more about each
        command, go to the documentation at https://wonderwords.readthedocs.io
        """,
        epilog="""Thanks to all contributors who made this possible.
        To contribute, go to https://github.com/mrmaxguns/wonderwordsmodule
        """,
    )

    #
    # Base commands
    #

    # Will be changed to a single positional MODE argument in version 3
    parser.add_argument(
        "-w",
        "--word",
        "--random-word",
        action="store_true",
        help="generate a random word",
    )

    parser.add_argument(
        "-f",
        "--filter",
        action="store_true",
        help="get a list of all known words matching the criteria specified",
    )

    parser.add_argument(
        "-l",
        "--list",
        action="store",
        type=int,
        help="return a list of a certain length of random words",
    )

    parser.add_argument(
        "-s",
        "--sentence",
        action="store",
        type=str,
        choices=[
            "bb",
            "ss",
            "bba",
            "s",
        ],
        help="return a sentence based on the structure chosen",
    )

    parser.add_argument(
        "-v", "--version", action="store_true", help="print the version number and exit"
    )

    #
    # Settings and modifiers
    #
    parser.add_argument(
        "-S",
        "--starts-with",
        action="store",
        default="",
        type=str,
        help="strings the random word(s) should start with",
    )

    parser.add_argument(
        "-e",
        "--ends-with",
        action="store",
        default="",
        type=str,
        help="strings the random word(s) should end with",
    )

    parser.add_argument(
        "-p",
        "--parts-of-speech",
        action="store",
        type=str,
        nargs="+",
        # The plural forms will be removed in version 3
        choices=["noun", "verb", "adjective", "nouns", "verbs", "adjectives"],
        help=(
            "only include certain parts of speech (by default all"
            " parts of speech are included)"
        ),
    )

    parser.add_argument(
        "-m",
        "--word-min-length",
        action="store",
        type=int,
        help="minimum length of the word(s)",
    )

    parser.add_argument(
        "-M",
        "--word-max-length",
        action="store",
        type=int,
        help="maximum length of the word(s)",
    )

    parser.add_argument(
        "-r",
        "--regex",
        "--re",
        "--regular-expression",
        action="store",
        type=str,
        help=(
            "a python-style regular expression for the word(s) to match"
        ),
    )

    parser.add_argument(
        "-x",
        "--exclude-with-spaces",
        action="store_true",
        default=False,
        help="exclude open compounds, such as 'contact lens'",
    )

    parser.add_argument(
        "-d",
        "--delimiter",
        default=", ",
        type=str,
        help=(
            "specify the delimiter to put between a list of words, default is ', '"
        ),
    )

    parser.add_argument(
        "-E",
        "--suppress-error-on-less",
        action="store_true",
        default=False,
        help="suppress errors when less words are returned in a list then wanted",
    )

    args = parser.parse_args()
    mode = get_mode(args)
    sys.exit(run_wonderwords(mode, args))


def get_mode(arguments):
    if arguments.version:
        return "version"
    elif arguments.word:
        return "word"
    elif arguments.filter:
        return "filter"
    elif arguments.list is not None:
        return "list"
    elif arguments.sentence is not None:
        return "sentence"
    else:
        return None


def run_wonderwords(mode, arguments):  # noqa: C901
    if mode == "version":
        cmdline.display_version()
        return 0

    kwargs = {
        "starts_with": arguments.starts_with,
        "ends_with": arguments.ends_with,
        "include_categories": arguments.parts_of_speech,
        "word_min_length": arguments.word_min_length,
        "word_max_length": arguments.word_max_length,
        "regex": arguments.regex,
        "exclude_with_spaces": arguments.exclude_with_spaces,
    }

    if mode == "word":
        try:
            cmdline.display_word(RandomWord().word(**kwargs))
        except NoWordsToChoseFrom:
            cmdline.display_word_not_found(one_word=True)
            return 1
    elif mode == "filter":
        words = RandomWord().filter(**kwargs)
        if words:
            cmdline.display_list(RandomWord().filter(**kwargs), delimiter=arguments.delimiter)
        else:
            cmdline.display_word_not_found(one_word=False)
    elif mode == "list":
        words = RandomWord().random_words(amount=arguments.list, return_less_if_necessary=True, **kwargs)
        if words is not None:
            cmdline.display_list(words, delimiter=arguments.delimiter)
        if not arguments.suppress_error_on_less and len(words) < arguments.list:
            cmdline.display_not_enough_words()
            return 1
    elif mode == "sentence":
        generator = RandomSentence()
        if arguments.sentence == "bb":
            cmdline.display_sentence(generator.bare_bone_sentence())
        elif arguments.sentence == "ss":
            cmdline.display_sentence(generator.simple_sentence())
        elif arguments.sentence == "bba":
            cmdline.display_sentence(generator.bare_bone_with_adjective())
        else:
            cmdline.display_sentence(generator.sentence())
    else:
        cmdline.display_hello()

    return 0


if __name__ == "__main__":
    main()
