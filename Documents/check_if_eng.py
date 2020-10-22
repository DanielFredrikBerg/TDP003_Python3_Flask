#!/usr/bin/python3

# Copyright 2020, Daniel Huber, All rights reserved.

import sys
import os
import re


def load_wordlist(word_list_file):
    """Makes a set of a '\n' separated wordlist file."""
    with open(str(word_list_file), 'r') as data_file:
        content = data_file.read()
        word_list = content.split('\n')
    return set(word_list)


def is_english(word, word_list):
    """Checks if lower case word is in word_list"""
    return word.lower() in word_list


def files_in_dir(top_dir, end):
    """Returns list of path of files with ending end in 'top_dir' and all subdirs."""
    path_list = []
    exclude = set(['venv', 'Iosevka'])
    for root, dirs, files in os.walk(str(top_dir)):
        dirs[:] = [dir_ for dir_ in dirs if dir_ not in exclude]
        for file_ in files:
            if file_.endswith(str(end)):
                path_list.append(os.path.join(root, file_))
    return path_list


def unknown_words_to_file(file_path, word_list, save_dir=''):
    """Writes words from 'file_path' not in word_list to 'file_path_uwords_.txt' in dir save_dir. Progress is printed in terminal.)"""
    unknown_words = set()
    with open(str(file_path), 'r') as file_:
        print('Checking file: ' + str(file_path))
        file_words = re.findall('[a-zA-Z]+', str(file_.read()))
        for word in file_words:
            if not is_english(word, word_list):
                unknown_words.add(word)
    #print("unknown words: ", unknown_words)
    if len(unknown_words) > 0:
        with open(''.join((save_dir, os.path.basename(file_path).split('.')[0] + '_uwords_.txt')), 'w') as file_:
            file_.write(str(file_path) + '\n\n' + str(unknown_words))
    else:
        print("No unknown words in file: ", file_path)
    return 0


def create_uword_dir(path=os.getcwd()):
    """Creates uword_directory in current working directory if it does not exist."""
    uword_dir_path = os.path.join(str(path), 'uword_directory/')
    try:
        os.mkdir(uword_dir_path)
        print("Creating uword_directory")
    except FileExistsError:
        print("uword directory already exists")
    finally:
        return uword_dir_path

    
def is_path_valid(path):
    """Check if 'path' is a valid path."""
    return os.path.exists(os.path.join(os.getcwd(), path))

    
def check_uword_of_file_type_in_path(path, word_list, file_type='.py', save_dir='uword_directory'):
    """Writes words from all file/s of 'file_type' on 'path' to 'file_name_uwords_.txt' in 'save_dir' not included in 'word_list'."""
    if os.path.isfile(path):
        print("Scanning file:", path)
        unknown_words_to_file(path, word_list, save_dir)
    elif os.path.isdir(path):
        print("Scanning directory:", path)
        for files in files_in_dir(path, str(file_type)):
            unknown_words_to_file(files, word_list, save_dir)
    print('All files checked.')

def main():
    print("Loading variables.")
    w_list = sys.argv[1]
    path = sys.argv[2]
    eng_set = load_wordlist(w_list)

    uword_dir = create_uword_dir()
    
    print("Checking valid path")
    if is_path_valid(path):
        check_uword_of_file_type_in_path(path, eng_set, file_type='.py', save_dir=uword_dir)
        print("Done")
    else:
        print('Error: ' + str(sys.argv[2]) + ' is neither file nor directory.')
        exit()

        
if __name__ == '__main__':
    print("First argument is this file.\n\
Second argument is the word list to be used.\n\
Third argument is the path, either file or dir, to be checked.")
    main()
else:
    print('Running as module')
    
    
