
.. _cli:

Command Line Interface
======================

The Wonderwords command line interface can be accessed with the ``wonderwords``
command. Usage

.. code-block:: text

    usage: wonderwords [-h] [-w] [-f] [-l LIST] [-s {bb,ss,bba,s}] [-v] [-S STARTS_WITH]
                       [-e ENDS_WITH]
                       [-p {noun,verb,adjective,nouns,verbs,adjectives} [{noun,verb,adjective,nouns,verbs,adjectives} ...]]
                       [-m WORD_MIN_LENGTH] [-M WORD_MAX_LENGTH] [-r REGEX] [-x] [-d DELIMITER]
                       [-E]

    Generate random words and sentences from the command line. Here is a full list of available
    commands. To learn more about each command, go to the documentation at
    https://wonderwords.readthedocs.io

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
                            only include certain parts of speech (by default all parts of speech
                            are included)
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

Examples
--------

::

  $ wonderwords -w -S ma -M 5 # choose a random word which starts with "ma" and is a max length of 5
  $ wonderwords -f -S a -e k -p nouns # choose all nouns that start with a, and ends with k
  $ wonderwords -l 5 -S n -d " & " # random a list of 5 nouns separated by " & " that start with "n"
  $ wonderwords -s bb # generate a random bare-bone sentence
  $ wonderwords -v # print the version
