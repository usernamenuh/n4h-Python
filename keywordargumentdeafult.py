def perkenalan(nama, usia=18, kota="Jakarta"):
    print(f"==== Perkenalan nama {nama.upper()}====")
    print(f"Usia: {usia}")
    print(f"Kota: {kota}")
    print("-------------------")
    
    
# Memanggil fungsi dengan semua argumen posisi
perkenalan("Andi", 20, "Bandung")

# Memanggil fungsi dengan argumen posisi dan keyword
perkenalan("Budi", kota="Surabaya")