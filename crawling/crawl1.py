# 2021.02.09_crawl1.py

import re

file = open("index.html", "r", encoding = "utf-8")
read = file.read()
print(read)

pattern = re.compile(r"<title>(?P<text>.*)</title>")
match = pattern.search(read)
print(match.group("text"))

pattern = re.compile(r"<li>(?P<litext>.*)</li>", re.MULTILINE)
matchs = pattern.finditer(read)
rows = []
for match in matchs:
   #print(match.group("litext"))
    rows.append(match.group("litext"))
print(rows)