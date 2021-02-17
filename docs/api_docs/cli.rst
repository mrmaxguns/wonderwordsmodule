
.. _cli:

Command Line Interface
======================

The Wonderwords command line interface can be accessed with the ``wonderwords``
command. Usage::

  usage: wonderwords [-h] [-w] [-f] [-l LIST] [-s {bb,ss,bba,s}] [-v] [-sw STARTS_WITH] [-ew ENDS_WITH]
                     [-p {noun,verb,adjective,nouns,verbs,adjectives} [{noun,verb,adjective,nouns,verbs,adjectives} ...]] [-min WORD_MIN_LENGTH]
                     [-max WORD_MAX_LENGTH] [-r REGEX] [-d DELIMITER]

  optional arguments:
    -h, --help            show this help message and exit
    -w, --word, --random-word
                          generate a random word
    -f, --filter          filter a list of words matching the criteria specified
    -l LIST, --list LIST  return a list of words of a certain length
    -s {bb,ss,bba,s}, --sentence {bb,ss,bba,s}
                          return a sentence based on the structure chosen
    -v, --version         Print the version number and exit
    -sw STARTS_WITH, --starts-with STARTS_WITH
                          specify what string the random word(s) should start with
    -ew ENDS_WITH, --ends-with ENDS_WITH
                          specify what string the random word(s) should end with
    -p {noun,verb,adjective,nouns,verbs,adjectives} [{noun,verb,adjective,nouns,verbs,adjectives} ...], --parts-of-speech {noun,verb,adjective,nouns,verbs,adjectives} [{noun,verb,adjective,nouns,verbs,adjectives} ...]
                          specify to only include certain parts of speech (by default all parts of speech are included)
    -min WORD_MIN_LENGTH, --word-min-length WORD_MIN_LENGTH
                          specify the minimum length of the word(s)
    -max WORD_MAX_LENGTH, --word-max-length WORD_MAX_LENGTH
                          specify the maximum length of the word(s)
    -r REGEX, --regex REGEX, --re REGEX, --regular-expression REGEX
                          specify a python-style regular expression that every word must match
    -d DELIMITER, --delimiter DELIMITER
                          Specify the delimiter to put between a list of words, default is ', '

Core commands
-------------

There are a number of core commands that provide basic functionality:

* ``-w`` or ``--random-word``: generate a random word
* ``-f`` or ``--filter``: return a list of words based on specified criteria
* ``-l LIST`` or ``--list LIST``: much like filter, except you need to specify
  an integer of the amount of words you want to get
* ``-s {bb,ss,bba,s}`` or ``--sentence {bb,ss,bba,s}`` generate a sentence. You
  must specify the sentence type from the following types:

    * ``bb``: bare bone sentence
    * ``ss``: simple sentence (bare bone sentence with a direct object)
    * ``bba``: bare bone sentence with an adjective
    * ``s``: simple sentence with an adjective

* ``-v`` or ``--version``: return the version and exit
* ``-h`` or ``--help``: show a list of commands

Other commands
--------------

The following commands apply only to ``random-word``, ``filter`` and ``list``:

* ``-sw`` or ``--starts-with``: the string the word(s) must start with
* ``-ew`` or ``--ends-with``:  the string the word(s) must end with
* ``-p`` or ``--parts-of-speech``: only include certain parts of speech, choose
  one or more from nouns, verbs and adjectives
* ``-min`` or ``--word-min-length``: the minimum length of each word
* ``-max`` or ``--word-max-length``: the maximum length of each word
* ``-r`` or ``--regex`` or ``--re`` or ``--regular-expression``: use a custom
  python regular expression in order to filter a word. All words that do not
  fully match the expression will be removed.

The following commands apply only to ``filter`` and ``list``:

* ``-d DELIMITER`` or ``--delimiter DELIMITER``: the delimiter used to separate
  words. Is ", " by default.

Examples
--------

::

  $ wonderwords -w -sw ma -max 5 # choose a random word which starts with "ma" and is a max length of 5
  $ wonderwords -f -sw a -ew k -p nouns # choose all nouns that start with a, and ends with k
  $ wonderwords -l 5 -sw n -d " & " # random a list of 5 nouns separated by " & " that start with "n"
  $ wonderwords -s bb # generate a random bare-bone sentence
  $ wonderwords -v # print the version
