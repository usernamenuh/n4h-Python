angka_rahasia = 7
tebakan = 0
percobaan = 0 # Mulai dari 0 percobaan

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka antara 1-10: "))
    percobaan = percobaan + 1 
    if tebakan < angka_rahasia:
        print("Terlalu rendah! Coba lagi.")
    elif tebakan > angka_rahasia:
        print("Terlalu tinggi! Coba lagi.")
    else:
        print("Selamat! Tebakan Anda benar dalam " + str(percobaan) + " percobaan.")