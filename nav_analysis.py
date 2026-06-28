import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# LOAD DATASET
# ==========================
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

# ==========================
# CONVERT DATE
# ==========================
print("\n========== CONVERT DATE ==========")

nav["date"] = pd.to_datetime(nav["date"])

print(nav.dtypes)

# ==========================
# DATE RANGE
# ==========================
print("\n========== DATE RANGE ==========")

print("Start Date :", nav["date"].min())
print("End Date   :", nav["date"].max())

# ==========================
# UNIQUE SCHEMES
# ==========================
print("\n========== UNIQUE SCHEMES ==========")

print("Total Schemes :", nav["amfi_code"].nunique())

print(nav["amfi_code"].unique())

# ==========================
# RECORDS PER SCHEME
# ==========================
print("\n========== RECORDS PER SCHEME ==========")

print(nav.groupby("amfi_code").size())

# ==========================
# SELECT ONE SCHEME
# ==========================

first_scheme = nav["amfi_code"].unique()[0]

print("\nUsing AMFI Code :", first_scheme)

scheme = nav[nav["amfi_code"] == first_scheme]

print(scheme.head())

# ==========================
# NAV TREND OF ONE SCHEME
# ==========================

# ==========================
# NAV TREND OF ONE SCHEME
# ==========================

plt.figure(figsize=(15,6))

plt.plot(
    scheme["date"],
    scheme["nav"],
    color="blue",
    linewidth=2,
    label="NAV"
)

# Highlight 2023 Bull Run
plt.axvspan(
    pd.Timestamp("2023-01-01"),
    pd.Timestamp("2023-12-31"),
    color="lightgreen",
    alpha=0.3,
    label="2023 Bull Run"
)

# Highlight 2024 Market Correction
plt.axvspan(
    pd.Timestamp("2024-01-01"),
    pd.Timestamp("2024-12-31"),
    color="lightcoral",
    alpha=0.3,
    label="2024 Market Correction"
)

plt.title(f"NAV Trend - AMFI Code {first_scheme}")

plt.xlabel("Date")
plt.ylabel("NAV")

plt.grid(True)

plt.legend()

plt.tight_layout()

# Save graph
plt.savefig("nav_trend.png", dpi=300)

plt.show()