
# 📊 Crypto Transactions Analysis

## ✅ 1. Data Cleaning & Preparation
- Verified **no missing or null values** across all columns.
- Converted `Transaction_Date` into **datetime format** and applied **monthly aggregation** to identify trends over time.
- Filtered the dataset to focus only on **Completed transactions** for more accurate and actionable insights.
- Checked for and removed **duplicate entries** and **invalid values** (e.g., zero or negative amounts).

## 🔍 2. Exploratory Data Analysis (EDA)

### General Observations
- Strong correlation between `Total_Value` and `Transaction_Fee` suggests a **proportional fee structure**.
- Most users made between **1–3 transactions**, spread across multiple platforms and wallet types.
- The dataset is relatively **balanced** across:
  - `Status` (Completed, Failed, Pending)
  - `Platform` (Binance, Coinbase, etc.)
  - `Crypto` assets (Polkadot, Ethereum, Bitcoin, etc.)

### Key KPIs
1. **Transaction Count by Type and Platform**: Measures common user behaviors and preferred exchanges.
2. **Total Transaction Value by Wallet Type**: Identifies high-value users and custody preferences.
3. **Monthly Growth in Transaction Value**: Highlights user activity trends and app adoption.

## 📈 3. Visualizations
- **Crypto Volume Share Over Time**: Shift from Polkadot to XRP; XRP may be a new user trend.
- **Transaction Type by Platform**: Coinbase dominates, especially in Staking; UX advantage possible.
- **Wallet Type vs Transaction Count**: Hot and Exchange wallets dominate, indicating frequent, accessible use.
- **Wallet Type vs Average Transaction Value**: Hardware wallets used by high-value users.

### Dashboard Filters
- ✅ Filtered to **Completed transactions**
- ✅ Date range starts **March 2023** (excluding Feb due to limited data)

## 💡 4. Business Insights & Recommendations
- Enhance staking features with better UX and incentives.
- Focus integrations around Binance and Coinbase.
- Offer premium features for hardware wallet users.
- Use monthly transaction trends to time rollouts.
- Promote Ethereum and Polkadot ecosystems in-app.
