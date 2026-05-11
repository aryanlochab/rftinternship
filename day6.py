import csv

sales_per_product = {}
total_revenue = 0
with open("day6.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row['PRODUCT']
        quantity = int(row['QUANTITY'])
        price = int(row['PRICE'])
        sales = quantity * price
        total_revenue += sales
        total = []
        total.append(sales)
    #sales per product,
        if product in sales_per_product:
            sales_per_product[product] += sales
        else:
            sales_per_product[product] = sales

"""
i am having trouble adding a new column
row[0].append('Total')
for i in range(1, len(row)):
    row[i].append(total[i - 1])

with open('day6.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(total)  """

top_product = max(sales_per_product, key = sales_per_product.get)
print("sales per product:")
for product, sales in sales_per_product.items():
    print(f"{product} : {sales}")

print("\nTotal Revenue", total_revenue)
print("\nTop Product", top_product)