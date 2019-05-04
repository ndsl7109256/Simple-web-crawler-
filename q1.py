import numpy as np
import matplotlib.pyplot as plt
import urllib.request;
import re;

#author = "Ian+Goodfellow"
author = input("Input Author: ")
authors = author
author = author.replace(" ","+")

#print(author)
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


pattern = 'title is-5 mathjax[\s\S]*?</p>'
result = re.findall(pattern, html_str)
patten2 = 'class=\"authors[\s\S]*?</li>'
years = re.findall(patten2, html_str)

count = 0

#print("[ Author: " + author + " ]")
for r in result:
    title = r.split("title is-5 mathjax\">")[1].split("</p>")[0].strip()
    count = count + 1
list =[]
for g in years:
    date = g.split("originally announced</span>")[1].split("</p>")[0].strip()
    year = date.split(' ')[1].split('.')[0].strip()
#    print(date)
    print(int(year))
#    print(g)

    if g.find(authors) != -1:
        list.append(int(year))
a = int(min(list))
b = int(max(list))

x=[]
y=[]
max_count = 0
for num in range(a,b+1):
    x.append(num)
    y.append(list.count(num))
    if(list.count(num) >max_count):
        max_count = list.count(num)


plt.xticks(np.arange(a,b+1,1.0))
plt.yticks(np.arange(0,max_count+1,1.0))
plt.bar(x,y,color="#ff7575")
plt.show()

#print(url)

#print(count)
