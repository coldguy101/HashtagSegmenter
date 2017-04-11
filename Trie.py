# This trie will allow the algorithm to go word by word and form groupings of words so it can
# choose the grouping which contains the least words.


class Trie:
    trie = dict()
    _end = '_end_'

    def __init__(self):
        print "hello"

    def make_trie(self, words):
        root = dict()
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[self._end] = self._end
        self.trie = root

    def in_trie(self, word):
        current_dict = self.trie
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return False
        else:
            if self._end in current_dict:
                return True
            else:
                return False

    def save(self):
        return None

    def load(self, path):
        return None
