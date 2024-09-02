"""
Program   : Evaluasi Fungsi: Jarak Antara Dua Titik (Least Square)
Deskripsi : Menghitung jarak antara dua buah titik pada koordinat kartesian dengan menggunakan fungsi dif2 dan FX2
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 02/09/2024
**************************************************************
DEFINISI DAN SPESIFIKASI
LS : 4 real → real
    { LS(x1, y1, x2, y2) adalah jarak antara dua buah titik (x1, y1) dengan (x2, y2) }
**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
dif2 : 2 real → real
    { dif2(x, y) adalah kuadrat dari selisih antara x dan y }
FX2 : real → real
    { FX2(x) adalah hasil kuadrat dari x }
**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def FX2(x: float) -> float:
    return x * x


def dif2(x: float, y: float) -> float:
    return FX2(x - y)


def LS(x1: float, y1: float, x2: float, y2: float) -> float:
    return (dif2(x2, x1) + dif2(y2, y1)) ** 0.5


"""
**************************************************************
APLIKASI
**************************************************************
"""
print(LS(1, 3, 5, 6))
