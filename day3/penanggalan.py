"""
Program   : Ekspresi kondisional: penanggalan versi 1 (tanpa memperhitungkan tahun kabisat)
Deskripsi : Program ini menghitung hari ke-n dari suatu tanggal berdasarkan tahun 1900+y tanpa memperhitungkan tahun kabisat.
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 13/09/2024
"""

"""
**************************************************************
DEFINISI DAN SPESIFIKASI
HariKe1900 : integer [1..31], integer [1..12], integer [0..99] → integer [1..366]
{HariKe1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari absolut dihitung mulai 1 Januari tahun 1900+y. 1 Januari tahun 1900+y adalah hari ke 1}

dpm : integer [1..12] → integer [1..366]
{dpm(B) adalah jumlah hari kumulatif dari tanggal 1 Januari hingga tanggal 1 bulan B pada tahun tertentu, tanpa memperhitungkan tahun kabisat.}
**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def dpm(bulan: int) -> int:
    if bulan == 1:
        return 1
    if bulan == 2:
        return 32
    if bulan == 3:
        return 60
    if bulan == 4:
        return 91
    if bulan == 5:
        return 121
    if bulan == 6:
        return 152
    if bulan == 7:
        return 182
    if bulan == 8:
        return 213
    if bulan == 9:
        return 244
    if bulan == 10:
        return 274
    if bulan == 11:
        return 305
    if bulan == 12:
        return 335


def HariKe1900(hari: int, bulan: int, tahun: int) -> int:
    return dpm(bulan) + hari - 1


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(HariKe1900(1, 1, 82))  # -> 1
print(HariKe1900(31, 12, 72))  # -> 366
print(HariKe1900(3, 4, 93))  # -> 93
