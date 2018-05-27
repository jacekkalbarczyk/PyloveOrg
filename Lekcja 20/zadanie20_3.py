import re

with open('20_2.txt', 'r', encoding='utf-8') as file:
    found = re.findall(r"(\d{4}.\d{2}.\d{2}) - (.+)( - (.+))\n", file.read())
    print(found)