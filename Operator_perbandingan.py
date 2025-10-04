name = "Muhammad Enuh"
nilaiUAS = 80
nilaiUTS = 90
nilaiTugas = 90


print("Nama saya adalah " + name)
print(nilaiUAS >= 75) # Lebih besar atau sama dengan, True
print(nilaiUTS >= 75) # Lebih besar atau sama dengan, True
print(nilaiTugas >= 75) # Lebih besar atau sama dengan, True

print(nilaiUAS < 75) # Lebih kecil dari, False
print(nilaiUTS < 75) # Lebih kecil dari, False
print(nilaiTugas < 75) # Lebih kecil dari, False

print(nilaiUAS <= 75) # Lebih kecil atau sama dengan, False
print(nilaiUTS <= 75) # Lebih kecil atau sama dengan, False
print(nilaiTugas <= 75) # Lebih kecil atau sama dengan, False

print(nilaiUAS == 75) # Sama dengan, False
print(nilaiUTS == 75) # Sama dengan, False
print(nilaiTugas == 75) # Sama dengan, False

print(nilaiUAS != 75) # Tidak sama dengan, True
print(nilaiUTS != 75) # Tidak sama dengan, True
print(nilaiTugas != 75) # Tidak sama dengan, True

if (nilaiUAS >= 75) and (nilaiUTS >= 75):
    print("Selamat, Anda lulus!")
else:
    print("Maaf, Anda tidak lulus.")