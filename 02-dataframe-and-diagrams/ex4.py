#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns

df = pd.read_csv("dataset.csv")

df = df.groupby(["reg_name", "year", "tax_name"], as_index=False)['amount'].sum()
df
sns.catplot(data=df, x="year", y="amount", kind="bar", hue="reg_name", row="tax_name")