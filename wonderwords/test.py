import random
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

test = pkg_resources.open_text('wonderwords', 'words.txt').readlines()

# Strip all newlines from the words
words_newline_stripped = []
for w in test:
    words_newline_stripped.append(w.rstrip())

print(random.choice(words_newline_stripped))