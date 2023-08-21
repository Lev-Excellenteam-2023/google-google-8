import string
import unittest
import insertion
import trie
from dataclasses import dataclass

file_content_list=['Advanced Bash-Scripting Guide',
'An in-depth exploration of the art of shell scripting',
'Mendel Cooper',
'<thegrendel.abs@gmail.com>',
]

def remove_punctuation(input_string):
    # Make a translation table that maps all punctuation characters to None
    translator = str.maketrans("", "", string.punctuation)

    # Apply the translation table to the input string
    result = input_string.translate(translator)

    return result

class InsertionTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def test_insert_to_tree_function(self):
        trie_tree_of_all_words = trie.Trie()
        trie_tree_of_all_words, _ = insertion.insert_to_tree(file_content_list, trie_tree_of_all_words, 1)
        list_without_punctuation=[remove_punctuation(line) for line in file_content_list]
        for line in list_without_punctuation:
            words=line.split()
            for word in words:
                self.assertIsNotNone(trie_tree_of_all_words.search(word))

    def test_insert_to_dic_function(self):
        dic_of_all_sentences = insertion.insert_to_file_dict("test_file",file_content_list,1)
        for index,line in enumerate(file_content_list):
            assert dic_of_all_sentences[index+1]==insertion.SentenceInfo(line,"test_file",index)









if __name__ == "__main__":
    unittest.main()