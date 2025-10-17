print("==== DATA NILAI DARI FILE DENGAN WITH ====")

try:
    with open("nilai.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print("Nama Siswa:", data[0], "| Nilai:", data[1])
except FileNotFoundError:
    print("File 'nilai3.txt' tidak ditemukan.")   
        
print("==== TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI ====")