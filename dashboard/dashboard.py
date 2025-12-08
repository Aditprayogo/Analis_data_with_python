import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='dark')

hour_df = pd.read_csv('hour_dashboard.csv')
day_df = pd.read_csv('day_dashboard.csv')

# Load data
day_df = pd.read_csv('day_dashboard.csv')
hour_df = pd.read_csv('hour_dashboard.csv')

# Pastikan kolom dteday dalam format datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Tambahkan kolom year dari tanggal
day_df['year'] = day_df['dteday'].dt.year
hour_df['year'] = hour_df['dteday'].dt.year


st.set_page_config(layout="wide")
st.title("Bike Sharing Dashboard")


# Sidebar filter by month/year
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=150)
    st.markdown("## Filter Data")
    year = st.selectbox("Pilih Tahun", options=day_df['year'].unique())
    filtered_hour = hour_df[hour_df['year'] == year]
    filtered_day = day_df[day_df['year'] == year]


# 1. PERTANYAAN 1 - Kapan waktu puncak peminjaman sepeda terjadi dalam sehari?
st.subheader("Peminjaman Sepeda per Jam")
avg_hourly = filtered_hour.groupby('hr')['cnt'].mean().reset_index()


fig1, ax1 = plt.subplots(figsize=(10,5))
sns.lineplot(data=avg_hourly, x='hr', y='cnt', marker='o', ax=ax1)
ax1.set_title("Rata-rata Jumlah Peminjaman Sepeda per Jam")
ax1.set_xlabel("Jam")
ax1.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig1)


# 2. PERTANYAAN 2 - Pengaruh cuaca dan suhu terhadap peminjaman
st.subheader("Pengaruh Cuaca dan Suhu")
col1, col2 = st.columns(2)


with col1:
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.barplot(data=filtered_hour, x='weathersit', y='cnt', estimator='mean', ax=ax2)
    ax2.set_title("Rata-rata Peminjaman per Kondisi Cuaca")
    ax2.set_xlabel("Kondisi Cuaca")
    ax2.set_ylabel("Jumlah Peminjaman")
    st.pyplot(fig2)


with col2:
    fig3, ax3 = plt.subplots(figsize=(6,4))
    sns.scatterplot(data=filtered_hour, x='temp_celsius', y='cnt', alpha=0.3, ax=ax3)
    ax3.set_title("Pengaruh Suhu terhadap Jumlah Peminjaman")
    ax3.set_xlabel("Suhu (°C)")
    ax3.set_ylabel("Jumlah Peminjaman")
    st.pyplot(fig3)


# 3. PERTANYAAN 3 - Hari kerja vs hari libur
st.subheader("Perbandingan Hari Kerja dan Libur")
fig4, ax4 = plt.subplots(figsize=(8,4))
sns.barplot(data=filtered_day, x='workingday', y='cnt', estimator='mean', ax=ax4)
ax4.set_title("Rata-rata Peminjaman: Hari Kerja vs Hari Libur")
ax4.set_xlabel("Working Day (1 = Ya)")
ax4.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig4)


# Footer
st.caption("Copyright (c) Aditiya Ihzar Eka Prayogo 2025")
