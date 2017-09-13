#!/usr/bin/python3
# Converts markdown to formatted html
# mdhtml.py readme.md -> readme.html

import sys
import os
import markdown
import argparse
# from bs4 import BeautifulSoup as bsoup

# Argparse

parser = argparse.ArgumentParser(description="Convert mardown to html. Supports tables, codeblocks, linebreaks, table of contents.")

parser.add_argument('-s', '--stylized',
                    action='store_true',
                    help='Prepend a default css dark theme to the html')

md_in = parser.add_mutually_exclusive_group()
md_in.add_argument('--stdin',
                   action='store_false',
                   default=False,
                   help='read markdown from stdin and output html to stdout, useful for piping')
md_in.add_argument('-f', '--infile',
                   help='(default) read from file and convert it to html file with same name')

html_out = parser.add_mutually_exclusive_group()
html_out.add_argument('--stdout',
                      action='store_true',
                      default=False,
                      help='output html to stdout')
html_out.add_argument('-o', '--outfile',
                      action='store_true',
                      help='(default) write html to file. Takes the file name and appends .html extension. Caution, will overwrite existing file.')

args = parser.parse_args()
# print(args)

# Read

content_md = ""

if args.stdin:
    content_md = sys.stdin.read()
elif args.infile is not None:
    file_md = args.infile
    if not os.path.isfile(file_md):
        sys.exit("File doesn't exist: " + file_md)
    with open(file_md) as file:
        content_md = file.read()
else:
    sys.exit('No markdown file specified')

# Process content

prefix = 'markdown.extensions.'
ext = ['tables', 'fenced_code', 'nl2br', 'toc']
content_html = markdown.markdown(content_md, extensions=[prefix + e for e in ext])

# Formatting

# content_html = bsoup(content_html, 'lxml').prettify()
content_html += '\n'  # EOF newline

if args.stylized:
    with open(sys.path[0] + '/style.css') as f:
        css = f.read()
    css = '<style type="text/css">\n{}</style>\n'.format(css)
    content_html = css + content_html

# Write

if args.stdout:
    # Doesn't seem to work for xclip
    sys.stdout.writelines(content_html)
    sys.stdout.flush()
else:
    file_html = os.path.splitext(file_md)[0] + '.html'
    with open(file_html, 'w') as file:
        file.write(content_html)
    # args.infile.close()
