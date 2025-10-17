print("==== MENAMPILKAN DATA NILAI DARI FILE ====")

file = open("nilai.txt", "r")

for line in file:
    data = line.strip().split(",")
    print("Nama Siswa:", data[0], "| Nilai:", data[1])
    
file.close()

print("==== TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI ====")