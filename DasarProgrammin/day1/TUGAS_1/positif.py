"""
Program   : Ekspresi Boolean: POSITIF
Deskripsi : Membuat predikat yang menerima sebuah bilangan bulat dan bernilai benar jika bilangan tersebut positif
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 02/09/2024
**************************************************************
DEFINISI DAN SPESIFIKASI
IsPositif? : integer → boolean
    { IsPositif? (x): benar jika x positif atau nol, false jika x negatif }
**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def IsPositif(x: int) -> bool:
    return x >= 0


"""
**************************************************************
APLIKASI
**************************************************************
"""
print(IsPositif(1))
print(IsPositif(0))
print(IsPositif(-1))
