"""
LATIHAN B
Program   : Menghitung deret geometri: 1 + 3 + 9 + 27 + …
Deskripsi : Program ini adalah sebuah program yang berfungsi untuk Menghitung deret geometri: 1 + 3 + 9 + 27 + …
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 10/06/2024
"""

"""
DEFINISI DAN SPESIFIKASI
    menghitung_deret_aritmatika_369 : integer → integer
        { menghitung_deret_aritmatika_369(n) Menghitung deret geometri: 1 + 3 + 9 + 27 + … dengan rekursif }
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def menghitung_deret_aritmatika_369(n):
    if n == 1:
        return 3
    return 3 * (n) + menghitung_deret_aritmatika_369(n - 1)


"""
**************************************************************
APLIKASI
**************************************************************
"""


print(f"menghitung_deret_aritmatika_369(1) : 3 = {menghitung_deret_aritmatika_369(1)}")
print(
    f"menghitung_deret_aritmatika_369(2) : 3 + 6 = {menghitung_deret_aritmatika_369(2)}"
)
print(
    f"menghitung_deret_aritmatika_369(3) : 3 + 6 + 9 = {menghitung_deret_aritmatika_369(3)}"
)
