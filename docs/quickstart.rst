
.. _quickstart:

Quickstart
==========

Wonderwords is a lightweight, pure python tool that can be used to
generate random words and sentences. In this tutorial you will learn the basics
of Wonderwords and the command line interface. This tutorial is meant for those
who have never used Wonderwords or those who want to learn more about it.
For a full reference of all commands, visit the API documentation.

.. note::

  This tutorial assumes you have already installed Wonderwords. If this is not
  the case, head over to the :ref:`install` page before proceeding.

The ``RandomWord`` class
------------------------

One of the core Wonderwords classes is the ``RandomWord`` class. This class
encapsulates operations dealing with individual words. One method of this
class is the ``word`` method, which can be used to generate individual random
words::

  >>> from wonderwords import RandomWord
  >>>
  >>> w = RandomWord()
  >>> w.word()
  >>> 'sordid'

Calling the word class returned a string containing a word. When using
Wonderwords, it is helpful to create an instance of the ``RandomWord`` class
in the top-level module of your project and import it when necessary.

The ``word`` Method
^^^^^^^^^^^^^^^^^^^

What if we want to generate a word that starts with a certain string, say ``n``?
Here is where the ``starts_with`` and ``ends_with`` arguments come into play.
For example, to retrieve a word that starts with ``"n"`` and ends with
``"ies"``, we can do the following::

  >>> w.word(starts_with="n", ends_with="es")
  'noodles'

You don't have to use both arguments. You can specify either one individually
like so::

  >>> w.word(starts_with="can")
  'cannon'

Sometimes, however, we may try to look for a pattern that doesn't exist. In that
case a ``NoWordsToChoseFrom`` exception is raised::

  >>> w.word(starts_with="ja", ends_with="ka")
  NoWordsToChoseFrom: There aren't enough words to choose from. Cannot generate 1 word(s)

We can also narrow down a word by part of speech. By default, nouns, verbs and
adjectives are all enabled. If you want to generate a word by only a certain
part of speech, you can use the ``include_parts_of_speech`` parameter::

  >>> w.word(include_parts_of_speech=["adjectives"])
  'tough'
  >>> w.word(include_parts_of_speech=["nouns", "verbs"])
  'cinder'

Finally, we can also filter words by length using the ``word_min_length`` and
``word_max_length`` parameters::

  >>> w.word(word_min_length=5)
  'documentary'
  >>> w.word(word_max_length=3)
  'dog'
  >>> w.word(word_min_length=9, word_max_length=10)
  'velodrome'

Remember that we can combine multiple filters together, like so::

  >>> w.word(
  ...     word_min_length=4,
  ...     starts_with="k",
  ...     include_parts_of_speech=["verbs"]
  ... )
  'keep'

The ``filter`` method
^^^^^^^^^^^^^^^^^^^^^

As you saw above, the word class allows the filtering of many words. What if we
want to get a list of all words that match a certain filter? The ``filter``
method allows us to get all words matching a certain criteria::

  >>> w.filter(word_min_length=4, starts_with="loc")
  ['locality',
   'local',
   'locket',
   'location',
   'locomotive',
   'locust',
   'locker',
   'lock',
   'locate']

The ``filter`` method has the same arguments as the ``word`` method, except it
returns **all** matching words, while the ``word`` method matches a random word
fitting the criteria.

The ``random_words`` method
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``random_words`` methods acts just like the ``filter`` method, except with
two differences:

  * You can limit the amount of words fitting the criteria
  * If there aren't enough words to reach the limit, a ``NoWordsToChoseFrom``
    exception is raised **unless** ``return_less_if_necessary`` is set to
    ``True``.

This method is useful if we want to get a list of words::

  >>> w.random_words(3)
  ['prince', 'handover', 'cell']
  >>> w.random_words(4, word_min_length=5, starts_with="a")
  ['abrogation', 'animal', 'appropriation', 'angry']
  >>> w.random_words(3, word_min_length=5, starts_with="alg") # The exception is
  ...                                                         # raised as 3 words cannot be generated
  NoWordsToChoseFrom: There aren't enough words to choose from. Cannot generate 3 word(s)
  >>> w.random_words(3, word_min_length=5, starts_with="alg", return_less_if_necessary=True)
  ['algebra', 'algorithm']

The ``RandomSentence`` class
----------------------------

Wonderwords makes generation of structured sentences made of random words easy.
The ``RandomSentence`` class houses many of these features. You should keep
an instance of this class at the top-level of your project just like the
``RandomWord`` class::

  >>> from wonderwords import RandomSentence
  >>>
  >>> s = RandomSentence()

Creating sentences with the RandomSentence class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The RandomSentence class provides multiple methods to generate random sentences,
for example::

  >>> s.bare_bone_sentence() # generate a bare-bone sentence (The [subject] [predicate])
  'The hut frames.'
  >>> s.simple_sentence() # generate a simple sentence
  'The reprocessing formulates enrollment.'
  >>> s.sentence() # a sentence with a subject, predicate, adjective and direct object
  'The strong mean shears movement.'

