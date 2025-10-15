# Mengakses Eleman List
daftar_buah = ["apel", "pisang", "jeruk", "mangga"]
print("Buah pertama:", daftar_buah[0])  # Mengakses elemen pertama
print("Buah kedua:", daftar_buah[1])    # Mengakses elemen kedua
print("Buah terakhir:", daftar_buah[-1]) # Mengakses elemen terakhir

# Mengubah Eleman List
daftar_buah[1] = "kiwi"  # Mengubah elemen kedua
print("Daftar buah setelah diubah:", daftar_buah)

# Menambahkan Eleman List
daftar_buah.append("nanas")  # Menambahkan elemen di akhir list
print("Daftar buah setelah ditambahkan:", daftar_buah)
daftar_buah.insert(1, "stroberi")  # Menambahkan elemen di indeks 1
print("Daftar buah setelah disisipkan:", daftar_buah)

# Hapus Eleman List
del daftar_buah[2]  # Menghapus elemen di indeks 2
print("Daftar buah setelah dihapus:", daftar_buah)
daftar_buah.remove("mangga")  # Menghapus elemen dengan nilai "mangga"
print("Daftar buah setelah menghapus mangga:", daftar_buah)
daftar_buah.pop()  # Menghapus elemen terakhir
print("Daftar buah setelah pop:", daftar_buah)

# Menghitung Panjang List
panjang = len(daftar_buah)
print("Panjang daftar buah:", panjang)

# Looping melalui List
print("Daftar buah:")
for buah in daftar_buah:
    print("-", buah)
# List kosong

# Menggunakan list() untuk membuat list dari iterable
satu = [1, 2, 3]
print("List dari iterable:", list(satu))
dua = ['a', 'b', 'c']
print("List dari iterable:", list(dua))

gabungan = satu + dua
print("Gabungan dua list:", gabungan)

# Mengulang elemen dalam list
ulang = ["Mangga"] * 5
print("List dengan elemen diulang:", ulang)

# Perulangan list

banyak_buat = ["apel", "pisang", "jeruk"]
for buah in banyak_buat:
    print("Saya suka buah", buah)
    
# Cara 2
for i in range(len(banyak_buat)):
    print("Saya suka buah", banyak_buat[i])
    
# Pengecekan keanggotaan
pasar = ["apel", "mangga", "kiwi", "pisang", "jeruk"]
if "Jooo" in pasar:
    print("Apel ada di pasar")
else:
    print("Apel tidak ada di pasar")