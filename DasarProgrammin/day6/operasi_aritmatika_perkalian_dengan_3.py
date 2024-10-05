"""
LATIHAN B
Program   : Menghitung perkalian dengan 3 atau f(n) = 3 * n
Deskripsi : Program ini adalah sebuah program yang berfungsi untuk menghitung Menghitung perkalian dengan 3 atau f(n) = 3 * n
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 10/06/2024
"""

"""
DEFINISI DAN SPESIFIKASI
    menghitung_perkalian_dengan_3 : integer → integer
        { menghitung_perkalian_dengan_3(a) menghitung a kali 3 dengan rekursif }
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def menghitung_perkalian_dengan_3(n):
    if n == 1:
        return 3
    return 3 + menghitung_perkalian_dengan_3(n - 1)


print(f"menghitung_perkalian_dengan_3(5) : 3 . 5 = {menghitung_perkalian_dengan_3(5)}")
print(f"menghitung_perkalian_dengan_3(1) : 3 . 1 = {menghitung_perkalian_dengan_3(1)}")
print(f"menghitung_perkalian_dengan_3(9) : 3 . 9 = {menghitung_perkalian_dengan_3(9)}")
