import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# Generating a mock dataset matching the project requirements
np.random.seed(42)
n_customers = 200

mock_data = {
    "Customer ID": [f"CUST_{i:03d}" for i in range(1, n_customers + 1)],
    "Age": np.random.randint(18, 70, size=n_customers),
    "Spending": np.random.randint(100, 5000, size=n_customers),
    "Visits": np.random.randint(1, 30, size=n_customers),
}

df = pd.DataFrame(mock_data)
print("--- Dataset Preview ---")
print(df.head(), "\n")


spending_bins = [0, 1500, 3500, float("inf")]
segment_labels = ["Low", "Medium", "High"]

# Create Simple Segments (Bonus Task)
df["Segment"] = pd.cut(
    df["Spending"], bins=spending_bins, labels=segment_labels
)

# Identify High-Value Customers (High spending AND frequent visits)
# Let's define frequent visits as being above the median number of visits.
median_visits = df["Visits"].median()
high_value_mask = (df["Segment"] == "High") & (df["Visits"] >= median_visits)
df["Is_High_Value"] = high_value_mask

# Identify Low-Engagement Users (Low spending AND infrequent visits)
low_engagement_mask = (df["Segment"] == "Low") & (
    df["Visits"] < median_visits
)
df["Is_Low_Engagement"] = low_engagement_mask

# Display summaries
print("--- Customer Segments Count ---")
print(df["Segment"].value_counts(), "\n")

print(
    f"Total High-Value Customers Identified: {df['Is_High_Value'].sum()}"
)
print(
    f"Total Low-Engagement Users Identified: {df['Is_Low_Engagement'].sum()}\n"
)


# Set the plot style
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Spending Distribution
sns.histplot(
    data=df, x="Spending", kde=True, ax=axes[0], color="skyblue", bins=20
)
axes[0].set_title("Customer Spending Distribution", fontsize=14)
axes[0].set_xlabel("Spending Amount ($)")
axes[0].set_ylabel("Count of Customers")

# Plot 2: Customer Categories (Segments)
sns.countplot(
    data=df,
    x="Segment",
    ax=axes[1],
    palette="pastel",
    hue="Segment",
    legend=False,
)
axes[1].set_title("Customer Segments (High / Medium / Low)", fontsize=14)
axes[1].set_xlabel("Segment")
axes[1].set_ylabel("Number of Customers")

plt.tight_layout()
plt.show()