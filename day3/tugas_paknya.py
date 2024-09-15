# TUGAS PAKNYA **************************************************************

"""
Program   : Ekspresi Kondisional: Penanggalan dari paknya
Deskripsi : Program ini menghitung hari ke-n dari suatu tanggal berdasarkan tahun 1900+y dan memeriksa apakah lusa (hari setelah besok) adalah hari Kamis.
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 15/09/2024
"""

"""
**************************************************************
DEFINISI DAN SPESIFIKASI
HariKe1900 : integer [1..31], integer [1..12], integer [0..99] → integer [1..366]
{HariKe1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari absolut dihitung mulai 1 Januari tahun 1900+y. 1 Januari tahun 1900+y adalah hari ke 1}

dpm : integer [1..12] → integer [1..366]
{dpm(B) adalah jumlah hari kumulatif dari tanggal 1 Januari hingga tanggal 1 bulan B pada tahun tertentu, tanpa memperhitungkan tahun kabisat.}

totalKabisat : integer [0..99] → integer [0..366]
{totalKabisat(y) menghitung jumlah tahun kabisat dari tahun 1900 hingga tahun 1900+y-1.}

ApakahLusaHariKamis : integer [1..31], integer [1..12], integer [0..99] → boolean
{ApakahLusaHariKamis(d, m, y) memeriksa apakah lusa (hari setelah besok) dari tanggal <d,m,y> adalah hari Kamis.}
**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def dpm(bulan: int) -> int:
    """menghitung jumlah hari kumulatif dari tanggal 1 Januari hingga tanggal 1 bulan B pada tahun tertentu"""
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
    """menghitung hari ke-n dari tanggal <hari, bulan, tahun> dari 1 Januari 1900+y"""
    return dpm(bulan) + hari - 1


def TotalKabisat(y: int) -> int:
    """menghitung jumlah tahun kabisat dari 1900 hingga tahun 1900+y-1"""
    return y // 4 - y // 100 + y // 400


def ApakahLusaHariKamis(d: int, m: int, y: int) -> bool:
    # memeriksa apakah lusa (hari setelah besok) dari tanggal <d, m, y> adalah hari Kamis
    totalHari = HariKe1900(d + 2, m, y)
    tahunBerlalu = y - 1900
    kabisat = TotalKabisat(tahunBerlalu)
    hariTambahan = tahunBerlalu * 365 + kabisat

    # total hari sejak 1900 modulo 7 = 3 -> hari Kamis
    return (totalHari + hariTambahan) % 7 == 3


"""
**************************************************************
APLIKASI
**************************************************************
"""
d, m, y = 12, 9, 2006
print(f"Apakah Lusa hari Kamis ({d},{m},{y}): {ApakahLusaHariKamis(d,m,y)}")
d, m, y = 19, 9, 2023
print(f"Apakah Lusa hari Kamis ({d},{m},{y}): {ApakahLusaHariKamis(d,m,y)}")
d, m, y = 17, 9, 2024
print(f"Apakah Lusa hari Kamis ({d},{m},{y}): {ApakahLusaHariKamis(d,m,y)}")
d, m, y = 18, 9, 2029
print(f"Apakah Lusa hari Kamis ({d},{m},{y}): {ApakahLusaHariKamis(d,m,y)}")

"""
**************************************************************
NOTASI FUNGSIONAL??
**************************************************************

totalKabisat(y):
  (y - 1) // 4 
  - (y - 1) // 100
  + (y - 1) // 400
  - (1900 // 4 - 1900 // 100 + 1900 // 400)

ApakahLusaHariKamis(d, m, y) = 
  let totalHari = HariKe1900(d + 2, m, y) in
  let totalHariSejak1900 = totalHari + (y - 1900) * 365 + totalKabisat(y) in
  totalHariSejak1900 mod 7 = 3
"""
