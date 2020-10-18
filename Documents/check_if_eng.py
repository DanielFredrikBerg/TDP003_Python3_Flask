import sys
import os

def load_wordlist(wordlist_file)-> set:
    """Makes a set of a '\n' separated wordlist file."""
    with open(str(wordlist_file), 'r') as data_file:
        content = data.read()
        wordlist = content.split('\n')
    return set(wordlist)
    

def if_english(word, word_list)-> bool:
    """Checks if word is in word_list"""
    return word in word_list


def files_in_dir(top_dir, end):
    """Returns list of path of files with ending end \
    in top_dir and all subdirs."""
    path_list = []
    for root, dirs, files in os.walk(str(top_dir)):
        for file_ in files:
            if file_.endswith(str(end)):
                path_list.append(os.path.join(root, file_))
    return path_list



                                 
def main():
    w_list  = sys.argv[1]
    folder = sys.argv[2]
    eng_set = load_wordlist(w_list)
    
    
