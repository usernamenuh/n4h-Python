nama = "muhammad enuh"
print("Original String:", nama)
nama_upper = nama.upper()
print("Upper Case:", nama_upper) # Mengubah semua karakter menjadi huruf besar
nama_lower = nama.lower()
print("Lower Case:", nama_lower) # Mengubah semua karakter menjadi huruf kecil
nama_title = nama.title()
print("Title Case:", nama_title) # Mengubah karakter pertama setiap kata menjadi huruf besar
nama_capitalize = nama.capitalize()
print("Capitalize:", nama_capitalize) # Mengubah karakter pertama string menjadi huruf besar
nama_swapcase = nama.swapcase()
print("Swap Case:", nama_swapcase) # Menukar huruf besar menjadi kecil dan sebaliknya

name = "   muhammad enuh   "
print("\nOriginal String with spaces:", repr(name))
name_strip = name.strip()
print("After strip():", repr(name_strip)) # Menghapus spasi di awal dan akhir
name_lstrip = name.lstrip()
print("After lstrip():", repr(name_lstrip)) # Menghapus spasi di awal
name_rstrip = name.rstrip()
print("After rstrip():", repr(name_rstrip)) # Menghapus spasi di akhir

kalimat = "saya belajar python di python kelas python"
print("\nOriginal Sentence:", kalimat)
count_python = kalimat.count("python")
print("Count 'python':", count_python) # Menghitung jumlah kemunculan substring
find_belajar = kalimat.find("belajar")
print("Find 'belajar':", find_belajar) # Mencari posisi pertama substring
find_java = kalimat.find("java")
print("Find 'java':", find_java) # Mencari posisi substring yang tidak ada
replace_python = kalimat.replace("python", "java")
print("After replace 'python' with 'java':", replace_python) # Mengganti substring

# Karakter khusus
kalimat1 = "Halo, nama saya Enuh.\nSaya belajar Python." # \n untuk baris baru
print(kalimat1)

kalimat2 = "Halo, nama saya Enuh.\tSaya belajar Python." # \t untuk tab
print(kalimat2)

kalimat3 = "Halo, nama saya Enuh.\\Saya belajar Python." # \\ untuk backslash
print(kalimat3)

kalimat4 = 'Halo, nama saya Enuh. Saya belajar Python di kelas \'Python\'.' # \' untuk single quote
print(kalimat4)

kalimat5 = "Halo, nama saya Enuh. Saya belajar Python di kelas \"Python\"." # \" untuk double quote
print(kalimat5)

# Menggabungkan string
first_name = "Muhammad"
last_name = "Enuh"
full_name = first_name + " " + last_name
print("\nFull Name:", full_name) # Menggabungkan dua string dengan spasi di antaranya

# String Interpolation
nama = "Enuh"
umur = 20
alamat = "Jl. Merdeka No. 10"

info = f"Nama saya {nama}, umur saya {umur} tahun, dan saya tinggal di {alamat}."
print(info) # Menggunakan f-string untuk interpolasi string

harga = 15000
jumlah = 3

total = f"Harga total untuk {jumlah} barang adalah Rp {harga * jumlah}."
print(total) # Menghitung total harga dengan interpolasi string

name = "Enuh"
kalimatUpper = f"Halo, nama saya {name.upper()}."
print(kalimatUpper) # Menggunakan metode string dalam f-string