#!/usr/bin/python3
import codecs
import sys

def is_utf8(file_name):
    """Checks if file 'file_name' has valid utf-8 encoding."""
    try:
        codecs.open(str(file_name), encoding="utf-8", errors='strict').readlines()
        return str(file_name) + ' is valid utf-8.'
    except UnicodeDecodeError:
        return str(file_name) + ' is invalid utf-8'


def main():
    print(is_utf8(sys.argv[1]))


if __name__ == '__main__':
    main()
else:
    print('Running as module')
    
