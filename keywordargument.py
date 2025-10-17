def mahasiswa(nama, umur, jurusan, nim):
    print("Nama:", nama)
    print("Umur:", umur)
    print("Jurusan:", jurusan)
    print("NIM:", nim)
    print("-------------------")
    
    
# positional arguments
mahasiswa("Andi", 20, "Informatika", "123456")

# keyword arguments
mahasiswa(nama="Budi", umur=21, jurusan="Sistem Informasi", nim="654321")
mahasiswa(umur=22, nama="Citra", nim="112233", jurusan="Teknik Elektro")