def cetak_list(*list):
    for item in list:
        print(item)
        
cetak_list('apel', 'pisang', 'jeruk')
cetak_list(1, 2, 3, 4, 5)


# dictionary sebagai parameter dinamis
def cetak_dict(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
cetak_dict(nama='Andi', umur=25, kota='Jakarta')
cetak_dict(merek='Toyota', model='Corolla', tahun=2020)