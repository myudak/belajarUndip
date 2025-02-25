"""
Program   : Ekspresi Boolean dengan Operator Boolean: APAKAH VALID
Deskripsi : Membuat predikat yang menerima sebuah besaran integer, dan menentukan apakah bilangan tersebut valid.
            Bilangan disebut valid jika nilainya lebih kecil dari 5 atau lebih besar dari 500.
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 02/09/2024
**************************************************************
DEFINISI DAN SPESIFIKASI
IsValid? : integer → boolean
    { IsValid? (x): benar jika x bernilai lebih kecil dari 5 atau lebih besar dari 500 }
**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def IsValid(x: int) -> bool:
    return x < 5 or x > 500


"""
**************************************************************
APLIKASI
**************************************************************
"""
print(IsValid(5))
print(IsValid(0))
print(IsValid(500))
print(IsValid(6000))
