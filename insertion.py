def insert_to_dic(file_path:str):
    with open(file_path, 'r') as file:
        file_content_list = file.readlines()
    dict_of_lines_in_file={}
    count_of_uid=1
    for sentence in file_content_list:
        dict_of_lines_in_file[count_of_uid]=sentence
        count_of_uid=count_of_uid+1
    return dict_of_lines_in_file

def insert_to_tree(file_path:str):
    with open(file_path, 'r') as file:
        file_content_list = file.readlines()



