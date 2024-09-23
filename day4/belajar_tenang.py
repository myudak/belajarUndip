"""
Program   : Belajar Tenang
Deskripsi : Program ini menghitung jarak berdasarkan intensitas suara (dB) dan memeriksa apakah jarak tersebut melebihi batas yang ditentukan. 
            Jika jarak melebihi batas, program akan memberi peringatan untuk mengisi bensin.
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 23/09/2024
"""

"""
**************************************************************
DEFINISI DAN SPESIFIKASI
**************************************************************

BelajarTenang : integer, integer -> string
{BelajarTenang(dB, m) menghitung jarak berdasarkan desibel (dB) dengan rumus 15 * 10^((dB - 40) / 20) dan membandingkannya dengan nilai batas jarak m. Menghasilkan "Isi bensin dulu, bang" jika hasil perhitungan lebih besar dari m, atau mengembalikan nilai jarak tersebut dalam meter jika lebih kecil atau sama dengan m.}
"""


def BelajarTenang(dB: int, m: int) -> str:
    return (
        "Isi bensin dulu, bang"
        if round(15 * 10 ** ((dB - 40) / 20), 3) > m
        else f"{round(15 * 10 ** ((dB - 40) / 20), 3)} meter"
    )


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(
    BelajarTenang(102, 20000),  # 18883.881 meter
    BelajarTenang(100, 1300),  # -> Isi bensin dulu, bang
)
