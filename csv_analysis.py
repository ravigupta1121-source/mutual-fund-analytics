"""
CSV Analysis Script
Mutual Fund Analytics Project

This script performs exploratory data analysis
on mutual fund datasets.
"""

import pandas as pd
import os

folder_path = "data/raw"

csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

print("Total CSV Files Found:", len(csv_files))

for file in csv_files:
    print("\n" + "="*50)
    print("File Name:", file)

    df = pd.read_csv(os.path.join(folder_path, file))

    print("Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Rows:")
    print(df.head())
    