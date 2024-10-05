"""
LATIHAN A
Program   : Operasi Aritmatika Pembagian
Deskripsi : Program ini adalah sebuah program yang berfungsi untuk menghitung Operasi Aritmatika Pembagian
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 10/06/2024
"""

"""
DEFINISI DAN SPESIFIKASI
    pembagian : integer, integer → integer
        { pembagian(a, b) menghitung pembagian dari a dengan b dengan rekursif }
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def pembagian(a, b):
    if b == 0:
        return 0
    return 1 + pembagian(a - b, b - 1)


"""
**************************************************************
APLIKASI
**************************************************************
"""


print(f"pembagian(15, 3) : 15 / 3 -> {pembagian(15, 3)}")
print(f"pembagian(60, 10) : 60 / 10 -> {pembagian(60, 10)}")
print(f"pembagian(60, 15) : 60 / 15 -> {pembagian(60, 15)}")
