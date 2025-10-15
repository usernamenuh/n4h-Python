# Latihan kecil kecilan
pasar = ["apel", "mangga", "kiwi", "pisang", "jeruk"]

masukan = input("Masukkan nama buah yang ingin Anda cari: ")
if masukan in pasar:
    print(f"{masukan} ditemukan di pasar.")
else:
    print(f"{masukan} tidak ditemukan di pasar.")