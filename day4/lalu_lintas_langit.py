"""
Program   : Jam Pasir Ajaib
Deskripsi : Program ini menghitung hari ke-n dari suatu tanggal berdasarkan tahun 1900+y dengan memperhitungkan tahun kabisat.
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 23/09/2024
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


def monitor_pesawat(x, y, z):
    if x < 5000 and (200 < y < 900) and z > 50:
        return "Aman untuk Mendarat"
    if z < 20:
        return "Bahan Bakar Rendah"
    if x > 12000:
        return "Terlalu Tinggi"
    if y > 900 or y < 200:
        return "Kecepatan Berbahaya"
    return "Berjalan Normal"


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(
    f"{monitor_pesawat(4000,850,55)} -> Aman untuk Mendarat",
    f"{monitor_pesawat(5000,950,70)} -> Kecepatan Berbahaya",
)
