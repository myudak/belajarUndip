"""
Program   : Jam Pasir Ajaib
Deskripsi : Program ini memvalidasi input waktu dalam format jam, menit, dan detik, kemudian mencetak hasilnya dalam format yang benar atau menampilkan pesan jika waktu tidak valid.
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 23/09/2024
"""

"""
**************************************************************
DEFINISI DAN SPESIFIKASI
**************************************************************

jam : integer [0..24], integer [0..59], integer [0..59] → string
{jam(j,m,s) memvalidasi apakah tuple (j,m,s) merupakan waktu yang valid. Jika valid, mengembalikan string dengan format "Jam: j, Menit: m, Detik: s". Jika tidak, mengembalikan "Waktu tidak valid".}

**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def jam(j: int, m: int, s: int) -> str:
    return (
        f"Jam: {j}, Menit: {m}, Detik: {s}"
        if 0 <= j <= 24 and 0 <= m <= 59 and 0 <= s <= 59
        else "Waktu tidak valid"
    )


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(jam(12, 30, 45))  # -> Jam: 12, Menit: 30, Detik: 45
print(jam(12, 45, 60))  # -> Waktu tidak valid
