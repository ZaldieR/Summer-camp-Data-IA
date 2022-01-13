#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df = pd.read_csv('valeursfoncieres-2019.txt', delimiter = "|")
df


# In[23]:


def get_departements():
    departements = df["Code departement"]
    return (departements)
departements = get_departements()
print(departements)


# In[24]:


def get_postal_code():
    postal = df["Code postal"]
postal_code = get_postal_code()
print(postal_code)


# In[25]:


def get_departement_housing(departement_id):
    res = []
    data = df[df["Code departement"] == departement_id]
    for i, j, k, l in zip(data['Date mutation'], data['Nature mutation'], data['Valeur fonciere'],     data['Surface reelle bati']):
        res.append({'date':i, 'type':j, 'price':k, 'square_meter':l})
    return res
res = get_departement_housing(1)
for i in res:
    print(i)


# In[26]:


def get_postal_code_housing(postal_code):
    res = []
    data = df[df["Code postal"] == postal_code]
    for i, j, k, l in zip(data['Date mutation'], data['Nature mutation'], data['Valeur fonciere'],     data['Surface reelle bati']):
        res.append({'date':i, 'type':j, 'price':k, 'square_meter':l})
    return res
res = get_postal_code_housing(1000)
for i in res:
    print(i)

