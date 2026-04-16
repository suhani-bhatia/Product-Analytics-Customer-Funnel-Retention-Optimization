from analysis import load_and_prepare_data, compute_funnel, compute_retention
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = load_and_prepare_data("data.csv")  # change if needed

# -------------------------
# FUNNEL
# -------------------------
funnel = compute_funnel(df)

print("\nFUNNEL:")
print("Total Users:", funnel["total_users"])
print("Engaged Users:", funnel["engaged_users"])
print("High Value Users:", funnel["high_value_users"])
print("Engagement Rate:", funnel["engagement_rate"])
print("High Value Conversion:", funnel["high_value_rate"])

plt.figure()
plt.bar(["Total", "Engaged", "High Value"], [
    funnel["total_users"],
    funnel["engaged_users"],
    funnel["high_value_users"]
])
plt.title("Customer Funnel")
plt.savefig("funnel_chart.png")
plt.close()

# -------------------------
# RETENTION
# -------------------------
retention = compute_retention(df)

print("\nRETENTION:")
print("Retained Users:", retention["retained"])
print("Churned Users:", retention["churned"])
print("Retention Rate:", retention["retention_rate"])

plt.figure()
sns.histplot(df["days_since_last_purchase"], bins=20)
plt.title("Retention Distribution")
plt.savefig("retention_chart.png")
plt.close()

import pandas as pd

# -------------------------
# CREATE SUMMARY TABLE
# -------------------------
results_summary = pd.DataFrame({
    "Metric": [
        "Total Users",
        "Engaged Users",
        "High Value Users",
        "Engagement Rate",
        "High Value Conversion",
        "Retention Rate",
        "Churn Rate"
    ],
    "Value": [
        funnel["total_users"],
        funnel["engaged_users"],
        funnel["high_value_users"],
        round(funnel["engagement_rate"], 3),
        round(funnel["high_value_rate"], 3),
        round(retention["retention_rate"], 3),
        round(1 - retention["retention_rate"], 3)
    ]
})

print("\nRESULT SUMMARY:")
print(results_summary)

# Save CSV
results_summary.to_csv("results_summary.csv", index=False)
