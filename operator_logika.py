age = 20

# Operator AND akan bernilai True jika kedua kondisi bernilai True
print(age > 18 and age < 30)  # True
print(age > 18 and age > 30)  # False

hari = "Sabtu"
# Operator OR akan bernilai True jika salah satu kondisi bernilai True
print(hari == "Sabtu" or hari == "Minggu")  # True
print(hari == "Sabtu" or hari == "Senin")   # True
print(hari == "Senin" or hari == "Selasa")   # False

aktif = True
# Operator NOT akan membalik nilai boolean
print(not aktif)  # False