import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

marks = [45, 50, 52, 55, 60, 61, 62, 65, 67, 70,
         72, 74, 75, 78, 80, 82, 85, 90, 95]

df = pd.DataFrame(marks, columns=["Marks"])

sns.histplot(df["Marks"], kde=True, color = "red" )

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")


print("Skewness:", df["Marks"].skew())

plt.show()