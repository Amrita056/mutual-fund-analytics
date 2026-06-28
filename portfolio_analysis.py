import pandas as pd
import matplotlib.pyplot as plt
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
print("\n========== CONVERT DATE ==========")

portfolio["portfolio_date"] = pd.to_datetime(portfolio["portfolio_date"])

print(portfolio.dtypes)
print("\n========== DATE RANGE ==========")

print("Start :", portfolio["portfolio_date"].min())
print("End   :", portfolio["portfolio_date"].max())
print("\n========== HIGHEST HOLDING ==========")

highest = portfolio.loc[portfolio["weight_pct"].idxmax()]

print(highest)
print("\n========== LOWEST HOLDING ==========")

lowest = portfolio.loc[portfolio["weight_pct"].idxmin()]

print(lowest)
print("\n========== TOP 10 HOLDINGS ==========")

top10 = portfolio.sort_values(
    by="weight_pct",
    ascending=False
).head(10)

print(top10[["stock_name","sector","weight_pct"]])
plt.figure(figsize=(14,6))

plt.bar(
    top10["stock_name"],
    top10["weight_pct"],
    color="teal"
)

plt.title("Top 10 Portfolio Holdings")

plt.xlabel("Stock")

plt.ylabel("Weight (%)")

plt.xticks(rotation=45, ha="right")

plt.grid(axis="y")

plt.tight_layout()

plt.savefig("portfolio_top10.png", dpi=300)

plt.show()
