#!/usr/bin/python3
# Converts markdown to formatted html
# mdhtml.py readme.md -> readme.html

import sys
import os
import markdown
import argparse
# from bs4 import BeautifulSoup as bsoup

# Argparse

parser = argparse.ArgumentParser(description='Convert mardown to html, supports tables, codeblocks, linebreaks, table of contents')

parse_src = parser.add_mutually_exclusive_group()
parse_src.add_argument('--stdin', dest='readfile', action='store_false', help='(default) read markdown from stdin and output html to stdout, useful for piping')
parse_src.add_argument('-f', '--file', dest='readfile', action='store', help='read from file and convert it to html file with same name')
parse_src.set_defaults(readfile=False)
args = parser.parse_args()
# print(args)

# Old manual arg processing
# if len(sys.argv) != 2:
#     sys.exit("Specify a markdown file to convert")

# file_md = args.readfile
# if not os.path.isfile(file_md):
#     sys.exit("File doesn't exist:\n" + file_md)


def md2html(content):
    prefix = 'markdown.extensions.'
    ext = ['tables', 'fenced_code', 'nl2br', 'toc']
    content_html = markdown.markdown(content_md, extensions=[prefix + e for e in ext])
    return ""


# Read

content_md = ""

if args.readfile:
    # content_md = args.readfile.read()
    file_md = args.readfile
    if not os.path.isfile(file_md):
        sys.exit("File doesn't exist:\n" + file_md)
    with open(file_md, 'r') as file:
        content_md = file.read()
else:
    # Supposedly:
    # for line in sys.stdin:
    #     content_md += line
    # Seems to work:
    content_md = sys.stdin.read()

# Process content

prefix = 'markdown.extensions.'
ext = ['tables', 'fenced_code', 'nl2br', 'toc']
content_html = markdown.markdown(content_md, extensions=[prefix + e for e in ext])

# Formatting

# content_html = bsoup(content_html, 'lxml').prettify()
content_html += '\n'  # EOF newline

# Write

if args.readfile:
    file_html = os.path.splitext(file_md)[0] + '.html'
    with open(file_html, 'w') as file:
        file.write(content_html)
    # args.readfile.close()
else:
    sys.stdout.write(content_html)
    sys.stdout.flush()
