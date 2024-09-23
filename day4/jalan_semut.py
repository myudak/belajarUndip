"""
Program   : Jalan Semut
Deskripsi : Program ini menghitung jarak terpendek yang ditempuh oleh semut dari sudut sebuah balok (0,0,0) ke sudut berlawanan (x,y,z) melalui permukaan balok.
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 23/09/2024
"""

"""
**************************************************************
DEFINISI DAN SPESIFIKASI
**************************************************************

jalanSemut : integer, integer, integer -> real 
{jalanSemut(x, y, z) menghitung jarak terpendek yang ditempuh oleh semut dari titik (0,0,0) ke titik (x,y,z) dengan menggunakan rumus jarak terpendek yang melibatkan tiga kombinasi jarak antara x, y, dan z.}

**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def jalanSemut(x: int, y: int, z: int) -> float:
    jarak1 = ((x + y) ** 2 + z**2) ** 0.5
    jarak2 = ((x + z) ** 2 + y**2) ** 0.5
    jarak3 = ((y + z) ** 2 + x**2) ** 0.5

    return round(min(jarak1, jarak2, jarak3), 3)


"""
**************************************************************
APLIKASI
**************************************************************
"""


print(jalanSemut(3, 4, 5))  # -> 8.602
print(jalanSemut(1, 2, 7))  # -> 7.616
