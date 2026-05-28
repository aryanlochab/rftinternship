import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

#lets grab 1 year of apple data
ticker = 'HINDUNILVR.NS'
data = yf.download(ticker, start='2025-01-01', end='2026-05-01')
df = data[['Close']].copy()
df.columns = ['Price']

#moving avg
df['MA_20'] = df['Price'].rolling(window=20).mean()

#local peak and local drop
df['Peak'] = (df['Price'] > df['Price'].shift(1)) & (df['Price'] > df['Price'].shift(-1))

df['Drop'] = (df['Price'] < df['Price'].shift(1)) & (df['Price'] < df['Price'].shift(-1))

plt.figure(figsize=(14, 7))
plt.plot(df.index, df['Price'], label='Actual Stock Price', color='blue', alpha=0.6)
plt.plot(df.index, df['MA_20'], label='20-Day Moving Average', color='orange', linestyle='--')

plt.scatter(df[df['Peak']].index, df[df['Peak']]['Price'], 
            color='green', marker='^', label='Peaks', s=60, zorder=5)

plt.scatter(df[df['Drop']].index, df[df['Drop']]['Price'], 
            color='red', marker='v', label='Drops', s=60, zorder=5)

plt.title(f'{ticker} Stock Price Analysis - Trend, MA, Peaks & Drops', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, linestyle=':', alpha=0.6)

# Show the plot
plt.tight_layout()
plt.show()