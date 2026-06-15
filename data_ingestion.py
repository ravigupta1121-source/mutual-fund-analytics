"""
Data Ingestion Script
Mutual Fund Analytics Project

This script collects and imports mutual fund data
from source files for further processing.
"""

import pandas as pd

df = pd.read_csv("data/raw/hdfc_nav.csv")

# print("Shape:")
# print(df.shape)

# print("\nColumns:")
# print(df.columns)

# print("\nData Types:")
# print(df.dtypes)

# print("\nFirst 5 Rows:")
# print(df.head())

# print("\nMissing Values:")
# print(df.isnull().sum())

# print("\nDuplicate Rows:")
# print(df.duplicated().sum())