import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("PRDECT-ID Dataset_500.xlsx")

# 1. Mean
mean_price = df["Price"].mean()
mean_sold = df["Number Sold"].mean()
mean_rating = df["Customer Rating"].mean()

# 2. Median
median_price = df["Price"].median()
median_sold = df["Number Sold"].median()
median_rating = df["Customer Rating"].median()

# 3. Mode
mode_category = df["Category"].mode()[0]
mode_location = df["Location"].mode()[0]
mode_sentiment = df["Sentiment"].mode()[0]

# 4. Standard Deviation
std_price = df["Price"].std()
std_sold = df["Number Sold"].std()
std_rating = df["Customer Rating"].std()

# 5. Distribusi
price_dist = df["Price"].describe()
sentiment_dist = df["Sentiment"].value_counts()

# 6. Korelasi
corr = df[["Price", "Number Sold", "Overall Rating", "Customer Rating", "Total Review"]].corr()

# Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

mean_price, median_price, mode_category, std_price, corr
