def ambil_soal():
    soal_asli = [] 
    with open("bank_soal.txt", "r") as file:
        for line in file:
            soal_asli.append(line.strip())
    return soal_asli

def buat_soal():
    soal_asli = ambil_soal()
    
    import random
    random.shuffle(soal_asli)  # Untuk mengacak list soal
    
    soal_ujian = []
    for i in range(10):
        soal = soal_asli[i] # Pertanyaan|jawaban1,jawaban2,jawaban3,jawaban4
        data = soal.split("|") # Jadi list [pertanyaan, jawaban1,jawaban2,jawaban3,jawaban4]
        
        pertanyaan = data[0] # Pertanyaan
        semua_jawaban = data[1] # jawaban1,jawaban2,jawaban3,jawaban4 [Dalam Bentuk string]
        
        jawaban = semua_jawaban.split(",") # di split menjadi list [jawaban1, jawaban2, jawaban3, jawaban4]
        jawaban_benar = jawaban[0] # Jawaban yang benar adalah jawaban1
        
        random.shuffle(jawaban)  # Mengacak pilihan jawaban [jawaban1, jawaban2, jawaban3, jawaban4]
        
        soal_ujian.append({
            "pertanyaan": pertanyaan,
            "jawaban": jawaban,
            "jawaban_benar": jawaban_benar
        })
    return soal_ujian

def app_ujian():
    soal_ujian = buat_soal()
    opsi = ["A", "B", "C", "D"]
    
    jawaban_benar = 0
    jawaban_salah = 0
    
    for i in range(len(soal_ujian)):
        soal = soal_ujian[i]
        print("Pertanyaan ->", i + 1, ":", soal["pertanyaan"])
        print("Jawaban Pilihan:")
        
        
        for j in range(len(soal["jawaban"])):
            jawaban = soal["jawaban"][j]
            print(opsi[j], ".", jawaban)
            
            
        jawaban_user = input("Masukkan jawaban Anda (A/B/C/D): ")
        jawaban_user_index = opsi.index(jawaban_user)
        jawaban_asli_user = soal["jawaban"][jawaban_user_index]
        
        if jawaban_asli_user == soal["jawaban_benar"]:
            print("Jawaban Anda benar!")
            jawaban_benar += 1
        else:
            print("Jawaban Anda salah! Jawaban yang benar adalah:", soal["jawaban_benar"])
            jawaban_salah += 1
        print("-----------------------------")
        
    print("Hasil Ujian Anda:")
    print("Jawaban Benar:", jawaban_benar)
    print("Jawaban Salah:", jawaban_salah)
    print("Hasil Ujian", jawaban_benar / (jawaban_benar + jawaban_salah) * 100, "%")

app_ujian()