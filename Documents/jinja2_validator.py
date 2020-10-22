#!/usr/bin/python3

# Copyright 2020, Daniel Huber, All rights reserved.

import sys
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

def jinja2_parser(path):
    """Checks jinja2 syntax. Returns 0 if correct. Raises error TemplateSyntaxError if incorrect."""
    env = Environment(
        loader=FileSystemLoader(str(path)),
        autoescape=select_autoescape(['html'])
    )
    templates = [x for x in env.list_templates() if x.endswith('.html')]
    for template in templates:
        t = env.get_template(template)
        print('Now parsing file: ' + str(template))
        env.parse(t)
    return 0

def main():
    if not jinja2_parser(sys.argv[1]):
        print('Exited without errors')

if __name__ == '__main__':
    main()

