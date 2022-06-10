#!/usr/bin/env python
# coding: utf-8

# In[16]:


import urllib.request as req
url="https://tw.stock.yahoo.com/class-quote?sectorId=3&exchange=TAI"
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)
#解析資料
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div" , class_="title")
for script in titles:
    if title.a !=None:
        print(script)


# In[ ]:




