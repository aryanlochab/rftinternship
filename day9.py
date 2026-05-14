import pandas as pd
#learning pandas
# Read CSV file
df = pd.read_csv("day9.csv")


# Display original data
print("Original Data:\n")
print(df)

filtered_data = df[(df["SALARY"] > 50000) & (df["AGE"] < 30)]

# Display filtered results
print("\nFiltered Data:\n")
print(filtered_data)

# Save filtered data to new CSV file
filtered_data.to_csv("day9_filtered_data.csv", index=False)

print("\nFiltered data saved to filtered_data.csv")