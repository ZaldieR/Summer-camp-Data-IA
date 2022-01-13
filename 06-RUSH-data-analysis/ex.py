#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("2020_LoL.csv")
df


# In[47]:


blue = df[df['side'] == 'Blue']['result']
red = df[df['side'] == 'Red']['result']
count_w = 0
count_l = 0
for i in blue:
    if i == 1:
        count_w += 1
    elif i == 0:
        count_l += 1
total = count_w + count_l
print("Winrate Blue", count_w / total)
print("Winrate Red ", count_l / total)


# In[48]:


fblood = df[df['firstblood'] == 1]
le = len(fblood)
print("First Blood ratio Blue", fblood[fblood['side'] == 'Blue']['side'].count() / le)
print("First Blood ratio Red ", fblood[fblood['side'] == 'Red']['side'].count() / le)


# In[49]:


ban = df['ban1'].value_counts()
ban += df['ban2'].value_counts()
ban += df['ban3'].value_counts()
ban += df['ban4'].value_counts()
ban += df['ban5'].value_counts()
maxi = 0
name = ""
for i in ban.items():
    if i[1] > maxi:
        maxi = i[1]
        name = i[0]
print(f"The most banned champion is {name} ({maxi})")


# In[58]:


wards = df.groupby(["side"])['wardsplaced'].sum()
total = wards[0] + wards[1]
print(f'Wards Placed rate Blue {wards[0] / total}')
print(f'Wards Placed rate Red  {wards[1] / total}')


# In[ ]:




