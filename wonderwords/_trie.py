"""An incomplete trie implementation used
to efficiently find words with a given prefix
or suffix.
"""

from dataclasses import dataclass


@dataclass
class TrieNode:
    end_of_word: bool
    children: dict


class Trie:
    def __init__(self, words=None):
        self.root = self._new_node()

        if words is not None:
            for word in words:
                self.insert(word)

    def insert(self, word):
        current_node = self.root
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                current_node.children[letter] = self._new_node()
                current_node = current_node.children[letter]
        current_node.end_of_word = True

    def query_characters(self, characters):
        current_node = self.root
        for character in characters:
            if character in current_node.children:
                current_node = current_node.children[character]
            else:
                return
        return current_node

    def get_words_that_start_with(self, characters):
        trunk = self.query_characters(characters)
        if trunk is None:
            return set()
        return self.get_words_from_branch(trunk, characters)
    
    def get_words_from_branch(self, branch, word_fragment):
        words = set()

        if branch.end_of_word:
            words.add(word_fragment)

        for character, data in branch.children.items():
            if data.end_of_word:
                words.add(word_fragment + character)
            
            if data.children:
                words = words | self.get_words_from_branch(data, word_fragment + character)

        return words

    def _new_node(self):
        return TrieNode(end_of_word=False, children={})
