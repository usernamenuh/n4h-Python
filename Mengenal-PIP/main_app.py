# Dengan numpy kita bisa membuat matriks dan vektor dengan mudah

import numpy as np

list_a = [1, 2, 3, 4, 5]
vector_a = np.array([1, 2, 3, 4])

print(f"List a: {list_a}")
# Kuadratkan list a akan error karena list tidak bisa dikuadratkan
# print(f"Kuadrat list a: {list_a ** 2}")

# Kuadratkan vector a tiadak error karena vector bisa dikuadratkan
print(f"Kuadrat vector a: {vector_a ** 2}")
print(f"Kali 5 vector a: {vector_a * 5}")
print(f"Vector a: {vector_a}")

matrix_b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Matrix b: \n{matrix_b}")
print(f"Matrix b^2 : \n{matrix_b ** 2}")

# Matrix kosong
zeros_c = np.zeros((3, 3))
print(f"Matrix kosong c: \n{zeros_c}")

# Matrix satu
ones_d = np.ones((3, 3))
print(f"Matrix satu d: \n{ones_d}")

# Matrix identitas
identity_e = np.identity(3)
print(f"Matrix identitas e: \n{identity_e}")

# Matrix random
random_f = np.random.rand(3, 3)
print(f"Matrix random f: \n{random_f}")

# bisa menambahkan
jumlah = matrix_b + matrix_b**2 + ones_d
print(f"Jumlah = \n{jumlah}")