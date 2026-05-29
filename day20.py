import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 1. Import the multi-page PDF tool
from matplotlib.backends.backend_pdf import PdfPages

file_name = 'whi.csv'


df = pd.read_csv(file_name)
df = df.drop_duplicates()

keep_columns = ['Country', 'Happiness Score', 'Economy', 'Family', 'Health', 'Corruption']
df = df[keep_columns]

mean_family = df.loc[df['Family'] != 0, 'Family'].mean()
df['Family'] = df['Family'].replace(0, np.nan).fillna(mean_family)

df_top10 = df.sort_values(by='Happiness Score', ascending=False).head(10)



with PdfPages('Happiness_Report.pdf') as pdf:

    # --- PAGE 1: Happiness Score Bar Chart ---
    fig1 = plt.figure(figsize=(11, 8.5))
    sns.barplot(
        data=df_top10, x='Country', y='Happiness Score', 
        hue='Country', palette='viridis', legend=False
    )
    plt.title('Top 10 Countries by Happiness Score', fontsize=16, fontweight='bold', pad=15)
    plt.xticks(rotation=45)
    plt.tight_layout()
    pdf.savefig(fig1)  # Saves this figure as Page 1
    plt.close(fig1)    # Closes it to clear memory

    # --- PAGE 2: Economy vs Happiness Scatter Plot ---
    fig2 = plt.figure(figsize=(11, 8.5))
    sns.scatterplot(
        data=df_top10, x='Economy', y='Happiness Score', 
        hue='Country', palette='deep', s=200
    )
    plt.title('Economy (GDP per Capita) vs Happiness Score', fontsize=16, fontweight='bold', pad=15)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    pdf.savefig(fig2)  # Saves this figure as Page 2
    plt.close(fig2)

    # --- PAGE 3: Health Scores Line Plot ---
    fig3 = plt.figure(figsize=(11, 8.5))
    sns.lineplot(
        data=df_top10, x='Country', y='Health', 
        marker='o', markersize=10, color='teal', linewidth=3
    )
    plt.title('Health Ratings Across Top 10 Countries', fontsize=16, fontweight='bold', pad=15)
    plt.xticks(rotation=45)
    plt.tight_layout()
    pdf.savefig(fig3)  # Saves this figure as Page 3
    plt.close(fig3)

    # --- PAGE 4: Corruption Scores Horizontal Bar Chart ---
    fig4 = plt.figure(figsize=(11, 8.5))
    sns.barplot(
        data=df_top10, x='Corruption', y='Country', 
        hue='Corruption', palette='magma', legend=False
    )
    plt.title('Perceived Corruption Scores (Lower is Better)', fontsize=16, fontweight='bold', pad=15)
    plt.tight_layout()
    pdf.savefig(fig4)  # Saves this figure as Page 4
    plt.close(fig4)

print("Success! Your 4-page report has been saved as 'Happiness_Report.pdf'.")

plt.show()