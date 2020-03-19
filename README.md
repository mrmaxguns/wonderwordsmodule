# Wonderwords
[![GitHub license](https://img.shields.io/github/license/mrmaxguns/wonderwordsmodule)](https://github.com/mrmaxguns/wonderwordsmodule/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/mrmaxguns/wonderwordsmodule)](https://github.com/mrmaxguns/wonderwordsmodule/stargazers)

Wonderwords is a python library for dealing with getting words in the english language.

## Installation
Currently only on Test Pypi: https://test.pypi.org/project/wonderwords-mrmaxguns/#description
```shell script
pip install -i https://test.pypi.org/simple/ wonderwords-mrmaxguns
```

## Usage
```python
from wonderwords import random_word

ww = random_word()

#Get a random word
random_word = ww.word()

#Get a list of 5 random words
list_of_words = ww.words_list(5)

#Get a random word that starts with the letter a
random_a_word = ww.starts_with('a')
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
