import os
from typing import List
from score import score_completion
from AutoCompleteDataClass import AutoCompleteData
import insertion

# move to const.py
NUM_OF_COMPLETIONS = 5

trie_tree = None
dict_del = {}


def search_word_in_tree(word: str) -> dict:
    """
    The function searches for a word in the tree and returns a dictionary.
    :param word: The word you are looking for in the tree.
    :return: Dictionary: key is id of the sentence,
    value is list of the positions in the sentence where the word is found.
    """
    try:
        return trie_tree.search(word).dict
    except:
        return {}


def find_in_dict(sid: int) -> insertion.SentenceInfo:
    """
    Gets an ID of a statement and returns its value.
    :return:data structure that contains a sentence, source and offset.
    """
    try:
        return dict_del[sid]
    except:
        return None


def get_word_corrections(word: str) -> list:
    """
    Generate list of words from the tree that are possible fixes for the received word
    :param word: word to fix
    :return: list of correction suggestions
    """
    possible_corrections = []

    # append to end
    for ch in range(ord('a'), ord('z') + 1):
        letter = chr(ch)
        possible_corrections.append(word + letter)

    # insert and replace
    for i in range(len(word)):
        possible_corrections.append(word[:i] + word[i + 1:])
        for ch in range(ord('a'), ord('z') + 1):
            letter = chr(ch)
            possible_corrections.append(word[:i] + letter + word[i + 1:])
            possible_corrections.append(word[:i] + letter + word[i:])

    # filter words not in tree
    in_tree_possible_corrections = []
    for word in possible_corrections:
        if search_word_in_tree(word):
            in_tree_possible_corrections.append(word)

    return in_tree_possible_corrections


def finding_follower_number(num: int, lt: list) -> int:
    """
    The function searches for a consecutive number to the number received in the list.
    :param num: A number for which a follower is being sought.
    :param lt: A list in which to search.
    :return: The consecutive number and if there is no consecutive number returns -1
    """
    for i in lt:
        if i == num + 1:
            return i
        elif i > num + 1:
            return -1
    return -1


def correction_to_input(words: list) -> dict:
    """
    The function receives a list of words and tries to correct each of the words.
    :param words: The list of words the user entered.
    :return: A dictionary that the key entered after the correction and the value is a list of all the sid of the auto complete completions.
    """
    complete_sentences = {}
    for i, word in enumerate(words):
        change_words = words
        word_corrections = get_word_corrections(word)
        for try_word in word_corrections:
            change_words[i] = try_word
            list_suggest = search_suggestion(change_words)
            if list_suggest:
                complete_sentences[" ".join(change_words)] = list_suggest
    return complete_sentences


def remove_duplicates(input_list: list) -> list:
    """
    Removes duplicates from list
    :param input_list: list to filter
    :return: list filtered from duplicates
    """
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


def get_best_k_completions(prefix: str) -> List[AutoCompleteData]:
    """
    The function receives input from the user and finds suggestions for completion
    :param prefix:input
    :return: AutoCompleteData
    """
    auto_complete = []
    words = prefix.split()
    list_sid = search_suggestion(words)
    for sid in list_sid:
        sentence = find_in_dict(sid)
        if sentence is not None:
            completed_sentence = sentence.sentence
            source_text = sentence.source
            offset = sentence.offset
            score = len(prefix) * 2
            auto_complete.append(AutoCompleteData(completed_sentence, source_text, offset, score))

    if len(list_sid) < NUM_OF_COMPLETIONS:
        correction = correction_to_input(words)
        for correct_word in correction:
            for sid in correction[correct_word]:
                sentence = find_in_dict(sid)
                if sentence is not None:
                    completed_sentence = sentence.sentence
                    source_text = sentence.source
                    offset = sentence.offset
                    score = score_completion(prefix, correct_word)
                    auto_complete.append(AutoCompleteData(completed_sentence, source_text, offset, score))

    uniq_auto_complete = remove_duplicates(auto_complete)

    # return the first five considering score and alphabet order
    uniq_auto_complete.sort(reverse=True, key=lambda x: x.score)
    top_k = uniq_auto_complete[:NUM_OF_COMPLETIONS]
    i = NUM_OF_COMPLETIONS
    while i < len(uniq_auto_complete) and uniq_auto_complete[i].score == top_k[-1].score:
        top_k.append(uniq_auto_complete[i])
        i += 1
    top_k.sort(reverse=False, key=lambda x: x.completed_sentence)
    return top_k[:NUM_OF_COMPLETIONS]


def search_suggestion(words: List) -> List[int]:
    """
    The function receives a list of string and searches for every word in the tree.
    :param words: The words for which we want to find completion.
    :return: A list of all possible completions. list of sid.
    """
    intersection_dict = search_word_in_tree(words[0])
    words = words[1:]
    for word in words:  # Go through all the words in the input runtime o(the number of words in the input)
        if intersection_dict == {} or intersection_dict is None:
            return []
        ans_dict = search_word_in_tree(word)  # Running time = as long as the word
        if ans_dict == {} or ans_dict is None:
            return []
        # Finding all the sentences that the two words have in common
        common_sid = intersection_dict.keys() & ans_dict.keys()
        new_intersection_dict = {}
        for sid in common_sid:  # Checking that the two words are in consecutive positions in the sentence
            for i in intersection_dict[sid]:
                num = finding_follower_number(i, ans_dict[sid])
                if num != -1:
                    if sid in new_intersection_dict.keys():
                        new_intersection_dict[sid].append(num)
                    else:
                        new_intersection_dict[sid] = [num]
        intersection_dict = new_intersection_dict
    return list(intersection_dict.keys())


def init_system(path):
    """
    Initialize data structures according to given dataset
    :param path: path to dataset
    """
    global trie_tree
    global dict_del
    path_list = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            path_list.append(os.path.join(subdir, file))
    dict_del, trie_tree = insertion.insert(path_list)
