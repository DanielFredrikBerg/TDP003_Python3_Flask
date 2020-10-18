import sys
import os
import re

def load_wordlist(wordlist_file)-> set:
    """Makes a set of a '\n' separated wordlist file."""
    with open(str(wordlist_file), 'r') as data_file:
        content = data.read()
        wordlist = content.split('\n')
    return set(wordlist)
    

def is_english(word, word_list)-> bool:
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


def unknown_words_to_file(file_path, wordlist):
    """Writes words from 'file_path' not in wordlist to 'file_path.txt)"""
    unknown_words = set()
    with open(str(file_path), 'r') as file_:
        file_words = re.findall(r'\S+', str(file_.read()))
        for word in file_words:
            if not is_english(word, wordlist):
                unknown_words.add(word)
    if len(unknown_words) > 0:
        with open(''.join(str(file_path), '_words.txt'), 'w') as file_:
            file_.write(unknown_words)
    return 0
                                 
def main():
    w_list  = sys.argv[1]
    folder = sys.argv[2]
    eng_set = load_wordlist(w_list)
    
    
