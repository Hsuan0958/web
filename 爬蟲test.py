#!/usr/bin/env python
# coding: utf-8

# In[6]:


import urllib.request as req
url="https://www.ptt.cc/bbs/C_Chat/index.html"
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#解析資料
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div" , class_="title")
for title in titles:
    if title.a !=None:
        print(title.a.string)


# In[ ]:




