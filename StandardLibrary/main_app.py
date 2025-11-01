import datetime

# Untuk menghitung array
from collections import Counter


data_waktu = datetime.datetime.now()
print(data_waktu)

print(f"Data tahun: {data_waktu.year}")
print(f"Data bulan: {data_waktu.month}")
print(f"Data hari: {data_waktu.day}")
print(f"Data jam: {data_waktu.hour}")
print(f"Data menit: {data_waktu.minute}")
print(f"Data detik: {data_waktu.second}")
print(f"Data mikrodetik: {data_waktu.microsecond}")
print(f"Data waktu: {data_waktu.strftime('%A, %d %B %Y %H:%M:%S')}")


data = ['apple', 'banana', 'cherry', 'apple', 'banana', 'apple']

counter = Counter[str](data)

print(counter)

import io

file = io.open('data.txt', 'r')
print(file.read())
