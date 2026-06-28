import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# LOAD DATASET
# ==========================

investor = pd.read_csv("08_investor_transactions.csv")

print("========== FIRST 5 ROWS ==========")
print(investor.head())

print("\n========== DATASET INFO ==========")
investor.info()

print("\n========== SHAPE ==========")
print(investor.shape)

print("\n========== COLUMN NAMES ==========")
print(investor.columns)

print("\n========== MISSING VALUES ==========")
print(investor.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(investor.duplicated().sum())

# ==========================
# CONVERT DATE
# ==========================

investor["transaction_date"] = pd.to_datetime(investor["transaction_date"])

print("\n========== DATE RANGE ==========")
print("Start :", investor["transaction_date"].min())
print("End   :", investor["transaction_date"].max())

# ==========================
# TRANSACTION TYPE COUNT
# ==========================

print("\n========== TRANSACTION TYPES ==========")

transaction_count = investor["transaction_type"].value_counts()

print(transaction_count)

# ==========================
# BAR CHART
# ==========================

plt.figure(figsize=(8,5))

transaction_count.plot(
    kind="bar",
    color=["royalblue","orange"]
)

plt.title("Purchase vs Redemption Transactions")

plt.xlabel("Transaction Type")

plt.ylabel("Number of Transactions")

plt.grid(axis="y")

plt.tight_layout()

plt.savefig("transaction_type.png", dpi=300)

plt.show()
print("\n========== AGE GROUP DISTRIBUTION ==========")
print(investor["age_group"].value_counts())

plt.figure(figsize=(8,8))

investor["age_group"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Investor Age Group Distribution")

plt.ylabel("")

plt.tight_layout()

plt.savefig("age_group_pie.png", dpi=300)

plt.show()

# ==========================
# TOP 10 STATES
# ==========================

print("\n========== TOP STATES ==========")

top_states = investor["state"].value_counts().head(10)

print(top_states)

plt.figure(figsize=(10,5))

top_states.plot(
    kind="bar",
    color="green"
)

plt.title("Top 10 States by Number of Investors")

plt.xlabel("State")

plt.ylabel("Number of Investors")

plt.grid(axis="y")

plt.tight_layout()

plt.savefig("top_states.png", dpi=300)

plt.show()

# ==========================
# PAYMENT MODES
# ==========================

print("\n========== PAYMENT MODES ==========")

payment = investor["payment_mode"].value_counts()

print(payment)

plt.figure(figsize=(6,6))

plt.pie(
    payment,
    labels=payment.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Payment Mode Distribution")

plt.tight_layout()

plt.savefig("payment_mode.png", dpi=300)

plt.show()
plt.figure(figsize=(8,8))

investor["age_group"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Investor Age Group Distribution")

plt.ylabel("")

plt.tight_layout()

plt.savefig("age_group_pie.png", dpi=300)

plt.show()
print("\n========== GENDER DISTRIBUTION ==========")
print(investor["gender"].value_counts())

plt.figure(figsize=(7,7))

investor["gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Investor Gender Distribution")

plt.ylabel("")

plt.tight_layout()

plt.savefig("gender_pie.png", dpi=300)

plt.show()
print("\n========== STATE-WISE SIP AMOUNT ==========")

state_data = (
    investor.groupby("state")["amount_inr"]
    .sum()
    .sort_values(ascending=False)
)

print(state_data)

plt.figure(figsize=(12,7))

state_data.plot(
    kind="barh",
    color="teal"
)

plt.title("State-wise Investment Amount")
plt.xlabel("Total Investment Amount (INR)")
plt.ylabel("State")

plt.tight_layout()

plt.savefig("state_distribution.png", dpi=300)

plt.show()
print("\n========== CITY TIER ==========")
print(investor["city_tier"].value_counts())

plt.figure(figsize=(7,7))

investor["city_tier"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("T30 vs B30 Investors")

plt.ylabel("")

plt.tight_layout()

plt.savefig("city_tier_pie.png", dpi=300)

plt.show()
import seaborn as sns

plt.figure(figsize=(9,6))

sns.boxplot(
    x="age_group",
    y="amount_inr",
    data=investor
)

plt.title("SIP Amount Distribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Investment Amount (INR)")

plt.tight_layout()

plt.savefig("sip_boxplot_age.png", dpi=300)

plt.show()
print("\n========== CITY TIER ==========")
print(investor["city_tier"].value_counts())

plt.figure(figsize=(7,7))

investor["city_tier"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("T30 vs B30 Investors")

plt.ylabel("")

plt.tight_layout()

plt.savefig("city_tier_pie.png", dpi=300)

plt.show()

print("\n========== AGE GROUP DISTRIBUTION ==========")

print(investor["age_group"].value_counts())

# ==========================
# KYC STATUS
# ==========================

print("\n========== KYC STATUS ==========")

print(investor["kyc_status"].value_counts())

# ==========================
# AGE GROUPS
# ==========================

print("\n========== AGE GROUP ==========")

print(investor["age_group"].value_counts())