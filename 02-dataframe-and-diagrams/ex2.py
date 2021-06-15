#!/usr/bin/env python
# coding: utf-8

import pandas as pd

df = pd.read_csv("dataset.csv")

df = df.groupby(["reg_name", "year", "tax_name"])['amount'].sum()
df