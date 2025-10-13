username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == "admin":
    if password == "admin123":
        print("Login berhasil! Selamat datang, admin.")
    else:
        print("Password salah. Akses ditolak.")
else:
    print("Username tidak ditemukan. Akses ditolak.")