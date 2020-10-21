#!/usr/bin/python3

import sys
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

def jinja2_parser(path):
    env = Environment(
        loader=FileSystemLoader(str(path)),
        autoescape=select_autoescape(['html'])
    )
    templates = [x for x in env.list_templates() if x.endswith('.html')]
    for template in templates:
        t = env.get_template(template)
        env.parse(t)
    return 0

def main():
    print(jinja2_parser(sys.argv[1]))

if __name__ == '__main__':
    main()

