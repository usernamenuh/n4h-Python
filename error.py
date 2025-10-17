print("==== KALKULATOR SEDERHANA ====")
try:
    angka1 = input("Masukkan angka pertama: ")
    angka2 = input("Masukkan angka kedua: ")
    operator = input("Masukkan operator (+, -, *, /): ")

    a = int(angka1)
    b = int(angka2)

    if operator == '+':
        hasil = a + b
        print(f"Hasil: {hasil}")
    elif operator == '-':
        hasil = a - b
        print(f"Hasil: {hasil}")
    elif operator == '*':
        hasil = a * b
        print(f"Hasil: {hasil}")
    elif operator == '/':
        if b != 0:
            hasil = a / b
            print(f"Hasil: {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
    else:
        print("Error: Operator tidak valid.")
        
except ValueError:
    print("Error: Input tidak valid. Harap masukkan angka yang benar.")
except ZeroDivisionError:
    print("Error: Pembagian dengan nol tidak diperbolehkan.")
except:
    print("Error: Input tidak valid. Harap masukkan angka yang benar.")
    
print("==== TERIMA KASIH TELAH MENGGUNAKAN KALKULATOR SEDERHANA ====")