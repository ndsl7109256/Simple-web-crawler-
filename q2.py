import matplotlib.pyplot as plt
import urllib.request;
import re;

#author = "Ian+Goodfellow"

author = input("Input Author: ")
authors = author
author = author.replace(" ","+")


url = "https://arxiv.org/search/?query=" + author + "&searchtype=author&size=200"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')


page = html_str.count('pagination-link')/2
#print(page)
if page>=2.0:
    for p in range(1,int(page)):
#        print(p)
        start = p*200
        url2 = url + "&start="+str(start)
        content = urllib.request.urlopen(url2)
        print(url2)
        html_str = html_str + content.read().decode('utf-8')

pattern = '<li class=\"arxiv-result[\s\S]*?</li>'
pattern2 = '<a href=\"/search/\?searchtype=author[\s\S]*?</a>'
result = re.findall(pattern, html_str)


names = []

#print("[ Author: " + author + " ]")
for r in result:
    #print(r)
    if r.find(authors) != -1:    
        nameList = re.findall(pattern2,r)
        for n in nameList:
            co = n.split("\">")[1].split("</a>")[0].strip()
            names.append(co)


p = list(set(names))
p.sort()

author_name = author.replace("+"," ")


for g in p:
    if g != author_name:
        print(' %s : %d times' %(g,names.count(g)))


