import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Membuat window utama
window = tk.Tk()

# Atur warna background
window.configure(bg="white")

# Atur ukuran window
window.geometry("300x250")

# Supaya tidak bisa di-resize
window.resizable(False, False)

# Beri judul pada window
window.title("My First GUI")

# Frame input
input_frame = ttk.Frame(window)
input_frame.pack(pady=10, padx=10, fill="x", expand=True)

# Komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(pady=10, padx=10, fill="x", expand=True)

# 2. Entry nama depan

NAMA_DEPAN = tk.StringVar()
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(pady=10, padx=10, fill="x", expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(pady=10, padx=10, fill="x", expand=True)

# 4. Entry nama belakang
NAMA_BELAKANG = tk.StringVar()
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(pady=10, padx=10, fill="x", expand=True)

# 5. Button submit

def tombol_click():
    print(f"Nama: {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}")
    showinfo("Info", "Hello, " + NAMA_DEPAN.get() + " " + NAMA_BELAKANG.get())

tombol_sapa = ttk.Button(input_frame, text="Sapa!", command=tombol_click)
tombol_sapa.pack(pady=10, padx=10, fill="x", expand=True)


# main loop window
window.mainloop()
