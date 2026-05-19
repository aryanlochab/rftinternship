import matplotlib.pyplot as plt

dates = ["MON", "TUE", "WED", "THU", "FRI"]

sales = [200, 250, 300, 280, 350]

# line plot
plt.plot(dates, sales, marker='o')

# title and labels
plt.title("Sales Trend Visualization")

plt.xlabel("Days")

plt.ylabel("Sales")

# highest and lowest sales

highest_sale = max(sales)
lowest_sale = min(sales)

highest_index = sales.index(highest_sale)
lowest_index = sales.index(lowest_sale)

# highlight highest point
plt.scatter(
    dates[highest_index],
    sales[highest_index],
    color='green',
    s=100,
    label='Highest Sale'
)

# highlight lowest point
plt.scatter(
    dates[lowest_index],
    sales[lowest_index],
    color='red',
    s=100,
    label='Lowest Sale'
)

plt.legend()

# show graph
plt.show()