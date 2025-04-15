
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load dataset
df = pd.read_csv('crypto_transactions_data.csv')

# Convert date column
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])

# Filter for completed transactions and post-February data
df = df[(df['Status'] == 'Completed') & (df['Transaction_Date'] >= '2023-03-01')]

# 1. Wallet Type Usage
wallet_usage = df['Wallet_Type'].value_counts()
plt.figure(figsize=(10, 5))
sns.barplot(x=wallet_usage.values, y=wallet_usage.index, palette='coolwarm')
plt.title('Wallet Type Usage')
plt.xlabel('Number of Transactions')
plt.ylabel('Wallet Type')
plt.tight_layout()
plt.show()

# 2. Average Transaction Value by Wallet Type
wallet_value_fee = df.groupby('Wallet_Type')['Total_Value'].mean().sort_values()
plt.figure(figsize=(10, 5))
ax = wallet_value_fee.div(1e6).plot(kind='barh', color='steelblue')
ax.set_title('Avg Transaction Value by Wallet Type')
ax.set_xlabel('Average Value (in Millions $)')
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.1f}M'))
plt.ylabel('Wallet Type')
plt.tight_layout()
plt.show()

# 3. Top Cryptos by Transaction Value Over Time
df['Month'] = df['Transaction_Date'].dt.to_period('M')
crypto_monthly = df.groupby(['Month', 'Crypto'])['Total_Value'].sum().unstack().fillna(0)
crypto_monthly = crypto_monthly.div(1e6)

crypto_monthly.plot(figsize=(14, 6))
plt.title('Crypto Volume Share Over Time')
plt.xlabel('Month')
plt.ylabel('Total Value (in Millions $)')
plt.legend(title='Crypto', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 4. Transaction Type by Platform
tx_type_platform = df.groupby(['Platform', 'Transaction_Type'])['Transaction_ID'].count().unstack().fillna(0)
tx_type_platform.plot(kind='bar', stacked=True, figsize=(14, 6), colormap='tab20c')
plt.title('Transaction Type by Platform')
plt.xlabel('Platform')
plt.ylabel('Number of Transactions')
plt.tight_layout()
plt.show()
