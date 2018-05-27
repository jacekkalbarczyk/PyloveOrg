import re

with open('wiki_python', 'r', encoding='utf-8') as infile:
    found = re.findall(r"[Pp]ython", infile.read())
    print(len(found))