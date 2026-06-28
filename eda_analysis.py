import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
fund_master = pd.read_csv("01_fund_master.csv")

print("========== FIRST 5 ROWS ==========")
print(fund_master.head())

print("\n========== DATASET INFO ==========")
fund_master.info()

print("\n========== SHAPE ==========")
print(fund_master.shape)

print("\n========== COLUMN NAMES ==========")
print(fund_master.columns)

print("\n========== MISSING VALUES ==========")
print(fund_master.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(fund_master.duplicated().sum())

print("\n========== STATISTICAL SUMMARY ==========")
print(fund_master.describe())
print("\n========== FUND HOUSES ==========")
print(fund_master["fund_house"].unique())

print("\n========== CATEGORIES ==========")
print(fund_master["category"].unique())

print("\n========== RISK CATEGORIES ==========")
print(fund_master["risk_category"].unique())

print("\n========== SCHEMES BY FUND HOUSE ==========")

fund_house_count = fund_master["fund_house"].value_counts()

print(fund_house_count)

fund_house_count.plot(kind="bar", figsize=(10,5))

plt.title("Number of Schemes by Fund House")
plt.xlabel("Fund House")
plt.ylabel("Number of Schemes")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()