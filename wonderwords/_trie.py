"""An incomplete trie implementation used
to efficiently find words with a given prefix
or suffix.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Set, Optional, Iterable


@dataclass
class TrieNode:
    end_of_word: bool
    children: Dict[str, TrieNode]


class Trie:
    def __init__(self, words: Optional[Iterable[str]] = None):
        self.root: TrieNode = self._new_node()

        if words is not None:
            for word in words:
                self.insert(word)

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        current_node = self.root
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                current_node.children[letter] = self._new_node()
                current_node = current_node.children[letter]
        current_node.end_of_word = True

    def query_characters(self, characters: str) -> Optional[TrieNode]:
        """Find the trie node matching as many ``characters`` as possible."""
        current_node = self.root
        for character in characters:
            if character in current_node.children:
                current_node = current_node.children[character]
            else:
                return None
        return current_node

    def get_words_that_start_with(self, characters: str) -> Set[str]:
        """Get all words in the trie that start with ``characters``."""
        trunk = self.query_characters(characters)
        if trunk is None:
            return set()
        return self.get_words_from_branch(trunk, characters)

    def get_words_from_branch(self, branch: TrieNode, word_fragment: str) -> Set[str]:
        """Get all words that start with ``word_fragment`` starting from the node ``branch``."""
        words: Set[str] = set()

        if branch.end_of_word:
            words.add(word_fragment)

        for character, data in branch.children.items():
            if data.end_of_word:
                words.add(word_fragment + character)

            if data.children:
                words = words | self.get_words_from_branch(
                    data, word_fragment + character
                )

        return words

    def _new_node(self) -> TrieNode:
        """Create a new empty trie node."""
        return TrieNode(end_of_word=False, children={})
