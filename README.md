# Welcome To Wonderwords
[![GitHub issues](https://img.shields.io/github/issues/mrmaxguns/wonderwordsmodule)](https://github.com/mrmaxguns/wonderwordsmodule/issues)
[![GitHub forks](https://img.shields.io/github/forks/mrmaxguns/wonderwordsmodule)](https://github.com/mrmaxguns/wonderwordsmodule/network)
[![GitHub stars](https://img.shields.io/github/stars/mrmaxguns/wonderwordsmodule)](https://github.com/mrmaxguns/wonderwordsmodule/stargazers)
[![GitHub license](https://img.shields.io/github/license/mrmaxguns/wonderwordsmodule)](https://github.com/mrmaxguns/wonderwordsmodule/blob/master/LICENSE)

Latest version: v1.1.9

Welcome to the readme. Here you can find basic info about what wonderwords is about.

Wonderwords is an open source project and python package that helps python developers add random words and sentences to their programs. Wonderwords has multiple functions which return random words, lists of random words and even random sentences. Please make sure to check out our full documentation at https://github.com/mrmaxguns/wonderwordsmodule/wiki/Wonderwords-Documentation.

Wonderwords has a command line interface and python API which are both installed together through PyPI (see below).


***
## Table of Contents
* [Requirements](#Requirements)
* [Installation](#Installation)
* [Importing Wonderwords](#Import)
* [Command line interface](#Commandline)
* [API Usage](#API)
* [License](#License)
* [Contribution](#Contribution)
* [Usage documentation and sub-modules](#Documentation)


***
## Requirements
Wonderwords requires:
* At least python 3.6
* The [random](https://docs.python.org/3/library/random.html) package (usually installed with python)
* [importlib_resources](https://pypi.org/project/importlib-resources/) **OR** [importlib.resources](https://pypi.org/project/importlib/)


***
## Installation
**Please make sure you have met all of the requirements before installing the package**

Since wonderwords is still experimental, you can only download this package from [Test Pypi](https://test.pypi.org).

All the installation files can be found at https://test.pypi.org/wonderwords-mrmaxguns/.

To install from the command line, use pip:
```
pip install wonderwords
```

To install the latest version (if above fails):
```
pip install wonderwords==1.1.9
```

Please contact @mrmaxguns if you have trouble installing wonderwords.

***
## Import
Please make sure you have installed wonderwords before importing it. To import wonderwords, use the following syntax:
```python
import wonderwords
```
If an error occurs make sure you have installed wonderwords and that you do not have a python program also called wonderwords in the working directory.

***

## Commandline
Here is the basic command line usage for wonderwords. (Make sure to have it installed from Pypi)

Usage:
```
usage: wonderwords [-h] [-n] [-v] [-a] [-min MIN] [-max MAX] [-amount AMOUNT]
                   [-sep SEP] [-s] [-sw SW] [-stype STYPE]
                   mode
```

### Positional arguments
To user wonderwords you first specify the positional argument mode. There are three options:
* **rw**: to generate random words
* **rl**: to generate a list of random words
* **rs**: to generate a random sentence

For example:
```
$ wonderwords rw
unarmed
```

### Optional arguments
Here are optional arguments you can add to enhance the generation of random words, lists and sentences:
#### Optional arguments for rw mode:
If none of the optional arguments for this mode are specified, using the mode will generate a random word from a list of nouns, verbs and adjectives. The arguments below can enhance the generation of the word. For example:

Generate a noun or verb with a minimum length of four chatacters and a maximum length of ten characters.
```
$ wonderwords rw -n -v -min 4 -max 10
variation
```

**Specify parts of speech:**

When none of the part of speech options below are chosen, all parts of speech will be generated. If one or more of these part of speech arguments are used, only words of the specified parts of speech will be generated.
* **-n**: Include nouns.
* **-v**: Include verbs.
* **-a**: Include adjectives.

**Specify length of words:**

Here you can specify the minimum length of the random word, maximum length or both.
* **-min MIN**: The minimum length of the word. Ex: `-min 4` will give a word at least four letters long.
* **-max MAX**: The maximum length of the word. Ex: `-max 7` will give a word with at most 7 letters

**Specify what the word starts with:**
* **-sw SW**: Type one letter that the word starts with. Ex: `-sw a` will generate a word that starts with `a`

#### Optional arguments for rl mode
rl mode generates a python list of random words. However you can customize the word types, lengths and separators between the words in the list. For example:

Generate a list of 5 adjectives separated by `,` and with spaces after each `,`:
```
$ wonderwords rl -amount 5 -a -sep , -s
fearless, yellow, slow, belligerent, shy
```

**Specify the amount of words in the list:**
* **-amount AMOUNT**: The amount of words you want in the random list. Ex: `-amount 5` will return a list of 5 words.

**Specify the separators in-between words in the list:**
* **-sep SEP**: What you want in-between words in the list. Ex: `-sep " & "` will separate all words in the list with `&`. *Keep in mind the spaces or else the & will be squished between the words like&so*.
* **-s**: add a space after the separator. Ex: `wonderwords rl -amount 2 -sep "," -s` will return this: `stomach, red`. Notice the space in between the `,` and `r`.

**Specify parts of speech:**

When none of the part of speech options below are chosen, all parts of speech will be generated. If one or more of these part of speech arguments are used, only words of the specified parts of speech will be generated.
* **-n**: Include nouns.
* **-v**: Include verbs.
* **-a**: Include adjectives.

**Specify length of words:**

Here you can specify the minimum length of the random word, maximum length or both.
* **-min MIN**: The minimum length of the word. Ex: `-min 4` will give a word at least four letters long.
* **-max MAX**: The maximum length of the word. Ex: `-max 7` will give a word with at most 7 letters

#### Optional arguments for rs mode
There is only one optional argument for rs mode (more to come!) that specifies the type of sentence:

* **-stype STYPE**: `-stype` will specify the type of sentence to generate. Look below for options.

**Options for -stype:**
* **bb**: Will generate a bare bone sentence in the form of: `The [noun] [verb]s`
* **ss**: Will generate a simple sentence in the form of `The [noun] [verb]s [direct object]`
* **bba**: Will generate a bare bone sentence with an adjective in the form of `The [adjective] [noun] [verb]s`
* **s**: Will generate a sentence in the form of `The [adjective] [noun] [verb]s [direct object]`

## API
For full usage instructions please visit the [documentation](https://github.com/mrmaxguns/wonderwordsmodule/wiki/Wonderwords-Documentation).

Here is a simple demonstration of the wonderwords python api. However more optional parameters exist that can be found in the documentation. (see above)
```python
from wonderwords import random_word
from wonderwords import random_sentence

rw = random_word.random_word()
rs = random_sentence.random_sentence()

# Get a random word
rw.word()

# Get a list of 5 random words
rw.words_list(5)

# Get a word that starts with c
rw.starts_with('c')

# Get a random bare-bone sentence
rs.bare_bone_sentence()

# Get a random bare-bone sentence with a direct object
rs.simple_sentence()

# Get a random bare-bone sentence with an adjective
rs.bare_bone_with_adjective()

# Get a random sentence with a subject, predicate, direct object and adjective
rs.sentence()
```

***
## License
[MIT license](https://choosealicense.com/licenses/mit/).

***
## Contribution
If you want to contribute to this project, please check out [CONTRIBUTING.md](https://github.com/mrmaxguns/wonderwordsmodule/blob/master/CONTRIBUTING.md). Please email [mrmaxguns@gmail.com](mailto:mrmaxguns@gmail.com) for any questions regarding contribution.

***
## Documentation
To visit the official documentation please visit: https://github.com/mrmaxguns/wonderwordsmodule/wiki/Wonderwords-Documentation
