# Data Dictionary

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Mutual Fund Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | Text | Unique Investor ID |
| transaction_date | Date | Transaction Date |
| amfi_code | Integer | Scheme Code |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction Amount |
| state | Text | Investor State |
| city | Text | Investor City |
| kyc_status | Text | KYC Status |

## fact_performance

| Column | Type | Description |
|----------|----------|----------|
| scheme_name | Text | Fund Name |
| fund_house | Text | AMC Name |
| return_1yr_pct | Float | 1 Year Return |
| return_3yr_pct | Float | 3 Year Return |
| expense_ratio_pct | Float | Expense Ratio |
| aum_crore | Float | Assets Under Management |
| risk_grade | Text | Risk Category |