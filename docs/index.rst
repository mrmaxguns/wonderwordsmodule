.. Wonderwords documentation master file - index page

Wonderwords Official Documentation
==================================

Wonderwords is a python package with a command line interface with the purpose
of generating random words and sentences. Wonderwords is free software under
the MIT license. Contributions to the library are welcome.

While Wonderwords supports English by default, custom word lists can be
used to generate and filter words in other languages as well.

Here is a simple example::

    >>> from wonderwords import RandomWord
    >>> generator = RandomWord()
    >>> generator.word()
    'stomach'

The random words can also be further customized::

    >>> generator.word(starts_with="ap", include_categories=["adjectives"])
    'apathetic'

With Wonderwords you can also generate lists of words and sentences.
To install, head over to the :ref:`install <install_uninstall_upgrade>` page.
The :ref:`quickstart <quickstart>` is a great place to get started with Wonderwords.

A full reference of all modules can be found at the :ref:`API documentation <docs>`
page.

Documentation
-------------

.. toctree::
   :maxdepth: 2
   :caption: Contents

   install
   quickstart
   advanced
   api_docs/index

Indices and tables
------------------

* :ref:`genindex`
* :ref:`docs`
* :ref:`modindex`
* :ref:`search`
