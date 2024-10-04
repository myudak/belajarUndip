"""
Program   : Sequence Bilangan Penyebut
Deskripsi : Program ini menentukan apakah urutan angka yang terulang setelah koma sesuai dengan 
            hasil pembagian 1 dengan bilangan bulat positif. Jika ya, program akan mengembalikan 
            nilai bilangan bulat pembagi tersebut. Jika tidak, program akan mengeluarkan string 
            "Tidak ada".
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 23/09/2024
"""

"""
**************************************************************
DEFINISI DAN SPESIFIKASI
**************************************************************

denumeratorSeq : string → string
{denumeratorSeq(x) memeriksa apakah urutan angka terulang yang diberikan dalam bentuk string 
berasal dari hasil pembagian 1 dengan bilangan bulat positif. Parameter:
x (string): Urutan angka terulang yang ingin diperiksa.

Fungsi ini akan mengembalikan string yang menyatakan apakah ada penyebut integer yang sesuai 
atau tidak. Jika ada, format outputnya adalah "Ada: y", di mana y adalah penyebut integer. 
Jika tidak ada, akan mengembalikan "Tidak ada".}

**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def denumeratorSeq(x: str) -> str:
    sembilan = 10 ** len(x) - 1
    return f"Ada: { sembilan // int(x)}" if sembilan % int(x) == 0 else "Tidak ada"


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(f"{denumeratorSeq('3')} -> Ada: 3")  # -> 3
print(f"{denumeratorSeq('166')} -> Tidak ada")  # -> Tidak ada
