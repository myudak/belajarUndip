"""
Program   : Ekspresi Boolean: APAKAH HURUF A
Deskripsi : Membuat predikat yang menerima sebuah karakter dan bernilai benar jika karakter tersebut adalah huruf ‘A’
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 02/09/2024
**************************************************************
DEFINISI DAN SPESIFIKASI
IsAnA? : character → boolean
    { IsAnA (C): benar jika C adalah karakter (huruf) ‘A’ }
**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def IsAnA(C: str) -> bool:
    return C == "A"


"""
**************************************************************
APLIKASI
**************************************************************
"""
print(IsAnA("A"))
print(IsAnA("B"))
print(IsAnA("a"))
