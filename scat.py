import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("PRDECT-ID Dataset_500.xlsx")

plt.figure(figsize=(7,5))
plt.scatter(df["Price"], df["Number Sold"])
plt.title("Scatter Plot: Harga vs Jumlah Terjual")
plt.xlabel("Harga (Price)")
plt.ylabel("Jumlah Terjual (Number Sold)")
plt.show()
