class TrieNode:
    # Trie node class
    def __init__(self):
        self.children = [None] * 26
        self.dict=None


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        return ord(ch.lower()) - ord('a')

    def insert(self, word:str,dictionary_of_word:dict):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        word=word.lower()

        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.dict = dictionary_of_word



    def search(self, word:str):
        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        word = word.lower()

        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])
            if not pCrawl.children[index]:
                return None
            pCrawl = pCrawl.children[index]

        if pCrawl.dict!=None:
            return pCrawl
        return None

