#!/usr/bin/python3
import json
import sys

def test_json(json_string, file_):
    """Prints confirmation if file is correct JSON. Prints error if not."""
    try:
        json.loads(json_string)
        print(str(file_) + ' is valid JSON.')
    except ValueError as v:
        print("Error: " + str(v) + ', ' + str(file_) + ' is not a valid JSON.')

def main():
    with open(str(sys.argv[1]), 'r') as file_:
        content = file_.read()
        test_json(content, sys.argv[1])

if __name__ == '__main__':
    main()
