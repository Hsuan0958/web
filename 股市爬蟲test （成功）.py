#!/usr/bin/env python
# coding: utf-8

# In[24]:


from bs4 import BeautifulSoup 
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
}
url = "https://tw.stock.yahoo.com/rank/price"

response = requests.get(url, headers=headers)

# 解析資料

soup = BeautifulSoup(response.text, 'lxml')

name_data = soup.find_all(class_="Fz(14px) C(#979ba7) Ell")
ticker_data = soup.find_all(class_="Lh(20px) Fw(600) Fz(16px) Ell")

for i in range(0, len(name_data)):
    print(name_data[i].text + " " +ticker_data[i].text)


# In[ ]:




