#!/usr/bin/python3
import sys
import os
import re


   

def is_english(word, word_list):
    """Checks if word is in word_list"""
    return word in word_list

def load_wordlist(wordlist_file):
    """Makes a set of a '\n' separated wordlist file."""
    with open(str(wordlist_file), 'r') as data_file:
        content = data_file.read()
        wordlist = content.split('\n')
    return set(wordlist)


def files_in_dir(top_dir, end):
    """Returns list of path of files with ending end in top_dir and all subdirs."""
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
        with open(''.join((str(file_path.strip('.')[0]), '_words.txt')), 'w') as file_:
            file_.write(str(unknown_words))
    return 0
                                 
def main():
    print("Loading variables.")
    w_list = sys.argv[1]
    file_or_dir = sys.argv[2]
    eng_set = load_wordlist(w_list)
    print("Defining file or directory")
    if os.path.isfile(file_or_dir):
        file_ = file_or_dir
    elif os.path.isdir(file_or_dir):
        dir_ = file_or_dir
    else:
        print('Neither file nor dir')
        exit()

    if file_:
        print("Scanning file: ", file_)
        unknown_words_to_file(file_, eng_set)
    elif dir_:
        print("Scanning directory: ", dir_)
        for files in files_in_dir(dir_, '.py'):
            unknown_words_to_file(files, eng_set)

if __name__ == '__main__':
    main()
else:
    print('Running as module')
    
    
