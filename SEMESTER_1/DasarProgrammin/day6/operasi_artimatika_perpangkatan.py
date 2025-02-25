"""
LATIHAN A
Program   : Operasi Aritmatika Perpangkatan
Deskripsi : Program ini adalah sebuah program yang berfungsi untuk menghitung Operasi Aritmatika Perpangkatan
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 10/06/2024
"""

"""
DEFINISI DAN SPESIFIKASI
    perpangkatan : integer, integer → integer
        { perpangkatan(a, b) menghitung perpangkatan dari a dengan b dengan rekursif }
"""


"""
**************************************************************
REALISASI
**************************************************************
"""


def perpangkatan(a, b):
    if b == 0:
        return 1
    return a * perpangkatan(a, b - 1)


"""
**************************************************************
APLIKASI
**************************************************************
"""


print(f"perpangkatan(5, 3) : 5 ^ 3 = {perpangkatan(5, 3)}")
print(f"perpangkatan(6, 9) : 6 ^ 9 = {perpangkatan(6, 9)}")
print(f"perpangkatan(4, 2) : 4 ^ 2 = {perpangkatan(4, 2)}")
