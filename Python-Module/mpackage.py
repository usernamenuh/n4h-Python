# Import dari package
import time
import sains.matematika

t_start = time.time()

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = sains.matematika.kali(1,2,1,2,9)
print(f"hasil kali = {hasil_kali}")

pangkat = sains.matematika.pangkat(3)
print(f"Pangkat dari 3 adalah {pangkat(3)}")

t_end = time.time()

print(f"Waktu eksekusi adalah = {t_end - t_start}")