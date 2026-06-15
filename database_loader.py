"""
Database Loader Script
Mutual Fund Analytics Project

This script loads cleaned data into SQLite database.
"""

import pandas as pd
from sqlalchemy import create_engine

# SQLite Database Create
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned files
nav_df = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

txn_df = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

perf_df = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

# Save into database tables
nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database Created Successfully")
print("Tables Loaded:")
print("- fact_nav")
print("- fact_transactions")
print("- fact_performance")