
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


def search_suggestion(input_user: str) -> list:
    """
    The function receives the input string, separates it into words and searches for every word in the tree.
    :param input_user: The input we received from the user - the words for which we want to find completion.
    :return: A list of all possible completions.
    """
    words = input_user.split()
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
