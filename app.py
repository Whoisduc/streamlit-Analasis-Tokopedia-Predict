import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ========================
# KONFIGURASI HALAMAN
# ========================
st.title("TIM FUBUKI\n 1. M.Nur Alfiansyah (2371020139) \n 2. Sultan Muliya Pratama (2371020152)")

st.set_page_config(
    layout="wide",
    page_title="Dashboard Analisis Tokopedia - PRDECT-ID"
)

st.title("Dashboard Analisis Produk & Review Tokopedia (PRDECT-ID Dataset)")

# ========================
# LOAD DATASET
# ========================
@st.cache_data
def load_data():
    df = pd.read_excel("PRDECT-ID Dataset_500.xlsx")
    return df

df = load_data()

# ========================
# SIDEBAR FILTERS
# ========================
st.sidebar.header("Filter Data")

# Filter kategori
categories = ["All"] + sorted(df["Category"].unique().tolist())
selected_category = st.sidebar.selectbox("Pilih Kategori Produk:", categories)

# Filter lokasi
locations = ["All"] + sorted(df["Location"].unique().tolist())
selected_location = st.sidebar.selectbox("Pilih Lokasi Penjual:", locations)

# Filter sentimen
sentiments = ["All"] + sorted(df["Sentiment"].unique().tolist())
selected_sentiment = st.sidebar.selectbox("Pilih Sentimen Review:", sentiments)

# Filter emosi (Emotion)
emotions = ["All"] + sorted(df["Emotion"].unique().tolist())
selected_emotion = st.sidebar.selectbox("Pilih Emosi Pelanggan:", emotions)

# ========================
# APPLY FILTERS
# ========================
filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

if selected_location != "All":
    filtered_df = filtered_df[filtered_df["Location"] == selected_location]

if selected_sentiment != "All":
    filtered_df = filtered_df[filtered_df["Sentiment"] == selected_sentiment]

if selected_emotion != "All":
    filtered_df = filtered_df[filtered_df["Emotion"] == selected_emotion]

# ========================
# RINGKASAN DATA
# ========================
st.subheader("Ringkasan Data Setelah Filter")

col1, col2, col3 = st.columns(3)

# Jumlah produk
col1.metric("Jumlah Produk", len(filtered_df))

# Rata-rata harga
avg_price = filtered_df["Price"].mean()
if np.isnan(avg_price):
    col2.metric("Rata-rata Harga", "Tidak Ada Data")
else:
    col2.metric("Rata-rata Harga", f"Rp {int(avg_price):,}")

# Rata-rata rating
avg_rating = filtered_df["Customer Rating"].mean()
if np.isnan(avg_rating):
    col3.metric("Rata-rata Rating", "Tidak Ada Data")
else:
    col3.metric("Rata-rata Rating", round(avg_rating, 2))

# ========================
# STATISTIK DESKRIPTIF
# ========================
st.subheader("Statistik Deskriptif")

if not filtered_df.empty:
    numeric_cols = ["Price", "Overall Rating", "Number Sold", "Total Review", "Customer Rating"]

    # Hitung statistik
    mean_vals = filtered_df[numeric_cols].mean()
    median_vals = filtered_df[numeric_cols].median()
    std_vals = filtered_df[numeric_cols].std()
    mode_vals = filtered_df[numeric_cols].mode().iloc[0]

    # Tabel statistik
    stats_df = pd.DataFrame({
        "Mean": mean_vals,
        "Median": median_vals,
        "Modus": mode_vals,
        "Std Dev": std_vals
    })

    st.dataframe(stats_df)

    # Histogram harga (distribusi data)
    st.subheader("Distribusi Harga Produk (Histogram)")
    fig_hist, ax_hist = plt.subplots(figsize=(8, 4))
    ax_hist.hist(filtered_df["Price"], bins=30, edgecolor='black')
    ax_hist.set_xlabel("Harga Produk")
    ax_hist.set_ylabel("Frekuensi")
    ax_hist.set_title("Distribusi Harga Produk")
    st.pyplot(fig_hist)

else:
    st.info("Statistik tidak dapat ditampilkan karena data kosong akibat filter.")

# Kalau tidak ada data sama sekali setelah filter, jangan gambar grafik lain
if filtered_df.empty:
    st.warning("Tidak ada data untuk kombinasi filter yang dipilih. Silakan ubah filter di sidebar.")
else:
    # ========================
    # GRAPH 1 – Bar Chart Category
    # ========================
    st.subheader("Jumlah Produk per Kategori")

    fig1, ax1 = plt.subplots(figsize=(8, 4))
    filtered_df["Category"].value_counts().plot(kind="bar", ax=ax1)
    ax1.set_xlabel("Kategori")
    ax1.set_ylabel("Jumlah")
    ax1.set_title("Distribusi Produk per Kategori")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig1)

    # ========================
    # GRAPH 2 – Pie Chart Sentiment
    # ========================
    st.subheader("Distribusi Sentimen Pelanggan")

    fig2, ax2 = plt.subplots(figsize=(6, 6))
    filtered_df["Sentiment"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax2)
    ax2.set_ylabel("")
    ax2.set_title("Proporsi Sentimen Review")
    st.pyplot(fig2)

    # ========================
    # GRAPH 3 – Scatter Plot Price vs Number Sold
    # ========================
    st.subheader("Scatter Plot: Harga vs Jumlah Terjual")

    fig3, ax3 = plt.subplots(figsize=(8, 5))
    ax3.scatter(filtered_df["Price"], filtered_df["Number Sold"])
    ax3.set_xlabel("Harga Produk (Price)")
    ax3.set_ylabel("Jumlah Terjual (Number Sold)")
    ax3.set_title("Hubungan Harga dan Jumlah Terjual")
    st.pyplot(fig3)

# ========================
# DATA TABLE
# ========================
st.subheader("Data Produk & Review (Setelah Filter)")
st.dataframe(filtered_df.reset_index(drop=True))
