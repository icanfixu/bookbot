
def get_num_words(file_contents):
    return len(file_contents.split())

def get_num_chars(file_contents):
    char_dic = {}
    for i in file_contents.lower():
        if char_dic.get(i) == None:
            char_dic[i] = 1
        else:
            char_dic[i] += 1
    return char_dic

def get_dic_char(char_dic):
    l_dic = []
    for k,v in char_dic.items():
        l_dic.append({"char":k,"num":v})

    l_dic.sort(reverse = True, key = lambda x : x["num"])
    
    return l_dic