# 🚲 Bike Sharing Dashboard with Streamlit

Dashboard ini dibuat untuk menganalisis data peminjaman sepeda dan memberikan insight interaktif melalui visualisasi. Proyek ini merupakan bagian dari submission *Analisis Data dengan Python* yang mencakup proses data cleaning, eksplorasi, visualisasi, serta penerapan teknik analisis lanjutan seperti **clustering** dan **RFM analysis**.

## 📌 Fitur Utama

🔍 **Exploratory Data Analysis**  
Melihat pola penggunaan sepeda berdasarkan waktu, cuaca, dan hari kerja/libur.

📊 **Data Visualization**  
Visualisasi interaktif yang efektif dan informatif menggunakan Matplotlib & Seaborn.

🏷️ **Customer Segmentation - Clustering**  
Pengelompokan pengguna berdasarkan pola peminjaman menggunakan manual grouping dan binning.

📈 **RFM Analysis**  
Menghitung Recency, Frequency, dan Monetary sebagai dasar analisis perilaku pengguna.

📁 **Dashboard Interaktif**  
Dibangun menggunakan **Streamlit** agar mudah digunakan dan dijalankan secara lokal.

---

## 🧾 Dataset

Dataset yang digunakan berasal dari [UCI Machine Learning Repository - Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset).

File yang digunakan:
- `hour_dashboard.csv`: Data peminjaman per jam
- `day_dashboard.csv`: Data peminjaman per hari

---

## 📂 Struktur Folder

```
submission/
│
├── dashboard/
│   ├── dashboard.py
│   ├── hour_dashboard.csv
│   └── day_dashboard.csv
│
├── data/
│   └── Bike-sharing-dataset/
│       ├── day.csv
│       ├── hour.csv
│       └── Readme.txt
│
├── Proyek_Analisis_Data.ipynb
├── cleaning.py
├── requirements.txt
├── README.md
└── streamlit_dashboard.png
```

---

## ⚙️ Cara Menjalankan Dashboard

### Persyaratan
Pastikan Anda sudah menginstall:

- Python ≥ 3.x
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Babel (jika digunakan untuk formatting tanggal/waktu)

### Instalasi
Clone repository ini dan install dependensi:

```bash
pip install -r requirements.txt
```

### Jalankan Dashboard

```bash
cd dashboard
streamlit run dashboard.py
```

Dashboard akan terbuka secara otomatis di browser Anda.

---

## 📌 Insight dari Dashboard

1. **Waktu Puncak Peminjaman**
   - Terjadi pada pukul 8 pagi dan 5-6 sore, sesuai dengan jam berangkat dan pulang kerja.

2. **Pengaruh Cuaca dan Suhu**
   - Semakin cerah cuaca dan semakin hangat suhu, jumlah peminjaman cenderung meningkat.

3. **Hari Kerja vs Hari Libur**
   - Hari libur justru menunjukkan rata-rata peminjaman yang sedikit lebih tinggi dibandingkan hari kerja.

---

## 📷 Preview Dashboard

![Streamlit Dashboard](/streamlit_dashboard.png)

---

## 🙌 Kontribusi & Kredit

Proyek ini dikerjakan oleh **Aditiya Ihzar Eka Prayogo** sebagai bagian dari pembelajaran di Dicoding Academy.

---

Kalau kamu ingin eksplorasi lebih jauh atau kontribusi, jangan ragu buat fork dan bintangin ⭐ repository ini!