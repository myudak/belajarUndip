"""
Program   : Hitung Energi dan Gradien Magis di Dunia Numeris
Deskripsi : Program ini menghitung energi magis di titik a dan b serta gradien magis di antara kedua titik menggunakan fungsi "kuno" f(x).
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 23/09/2024
"""

"""
**************************************************************
DEFINISI DAN SPESIFIKASI
**************************************************************

f : integer -> real
{f(x) adalah fungsi yang digunakan untuk menghitung energi magis pada titik x, dengan rumus f(x) = 3 * x^2 + 2 * x - 5}

gradien : integer, integer -> real
{gradien(a, b) menghitung gradien magis antara titik a dan b dengan rumus (f(a) - f(b)) / (a - b), di mana a ≠ b}
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def f(x: int) -> float:
    return 3 * x**2 + 2 * x - 5


def gradien(a: int, b: int) -> float:
    return (f(a) - f(b)) / (a - b)


"""
**************************************************************
APLIKASI
**************************************************************
"""


print(gradien(3, 1))
