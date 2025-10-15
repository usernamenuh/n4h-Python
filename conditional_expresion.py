angka = int(input("Masukkan angka: "))

# Dengan if-else
if angka > 0:
    hasil = "Positif"
elif angka < 0:
    hasil = "Negatif"
else:
    hasil = "Nol"
print(f"Angka tersebut adalah: {hasil}")


# Dengan ekspresi kondisional
hasil = "Positif" if angka > 0 else "Negatif" if angka < 0 else "Nol"
print(f"Angka tersebut adalah: {hasil}")