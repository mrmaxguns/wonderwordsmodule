# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
since version 2.

## [Unreleased]

### Added

- Added `CHANGELOG.md`.
- Added custom word categories.
- The Rich library is now an optional dependency.
- Bumped dependency version numbers.
- Added a list of profanities.
- Refactored code.
- Removed profanities by default.
- Added singular forms of categories as default such as "noun" instead of
  "nouns".

### Changed

- Changed the implementation behind the scenes. Now, word lists are loaded once
  and reused between instances of the `RandomWord` class. This is more
  efficient.
- Changed the implementation of `RandomSentence` to make up for the changes in
  `RandomWord`.
- `RandomWord.parts_of_speech` will soon be deprecated.
- The `include_parts_of_speech` argument for RandomWord methods will soon be
  deprecated. The alternative is now `include_categories`.

## [2.1.0] - 2020-09-11

### Added

- Added the regex word matcher for both the CLI and the `RandomWord` class.
- Added "Prerequisites" section to the install page.
- Added sphinx-copybutton to the documentation so that it is easy to copy code
  snippets.

### Fixed

- Fixed incorrect code snippet in docstring.
- Fixed broken link in documentation.


## [2.0.1] - 2020-09-10

### Fixed

- Added dependencies to `setup.py` (somehow completely forgot), fixing the
  dependency issue.
- Fixed incorrect commands in the CLI documentation.
- Fixed broken link in the CLI.


## [2.0.0] - 2020-09-09

### Changed

- Refactored the `RandomSentence` class (usage stays the same) in order to be
  more modular by introducing the `_present_tense` function.

### Fixed

- Reconfigured Readthedocs settings in order for autodoc to work.


## [2.0.0-alpha] - 2020-09-09

### Added
- The `RandomWord` class which offers:
  - Random word filtering by starting and ending letters, parts of speech, and
    lengths.
  - The `filter` method for filtering words.
  - The `random_words` method to get a list of words.
  - The `word` method to generate a random word.
- The `RandomSentence` method to generate random sentences (same as
  `random_sentence` class in previous release).
- A documentation on Readthedocs.

### Changed
- Changed the command line interface to be more efficient and styled it with the
  help of Rich.

### Removed
- The `random_word` class (wasn't pep 8 compliant, older functionality was
  refactored into the `RandomWord` class).
- The `random_sentence` class was removed and renamed to the `RandomSentence`
  class.


## [<1.1.9] - 2020-05-03
### Added
- Simple random word generation.
- Random word list generation.
- Generate random words that start with a letter.
- Random sentence generation.
