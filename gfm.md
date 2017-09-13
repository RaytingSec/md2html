<script src="https://cdn.jsdelivr.net/highlight.js/9.9.0/highlight.min.js"></script>
<link rel="stylesheet" href="./monokai-sublime.css">
<script>hljs.initHighlightingOnLoad();</script>

Markdown Formatting Tester
==============================

[TOC]

## Simple tests

Rich text formatting is useful! This is what a document filled with awesome will look like.

I _said_.... I **said**...

> and I quote...

- First
- Second
- Third
    + Third First
    + Third Second
        * Third Second First
        * Third Second Second
    + Third Third
- Fourth
    + Fourth First

1. One
2. Two
3. Three
4. Four

### This won't work

~~no wait don't do that~~

### Table

|  Len    |  Wid    |  Heig  |
| ------- | ------- | ------ |
|  14.86  |  09.93  |  0.96  |
|  16.38  |  10.85  |  1.35  |

### Newline

10 + 2 * 5
= 10 + 10
= 20

## Code

Code block

```
#!/usr/bin/python3
b = [a for a in range(0,10)]
if b.len() > 1:
    print('b: {}'.format(b))
```

Python code block

```python
#!/usr/bin/python3
b = [a for a in range(0,10)]
if b.len() > 1:
    print('b: {}'.format(b))
```
