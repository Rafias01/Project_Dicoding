import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  
data_path = os.path.join(base_path, "data")

# Path lengkap ke file CSV
path_day = os.path.join(data_path, "day.csv")
path_hour = os.path.join(data_path, "hour.csv")

day_df = pd.read_csv(path_day)
hour_df = pd.read_csv(path_hour)

# Menghitung rata-rata peminjaman sepeda per musim
peminjaman_per_musim = day_df.groupby("season")["cnt"].mean().reset_index()

# Menghitung total peminjaman sepeda per jam
peminjaman_per_jam = hour_df.groupby("hr")["cnt"].sum().reset_index()

# Mapping label musim
season_labels = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Dingin"}
peminjaman_per_musim["season_label"] = peminjaman_per_musim["season"].map(season_labels)

# Streamlit App
st.title("📊 Analisis Peminjaman Sepeda")

# Sidebar untuk filter interaktif
st.sidebar.header("Filter Data")
season_options = ["All Seasons", "Semi", "Panas", "Gugur", "Dingin"]
season_mapping = {"All Seasons": None, "Semi": 1, "Panas": 2, "Gugur": 3, "Dingin": 4}
selected_season = st.sidebar.selectbox("Pilih Musim", season_options)
selected_hour = st.sidebar.slider("Pilih Rentang Jam", 0, 23, (0, 23))

# Menampilkan Identitas di Sidebar
st.sidebar.markdown("### Identitas")
st.sidebar.text("Nama  : Rafi Ananda Subekti")
st.sidebar.text("Email : rafiasubekti@gmail.com")
st.sidebar.text("Cohort ID : MC009D5Y0612")
st.sidebar.text("Kelas : MC-52")

# Filter Data berdasarkan Musim
if season_mapping[selected_season] is None:
    filtered_season_data = peminjaman_per_musim
else:
    filtered_season_data = peminjaman_per_musim[peminjaman_per_musim["season"] == season_mapping[selected_season]]

# Filter Data berdasarkan Jam
filtered_hour_data = peminjaman_per_jam[
    (peminjaman_per_jam["hr"] >= selected_hour[0]) & (peminjaman_per_jam["hr"] <= selected_hour[1])
]

# Visualisasi Peminjaman Berdasarkan Musim
st.subheader("📌 Banyaknya Penggunaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(x="season_label", y="cnt",data=filtered_season_data, palette="coolwarm", legend=False)

# Menyesuaikan label sumbu X agar sejajar dengan batang
ax.set_xlabel("Musim Peminjaman")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")
ax.grid(axis='y')

st.pyplot(fig)

# Visualisasi Peminjaman Berdasarkan Jam
st.subheader("⏰ Total Peminjaman Sepeda Berdasarkan Jam")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="hr", y="cnt", data=filtered_hour_data, marker="o", color="b")
ax.set_xlabel("Jam (hr)")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_xticks(range(0, 24))
ax.grid(True)
st.pyplot(fig)

st.write("\n**🔍 Keterangan:** Kita bisa memilih musim dan rentang jam untuk melihat tren peminjaman sepeda berdasarkan filter yang kita pilih.")
