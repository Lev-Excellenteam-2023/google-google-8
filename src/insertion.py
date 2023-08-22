import string
from dataclasses import dataclass
import trie
import os
from dataclasses import dataclass


@dataclass
class SentenceInfo:
    sentence: str
    source: str
    offset: int


def remove_not_letters(input_string):
    """
    return the input string without punctuation
    :param input_string:
    :return: string without no-letters
    """
    string_with_only_letters = ''
    for letter in input_string:
        if ('a' <= letter <= 'z') or ('A' <= letter <= 'Z') or letter == ' ':
            string_with_only_letters += letter
    return string_with_only_letters


def insert_to_file_dict(file_path: str, file_content_list: list, count_uid: int) -> dict:
    """
    insert the lines of the file into a dictionary that the keys are uid of the line
    and the values are tuples of the file path and the sentence itself
    :param file_path: the file path
    :param file_content_list: list of all the lines to insert to the dictionary
    :param count_uid: the next uid of line to use
    :return the dictionary and the uid of the next line:
    """
    dict_of_lines_in_file = {}
    count_lines = 0
    for i, sentence in enumerate(file_content_list):
        dict_of_lines_in_file[count_uid] = SentenceInfo(sentence, file_path, i)
        count_uid = count_uid + 1
        count_lines += 1
    return dict_of_lines_in_file


def insert_to_tree(file_content_list: list, trie_tree_of_all_words: trie.Trie, count_uid: int) -> (trie.Trie, int):
    """
    insert the words from the file to trie tree

    :param file_content_list: list of all the lines to insert its words to the trie tree
    :param trie_tree_of_all_words: trie tree to insert the words to
    :param count_uid: the next uid of line to use
    :return the trie tree and the uid of the next line:
    """

    list_without_punctuation = [remove_not_letters(line) for line in file_content_list]
    for line in list_without_punctuation:
        words = line.split()
        for index, word in enumerate(words):
            if trie_tree_of_all_words.search(word) is None:
                dic_of_word = {count_uid: [index]}
                trie_tree_of_all_words.insert(word, dic_of_word)
            else:
                if count_uid in trie_tree_of_all_words.search(word).dict:
                    trie_tree_of_all_words.search(word).dict[count_uid].append(index)
                else:
                    trie_tree_of_all_words.search(word).dict[count_uid] = [index]
        count_uid = count_uid + 1
    return trie_tree_of_all_words, count_uid


def insert(file_paths: list) -> (dict, trie.Trie):
    """
    insert all the words in all the files into the trie tree and all the lines into the dictionary
    that its keys are the uid of the lines and its values are tuples of the file path and the sentence itself

    :param file_paths:list of file paths
    :return:the dictionary of all sentences and the tree of all words
    """

    dict_of_all_sentences = {}
    trie_of_all_words = trie.Trie()
    count_id = 1
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content_list = file.readlines()
        sentence_dict = insert_to_file_dict(file_path, file_content_list, count_id)
        count_id += len(sentence_dict)
        dict_of_all_sentences = sentence_dict | dict_of_all_sentences
    count_id = 1
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content_list = file.readlines()
        trie_of_all_words, count_id = insert_to_tree(file_content_list, trie_of_all_words, count_id)
    return dict_of_all_sentences, trie_of_all_words


def main(path="Archive1"):
    path_list = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            path_list.append(os.path.join(subdir, file))
    return insert(path_list)


if __name__ == "__main__":
    main()
