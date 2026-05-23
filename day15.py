import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    "Name": ["Aman", "Riya", "Karan", "Sneha", "Rohit"],
    "Marks": [78, 92, 65, 88, 95],
    "Study_Hours": [4, 7, 3, 6, 8]
}

df = pd.DataFrame(data)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12,10))

# LINE CHART
axes[0,0].grid(True)
axes[0,0].plot(df["Name"], df["Marks"], marker='o')
axes[0,0].set_title("Marks Trend")
axes[0,0].set_xlabel("Students")
axes[0,0].set_ylabel("Marks")

# BAR CHART
axes[0,1].grid(True)
axes[0,1].bar(df["Name"], df["Marks"], color='orange')
axes[0,1].set_title("Marks Comparison")
axes[0,1].set_xlabel("Students")
axes[0,1].set_ylabel("Marks")

# HISTOGRAM
axes[1,0].grid(True)
axes[1,0].hist(df["Marks"], bins=5, color='yellow')
axes[1,0].set_title("Marks Distribution")
axes[1,0].set_xlabel("Marks")
axes[1,0].set_ylabel("Frequency")

# study hour comparison
axes[1,1].grid(True)
axes[1,1].bar(df["Name"], df["Study_Hours"], color='red')
axes[1,1].set_title("Study Hour Comparison")
axes[1,1].set_xlabel("Name")
axes[1,1].set_ylabel("Study Hours")

plt.tight_layout(pad=3)

plt.show()