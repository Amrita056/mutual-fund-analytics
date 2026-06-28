import pandas as pd

# Load Dataset
sip = pd.read_csv("04_monthly_sip_inflows.csv")

print("========== FIRST 5 ROWS ==========")
print(sip.head())

print("\n========== DATASET INFO ==========")
sip.info()

print("\n========== SHAPE ==========")
print(sip.shape)

print("\n========== COLUMN NAMES ==========")
print(sip.columns)

print("\n========== MISSING VALUES ==========")
print(sip.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(sip.duplicated().sum())
print("\n========== CONVERT MONTH TO DATE ==========")

sip["month"] = pd.to_datetime(sip["month"])

print(sip.dtypes)
print("\n========== DATE RANGE ==========")

print("Start Month :", sip["month"].min())
print("End Month   :", sip["month"].max())
print("\n========== HIGHEST SIP INFLOW ==========")

highest = sip.loc[sip["sip_inflow_crore"].idxmax()]

print(highest)
import matplotlib.pyplot as plt

plt.figure(figsize=(15,6))

plt.plot(
    sip["month"],
    sip["sip_inflow_crore"],
    marker="o",
    linewidth=2,
    color="blue"
)

plt.title("Monthly SIP Inflow Trend (2022–2025)")
plt.xlabel("Month")
plt.ylabel("SIP Inflow (Crore ₹)")
plt.grid(True)
# Highlight Highest SIP Inflow

highest = sip.loc[sip["sip_inflow_crore"].idxmax()]

plt.scatter(
    highest["month"],
    highest["sip_inflow_crore"],
    color="red",
    s=120,
    zorder=5
)

plt.annotate(
    "₹31,002 Cr\n(Dec 2025)",
    xy=(highest["month"], highest["sip_inflow_crore"]),
    xytext=(-80, 30),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=10,
    color="red"
)

plt.tight_layout()
plt.savefig("sip_trend.png", dpi=300)

plt.show()