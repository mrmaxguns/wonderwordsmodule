# flake8: noqa
from .random_word import RandomWord, NoWordsToChoseFrom, Defaults, WordList
from .random_sentence import RandomSentence

__author__ = "Maxim Rebguns"
__copyright__ = "Copyright 2024, Maxim Rebguns"
__credits__ = ["Maxim Rebguns"]
__license__ = "MIT"
__maintainer__ = "Maxim Rebguns"
__email__ = "mrmaxguns@gmail.com"
__status__ = "Production"

try:
    from ._version import version as __version__  # type: ignore
    from ._version import version_tuple  # type: ignore
except ImportError:
    __version__ = "unknown version"
    version_tuple = (0, 0, "unknown version")
