import pandas as pd
import matplotlib.pyplot as plt

# Data transaksi toko bunga
data_transaksi = [
    {"No": 1, "Tanggal Transaksi": "2024-06-01", "Nama Pelanggan": "Andi", "Barang yang Dibeli": "Bunga Mawar Merah", "Jumlah": 10, "Total Belanja (IDR)": 500000},
    {"No": 2, "Tanggal Transaksi": "2024-06-03", "Nama Pelanggan": "Budi", "Barang yang Dibeli": "Bunga Lily Putih", "Jumlah": 5, "Total Belanja (IDR)": 350000},
    {"No": 3, "Tanggal Transaksi": "2024-06-07", "Nama Pelanggan": "Cindy", "Barang yang Dibeli": "Bunga Matahari Kuning", "Jumlah": 12, "Total Belanja (IDR)": 720000},
    {"No": 4, "Tanggal Transaksi": "2024-06-12", "Nama Pelanggan": "Dian", "Barang yang Dibeli": "Bunga Tulip Warna Campuran", "Jumlah": 8, "Total Belanja (IDR)": 400000},
    {"No": 5, "Tanggal Transaksi": "2024-06-15", "Nama Pelanggan": "Erika", "Barang yang Dibeli": "Bunga Anggrek Ungu", "Jumlah": 6, "Total Belanja (IDR)": 900000}
]

# Data stok barang di toko bunga
data_stok = [
    {"No": 1, "Nama Barang": "Bunga Mawar Merah", "Stok Tersedia": 50, "Harga Satuan (IDR)": 50000},
    {"No": 2, "Nama Barang": "Bunga Lily Putih", "Stok Tersedia": 30, "Harga Satuan (IDR)": 70000},
    {"No": 3, "Nama Barang": "Bunga Matahari Kuning", "Stok Tersedia": 40, "Harga Satuan (IDR)": 60000},
    {"No": 4, "Nama Barang": "Bunga Tulip Warna Campuran", "Stok Tersedia": 25, "Harga Satuan (IDR)": 50000},
    {"No": 5, "Nama Barang": "Bunga Anggrek Ungu", "Stok Tersedia": 15, "Harga Satuan (IDR)": 150000}
]

# Data penjualan bulanan toko bunga
data_penjualan_bulanan = [
    {"Bulan": "Januari", "Jumlah Transaksi": 50, "Total Pendapatan (IDR)": 5000000},
    {"Bulan": "Februari", "Jumlah Transaksi": 45, "Total Pendapatan (IDR)": 4500000},
    {"Bulan": "Maret", "Jumlah Transaksi": 55, "Total Pendapatan (IDR)": 5500000},
    {"Bulan": "April", "Jumlah Transaksi": 60, "Total Pendapatan (IDR)": 6000000},
    {"Bulan": "Mei", "Jumlah Transaksi": 65, "Total Pendapatan (IDR)": 6500000},
    {"Bulan": "Juni", "Jumlah Transaksi": 40, "Total Pendapatan (IDR)": 4000000}
]

# Data pelanggan setia toko bunga
data_pelanggan_setia = [
    {"Nama Pelanggan": "Andi", "Jumlah Transaksi": 5, "Total Belanja (IDR)": 2500000},
    {"Nama Pelanggan": "Budi", "Jumlah Transaksi": 7, "Total Belanja (IDR)": 2450000},
    {"Nama Pelanggan": "Cindy", "Jumlah Transaksi": 8, "Total Belanja (IDR)": 4000000},
    {"Nama Pelanggan": "Dian", "Jumlah Transaksi": 6, "Total Belanja (IDR)": 3200000},
    {"Nama Pelanggan": "Erika", "Jumlah Transaksi": 4, "Total Belanja (IDR)": 3600000}
]

# 1. Pembersihan Data (tidak perlu dilakukan karena data sudah bersih)

# 2. Analisis Deskriptif

# Data transaksi toko bunga
df_transaksi = pd.DataFrame(data_transaksi)
deskripsi_transaksi = df_transaksi.describe()
print("Statistik Deskriptif untuk Data Transaksi Toko Bunga:")
print(deskripsi_transaksi)

# Data stok barang di toko bunga
df_stok = pd.DataFrame(data_stok)
total_stok = df_stok["Stok Tersedia"].sum()
print("\nTotal Stok Barang di Toko Bunga:")
print(total_stok)

# Data penjualan bulanan toko bunga
df_penjualan_bulanan = pd.DataFrame(data_penjualan_bulanan)
rata_rata_pendapatan = df_penjualan_bulanan["Total Pendapatan (IDR)"].mean()
median_pendapatan = df_penjualan_bulanan["Total Pendapatan (IDR)"].median()
std_deviasi_pendapatan = df_penjualan_bulanan["Total Pendapatan (IDR)"].std()
print("\nAnalisis Deskriptif untuk Penjualan Bulanan Toko Bunga:")
print(f"Rata-rata Pendapatan Bulanan: IDR {rata_rata_pendapatan:.0f}")
print(f"Median Pendapatan Bulanan: IDR {median_pendapatan:.0f}")
print(f"Standar Deviasi Pendapatan Bulanan: IDR {std_deviasi_pendapatan:.0f}")

# Data pelanggan setia toko bunga
df_pelanggan_setia = pd.DataFrame(data_pelanggan_setia)
frekuensi_transaksi = df_pelanggan_setia["Jumlah Transaksi"].value_counts()
print("\nDistribusi Frekuensi untuk Jumlah Transaksi Pelanggan Setia:")
print(frekuensi_transaksi)

# 3. Visualisasi Data

# Histogram untuk distribusi jumlah barang yang dibeli
plt.figure(figsize=(8, 6))
plt.hist(df_transaksi["Jumlah"], bins=5, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Jumlah Barang yang Dibeli')
plt.ylabel('Frekuensi')
plt.title('Histogram Distribusi Jumlah Barang yang Dibeli')
plt.grid(True)
plt.show()

# Grafik bar untuk total pendapatan bulanan
plt.figure(figsize=(10, 6))
plt.bar(df_penjualan_bulanan["Bulan"], df_penjualan_bulanan["Total Pendapatan (IDR)"], color='green')
plt.xlabel('Bulan')
plt.ylabel('Total Pendapatan (IDR)')
plt.title('Total Pendapatan Bulanan Toko Bunga')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Pie chart untuk distribusi frekuensi jumlah transaksi pelanggan setia
plt.figure(figsize=(8, 6))
plt.pie(frekuensi_transaksi, labels=frekuensi_transaksi.index, autopct='%1.1f%%', startangle=140)
plt.title('Proporsi Jumlah Transaksi Pelanggan Setia')
plt.axis('equal')
plt.tight_layout()
plt.show()
