# Dictionary

siswa = {
    "nama": "Budi",
    "umur": 15,
    "kelas": "10A"
}
print(siswa["nama"])  # Output: Budi
print(siswa["umur"])  # Output: 15
print(siswa["kelas"]) # Output: 10A

# Menambahkan data baru
siswa["alamat"] = "Jakarta"
print(siswa)

# Mengubah data
siswa["umur"] = 16
print(siswa)

# Menghapus data
del siswa["kelas"]
print(siswa)

# Perulangan melalui dictionary
for key in siswa:
    print(f"{key}: {siswa[key]}")
    
    
# Mengakses langsung keduanya
for key, value in siswa.items():
    print(f"{key}: {value}")
    
    
# Mengecek keanggotaan
if "nama" in siswa:
    print("Nama ditemukan dalam data siswa.")
else:
    print("Nama tidak ditemukan dalam data siswa.")
    
