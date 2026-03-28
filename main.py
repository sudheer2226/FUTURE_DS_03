import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folder
os.makedirs("outputs/charts", exist_ok=True)

# Load dataset (IMPORTANT: encoding fix)
df = pd.read_csv("data/churn.csv", encoding='latin1')

print("✅ Data Loaded")
print(df.head())

# -------------------------
# DATA CLEANING
# -------------------------
df = df.dropna()

print("✅ Data Cleaned")

# -------------------------
# CHURN COUNT
# -------------------------
churn_count = df['Churn'].value_counts()

plt.figure()
churn_count.plot(kind='bar')
plt.title("Churn vs Non-Churn")
plt.xlabel("Churn")
plt.ylabel("Count")
plt.savefig("outputs/charts/churn_count.png")
plt.close()

# -------------------------
# CHURN RATE
# -------------------------
churn_rate = (df['Churn'] == "Yes").mean() * 100
print(f"Churn Rate: {churn_rate:.2f}%")

# -------------------------
# CHURN BY GENDER
# -------------------------
gender_churn = pd.crosstab(df['gender'], df['Churn'])

plt.figure()
gender_churn.plot(kind='bar')
plt.title("Churn by Gender")
plt.savefig("outputs/charts/gender_churn.png")
plt.close()

# -------------------------
# CHURN BY CONTRACT TYPE
# -------------------------
contract_churn = pd.crosstab(df['Contract'], df['Churn'])

plt.figure()
contract_churn.plot(kind='bar')
plt.title("Churn by Contract Type")
plt.savefig("outputs/charts/contract_churn.png")
plt.close()

# -------------------------
# MONTHLY CHARGES ANALYSIS
# -------------------------
plt.figure()
plt.scatter(df['MonthlyCharges'], df['tenure'])
plt.title("Monthly Charges vs Tenure")
plt.xlabel("Monthly Charges")
plt.ylabel("Tenure")
plt.savefig("outputs/charts/charges_vs_tenure.png")
plt.close()

# -------------------------
# BASIC INSIGHTS
# -------------------------
print("\n📊 INSIGHTS:")

print("Total Customers:", len(df))
print("Churn Rate:", churn_rate)

print("\nCustomers churn more in:")
print(contract_churn.idxmax())

print("\n✅ Analysis Done! Check outputs folder.")