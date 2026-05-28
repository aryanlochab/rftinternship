import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


data = {
    "Movie Name": [
        "Inception",
        "The Dark Knight",
        "Interstellar",
        "Avatar",
        "The Avengers",
        "Titanic",
        "Toy Story 4",
        "The Conjuring",
        "Get Out",
        "Superbad",
        "The Hangover",
        "La La Land",
    ],
    "Rating": [8.8, 9.0, 8.6, 7.8, 8.0, 7.9, 7.7, 7.5, 7.7, 7.6, 7.7, 8.0],
    "Genre": [
        "Sci-Fi",
        "Action",
        "Sci-Fi",
        "Sci-Fi",
        "Action",
        "Drama",
        "Animation",
        "Horror",
        "Horror",
        "Comedy",
        "Comedy",
        "Drama",
    ],
    "Revenue": [836, 1006, 701, 2923, 1518, 2264, 1073, 320, 255, 170, 467, 447],
}

df = pd.DataFrame(data)
print("--- original dataset ---")
print(df)
print("\n" + "=" * 50 + "\n")



# Task A: Highest Rated Movies (Sorted by Rating descending)
highest_rated = df.sort_values(by="Rating", ascending=False)
print("--- HIGHEST RATED MOVIES ---")
print(highest_rated[["Movie Name", "Rating"]])
print("\n")

# Task B: Most Profitable Genres (Aggregated total revenue by Genre)
profitable_genres = (
    df.groupby("Genre")["Revenue"].sum().reset_index().sort_values(by="Revenue", ascending=False)
)
print("--- MOST PROFITABLE GENRES (Total Revenue) ---")
print(profitable_genres)
print("\n" + "=" * 50 + "\n")

# ----------------------------------------------------
# 2. BONUS TASKS
# ----------------------------------------------------

# Bonus B: Top 5 Movies (Based on Revenue)
top_5_movies = df.nlargest(5, "Revenue")
print("--- BONUS: TOP 5 MOVIES BY REVENUE ---")
print(top_5_movies[["Movie Name", "Revenue"]])
print("\n" + "=" * 50 + "\n")

# Bonus A: Correlation Between Rating & Revenue Calculation
correlation_value = df["Rating"].corr(df["Revenue"])
print(f"--- BONUS: CORRELATION BETWEEN RATING & REVENUE ---")
print(f"Pearson Correlation Coefficient: {correlation_value:.2f}")

# ----------------------------------------------------
# 3. VISUALIZE: Plotting the Results
# ----------------------------------------------------
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Genre vs Revenue (Bar Plot)
sns.barplot(ax=axes[0, 0], data=df, x="Genre", y="Revenue", estimator=sum, errorbar=None, palette="muted")
axes[0, 0].set_title("Genre vs Total Revenue")
axes[0, 0].set_xlabel("Genre")
axes[0, 0].set_ylabel("Total Revenue (in Millions)")

# Plot 2: Rating Distribution (Histogram / KDE)
sns.histplot(ax=axes[0, 1], data=df, x="Rating", kde=True, color="skyblue", bins=6)
axes[0, 1].set_title("Distribution of Movie Ratings")
axes[0, 1].set_xlabel("Rating")
axes[0, 1].set_ylabel("Count")

# Plot 3: Correlation (Scatter Plot - Bonus Task)
sns.scatterplot(ax=axes[1, 0], data=df, x="Rating", y="Revenue", hue="Genre", s=100)
sns.regplot(ax=axes[1, 0], data=df, x="Rating", y="Revenue", scatter=False, color="red", linestyle="--")
axes[1, 0].set_title(f"Correlation: Rating vs Revenue (r = {correlation_value:.2f})")
axes[1, 0].set_xlabel("Movie Rating")
axes[1, 0].set_ylabel("Revenue (in Millions)")

# Plot 4: Top 5 Movies by Revenue (Horizontal Bar Plot for variety)
sns.barplot(ax=axes[1, 1], data=top_5_movies, x="Revenue", y="Movie Name", palette="viridis")
axes[1, 1].set_title("Top 5 Highest Grossing Movies")
axes[1, 1].set_xlabel("Revenue (in Millions)")
axes[1, 1].set_ylabel("Movie Name")

# Adjust layout and display plots
plt.tight_layout()
plt.show()