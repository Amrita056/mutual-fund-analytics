import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load NAV Dataset
nav = pd.read_csv("02_nav_history.csv")

print("========== FIRST 5 ROWS ==========")
print(nav.head())

print("\n========== DATASET INFO ==========")
nav.info()

print("\n========== SHAPE ==========")
print(nav.shape)

print("\n========== COLUMN NAMES ==========")
print(nav.columns)

print("\n========== MISSING VALUES ==========")
print(nav.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(nav.duplicated().sum())

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Pivot data
pivot = nav.pivot_table(
    index="date",
    columns="amfi_code",
    values="nav"
)

# Daily returns
returns = pivot.pct_change().dropna()

# Select first 10 funds
corr = returns.iloc[:, :10].corr()

print("\n========== CORRELATION MATRIX ==========")
print(corr)

# Heatmap
plt.figure(figsize=(10,8))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("NAV Return Correlation Heatmap")

plt.tight_layout()

plt.savefig("correlation_heatmap.png", dpi=300)

plt.show()