import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# LOAD DATASET
# ==========================

scheme = pd.read_csv("07_scheme_performance.csv")

print("========== FIRST 5 ROWS ==========")
print(scheme.head())

print("\n========== DATASET INFO ==========")
scheme.info()

print("\n========== SHAPE ==========")
print(scheme.shape)

print("\n========== COLUMN NAMES ==========")
print(scheme.columns)

print("\n========== MISSING VALUES ==========")
print(scheme.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(scheme.duplicated().sum())

# ==========================
# TOP 10 SCHEMES (5-YEAR RETURN)
# ==========================

top10 = scheme.sort_values(
    by="return_5yr_pct",
    ascending=False
).head(10)

print("\n========== TOP 10 SCHEMES ==========")
print(top10[["scheme_name","return_5yr_pct"]])

# ==========================
# BAR CHART
# ==========================

plt.figure(figsize=(14,6))

plt.bar(
    top10["scheme_name"],
    top10["return_5yr_pct"],
    color="royalblue"
)

plt.xticks(rotation=60, ha="right")

plt.title("Top 10 Mutual Fund Schemes (5-Year Return)")
plt.xlabel("Scheme")
plt.ylabel("5-Year Return (%)")

plt.grid(axis="y")

plt.tight_layout()

plt.savefig("scheme_top10.png", dpi=300)

plt.show()

# ==========================
# BEST SHARPE RATIO
# ==========================

best = scheme.loc[scheme["sharpe_ratio"].idxmax()]

print("\n========== BEST SHARPE RATIO ==========")
print(best)