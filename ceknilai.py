# Data mahasiswa
mahasiswa = [
    {"nama": "Muhammad", "nim": 12345, "kelas": "A"},
    {"nama": "Rafi", "nim": 67890, "kelas": "B"},
    {"nama": "Dwi", "nim": 11223, "kelas": "A"},
    {"nama": "Siti", "nim": 33445, "kelas": "C"},
    {"nama": "Ani", "nim": 55667, "kelas": "B"},
    {"nama": "Budi", "nim": 77889, "kelas": "C"},
]

# Input nama dulu
nama = input("Masukkan Nama Anda: ")

# Cari mahasiswa berdasarkan nama
data_mahasiswa = None
for mhs in mahasiswa:
    if mhs["nama"] == nama:
        data_mahasiswa = mhs
        break

# Kalau nama tidak ditemukan → berhenti
if not data_mahasiswa:
    print("Nama tidak ditemukan dalam daftar.")
    exit()

# Input NIM dan Kelas
nim = int(input("Masukkan NIM Anda: "))
if nim != data_mahasiswa["nim"]:
    print("NIM tidak sesuai dengan nama tersebut.")
    exit()

kelas = input("Masukkan Kelas Anda: ")
if kelas != data_mahasiswa["kelas"]:
    print("Kelas tidak sesuai dengan data mahasiswa.")
    exit()

# Kalau semua cocok, lanjut input nilai
nilaiUTS = int(input("Masukkan Nilai UTS: "))
nilaiUAS = int(input("Masukkan Nilai UAS: "))
nilaiTugas = int(input("Masukkan Nilai Tugas: "))
nilaiAbsen = int(input("Masukkan Nilai Absen: "))

# Hitung hasil akhir
hasil = (nilaiUTS * 0.20) + (nilaiUAS * 0.40) + (nilaiTugas * 0.20) + (nilaiAbsen * 0.20)

# Tentukan nilai huruf
if hasil >= 85:
    nilai_huruf = "A"
elif hasil >= 70:
    nilai_huruf = "B"
elif hasil >= 55:
    nilai_huruf = "C"
elif hasil >= 40:
    nilai_huruf = "D"
else:
    nilai_huruf = "E"

# Tampilkan hasil
print("\n--- Data Mahasiswa ---")
print("Nama  :", nama)
print("NIM   :", nim)
print("Kelas :", kelas)
print("Nilai Akhir :", int(hasil))
print("Nilai Huruf :", nilai_huruf)
