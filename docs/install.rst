
.. _install:

Install
=======

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

The command line interface can be accessed with the ``wonderwords`` command.
Verify the command line interface by typing:

.. code-block:: bash

  $ wonderwords -v

You should get an output similar to the following:

.. raw:: html

  <pre><span style="background-color:#D3D7CF"><font color="#00005F">Running wonderwords version </font></span><span style="background-color:#D3D7CF"><font color="#729FCF"><b>2.0</b></font></span><span style="background-color:#D3D7CF"><font color="#00005F">.0a1</font></span></pre>

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
