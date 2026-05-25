import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sales_data = {
    'Date': [
        '2026-01-01', '2026-01-03', '2026-01-05', '2026-01-10', '2026-01-15',
        '2026-01-20', '2026-01-25', '2026-02-01', '2026-02-04', '2026-02-10',
        '2026-02-14', '2026-02-18', '2026-02-22', '2026-02-28', '2026-03-02',
        '2026-03-07', '2026-03-12', '2026-03-15', '2026-03-19', '2026-03-22',
        '2026-03-25', '2026-03-28', '2026-03-29', '2026-03-30', '2026-03-31'
    ],
    'Product': [
        'Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Laptop',
        'Smartphone', 'Tablet', 'Laptop', 'Smartphone', 'Headphones',
        'Tablet', 'Laptop', 'Smartphone', 'Headphones', 'Laptop',
        'Smartphone', 'Tablet', 'Headphones', 'Laptop', 'Smartphone',
        'Tablet', 'Headphones', 'Laptop', 'Smartphone', 'Tablet'
    ],
    'Region': [
        'North', 'East', 'South', 'West', 'North',
        'West', 'East', 'North', 'East', 'South',
        'West', 'North', 'South', 'West', 'East',
        'North', 'South', 'West', 'North', 'East',
        'South', 'West', 'North', 'East', 'South'
    ],
    'Sales': [
        1200.0, 850.0, 450.0, None, 1300.0,
        900.0, 480.0, 1250.0, None, 150.0,
        500.0, 1400.0, 950.0, 180.0, 1350.0,
        920.0, 510.0, 200.0, 1450.0, 980.0,
        None, 220.0, 1500.0, 1050.0, 550.0
    ]
}

df = pd.DataFrame(sales_data)
df['Date'] = pd.to_datetime(df['Date'])

print("Missing values before cleaning:", df['Sales'].isna().sum())

#taking median to fill in the blanks

sales_median = df['Sales'].median()
df['Sales'] = df['Sales'].fillna(sales_median)
print(df)

print("Missing values after cleaning:", df['Sales'].isna().sum())
print(f"Filled missing slots with the median value: ${sales_median}")

#1. total sales per product

product_perf = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).reset_index()
print("\n--- Total Sales Per Product ---")
print(product_perf)

#region wise 
region_perf = df.groupby('Region')['Sales'].sum().sort_values(ascending=False).reset_index()
print("\n--- Region-Wise Performance ---")
print(region_perf)

sns.set_theme(style='whitegrid')

plt.figure(figsize=(10, 4))
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()
plt.plot(daily_sales['Date'], daily_sales['Sales'], marker='o',color="#0f5fb5", linewidth=2 )
plt.xlabel('Date')
plt.ylabel('Sale')
plt.title('Sales trend over time (Q1 2026)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#barchart dor top products
plt.figure(figsize=(8,4))
sns.barplot(x='Product', y='Sales', data=product_perf, palette='Blues_r')
plt.title('Top Products by Total Sales Revenue', fontsize=14, fontweight='bold')
plt.xlabel('Product Categories')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.show()
