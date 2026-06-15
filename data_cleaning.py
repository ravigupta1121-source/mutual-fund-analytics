"""
Data Cleaning Script
Mutual Fund Analytics Project

This script cleans and preprocesses mutual fund data
for analysis and dashboard creation.
"""

import pandas as pd

# =========================
# NAV HISTORY CLEANING
# =========================

nav_df = pd.read_csv("data/raw/02_nav_history.csv")

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.sort_values(
    by=["amfi_code", "date"]
)

nav_df["nav"] = nav_df.groupby(
    "amfi_code"
)["nav"].ffill()

nav_df = nav_df.drop_duplicates()

nav_df = nav_df[nav_df["nav"] > 0]

nav_df.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("NAV History Cleaned")


# =========================
# INVESTOR TRANSACTIONS
# =========================

txn_df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"]
)

txn_df["transaction_type"] = txn_df[
    "transaction_type"
].str.title()

txn_df = txn_df[
    txn_df["amount_inr"] > 0
]

txn_df = txn_df.drop_duplicates()

txn_df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("Investor Transactions Cleaned")


# =========================
# SCHEME PERFORMANCE
# =========================

perf_df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    perf_df[col] = pd.to_numeric(
        perf_df[col],
        errors="coerce"
    )

perf_df = perf_df[
    (perf_df["expense_ratio_pct"] >= 0.1)
    &
    (perf_df["expense_ratio_pct"] <= 2.5)
]

perf_df = perf_df.drop_duplicates()

perf_df.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("Scheme Performance Cleaned")

print("\nAll Cleaning Completed Successfully")