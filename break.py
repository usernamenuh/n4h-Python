angka_rahasaia = 9
mencoba = 0

while True:
    tebak_angka = int(input("Tebak angka (1-10) : "))
    mencoba = mencoba + 1
    if tebak_angka == angka_rahasaia:
        print("Selamat, tebakan Anda benar! dengan percobaan ke-", mencoba)
        break    # Di ulangi terus perulangan sampai benar
    else:
        print("Tebakan Anda salah, coba lagi!")