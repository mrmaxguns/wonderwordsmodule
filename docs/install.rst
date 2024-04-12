
.. _install_uninstall_upgrade:

Install, Uninstall and Upgrade
==============================

Prerequisites
-------------

Before proceeding, make sure you have the following items installed:

* `Python <https://python.org>`_ version 3.8 or greater
* A python package manager, such as `pip <https://pip.pypa.io/en/stable/installing/>`_

Install
-------

To install Wonderwords, use your favorite PyPI package manager, such as pip to
install the package ``wonderwords``:

.. code-block:: bash

    $ pip install wonderwords

Once installed, verify that it was correctly installed by going to a python
console and typing::

    >>> import wonderwords

If you get a ``ModuleNotFoundError``, python cannot find Wonderwords. If you
have trouble with installation, create a new issue at the Wonderwords
`GitHub page <https://github.com/mrmaxguns/wonderwordsmodule>`_.

To install the command-line interface, additional dependencies are required
by Wonderwords. To do so, install the ``cli`` dependency category. With pip,
you can do so with:

.. code-block:: bash

    $ pip install wonderwords[cli]

The command line interface can be accessed with the ``wonderwords`` command.
Verify the command line interface by typing:

.. code-block:: bash

    $ wonderwords -v

You should get an output similar to the following:

.. raw:: html

    <pre>Wonderwords v2.3.0</pre>

Upgrade
-------

To upgrade Wonderwords to the latest stable version, use:

.. code-block:: bash

    $ pip install --upgrade wonderwords

Uninstall
---------

To uninstall with pip, use:

.. code-block:: bash

    $ pip uninstall wonderwords
