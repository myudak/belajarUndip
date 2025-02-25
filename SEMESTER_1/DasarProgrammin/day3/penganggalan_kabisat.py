"""
Program   : Ekspresi kondisional: penanggalan versi 2
Deskripsi : Program ini menghitung hari ke-n dari suatu tanggal berdasarkan tahun 1900+y dengan memperhitungkan tahun kabisat.
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

IsKabisat? : integer [0..99] → boolean
{IsKabisat?(y) menghasilkan True jika tahun 1900+y adalah tahun kabisat, yaitu habis dibagi 4 tetapi tidak habis dibagi 100, atau habis dibagi 400.}
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


def IsKabisat(y: int) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def HariKe1900(d: int, m: int, y: int) -> int:
    return dpm(m) + d - 1 + (1 if m > 2 and IsKabisat(y) else 0)


def ApakahLusaKamis(d: int, m: int, y: int) -> bool:
    return HariKe1900(d, m, y) % 7 + 2 == 6


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(HariKe1900(10, 3, 2000))
print(HariKe1900(31, 12, 2016))
print(ApakahLusaKamis(28, 3, 1945))
