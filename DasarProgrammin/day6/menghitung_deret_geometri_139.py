"""
LATIHAN B
Program   : Menghitung deret geometri: 1 + 3 + 9 + 27 + …
Deskripsi : Program ini adalah sebuah program yang berfungsi untuk menghitung Menghitung deret geometri: 1 + 3 + 9 + 27 + …
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 10/06/2024
"""

"""
DEFINISI DAN SPESIFIKASI
    menghitung_deret_geometri_139 : integer → integer
        { menghitung_deret_geometri_139(n) Menghitung deret geometri: 1 + 3 + 9 + 27 + … dengan rekursif }
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def menghitung_deret_geometri_139(n):
    if n == 1:
        return 1
    return 3 ** (n - 1) + menghitung_deret_geometri_139(n - 1)


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(f"menghitung_deret_geometri_139(1) : 1  = {menghitung_deret_geometri_139(1)}")
print(f"menghitung_deret_geometri_139(2) : 1 + 3  = {menghitung_deret_geometri_139(2)}")
print(
    f"menghitung_deret_geometri_139(3) : 1 + 3 + 9 = {menghitung_deret_geometri_139(3)}"
)
