"""
Mutual Fund Recommendation Engine

This script generates mutual fund recommendations
based on performance metrics.
"""

import pandas as pd

perf = pd.read_csv("data/raw/07_scheme_performance.csv")

def recommend_funds(risk_level):

    funds = perf[perf['risk_grade'] == risk_level]

    funds = funds.sort_values(
        by='sharpe_ratio',
        ascending=False
    ).head(3)

    return funds

print(recommend_funds("High"))