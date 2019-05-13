import re

wiki = open("bahan.txt", "r")
teks = wiki.read()
wiki.close()

print(re.findall(r'me\w+', teks.lower()))
