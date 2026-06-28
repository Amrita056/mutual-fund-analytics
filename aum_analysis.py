import pandas as pd
import matplotlib.pyplot as plt

aum = pd.read_csv("03_aum_by_fund_house.csv")

print("========== FIRST 5 ROWS ==========")
print(aum.head())

print("\n========== DATASET INFO ==========")
aum.info()

print("\n========== SHAPE ==========")
print(aum.shape)

print("\n========== COLUMN NAMES ==========")
print(aum.columns)

print("\n========== MISSING VALUES ==========")
print(aum.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(aum.duplicated().sum())

print("\n========== CONVERT DATE ==========")

aum["date"] = pd.to_datetime(aum["date"])

print(aum.dtypes)
print("\n========== DATE RANGE ==========")

print("Start Date :", aum["date"].min())
print("End Date   :", aum["date"].max())

print("\n========== AUM GROWTH CHART ==========")

plt.figure(figsize=(14,7))

for fund in aum["fund_house"].unique():
    data = aum[aum["fund_house"] == fund]

    plt.plot(
        data["date"],
        data["aum_crore"],
        marker="o",
        linewidth=2,
        label=fund
    )

plt.title("AUM Growth by Fund House (2022–2025)")
plt.xlabel("Date")
plt.ylabel("AUM (Crore ₹)")

plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig("aum_growth_chart.png", dpi=300)

plt.show()    

plt.tight_layout()

plt.savefig("aum_growth_chart.png", dpi=300)

plt.show()

# ==========================
# TOP AUM
# ==========================

# ==========================
# TOP AUM RECORD
# ==========================

print("\n========== TOP AUM ==========")

top = aum.loc[aum["aum_crore"].idxmax()]

print(top)