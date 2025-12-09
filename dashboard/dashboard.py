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

    st.markdown("---")
    st.markdown("### Info Dataset")
    st.markdown(f"Jumlah data (day): {filtered_day.shape[0]}")
    st.markdown(f"Jumlah data (hour): {filtered_hour.shape[0]}")
    st.markdown(f"Rentang tanggal: {filtered_day['dteday'].min().date()} s/d {filtered_day['dteday'].max().date()}")
    st.markdown("- Periode: 2011-2012")
    st.markdown("- Sumber: UCI ML Repository")


# 1. PERTANYAAN 1 - Kapan waktu puncak peminjaman sepeda terjadi dalam sehari?
st.subheader("Peminjaman Sepeda per Jam")
avg_hourly = filtered_hour.groupby('hr')['cnt'].mean().reset_index()
fig1, ax1 = plt.subplots(figsize=(10,5))
sns.lineplot(data=avg_hourly, x='hr', y='cnt', marker='o', ax=ax1)
ax1.set_title("Rata-rata Jumlah Peminjaman Sepeda per Jam")
ax1.set_xlabel("Jam")
ax1.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig1)
st.markdown("Insight: Jumlah peminjaman memuncak sekitar jam 08.00 dan 17.00, mencerminkan pola mobilitas pekerja.")


# 2. PERTANYAAN 2 - Pengaruh cuaca dan suhu terhadap peminjaman
st.subheader("Pengaruh Cuaca dan Suhu")
col1, col2 = st.columns(2)

# Buat kolom label cuaca agar cocok dengan warna
weather_labels = {
    1: 'Cerah',
    2: 'Berawan',
    3: 'Hujan Ringan',
    4: 'Ekstrem'
}

# Mapping label cuaca ke kolom baru
filtered_hour['weather_label'] = filtered_hour['weathersit'].map(weather_labels)

# Buat palette sesuai label (string)
weather_palette = {
    'Cerah': '#9beee0',
    'Berawan': '#fdd835',
    'Hujan Ringan': '#ff7043',
    'Ekstrem': '#d32f2f'
}

with col1:
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.barplot(
        data=filtered_hour,
        x='weather_label',  # Gunakan label sebagai x
        y='cnt',
        estimator='mean',
        palette=weather_palette,
        ax=ax2
    )
    ax2.set_title("Rata-rata Peminjaman Berdasarkan Kondisi Cuaca")
    ax2.set_xlabel("Kondisi Cuaca")
    ax2.set_ylabel("Jumlah Peminjaman")
    st.pyplot(fig2)
    st.markdown("Insight: Peminjaman sepeda cenderung lebih tinggi saat cuaca cerah dan menurun drastis saat cuaca ekstrem.")


with col2:
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    scatter = sns.scatterplot(
        data=filtered_hour,
        x='temp_celsius',
        y='cnt',
        hue='temp_celsius',
        palette='coolwarm',
        alpha=0.6,
        linewidth=0,
        ax=ax3,
        legend='brief'
    )
    ax3.set_title("Pengaruh Suhu terhadap Jumlah Peminjaman Sepeda")
    ax3.set_xlabel("Suhu (°C)")
    ax3.set_ylabel("Jumlah Peminjaman")
    ax3.legend(title="Suhu (°C)", loc='upper left')
    st.pyplot(fig3)
    st.markdown("Insight: Semakin tinggi suhu (dalam rentang nyaman), jumlah peminjaman meningkat.")


# 3. PERTANYAAN 3 - Hari kerja vs hari libur
st.subheader("Perbandingan Hari Kerja dan Libur")
filtered_day['kategori_hari'] = filtered_day['workingday'].map({0: 'Hari Non-Kerja', 1: 'Hari Kerja'})
day_palette = {
    'Hari Non-Kerja': '#90CAF9',  
    'Hari Kerja': '#EF5350'      
}
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.barplot(
    data=filtered_day,
    x='kategori_hari',
    y='cnt',
    estimator='mean',
    palette=day_palette,
    ax=ax4
)
ax4.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Kategori Hari")
ax4.set_xlabel("Kategori Hari")
ax4.set_ylabel("Rata-rata Jumlah Peminjaman")
st.pyplot(fig4)
st.markdown("Insight: Peminjaman sedikit lebih tinggi pada hari kerja dibandingkan hari libur.")


# Rata-rata peminjaman per musim
st.subheader("Peminjaman Berdasarkan Musim")
season_labels = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
filtered_day['season_label'] = filtered_day['season'].map(season_labels)
season_palette = {'Spring': '#AED581', 'Summer': '#FFF176', 'Fall': '#FF8A65', 'Winter': '#4FC3F7'}


fig5, ax5 = plt.subplots(figsize=(8,5))
sns.barplot(data=filtered_day, x='season_label', y='cnt', estimator='mean', palette=season_palette, ax=ax5)
ax5.set_title("Rata-rata Peminjaman Berdasarkan Musim")
ax5.set_xlabel("Musim")
ax5.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig5)
st.markdown("Insight: Aktivitas peminjaman sepeda cenderung tinggi di musim gugur dan musim panas.")

# 5. Tambahan: Distribusi peminjaman per hari dalam seminggu
st.subheader("Peminjaman Sepeda per Hari dalam Minggu")
filtered_day['weekday_name'] = filtered_day['dteday'].dt.day_name()
order_hari = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


fig6, ax6 = plt.subplots(figsize=(10,5))
sns.barplot(data=filtered_day, x='weekday_name', y='cnt', order=order_hari, palette='Set2', ax=ax6)
ax6.set_title("Distribusi Peminjaman per Hari")
ax6.set_xlabel("Hari")
ax6.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig6)
st.markdown("Insight: Peminjaman cenderung tinggi pada akhir pekan, kemungkinan untuk aktivitas rekreasi.")


# Footer
st.caption("Copyright (c) Aditiya Ihzar Eka Prayogo 2025")
