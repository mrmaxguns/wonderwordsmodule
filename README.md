# Wonderwords

*Generate random words and sentences with ease in python*

<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/wonderwords?style=for-the-badge">
<img alt="Libraries.io SourceRank" src="https://img.shields.io/librariesio/sourcerank/pypi/wonderwords?style=for-the-badge">
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/wonderwords?style=for-the-badge">

[GitHub Repository](https://github.com/mrmaxguns/wonderwordsmodule) |
[PyPI](https://pypi.org/project/wonderwords) |
[Documentation](https://wonderwords.readthedocs.io)

***

Wonderwords is a Python package useful for generating random words and
structured random sentences. It also comes with a colorful command line
interface for quickly generating random words. The latest version is available
[on GitHub](https://github.com/mrmaxguns/wonderwordsmodule) while the stable
version is available [on PyPI](https://pypi.org/project/wonderwords).

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [The Wonderwords Python API](#the-wonderwords-python-api)
  - [The Wonderwords CLI](#the-wonderwords-cli)
- [Versioning](#versioning)
- [License](#license)
- [Contributing](#contributing)
- [Credits](#credits)

## Features

Here's what Wonderwords is capable of:

- Random word generation in English
- Specify word length, what it starts and ends with, category, and even custom
  regular expressions
- Use custom word lists and define custom categories of words
- Generate structured random sentences
- Basic profanity filtering
- Beautiful command line interface
- Easy-to-use interface and comprehensive documentation
- Open source!

## Installation

To install the latest version of Wonderwords, use your favorite package manager
for the Python Package Index to install the ``wonderwords`` package. For example
with pip:

```bash
pip install wonderwords
```

To upgrade Wonderwords with pip use:

```bash
pip install --upgrade wonderwords
```

To verify that the installation worked, import Wonderwords in python:

```python
import wonderwords
```

If you get a `ModuleNotFound` error, make sure that you have installed
Wonderwords from the step above. For further issues,
[open a new issue from the GitHub page](https://github.com/mrmaxguns/wonderwordsmodule/issues/new/choose).

## Usage

This section will briefly describe Wonderwords usage. Since Wonderwords has
a command line interface and python module, you will find two subsections.

### The Wonderwords Python API

The base random word generation class is the `RandomWord` class. You can
generate words with the `word` method:

```python
from wonderwords import RandomWord

r = RandomWord()

# generate a random word
r.word()

# random word that starts with a and ends with en
r.word(starts_with="a", ends_with="en")

# generate a random noun or adjective, by default all parts of speech are included
r.word(include_parts_of_speech=["nouns", "adjectives"])

# generate a random word between the length of 3 and 8 characters
r.word(word_min_length=3, word_max_length=8)

# generate a random word with a custom Python regular expression
r.word(regex=".*a")

# some of the words in the default word lists have spaces, such as 'contact lens'
# this option disables them
r.word(exclude_with_spaces=True)

# you can combine multiple filtering options
r.word(starts_with="ru", word_max_length=10, include_parts_of_speech=["verbs"])
```

You can also get a list of all words matching some criteria using the `filter`
method:

```python
# get a list of ALL words that start with "am"
r.filter(starts_with="am")

# you can use all the options found in the word method:
r.filter(ends_with="k", include_parts_of_speech=["verbs"], word_min_length=4)
```

You can also generate a random list of words with the `random_words` method.
This is much like the filter method, except you specify the amount of words
to return, and the words are randomly chosen. If there aren't enough words to
satisfy the amount, a `NoWordsToChooseFrom` exception is raised:

```python
# get a list of 3 random nouns
r.random_words(3, include_parts_of_speech=["nouns"])

# you can use all the options found in the word method
r.random_words(5, starts_with="o", word_min_length=10)

# if the amount of words you want to get is larger than the amount of words
# there are, a NoWordsToChooseFrom exception is raised:
r.random_words(100, starts_with="n", word_min_length=16)
# there are less than 100 words that are at least 16 letters long and start with
# n, so an exception is raised

# you can silence the NoWordsToChooseFrom exception and return all words even
# if there are less, by setting return_less_if_necessary to True
r.random_words(100, starts_with="n", word_min_length=16, return_less_if_necessary=True)
```

Generating random sentences is easy using the `RandomSentence` class:

```python
from wonderwords import RandomSentence

s = RandomSentence()

# Get a random bare-bone sentence
s.bare_bone_sentence()

# Get a random bare-bone sentence with a direct object
s.simple_sentence()

# Get a random bare-bone sentence with an adjective
s.bare_bone_with_adjective()

# Get a random sentence with a subject, predicate, direct object and adjective
s.sentence()
```

Finally, starting with version 2.3, Wonderwords has explicit support for filtering
out profanities form lists of words. At the moment, this is rudimentary:

```python
from wonderwords import is_profanity, filter_profanity

# Test against words that could possibly be offensive. Good of user-facing apps.
is_profanity("apple") # False

# Can be done with a list
words = [ ... ]
# The function returns a generator, so we convert it to a list
words_clean = list(filter_profanity(words))
```

More advanced usage (and a tutorial!) is found in the documentation, such as
adding custom categories of words. The full documentation with all information
can be found at: https://wonderwords.readthedocs.io

## The Wonderwords CLI

**NOTE**: Before using the command-line interface (CLI), ensure that you installed
all required dependencies for the CLI using `pip install wonderwords[cli]`.
Wonderwords normally requires no dependencies, but uses Rich for colorized
output in the command line.

Wonderwords provides a command line interface, too, which can be used with the
`wonderwords` command. Usage:

```
usage: wonderwords [-h] [-w] [-f] [-l LIST] [-s {bb,ss,bba,s}] [-v] [-S STARTS_WITH] [-e ENDS_WITH]
                   [-p {noun,verb,adjective,nouns,verbs,adjectives} [{noun,verb,adjective,nouns,verbs,adjectives} ...]]
                   [-m WORD_MIN_LENGTH] [-M WORD_MAX_LENGTH] [-r REGEX] [-x] [-d DELIMITER] [-E]

Generate random words and sentences from the command line. Here is a full list of available commands. To learn more
about each command, go to the documentation at https://wonderwords.readthedocs.io

options:
  -h, --help            show this help message and exit
  -w, --word, --random-word
                        generate a random word
  -f, --filter          get a list of all known words matching the criteria specified
  -l LIST, --list LIST  return a list of a certain length of random words
  -s {bb,ss,bba,s}, --sentence {bb,ss,bba,s}
                        return a sentence based on the structure chosen
  -v, --version         print the version number and exit
  -S STARTS_WITH, --starts-with STARTS_WITH
                        strings the random word(s) should start with
  -e ENDS_WITH, --ends-with ENDS_WITH
                        strings the random word(s) should end with
  -p {noun,verb,adjective,nouns,verbs,adjectives} [{noun,verb,adjective,nouns,verbs,adjectives} ...], --parts-of-speech {noun,verb,adjective,nouns,verbs,adjectives} [{noun,verb,adjective,nouns,verbs,adjectives} ...]
                        only include certain parts of speech (by default all parts of speech are included)
  -m WORD_MIN_LENGTH, --word-min-length WORD_MIN_LENGTH
                        minimum length of the word(s)
  -M WORD_MAX_LENGTH, --word-max-length WORD_MAX_LENGTH
                        maximum length of the word(s)
  -r REGEX, --regex REGEX, --re REGEX, --regular-expression REGEX
                        a python-style regular expression for the word(s) to match
  -x, --exclude-with-spaces
                        exclude open compounds, such as 'contact lens'
  -d DELIMITER, --delimiter DELIMITER
                        specify the delimiter to put between a list of words, default is ', '
  -E, --suppress-error-on-less
                        suppress errors when less words are returned in a list then wanted
```

The basic commands are:

  * `-w`: generate a random word
  * `-f`: which works much like the `filter` function to return all words matching
    a certain criteria
  * `-l LIST`: get a list of `LIST` random words
  * `-s {bb,ss,bba,s}`: generate a random sentence:
    * `bb`: bare bone sentence
    * `ss`: simple sentence (bare bone sentence with direct object)
    * `bba`: bare bone sentence with adjective
    * `s`: generate a simple sentence with an adjective

# Versioning

During its early stages, Wonderwords didn't have a set versioning system and
therefore, versions before `v2.0.0-alpha` are in disarray. Starting with version
2 alpha, Wonderwords uses **sematic versioning**.

# License

Wonderwords is open source and is distributed under the MIT license. See LICENSE
for more details.

# Contributing

All contributions are welcome, and we hope Wonderwords will continue growing.
Start out by reading `CONTRIBUTING.md` for contributing guidelines and how to
get started.

# Credits

Wonderwords has been made possible thanks to the following works:

- `profanitylist.txt` from
  [RobertJGabriel/Google-profanity-words](https://github.com/RobertJGabriel/Google-profanity-words)
  under the
  [Apache-2.0 license](https://github.com/RobertJGabriel/Google-profanity-words/blob/master/LICENSE)
