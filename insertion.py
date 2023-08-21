import trie
import os
path = "Archive"
def insert_to_dic(file_path:str,count_uid:int)->(dict,int):
    """
    insert the lines of the file into a dictionary that the keys are uid of the line
    and the values are tuples of the file path and the sentence itself
    :param file_path: the file
    :param count_uid: the next uid of line to use
    :return the dictionary and the uid of the next line:
    """
    with open(file_path, 'r') as file:
        file_content_list = file.readlines()
    dict_of_lines_in_file={}
    for sentence in file_content_list:
        dict_of_lines_in_file[count_uid]=(file_path,sentence)
        count_uid=count_uid+1
    return dict_of_lines_in_file,count_uid

def insert_to_tree(file_path:str,trie_tree_of_all_words:trie.Trie,count_uid:int)->(trie.Trie,int):
    """
    insert the words from the file to trie tree

    :param file_path: the file
    :param trie_tree_of_all_words: trie tree to insert the words to
    :param count_uid: the next uid of line to use
    :return the trie tree and the uid of the next line:
    """
    with open(file_path, 'r') as file:
        file_content_list = file.readlines()
    for line in file_content_list:
        for index,word in enumerate(line):
            dic_of_word = {}
            dic_of_word[count_uid] = []
            dic_of_word[count_uid].append(index+1)
            trie_tree_of_all_words.insert(word,dic_of_word)
        count_uid=count_uid+1
    return trie_tree_of_all_words,count_uid


def insert(file_paths:list)->(dict,trie.Trie):
    """
    insert all the words in all the files into the trie tree and all the lines into the dictionary
    that its keys are the uid of the lines and its values are tuples of the file path and the sentence itself

    :param file_paths:list of file paths
    :return:the dictionary of all sentences and the tree of all words
    """
    dic_of_all_sentences={}
    trie_tree_of_all_words = trie.Trie()
    count_id=1
    for file in file_paths:
        dic,count_id=insert_to_dic(file,count_id)
        dic_of_all_sentences=dic|dic_of_all_sentences
        trie_tree_of_all_words,count_id=insert_to_tree(file,trie_tree_of_all_words,count_id)
    return dic_of_all_sentences,trie_tree_of_all_words

def main():
    dir_list = os.listdir(path)
    return insert(dir_list)

if __name__=="__main__":
    main()


