#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

df = df[df['reg_name'] == 'Auvergne-Rhône-Alpes']
df = df[df['tax_name'] == 'CVAE']
df = df.groupby(["year"], as_index=False).sum()

df
sns.displot(data=df, x="year")