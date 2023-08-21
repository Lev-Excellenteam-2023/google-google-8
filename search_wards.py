from typing import List
from score import score_completion

from AutoCompleteDataClass import AutoCompleteData

#move to const.py
NUM_OF_COMPLETIONS=5

def search_word_in_tree(word: str) -> dict:
    """
    The function searches for a word in the tree and returns a dictionary.
    :param word: The word you are looking for in the tree.
    :return: Dictionary: key = id of the sentence, value = list of the positions in the sentence where the word is found.
    """
    # dict1={1:"what yo do good do",2:"what the time to sleep"}

    return {}


def finding_sentences_by_id(lt: list) -> list:
    """
    The function searches the dictionary for all sentences whose key is in the list of the sid
    :param lt: List of sid of sentences.
    :return:
    """
    return []


def get_word_corrections(word: str) -> list:
    possible_corrections = []
    for ch in range(ord('a'), ord('z') + 1):
        possible_corrections.append(ch + word)
        possible_corrections.append(word + ch)

    for i in range(len(word)):
        for ch in range(ord('a'), ord('z') + 1):
            possible_corrections.append(word[:i] + ch + word[i + 1:])

    return possible_corrections


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
    comleate_sentences = {}
    for i, word in enumerate(words):
        change_words = words
        word_curects = get_word_corrections(word)
        for try_word in word_curects:
            change_words[i] = try_word
            comleate_sentences[" ".join(change_words)]=search_suggestion(words)
    return comleate_sentences

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
        # After the integration with the data structure, all fields need to be initialized.
        # completed_sentence: str
        # source_text: str
        # offset: int
        score = len(prefix)*2
        auto_complete.append(AutoCompleteData(completed_sentence, source_text, offset, score))

    if len(list_sid) < NUM_OF_COMPLETIONS:
        correction =correction_to_input(words)
        for correct_word,l_sid in correction:
            for sid in l_sid:
                #After the integration with the data structure, all fields need to be initialized.
                # completed_sentence: str
                # source_text: str
                # offset: int
                score = score_completion(prefix, correct_word)
                auto_complete.append(AutoCompleteData(completed_sentence, source_text, offset, score))

    auto_complete.sort(reverse=True,key=lambda x: x.score)
    return auto_complete[:NUM_OF_COMPLETIONS]



def search_suggestion(words: List) -> List[int]:
    """
    The function receives a list of string and searches for every word in the tree.
    :param words: The words for which we want to find completion.
    :return: A list of all possible completions. list of sid.
    """
    intersection_dict = search_word_in_tree(words[0])
    words = words[1:]
    for word in words:  # Go through all the words in the input runtime o(the number of words in the input)
        ans_dict = search_word_in_tree(word)  # Running time = as long as the word
        common_sid = intersection_dict.keys() & ans_dict.keys()
        for sid in common_sid:
            new_intersection_dict = {}
            for i in intersection_dict[sid]:
                num = finding_follower_number(i, ans_dict[sid])
                if num != -1:
                    if sid in new_intersection_dict.keys():
                        new_intersection_dict[sid].append(num)
                    else:
                        new_intersection_dict[sid] = [num]
            intersection_dict = new_intersection_dict
    return finding_sentences_by_id(intersection_dict.keys())
