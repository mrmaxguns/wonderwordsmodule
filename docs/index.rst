.. Wonderwords documentation master file - index page

Wonderwords Official Documentation
==================================

Wonderwords is a python package with a command line interface with the purpose
of generating random words and sentences. Wonderwords is **free** and **open
source**, meaning anyone can contribute to its repository.

Here is a simple example::

  >>> from wonderwords import RandomWord
  >>>
  >>> generator = RandomWord()
  >>> generator.word()
  'stomach'

The random words can also be further customized::

  >>> generator.word(starts_with="ap", include_parts_of_speech=["adjectives"])
  'apathetic'

With Wonderwords you can also generate lists of words and sentences, though
the sentence feature is in its early development. To install, head over to the
:ref:`install <install_uninstall_upgrade>` page. The :ref:`quickstart <quickstart>` is a great
place to get started with Wonderwords.

A full reference of all modules (the API documentation) can be found
:ref:`here <docs>`.

Documentation
-------------

.. toctree::
   :maxdepth: 2
   :caption: Contents

   install
   quickstart
   api_docs/index

Indices and tables
------------------

* :ref:`genindex`
* :ref:`docs`
* :ref:`modindex`
* :ref:`search`
