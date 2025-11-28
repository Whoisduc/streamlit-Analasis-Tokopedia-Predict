import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ========================
# PAGE CONFIG
# ========================
st.set_page_config(page_title="Dashboard Tokopedia", layout="wide")

# ========================
# CUSTOM CSS – FUTURISTIC GLOW DARK MODE + PLACEHOLDER INDONESIA
# ========================
st.markdown("""
<style>

/* MAIN BACKGROUND */
.block-container {
    background: #0d0d0f;
    padding: 2rem 2.5rem;
}

/* TEXT COLOR */
h1, h2, h3, h4, p, div, label, span {
    color: #e6e6e6 !important;
    font-family: 'Segoe UI', sans-serif;
}

/* GLOW CARD */
.glow-card {
    background: rgba(20, 20, 30, 0.55);
    backdrop-filter: blur(8px);
    padding: 18px 20px;
    border-radius: 15px;
    border: 1px solid rgba(120, 120, 255, 0.25);
    box-shadow: 0 0 12px rgba(140, 0, 255, 0.25);
    margin-bottom: 18px;
}

/* TITLE BOX */
.glow-title {
    background: linear-gradient(90deg, rgba(140,0,255,0.4), rgba(0,150,255,0.4));
    padding: 22px 30px;
    border-radius: 15px;
    margin-top: 30px;
    margin-bottom: 25px;
    border: 1px solid rgba(200,200,255,0.2);
    box-shadow: 0 0 25px rgba(140,0,255,0.4);
}

.glow-title h1 {
    color: white !important;
    font-size: 30px;
    font-weight: 800;
    letter-spacing: 1px;
}

.subtext {
    color: #dcdcdc !important;
    opacity: 0.85;
}

/* TAB STYLE */
div[role="tablist"] {
    background: rgba(40,40,60,0.4);
    border-radius: 12px;
    padding: 8px;
}

div[role="tab"] {
    color: white !important;
    font-weight: 600;
}

/* CUSTOM PLACEHOLDER INDONESIA UNTUK MULTISELECT */
div[data-baseweb="select"] input::placeholder {
    color: #bbbbbb !important;
    opacity: 0.85;
    font-style: italic;
}

/* SCROLLBAR */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: rgba(120,120,255,0.4);
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ========================
# HEADER
# ========================
st.markdown("""
<div class="glow-title">
    <h1>DASHBOARD TOKOPEDIA</h1>
    <p class="subtext">Analisis Produk & Review • PRDECT-ID Dataset (500 baris)</p>
    <h1>TIM FUBUKI</h1>
    <p class="subtext">1. M.Nur Alfiansyah (2371020139)</p>
    <p class="subtext">2. Sultan Muliya Pratama (2371020152)</p>
</div>
""", unsafe_allow_html=True)

# ========================
# LOAD DATA
# ========================
@st.cache_data
def load_data():
    return pd.read_excel("PRDECT-ID Dataset_500.xlsx")

df = load_data()

# ========================
# SIDEBAR FILTER (MULTISELECT + PLACEHOLDER)
# ========================
st.sidebar.markdown("<h2 style='color:#9d4dff;'>FILTER DATA</h2>", unsafe_allow_html=True)

categories = st.sidebar.multiselect(
    "Pilih Kategori Produk:",
    sorted(df["Category"].unique().tolist()),
    placeholder="Pilih kategori"
)

locations = st.sidebar.multiselect(
    "Pilih Lokasi Penjual:",
    sorted(df["Location"].unique().tolist()),
    placeholder="Pilih lokasi"
)

sentiments = st.sidebar.multiselect(
    "Pilih Sentimen Review:",
    sorted(df["Sentiment"].unique().tolist()),
    placeholder="Pilih sentimen"
)

emotions = st.sidebar.multiselect(
    "Pilih Emosi Pelanggan:",
    sorted(df["Emotion"].unique().tolist()),
    placeholder="Pilih emosi"
)

# ========================
# APPLY FILTER (MULTISELECT)
# ========================
filtered_df = df.copy()

if categories:
    filtered_df = filtered_df[filtered_df["Category"].isin(categories)]

if locations:
    filtered_df = filtered_df[filtered_df["Location"].isin(locations)]

if sentiments:
    filtered_df = filtered_df[filtered_df["Sentiment"].isin(sentiments)]

if emotions:
    filtered_df = filtered_df[filtered_df["Emotion"].isin(emotions)]

# ========================
# TABS
# ========================
tab1, tab2, tab3 = st.tabs(["📊 Statistik Ringkas", "📈 Visualisasi", "📋 Data Detail"])

# ========================
# TAB 1 – STATISTIK
# ========================
with tab1:

    st.markdown("<h2 style='color:#a970ff;'>📊 Statistik Ringkas</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    col1.markdown(f"""
    <div class="glow-card">
        <h3>Jumlah Produk</h3>
        <h1>{len(filtered_df)}</h1>
    </div>
    """, unsafe_allow_html=True)

    avg_price = filtered_df["Price"].mean()
    price_display = "Tidak Ada Data" if np.isnan(avg_price) else f"Rp {int(avg_price):,}"

    col2.markdown(f"""
    <div class="glow-card">
        <h3>Rata-rata Harga</h3>
        <h1>{price_display}</h1>
    </div>
    """, unsafe_allow_html=True)

    avg_rating = filtered_df["Customer Rating"].mean()
    rating_display = "Tidak Ada Data" if np.isnan(avg_rating) else round(avg_rating, 2)

    col3.markdown(f"""
    <div class="glow-card">
        <h3>Rata-rata Rating</h3>
        <h1>{rating_display}</h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='color:#a970ff;'>📘 Statistik Deskriptif</h2>", unsafe_allow_html=True)

    if not filtered_df.empty:
        numeric_cols = ["Price", "Overall Rating", "Number Sold", "Total Review", "Customer Rating"]
        stats_df = pd.DataFrame({
            "Mean": filtered_df[numeric_cols].mean(),
            "Median": filtered_df[numeric_cols].median(),
            "Mode": filtered_df[numeric_cols].mode().iloc[0],
            "Std Dev": filtered_df[numeric_cols].std()
        })
        st.dataframe(stats_df)
    else:
        st.info("Tidak ada data setelah filter diterapkan.")

# ========================
# TAB 2 – VISUALISASI
# ========================
with tab2:

    if filtered_df.empty:
        st.warning("Tidak ada data untuk divisualisasikan. Ubah filter di sidebar.")
    else:
        st.markdown("<h2 style='color:#a970ff;'>📈 Visualisasi Data</h2>", unsafe_allow_html=True)

        colA, colB = st.columns(2)

        with colA:
            st.markdown("<div class='glow-card'><h3>Kategori Produk</h3></div>", unsafe_allow_html=True)
            fig1, ax1 = plt.subplots(figsize=(6,4))
            filtered_df["Category"].value_counts().plot(kind="bar", color="#a970ff", ax=ax1)
            st.pyplot(fig1)

        with colB:
            st.markdown("<div class='glow-card'><h3>Sentimen Pelanggan</h3></div>", unsafe_allow_html=True)
            fig2, ax2 = plt.subplots(figsize=(6,4))
            filtered_df["Sentiment"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax2)
            st.pyplot(fig2)

        st.markdown("<div class='glow-card'><h3>Harga vs Jumlah Terjual</h3></div>", unsafe_allow_html=True)
        fig3, ax3 = plt.subplots(figsize=(8,4))
        ax3.scatter(filtered_df["Price"], filtered_df["Number Sold"], color="#00d4ff")
        st.pyplot(fig3)

# ========================
# TAB 3 – DATA DETAIL
# ========================
with tab3:
    st.markdown("<h2 style='color:#a970ff;'>📋 Data Produk & Review</h2>", unsafe_allow_html=True)
    st.dataframe(filtered_df.reset_index(drop=True))
