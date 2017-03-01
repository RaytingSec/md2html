#!/usr/bin/python3
# Converts markdown to formatted html
# mdhtml.py readme.md -> readme.html

import sys
import os
import markdown
# from bs4 import BeautifulSoup as bsoup

# Arg checking

if len(sys.argv) != 2:
    sys.exit("Specify a markdown file to convert")

file_md = sys.argv[1]
if not os.path.isfile(file_md):
    sys.exit("File doesn't exist:\n" + file_md)

# Read

with open(file_md, 'r') as file:
    content_md = file.read()

# Process content

prefix = 'markdown.extensions.'
ext = ['tables', 'fenced_code', 'nl2br', 'toc']
content_html = markdown.markdown(content_md, extensions=[prefix + e for e in ext])

# Formatting

# content_html = bsoup(content_html, 'lxml').prettify()
content_html += '\n'  # EOF newline

# Write

file_html = os.path.splitext(file_md)[0] + '.html'
with open(file_html, 'w') as file:
    file.write(content_html)
