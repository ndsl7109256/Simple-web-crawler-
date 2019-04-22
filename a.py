import matplotlib.pyplot as plt
import urllib.request;
import re;

author = "Ian+Goodfellow"
url = "https://arxiv.org/search/?query=" + author + "&searchtype=author"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')
pattern = 'title is-5 mathjax[\s\S]*?</p>'
result = re.findall(pattern, html_str)
patten2 = 'originally announced[\s\S]*?</p>'
years = re.findall(patten2, html_str)

count = 0

print("[ Author: " + author + " ]")
for r in result:
    print(r)
    title = r.split("title is-5 mathjax\">")[1].split("</p>")[0].strip()
    print(title)
    count = count + 1
list =[]
for g in years:
    date = g.split("originally announced</span>")[1].split("</p>")[0].strip()
    year = date.split(' ')[1].split('.')[0].strip()
    print(date)
    print(int(year))
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

print(url)
