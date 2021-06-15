#!/usr/bin/env python
# coding: utf-8

import pandas as pd

df = pd.read_csv("dataset.csv")

df = df[df['reg_name'] == 'Auvergne-Rhône-Alpes']
df = df[df['tax_name'] == 'CVAE']
df = df.groupby(["year"])['amount'].sum()
df