import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
category = pd.read_csv("05_category_inflows.csv")

print("========== FIRST 5 ROWS ==========")
print(category.head())

print("\n========== DATASET INFO ==========")
category.info()

print("\n========== SHAPE ==========")
print(category.shape)

print("\n========== COLUMN NAMES ==========")
print(category.columns)

print("\n========== MISSING VALUES ==========")
print(category.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(category.duplicated().sum())
print("\n========== CONVERT DATE ==========")

category["month"] = pd.to_datetime(category["month"])

print(category.dtypes)
print("\n========== DATE RANGE ==========")

print("Start :", category["month"].min())
print("End   :", category["month"].max())
print("\n========== FUND CATEGORIES ==========")

print(category["category"].unique())
print("\n========== PIVOT TABLE ==========")

pivot = category.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

print(pivot)
print("\n========== CATEGORY INFLOW HEATMAP ==========")

plt.figure(figsize=(14,8))

sns.heatmap(
    pivot,
    cmap="YlGnBu",
    annot=True,
    fmt=".0f"
)

plt.title("Category-wise Net Inflow Heatmap")

plt.xlabel("Month")
plt.ylabel("Fund Category")

plt.tight_layout()

plt.savefig("category_heatmap.png", dpi=300)

plt.show()