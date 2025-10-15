# Set adalah kumpulan data yang tidak berurutan dan tidak memiliki indeks.
# Setiap elemen dalam set harus unik (tidak boleh ada duplikasi).
# Set digunakan ketika Anda ingin menyimpan koleksi item yang tidak berurutan dan tidak memerlukan akses berdasarkan indeks.
# Set juga mendukung operasi matematika seperti union, intersection, dan difference.
# Membuat Set


pasar = {"apel", "mangga", "kiwi", "pisang", "jeruk"}
print("Set pasar:", pasar)

# Set kosong
set_kosong = set()
print("Set kosong:", set_kosong)

# Menambahkan Elemen ke Set
pasar.add("nanas")
pasar.add("nanas")  # Tidak akan menambahkan duplikasi
print("Set pasar setelah menambahkan nanas:", pasar)

# Menghapus Elemen dari Set
pasar.remove("kiwi")  # Akan menimbulkan error jika elemen tidak ditemukan
print("Set pasar setelah menghapus kiwi:", pasar)
pasar.discard("mangga")  # Tidak menimbulkan error jika elemen tidak ditemukan
print("Set pasar setelah menghapus mangga:", pasar)

# Mengakses Elemen dalam Set
for e in pasar:
    print("Buah di pasar:", e)