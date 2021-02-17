
.. _advanced:

Advanced Tutorial
=================

.. note::

  This tutorial assumes you already know the basics of Wonderwords. Check out
  the :ref:`quickstart` if you haven't already done so.

Random word generation is awesome, but what if we want to add a custom list of
words? In this tutorial, you will learn how to customize Wonderwords to unleash
its full potential.

Let's start out by creating file called ``random_name_generator.py``. At the end
of the tutorial we'll be creating a simple program which generates random names.

Custom categories
^^^^^^^^^^^^^^^^^

Wonderwords allows adding custom categories of words to our generator. The
``RandomWord`` class actually takes an unlimited amount of keyword arguments,
where the keys are the names of our custom categories, and the values are lists
of words in those categories.

Here's an example::

  from wonderwords import RandomWord

  fruits = ["apple", "orange", "banana", "strawberry"]
  generator = RandomWord(fruit=fruits)

  print(generator.word()) # ex: apple

Let's break this down:

1. First, we import the ``RandomWord`` class from ``wonderwords``.
2. We then define a list of fruits.
3. After that, we create a new instance of ``RandomWord``, where we create a
   category called ``fruit``. Normally, we define category names in the singular
   form, so ``fruit`` instead of ``fruits``.
4. We print a random word from all the available categories.

All of the arguments we had when generating random words from the default word
lists are available. Word length, what a word starts and ends with, and custom
regular expressions can all be specified when generating a random word with
custom categories.

We can add as many word lists as we want::

  animals = ["cow", "cat", "dog", "elephant"]
  plants = ["tree", "grass", "sunflower"]
  generator2 = RandomWord(animal=animals, plant=plants)

  print(generator2.word()) # ex: grass (all categories are enabled by default)
  print(generator2.word()) # ex: cat
  print(generator2.word(include_categories=["animal"])) # ex: dog

As illustrated in the example above, we can include only specific categories
with ``include_categories``. We have already seen this argument before, when
specifying parts of speech, such as "noun" and "verb". But now, we can no longer
generate random nouns, verbs, and adjectives. The following code won't work::

  generator2.word(include_categories=["noun"])
  # ValueError: 'noun' is an invalid category
  # :(

This is because when we specify custom categories, the default configuration is
overwritten. What if we want both a custom category, and one of the default
categories as well? This can be done with ``Defaults``::

  from wonderwords import RandomWord, Defaults

  writing_utensils = ["graphite pencil", "pen", "marker", "colored pencil"]
  generator = RandomWord(
      utensil=writing_utensils,
      adjective=Defaults.ADJECTIVES
  )
  print(generator.word()) # ex: angry
  print(generator.word(include_categories=["utensil"])) # ex: marker
  print(generator.word(include_categories=["adjective"])) # ex: sparkling

``Defaults`` is a python object that has a number of constants representing
various default categories. We can specify one of these categories instead of
a list of words, and a list of words represented by the category will be used.
With the help of ``Defaults`` and custom categories, we can define complex
configurations with relatively few lines of code. Currently, ``Defaults`` has
four categories:

* ``Defaults.NOUNS``: for nouns
* ``Defaults.VERBS``: for verbs
* ``Defaults.ADJECTIVES``: for adjectives
* ``Defaults.PROFANITIES``: for curse words

Creating the random name generator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With all of that, let's get back to our random name generator. First, we'll do
some initial setup. Put the following lines at the top of
``random_name_generator.py``::

  from wonderwords import RandomWord

  # Note: here, we put the names in a list, but when you're writing code with
  # large lists, you typically put them in a file, and read from there.
  FIRST_NAMES = ["Jane", "Bob", "Anne", "Max", "Jake"]
  LAST_NAMES = ["Jacobson", "Johnson", "Miller", "Rodriguez", "Davis"]

Here we import ``RandomWord`` and create a list of first names, and a list of
surnames. Now, let's create an instance of the ``RandomWord`` class::

  generator = RandomWord(name=FIRST_NAMES, surname=LAST_NAMES)

Here we create a random word generator with two categories: ``name`` and
``surname``. We pass the lists we defined earlier to the categories. Now it's
time to write our ``main`` function, where the bulk of our code will reside::

  def main():
      while True:
          # We put this here, so that the user can chose to generate another
          # word or quit.
          action = input("Generate (enter) or quit (q) ").strip()

          if action.lower() == "q":
              break

          first_name = generator.word(include_categories=["name"])
          last_name = generator.word(include_categories=["surname"])
          print(first_name, last_name)
      print("Thanks for using the generator!")

We start out by defining our ``main`` function. Here we create a ``while`` loop
that runs until the player decides to quit. The first thing we do is check if
the player wants to continue generating random words. We use the ``strip``
method to remove any trailing/leading whitespace. If the player types "q", or
"Q", then the program quits.

We then generate a random first and last name. We use ``include_categories`` to
specify the categories used. Finally, we print the generated full name.

The only thing left is to call our main function::

  if __name__ == "__main__":
      main()

In the code above, we call the ``main`` function as long as we run the code
directly. If someone imports our code, the ``main`` function won't run.

That's it! If you've read this far, you have completely mastered Wonderwords.
Go on, and put your newly learned skills to practice.
