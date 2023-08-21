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
    :return: Dictionary: key = id of the sentence, value = list of the positions in the sentence where the word is found.
    """
    # dict1={1:"what yo do good do",2:"what the time to sleep"}
    try:
        return trie_tree.search(word).dict
    except:
        return None

def find_in_dict(sid:int)-> insertion.SentenceInfo:
    return dict_del[sid]

def get_word_corrections(word: str) -> list:
    possible_corrections = []
    for ch in range(ord('a'), ord('z') + 1):
        letter = chr(ch)
        possible_corrections.append(word + letter)

    for i in range(len(word)):
        possible_corrections.append(word[:i] + word[i + 1:])
        for ch in range(ord('a'), ord('z') + 1):
            letter = chr(ch)
            possible_corrections.append(word[:i] + letter + word[i + 1:])
            possible_corrections.append(word[:i] + letter + word[i:])

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
            list_sugwst=search_suggestion(words)
            if list_sugwst!=[]:
                comleate_sentences[" ".join(change_words)] = search_suggestion(words)
    return comleate_sentences

def compare_func(x, y):
    if x.score>y.score:
        return 1
    elif x.score<y.score:
        return -1
    else:
        if x.completed_sentence>y.completed_sentence:
            return 1
        elif x.completed_sentence<y.completed_sentence:
            return -1
        return 0


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
        sentence=find_in_dict(sid)
        completed_sentence=sentence.sentence
        source_text=sentence.source
        offset=sentence.offset
        score = len(prefix) * 2
        auto_complete.append(AutoCompleteData(completed_sentence, source_text, offset, score))

    if len(list_sid) < NUM_OF_COMPLETIONS:
        correction = correction_to_input(words)
        for correct_word in correction:
            for sid in correction[correct_word]:
                sentence = find_in_dict(sid)
                completed_sentence = sentence.sentence
                source_text = sentence.source
                offset = sentence.offset
                score = score_completion(prefix, correct_word)
                auto_complete.append(AutoCompleteData(completed_sentence, source_text, offset, score))
    # It should be changed so that it returns the first five according to the ABC
    auto_complete.sort(reverse=True, key=lambda x: x.score)
    # auto_complete = sorted(auto_complete, key=cmp_func(compare_func))
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
        if intersection_dict == {} or intersection_dict==None:
            return []
        ans_dict = search_word_in_tree(word)  # Running time = as long as the word
        if ans_dict == {} or ans_dict==None:
            return []
        common_sid = intersection_dict.keys() & ans_dict.keys()
        new_intersection_dict = {}
        for sid in common_sid:
            for i in intersection_dict[sid]:
                num = finding_follower_number(i, ans_dict[sid])
                if num != -1:
                    if sid in new_intersection_dict.keys():
                        new_intersection_dict[sid].append(num)
                    else:
                        new_intersection_dict[sid] = [num]
        intersection_dict = new_intersection_dict
    return list(intersection_dict.keys())

def main(path="Archive1"):
    global trie_tree
    global dict_del
    path_list = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            path_list.append(os.path.join(subdir, file))
    dict_del, trie_tree = insertion.insert(path_list)
    print("dict_del")
    print(dict_del)
    print("search_word_in_tree()")
    # print(search_word_in_tree("documentation")) #work
    # print(search_suggestion(["documentation", "home", "documentation"]))

    print("get_best_k_completions()")
    l=get_best_k_completions("adocumentation home")
    print(l)
    print("get_best_k_completions()")

    # print(search_suggestion)


if __name__ == "__main__":
    main()
