print("==== SIPMPAN DATA NILAI ====")

file = open("nilai.txt", "w")

while True:
    nama = input("Nama siswa (enter 'exit' untuk keluar): ")
    if nama == "":
        break
    
    nilai = input("Nilai siswa: ")
    file.write(nama + "," + nilai + "\n")
    print("Data", nama, "dengan nilai", nilai, "telah disimpan.")
    
file.close()
print("==== TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI ====")