import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("PRDECT-ID Dataset_500.xlsx")

plt.figure(figsize=(7,5))
sns.heatmap(df[["Price","Number Sold","Overall Rating","Customer Rating","Total Review"]].corr(),
            annot=True, cmap="coolwarm")
plt.title("Heatmap Korelasi Variabel Numerik")
plt.show()
