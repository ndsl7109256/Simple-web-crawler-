import matplotlib.pyplot as plt
import urllib.request;
import re;

#author = "Ian+Goodfellow"
author = input("Input Author: ")
author = author.replace(" ","+")

#print(author)
url = "https://arxiv.org/search/?query=" + author + "&searchtype=author"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')

page = html_str.count('pagination-link')/2
#print(page)
if page>=2.0:
    for p in range(1,int(page)):
#        print(p)
        start = p*50
        url2 = url + "&start="+str(start)
        content = urllib.request.urlopen(url2)
#        print(url2)
        html_str = html_str + content.read().decode('utf-8')


pattern = 'title is-5 mathjax[\s\S]*?</p>'
result = re.findall(pattern, html_str)
patten2 = 'originally announced[\s\S]*?</p>'
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
#    print(int(year))
    list.append(int(year))
a = int(min(list))
b = int(max(list))

x=[]
y=[]
for num in range(a,b):
    x.append(num)
    y.append(list.count(num))

plt.figure()
plt.bar(x,y)
plt.show()

#print(url)

#print(count)
