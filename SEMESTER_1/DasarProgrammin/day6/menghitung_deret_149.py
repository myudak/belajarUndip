"""
LATIHAN B
Program   : Menghitung deret : 1 + 4 + 9 + 16 + …
Deskripsi : Program ini adalah sebuah program yang berfungsi Menghitung deret : 1 + 4 + 9 + 16 + …
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 10/06/2024
"""

"""
DEFINISI DAN SPESIFIKASI
    menghitung_deret_149 : integer → integer
        { menghitung_deret_149(n) Menghitung deret : 1 + 4 + 9 + 16 + … dengan rekursif }
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def menghitung_deret_149(n):
    if n == 1:
        return 1
    return n**2 + menghitung_deret_149(n - 1)


print(f"menghitung_deret_149(3) = {menghitung_deret_149(3)}")


"""
**************************************************************
APLIKASI
**************************************************************
"""
print(f"menghitung_deret_149(1) : 1 = {menghitung_deret_149(1)}")
print(f"menghitung_deret_149(2) : 1 + 4 = {menghitung_deret_149(2)}")
print(f"menghitung_deret_149(3) : 1 + 4 + 9 = {menghitung_deret_149(3)}")
print(f"menghitung_deret_149(4) : 1 + 4 + 9 + 16 = {menghitung_deret_149(4)}")
