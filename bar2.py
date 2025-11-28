import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("PRDECT-ID Dataset_500.xlsx")

df["Emotion"].value_counts().plot(kind="bar", figsize=(7,4))
plt.title("Distribusi Emosi Pelanggan")
plt.xlabel("Emosi")
plt.ylabel("Jumlah")
plt.show()