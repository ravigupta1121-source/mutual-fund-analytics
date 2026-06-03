-- Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- Transaction Count
SELECT COUNT(*) AS total_transactions
FROM fact_transactions;

-- Total Investment Amount
SELECT SUM(amount_inr) AS total_investment
FROM fact_transactions;

-- Transactions by State
SELECT state, COUNT(*) AS txn_count
FROM fact_transactions
GROUP BY state;

-- Transactions by Payment Mode
SELECT payment_mode, COUNT(*)
FROM fact_transactions
GROUP BY payment_mode;

-- Average Expense Ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;

-- High Performing Funds
SELECT scheme_name, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;

-- Funds with Expense Ratio < 1
SELECT scheme_name
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Risk Grade Distribution
SELECT risk_grade, COUNT(*)
FROM fact_performance
GROUP BY risk_grade;