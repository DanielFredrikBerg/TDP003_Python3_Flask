#!/usr/bin/python3
import sys
import os
import re


def load_wordlist(wordlist_file):
    """Makes a set of a '\n' separated wordlist file."""
    with open(str(wordlist_file), 'r') as data_file:
        content = data_file.read()
        wordlist = content.split('\n')
    return set(wordlist)


def is_english(word, word_list):
    """Checks if lower case word is in word_list"""
    return word.lower() in word_list


def files_in_dir(top_dir, end):
    """Returns list of path of files with ending end in top_dir and all subdirs."""
    path_list = []
    for root, dirs, files in os.walk(str(top_dir)):
        for file_ in files:
            if file_.endswith(str(end)):
                path_list.append(os.path.join(root, file_))
    return path_list


def unknown_words_to_file(file_path, wordlist, save_dir=None):
    """Writes words from 'file_path' not in wordlist to '_uwords_file_path.txt)"""
    unknown_words = set()
    with open(str(file_path), 'r') as file_:
        file_words = re.findall('[a-zA-Z]+', str(file_.read()))
        print(file_words)
        for word in file_words:
            if not is_english(word, wordlist):
                unknown_words.add(word)
    print("unknown word: ", unknown_words)
    if len(unknown_words) > 0:
        with open(''.join(('_uwords_', os.path.basename(file_path).split('.')[0] + '.txt')), 'w') as file_:
            file_.write(str(file_path) + '\n\n' + str(unknown_words))
    else:
        print("No unknown words in file: ", file_path)
    return 0

def create_uword_dir(path=os.getcwd()):
    """Creates directory in current working directory."""
    try:
        os.mkdir(os.path.join(str(path), 'uword_directory/'))
    except FileExistsError:
        print("uword directory already exists")


def main():
    print("Loading variables.")
    w_list = sys.argv[1]
    file_or_dir = sys.argv[2]
    eng_set = load_wordlist(w_list)
    create_uword_dir()
    print("Checking file or directory")
    if os.path.isfile(file_or_dir):
        print("Scanning file: ", file_)
        unknown_words_to_file(file_or_dir, eng_set)
    elif os.path.isdir(file_or_dir):
        print("Scanning directory: ", file_or_dir)
        for files in files_in_dir(file_or_dir, '.py'):
            unknown_words_to_file(files, eng_set)
    else:
        print('Argument is neither file nor dir')
        exit()

if __name__ == '__main__':
    main()
else:
    print('Running as module')
    
    
