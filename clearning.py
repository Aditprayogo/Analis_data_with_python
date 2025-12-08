# %% [markdown]
# # Proyek Analisis Data: [Input Nama Dataset]
# - **Nama:** Aditiya Ihzar Eka Prayogo
# - **Email:** adit.ihzar@gmail.com
# - **ID Dicoding:** aditPrayogo

# %% [markdown]
# ## Menentukan Pertanyaan Bisnis

# %% [markdown]
# - Kapan waktu puncak peminjaman sepeda terjadi dalam sehari?
# - Apa pengaruh cuaca dan suhu terhadap jumlah peminjam sepeda?
# - Apakah hari kerja dan hari libur memengaruhi peminjaman?

# %% [markdown]
# ## Import Semua Packages/Library yang Digunakan

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# %% [markdown]
# ## Data Wrangling

# %% [markdown]
# ### Gathering Data

# %%
# Load Tabel Day
day_df = pd.read_csv('data/day.csv')
day_df.head()

# %%
# Load Table Hour
hour_df = pd.read_csv('data/hour.csv')
hour_df.head()

# %% [markdown]
# **Insight:**
# - xxx
# - xxx

# %% [markdown]
# ### Assessing Data

# %%
hour_df.info()
day_df.info()

# %%
# Checking missing values in hour_df
print(hour_df.isnull().sum())

# %%
# Check for missing values in day_df
print(day_df.isnull().sum())

# %%
# Check for duplicates in hour_df
print(f"Number of duplicate rows in hour_df: {hour_df.duplicated().sum()}")

# %%
# Checking missing values in day_df
print(f"Number of duplicate rows in day_df: {day_df.duplicated().sum()}")

# %%
# Checking Statistical Summary hour_df
hour_df.describe()

# %%
# Checking Statistical Summary day_df
day_df.describe()

# %% [markdown]
# **Insight:**
# - xxx
# - xxx

# %% [markdown]
# ### Cleaning Data

# %%
# Menghapus kolom yang tidak relevan
hour_df.drop(columns=['instant'], inplace=True)
day_df.drop(columns=['instant'], inplace=True)

# %%
# Mengubah kolom kategori ke tipe data kategorikal
kategori_cols = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'hr']
for col in kategori_cols:
    if col in hour_df.columns:
        hour_df[col] = hour_df[col].astype('category')

for col in kategori_cols:
    if col in day_df.columns:
        day_df[col] = day_df[col].astype('category')

# %%
# Cek apakah total pengguna sesuai
assert (day_df['casual'] + day_df['registered'] == day_df['cnt']).all()
assert (hour_df['casual'] + hour_df['registered'] == hour_df['cnt']).all()

# %%
# Menggunakan IQR untuk mendeteksi outlier pada kolom cnt
Q1 = hour_df['cnt'].quantile(0.25)
Q3 = hour_df['cnt'].quantile(0.75)
IQR = Q3 - Q1
outliers = hour_df[(hour_df['cnt'] < Q1 - 1.5*IQR) | (hour_df['cnt'] > Q3 + 1.5*IQR)]
print(f"Jumlah outlier cnt: {len(outliers)}")

# %%
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Cek duplikat berdasarkan tanggal & jam
duplicates = hour_df.duplicated(subset=['dteday', 'hr']).sum()
print(f'Duplikasi berdasarkan tanggal dan jam: {duplicates}')

# %%
hour_df['temp_celsius'] = hour_df['temp'] * 41

# %%
hour_df.rename(columns={'yr': 'year', 'mnth': 'month'}, inplace=True)

# %%
# Berapa banyak nilai windspeed = 0?
print((hour_df['windspeed'] == 0).sum())

# %% [markdown]
# **Insight:**
# - xxx
# - xxx

# %% [markdown]
# ## Exploratory Data Analysis (EDA)

# %% [markdown]
# ### Explore ...

# %%


# %% [markdown]
# **Insight:**
# - xxx
# - xxx

# %% [markdown]
# ## Visualization & Explanatory Analysis

# %% [markdown]
# ### Pertanyaan 1:

# %%


# %% [markdown]
# ### Pertanyaan 2:

# %%


# %% [markdown]
# **Insight:**
# - xxx
# - xxx

# %% [markdown]
# ## Analisis Lanjutan (Opsional)

# %%


# %% [markdown]
# ## Conclusion

# %% [markdown]
# - Conclution pertanyaan 1
# - Conclution pertanyaan 2


