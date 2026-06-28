import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# LOAD DATASET
# ==========================

folio = pd.read_csv("06_industry_folio_count.csv")

print("========== FIRST 5 ROWS ==========")
print(folio.head())

print("\n========== DATASET INFO ==========")
folio.info()

print("\n========== SHAPE ==========")
print(folio.shape)

print("\n========== COLUMN NAMES ==========")
print(folio.columns)

print("\n========== MISSING VALUES ==========")
print(folio.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(folio.duplicated().sum())

# ==========================
# CONVERT DATE
# ==========================

folio["month"] = pd.to_datetime(folio["month"])

print("\n========== DATE RANGE ==========")
print("Start :", folio["month"].min())
print("End   :", folio["month"].max())

# ==========================
# HIGHEST & LOWEST VALUES
# ==========================

highest = folio.loc[folio["total_folios_crore"].idxmax()]
lowest = folio.loc[folio["total_folios_crore"].idxmin()]

print("\n========== HIGHEST TOTAL FOLIOS ==========")
print(highest)

print("\n========== LOWEST TOTAL FOLIOS ==========")
print(lowest)

# ==========================
# PLOT GRAPH
# ==========================

plt.figure(figsize=(15,6))

plt.plot(
    folio["month"],
    folio["total_folios_crore"],
    marker="o",
    linewidth=2,
    color="green",
    label="Total Folios"
)

# Highest Point
plt.scatter(
    highest["month"],
    highest["total_folios_crore"],
    color="red",
    s=120
)

plt.annotate(
    f'{highest["total_folios_crore"]:.2f}',
    xy=(highest["month"], highest["total_folios_crore"]),
    xytext=(-70,30),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->", color="red"),
    color="red"
)

# Lowest Point
plt.scatter(
    lowest["month"],
    lowest["total_folios_crore"],
    color="blue",
    s=120
)

plt.annotate(
    f'{lowest["total_folios_crore"]:.2f}',
    xy=(lowest["month"], lowest["total_folios_crore"]),
    xytext=(20,-30),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->", color="blue"),
    color="blue"
)

plt.title("Industry Total Folio Count (2022-2025)")
plt.xlabel("Month")
plt.ylabel("Total Folios (Crore)")
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig("folio_growth.png", dpi=300)

plt.show()