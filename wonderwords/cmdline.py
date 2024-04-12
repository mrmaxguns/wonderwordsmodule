from rich import print
from rich.markdown import Markdown

from . import __version__


WELCOME_MESSAGE = f"""# Wonderwords {__version__}
## Available Commands

* `wonderwords -w` - generate a random word
* `wonderwords -f` - get all words matching certain criteria
* `wonderwords -l AMOUNT` - get a list of `AMOUNT` random words
* `wonderwords -s SENT_TYPE` - generate a random sentence of a certain type

For a list of all options, use the `--help` option. To see a detailed and
comprehensive explanation of the commands, visit
[the documentation](https://wonderwords.readthedocs.io).
"""


def display_version() -> None:
    print(f"Wonderwords {__version__}")


def display_word(word: str) -> None:
    print(f"[cyan]{word}[/cyan]")


def display_list(words: list, delimiter=",") -> None:
    delimiter_colorized = f"[grey50]{delimiter}[/grey50]"
    print(delimiter_colorized.join([f"[cyan]{word}[/cyan]" for word in words]))


def display_word_not_found(one_word=True) -> None:
    print(
        f"[red]:exclamation: No word{'' if one_word else 's'} matching the criteria specified could be found.[/red]"
    )


def display_not_enough_words() -> None:
    print(
        f"[red]:exclamation: Couldn't find enough words matching the criteria specified.[/red]"
    )


def display_sentence(sentence: str) -> None:
    print(f"[cyan]{sentence}[/cyan]")


def display_hello() -> None:
    print(Markdown(WELCOME_MESSAGE))
