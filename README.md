# Welcome To Wonderwords
[![GitHub issues](https://img.shields.io/github/issues/mrmaxguns/wonderwordsmodule)](https://github.com/mrmaxguns/wonderwordsmodule/issues)
[![GitHub forks](https://img.shields.io/github/forks/mrmaxguns/wonderwordsmodule)](https://github.com/mrmaxguns/wonderwordsmodule/network)
[![GitHub stars](https://img.shields.io/github/stars/mrmaxguns/wonderwordsmodule)](https://github.com/mrmaxguns/wonderwordsmodule/stargazers)
[![GitHub license](https://img.shields.io/github/license/mrmaxguns/wonderwordsmodule)](https://github.com/mrmaxguns/wonderwordsmodule/blob/master/LICENSE)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/mrmaxguns/wonderwordsmodule)

Latest version: v1.0.5

Welcome to the readme. Here you can find basic info about what wonderwords is about.

Wonderwords is an open source project and python package that helps python developers add random words and sentences to their programs.
Wonderwords has multiple functions which return random words, lists of random words and even random sentences.
Please make sure to check out our full documentation at https://github.com/mrmaxguns/wonderwordsmodule/wiki/Wonderwords-Documentation.


***
## Table of Contents
* [Requirements](#Requirements)
* [Installation](#Installation)
* [Importing Wonderwords](#Import)
* [Basic Usage](#Usage)
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
pip install -i https://test.pypi.org/simple/ wonderwords-mrmaxguns
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
## Usage
For full usage instructions please visit the [documentation](https://github.com/mrmaxguns/wonderwordsmodule/wiki/Wonderwords-Documentation).
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
If you want to contribute to this project, please contact @mrmaxguns (https://www.github.com/mrmaxguns). If you have any ideas or problems, we suggest you open an issue or contact us. We value support from the community, so please speak up.

***
## Documentation
To visit the official documentation please visit: https://github.com/mrmaxguns/wonderwordsmodule/wiki/Wonderwords-Documentation
