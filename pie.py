import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("PRDECT-ID Dataset_500.xlsx")

df["Sentiment"].value_counts().plot(kind="pie", autopct="%1.1f%%", figsize=(6,6))
plt.title("Distribusi Sentimen Pelanggan")
plt.ylabel("")
plt.show()