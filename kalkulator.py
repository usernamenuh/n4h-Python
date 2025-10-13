inpu1 = input("Masukan Angka Pertama : ")
input2 = input("Masukan Angka Kedua : ")
operator = input("Masukan Operator ('+', '-', '*', '/') : ")

angka1 = int (inpu1)
angka2 = int (input2)

if (operator == '+'):
    hasil = angka1 + angka2
elif (operator == '-'):
    hasil = angka1 - angka2
elif (operator == '*'):
    hasil = angka1 * angka2
elif (operator == '/'):
    hasil = angka1 / angka2
else:
    print("Operator tidak ada")
    
print(hasil);