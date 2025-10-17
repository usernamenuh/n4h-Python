def tebak_angka():
    import random
    
    angka_rahasia = random.randint(1, 10)
    percobaan = 3
    mencoba = 0
    
    print("=== Permainan Tebak Angka ===")
    
    while mencoba < percobaan:
        tebakan = input("Tebak angka antara 1 sampai 10: ")
        try:
            tebakan_int = int(tebakan)
            mencoba += 1
            if tebakan_int < angka_rahasia:
                print("Tebakan Anda terlalu rendah. Sisa percobaan:", percobaan - mencoba)
            elif tebakan_int > angka_rahasia:
                print("Tebakan Anda terlalu tinggi. Sisa percobaan:", percobaan - mencoba)
            elif tebakan_int == angka_rahasia:
                print("Selamat! Tebakan Anda benar. Dengan angka:", angka_rahasia, "Dan Percobaan yang Anda gunakan:", mencoba)
            else:
                print("Maaf, Anda telah kehabisan percobaan", mencoba, "Angka yang benar adalah:", angka_rahasia)
                
                
            input("Tekan Enter untuk mencoba lagi...")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka antara 1 sampai 10.")
            
def menu():
    while True:
        print("=== Menu Permainan ===")
        print("1. Main Tebak Angka")
        print("2. Keluar")
        
        pilihan = input("Pilih opsi (1/2): ")
        
        if pilihan == '1':
            tebak_angka()
        elif pilihan == '2':
            print("Terima kasih telah bermain!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
menu()