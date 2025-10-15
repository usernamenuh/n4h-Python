angka = 1
while angka <= 5:
    print("Hello Word!")
    print(angka)
    angka += 1      # angka = angka + 1
print("Selesai")


password = ""
while password != "admin123":
    password = input("Masukkan password : ")
    if password != "admin123":
        print("Password salah!")
print("Password benar, Anda berhasil login!")