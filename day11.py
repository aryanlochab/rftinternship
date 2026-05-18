import matplotlib.pyplot as plt

dates = ["MON", "TUE", "WED", "THU", "FRI"]

sales = [200, 250, 300, 280, 350]

plt.plot(dates, sales, marker='o')

plt.title("Sales Trend")

plt.xlabel("Days")

plt.ylabel("Sales")

plt.show()