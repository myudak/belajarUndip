"""
LATIHAN A
Program   : Operasi Aritmatika Pengurangan
Deskripsi : Program ini adalah sebuah program yang berfungsi untuk menghitung Operasi Aritmatika Pengurangan.
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 10/06/2024
"""

"""
DEFINISI DAN SPESIFIKASI
    pengurangan : integer, integer → integer
        { pengurangan(a, b) menghitung pengurangan dari a dengan b dengan rekursif }
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def pengurangan(a, b):
    if b == 0:
        return a
    return pengurangan(a - 1, b - 1)


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(f"pengurangan(5, 3) : 5 - 3 -> {pengurangan(5, 3)}")
print(f"pengurangan(9, 6) : 9 - 6 -> {pengurangan(9, 6)}")
print(f"pengurangan(19, 10) : 19 - 10 -> {pengurangan(19, 10)}")
