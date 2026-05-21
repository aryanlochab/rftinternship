import matplotlib.pyplot as plt

# Data
categories = ["FOOD", "TRAVEL", "SHOPPING"]
expenses = [500, 300, 200]

# Highlight highest category
explode = [0.1, 0, 0]   # FOOD highlighted

# Create pie chart
plt.pie(
    expenses,
    labels=categories,
    autopct='%1.1f%%',   # percentage labels
    explode=explode,
    shadow=True,
    startangle=90
)

# Title
plt.title("Category Breakdown of Expenses")

# Show chart
plt.show()