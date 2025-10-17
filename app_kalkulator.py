# Aplikasi kalkulator sederhana

def app_penjumlahan():
    print("=== Penjumlahan ===")
    try:
        input1 = int(input("Masukkan angka pertama: "))
        input2 = int(input("Masukkan angka kedua: "))
        hasil = input1 + input2
        print(f"Hasil penjumlahan: {hasil}")
        
        input("Tekan Enter untuk melanjutkan...")
    except ValueError:
        print("Error: Input tidak valid. Harap masukkan angka yang benar.")
        input("Tekan Enter untuk melanjutkan...")
    
def app_pengurangan():
    print("=== Pengurangan ===")
    try:
        input1 = int(input("Masukkan angka pertama: "))
        input2 = int(input("Masukkan angka kedua: "))
        hasil = input1 - input2
        print(f"Hasil pengurangan: {hasil}")
        
        input("Tekan Enter untuk melanjutkan...")
        
    except ValueError:
        print("Error: Input tidak valid. Harap masukkan angka yang benar.")
        input("Tekan Enter untuk melanjutkan...")

def app_perkalian():
    print("=== Perkalian ===")
    try:
        input1 = int(input("Masukkan angka pertama: "))
        input2 = int(input("Masukkan angka kedua: "))
        hasil = input1 * input2
        print(f"Hasil perkalian: {hasil}")
        
        input("Tekan Enter untuk melanjutkan...")
        
    except ValueError:
        print("Error: Input tidak valid. Harap masukkan angka yang benar.")
        input("Tekan Enter untuk melanjutkan...")
    
def app_pembagian():
    print("=== Pembagian ===")
    try:
        input1 = int(input("Masukkan angka pertama: "))
        input2 = int(input("Masukkan angka kedua: "))
        if input2 != 0:
            hasil = input1 / input2
            print(f"Hasil pembagian: {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
            
        input("Tekan Enter untuk melanjutkan...")
    
    except ValueError:
        print("Error: Input tidak valid. Harap masukkan angka yang benar.")
        input("Tekan Enter untuk melanjutkan...")
        
def main():
    while True:
        print("==== KALKULATOR SEDERHANA ====")
        print("Pilih operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3/4): ")
        
        if pilihan == '1':
            app_penjumlahan()
        elif pilihan == '2':
            app_pengurangan()
        elif pilihan == '3':
            app_perkalian()
        elif pilihan == '4':
            app_pembagian()
        elif pilihan == '5':
            exit()
        else:
            print("Error: Pilihan tidak valid.")
            
        print("==== TERIMA KASIH TELAH MENGGUNAKAN KALKULATOR SEDERHANA ====")
    
main()