nama_global = "Muhammad Enuh"

def contoh():
    print("Nama di dalam fungsi:", nama_global)
    

# jika ingin mengubah nilai global di dalam fungsi
def ubah_nama():
    global nama_global
    nama_global = "Budi"
    print("Nama di dalam fungsi setelah diubah:", nama_global)
    
contoh()
ubah_nama()