import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("PRDECT-ID Dataset_500.xlsx")

df["Category"].value_counts().plot(kind="bar", figsize=(7,4))
plt.title("Jumlah Produk per Kategori")
plt.xlabel("Kategori Produk")
plt.ylabel("Jumlah")
plt.show()