As you can see, these sentences have almost no meaning, and are very simple and
structured. These sentences are good for creating memorable phrases for your
programs.

The Wonderwords CLI
-------------------

Wonderwords also provides a CLI, or *command line interface* which is installed
along with the python modules. To use the CLI, open your terminal and type
the command ``wonderwords``::

  $ wonderwords

.. raw:: html

  <pre><span style="background-color:#D3D7CF"><font color="#00005F"><b>╭─────────────────────────────────────────────────────────────────────────────╮</b></font></span>
  <span style="background-color:#D3D7CF"><font color="#00005F"><b>│                                                                             │</b></font></span>
  <span style="background-color:#D3D7CF"><font color="#00005F"><b>│                             WONDERWORDS 2.0.0a1                             │</b></font></span>
  <span style="background-color:#D3D7CF"><font color="#00005F"><b>│                                                                             │</b></font></span>
  <span style="background-color:#D3D7CF"><font color="#00005F"><b>╰─────────────────────────────────────────────────────────────────────────────╯</b></font></span>

   <b>                            No commands given 😞                             </b>


                                <u style="text-decoration-style:single"><b>Available Commands</b></u>

  <font color="#FCE94F"><b> • </b></font><span style="background-color:#2E3436"><font color="#EEEEEC">wonderwords -w</font></span> - generate a random word
  <font color="#FCE94F"><b> • </b></font><span style="background-color:#2E3436"><font color="#EEEEEC">wonderwords -f</font></span> - get all words matching a certain criteria
  <font color="#FCE94F"><b> • </b></font><span style="background-color:#2E3436"><font color="#EEEEEC">wonderwords -l AMOUNT</font></span> - get a list of <span style="background-color:#2E3436"><font color="#EEEEEC">AMOUNT</font></span> random words
  <font color="#FCE94F"><b> • </b></font><span style="background-color:#2E3436"><font color="#EEEEEC">wonderwords -s SENT_TYPE</font></span> - generate a random sentence of a certain type

  For a list of all options, type <span style="background-color:#2E3436"><font color="#EEEEEC">wonderwords -h</font></span>. To see a detailed and
  comprehensive explanation of the commands, visit <font color="#729FCF">the documentation</font>             </pre>

When typing the ``wonderwords`` command, you are greeted with a main page with
basic information, such as basic commands and the ``wonderwords`` version.
To get a full list of commands, type ``wonderwords -h`` or
``wonderwords --help``.

Generating random words
^^^^^^^^^^^^^^^^^^^^^^^

To generate a random word, use the ``-w`` or ``--word`` flag. A random word will
be printed to the console::

  $ wonderwords -w

.. raw:: html

  <pre><span style="background-color:#00005F"><font color="#EEEEEC"><b>poison</b></font></span></pre>

All of the filters that you have learned above have their own commands, too::

  $ wonderwords -w -sw a -ew e # -sw: starts with, -ew ends with; word that starts with a and ends with e
  $ wonderwords -p nouns verbs # -p: parts of speech; select only nouns and verbs
  $ wonderwords -min 3 -max 5 # -min: minimum length, -max maximum length; minimum length 3 and maximum length 5

Generating filters and lists
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also generate filters with the ``-f`` flag and lists with the ``-l``
flag. All modifiers such as ``-sw`` and ``-min`` can also be used. Additionally,
the ``-d`` flag can set a delimiter between words::

  $ wonderwords -f -min 3 # get all words with a minimum length of 3
  $ wonderwords -l 5 -sw ap # get 5 words that start with "ap"
  $ wonderwords -l 3 -d " | " # get 3 random words separated with " | "

Generating random sentences
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``-s`` flag followed by a sentence type can generate a random sentence.
The options of type are:

  * ``bb``: bare-bone sentence
  * ``ss``: simple sentence
  * ``bba``: bare-bone sentence with adjective
  * ``s``: a simple sentence plus and adjective

For example::

  $ wonderwords -s bb # generate a bare-bone sentence
  $ wonderwords -s ss # generate a simple sentence

And that's it!
--------------

The quickstart tutorial has come to an end. In this tutorial, you learned the
basics of Wonderwords. More specifically, you learned about:

* The ``RandomWord`` class
    * The ``word`` method
    * The ``filter`` method
    * The ``random_words`` method
* The ``RandomSentence`` class and some of its methods
* How to use the Wonderwords command line interface

What's next?
^^^^^^^^^^^^

After you have gotten comfortable using wonderwords, you can use the API
reference for help on specific classes, and functions. If you want to
contribute, please read the contribution guidelines. If you have any problems,
bugs, or feature requests, please open up an issue on the
`Wonderwords GitHub page <https://github.com/mrmaxguns/wonderwordsmodule/>`_.