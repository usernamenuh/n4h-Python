try:
    a = int(input("Masukkan angka pertama: "))
except ValueError:
    print("Input pertama bukan angka yang valid.")
else:
    print("Angka yang anda masukkan adalah:", a)
    
    if a > 0:
        print("Angka tersebut adalah bilangan positif.")
    elif a < 0:
        print("Angka tersebut adalah bilangan negatif.")
    else:
        print("Angka tersebut adalah nol.")
finally:
    print("Terima kasih telah menggunakan program ini.")