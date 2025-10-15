# Mencari password yang benar dengan batas pencobaan

password_benar = "admin123"
percobaan = 0
batas_percobaan = 3

while percobaan < batas_percobaan:
    password = input("Masukkan password: ")
    percobaan += 1
    if password == password_benar:
        print("Password benar, Anda berhasil login!")
        break
    else:
        print("Password salah, sisa cobaan:", batas_percobaan - percobaan)
else:
    print("Anda telah mencapai batas percobaan. Akses ditolak.")