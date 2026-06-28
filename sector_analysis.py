import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
portfolio = pd.read_csv("09_portfolio_holdings.csv")

print("========== FIRST 5 ROWS ==========")
print(portfolio.head())

print("\n========== DATASET INFO ==========")
portfolio.info()

print("\n========== SHAPE ==========")
print(portfolio.shape)

print("\n========== COLUMN NAMES ==========")
print(portfolio.columns)

print("\n========== MISSING VALUES ==========")
print(portfolio.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(portfolio.duplicated().sum())

# Sector-wise total weight
sector_weight = portfolio.groupby("sector")["weight_pct"].sum().sort_values(ascending=False)

print("\n========== SECTOR ALLOCATION ==========")
print(sector_weight)

# Donut Chart
plt.figure(figsize=(9,9))

plt.pie(
    sector_weight,
    labels=sector_weight.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops=dict(width=0.4)
)

plt.title("Sector Allocation Donut Chart")

plt.tight_layout()

plt.savefig("sector_donut.png", dpi=300)

plt.show()