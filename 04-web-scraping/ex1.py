#!/usr/bin/env python
# coding: utf-8

# In[145]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


# In[155]:


def get_ps5_prices():
    ua = "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/79.0.3945.74Safari/537.36 Edg/79.0.309.43"
    url = "https://www.leboncoin.fr/recherche?category=43&text=ps5"
    content = requests.get(url, headers={"User-Agent": ua})
    print(content)
    soup = BeautifulSoup(content.text, "html.parser")
    return(soup)
    
soup = get_ps5_prices()
soup


# In[156]:


def get_data(soup):
    result = []
    res = soup.find_all(class_="styles_adCard__2YFTi styles_classified__aKs-b")
    for i in res:
        temp_data = {}
        title = i.find_all(class_="AdCardTitle-e546g7-0 XGzNp")
        temp_data['title'] = title[0]['title']
        price = i.find_all(class_="_1hnil _1-TTU _35DXM")
        if price:
            temp_price = price[0].text.split('\xa0')
            temp_price2 = ""
            for k in range(0, len(temp_price) - 1):
                temp_price2 = temp_price2 + str(temp_price[k])
            temp_data['price'] = temp_price2 
        else:
            temp_data['price'] = "0" 
        date = i.find_all(class_="AdCardConsumerGoodsList__Date-sc-4yuraf-2 fdnWWL")
        location = date[0].string.split(" ")
        temp_data['date'] = date[1].string
        temp_data['city'] = location[0]
        temp_data['postal_code'] = location[1]
        result.append(temp_data)
    return result
result = get_data(soup)
for i in result:
    print(i)


# In[157]:


data = pd.DataFrame.from_dict(result)
data


# In[ ]:




