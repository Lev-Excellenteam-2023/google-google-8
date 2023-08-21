from typing import List

from AutoCompleteDataClass import AutoCompleteData

def search_word_in_tree(word: str) -> dict:
    """
    The function searches for a word in the tree and returns a dictionary.
    :param word: The word you are looking for in the tree.
    :return: Dictionary: key = id of the sentence, value = list of the positions in the sentence where the word is found.
    """
    return {}


def finding_sentences_by_id(lt: list) -> list:
    """
    The function searches the dictionary for all sentences whose key is in the list of the sid
    :param lt: List of sid of sentences.
    :return:
    """
    return []


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

# ההפונקציה שתמר ממשת
def curect_word(word:str)->list:
    return []

def curect_sentence(words:list)->list:
    """
    The function receives a list of words and tries to correct each of the words to return a list of suggestions to complete the sentence.
    :param words: The list of words the user entered.
    :return: sid list of sentences
    """
    list_comleate_sentences=[]
    for i,word in enumerate(words):
        word_curects=curect_word(word)
        for try_word in word_curects:
            words[i]=try_word
            list_comleate_sentences=list_comleate_sentences+search_suggestion(words)
    return list_comleate_sentences




def get_best_kֵ_completions(prefix: str) -> List[AutoCompleteData]:
    """

    :param prefix:
    :return:
    """
    words=prefix.split()
    list_sid=search_suggestion(words)
    if len(list_sid)<5:
        list_sid=list_sid+curect_sentence(words)




    return []


def search_suggestion(words: List) -> List:
    """
    The function receives the input string, separates it into words and searches for every word in the tree.
    :param input_user: The input we received from the user - the words for which we want to find completion.
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
