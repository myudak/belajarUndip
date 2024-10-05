"""
LATIHAN B
Program   : Menghitung deret bilangan integer: 1 + 2 + 3 + 4 + ...
Deskripsi : Program ini adalah sebuah program yang berfungsi untuk Menghitung deret bilangan integer: 1 + 2 + 3 + 4 + ...
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 10/06/2024
"""

"""
DEFINISI DAN SPESIFIKASI
    menghitung_deret_123 : integer → integer
        { menghitung_deret_123(a) Menghitung deret bilangan integer: 1 + 2 + 3 + 4 + ... dengan rekursif }
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def menghitung_deret_123(n):
    if n == 1:
        return 1
    return n + menghitung_deret_123(n - 1)


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(f"menghitung_deret_123(1) : 1 = {menghitung_deret_123(1)}")
print(f"menghitung_deret_123(2) : 1 + 2 = {menghitung_deret_123(2)}")
print(f"menghitung_deret_123(3) : 1 + 2 + 3 = {menghitung_deret_123(3)}")
print(f"menghitung_deret_123(4) : 1 + 2 + 3 + 4 = {menghitung_deret_123(4)}")
