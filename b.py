import matplotlib.pyplot as plt
import urllib.request;
import re;

author = "Ian+Goodfellow"
url = "https://arxiv.org/search/?query=" + author + "&searchtype=author&size=200"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')
pattern = '<a href=\"/search/\?searchtype=author[\s\S]*?</a>'
result = re.findall(pattern, html_str)


names = []

print("[ Author: " + author + " ]")
for r in result:
    co = r.split("\">")[1].split("</a>")[0].strip()
    names.append(co)


p = list(set(names))
p.sort()

author_name = author.replace("+"," ")


for g in p:
    if g != author_name:
        print(' %s : %d times' %(g,names.count(g)))


