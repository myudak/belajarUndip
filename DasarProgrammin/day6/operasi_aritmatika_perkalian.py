"""
LATIHAN A
Program   : Operasi Aritmatika Perkalian
Deskripsi : Program ini adalah sebuah program yang berfungsi untuk menghitung Operasi Aritmatika Perkalian
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 10/06/2024
"""

"""
DEFINISI DAN SPESIFIKASI
    perkalian : integer, integer → integer
        { perkalian(a, b) menghitung perkalian dari a dengan b dengan rekursif }
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def perkalian(a, b):
    if b == 0:
        return 0
    return a + perkalian(a, b - 1)


"""
**************************************************************
APLIKASI
**************************************************************
"""


print(f"perkalian(5, 3) : 5 . 3 = {perkalian(5, 3)}")
print(f"perkalian(6, 9) : 6 . 9 = {perkalian(6, 9)}")
print(f"perkalian(4, 2) : 4 . 2 = {perkalian(4, 2)}")
