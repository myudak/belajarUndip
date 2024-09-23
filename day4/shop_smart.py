"""
Program   : Sequence Bilangan Penyebut
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


def diskon(harga, persen):
    return harga - (harga * persen / 100)


def pajak(harga, persen):
    return harga + (harga * persen / 100)


def aturan_diskon(harga, kategori, VIP):
    if kategori == "elektronik":
        return diskon(harga, 30) if VIP else diskon(harga, 10)
    if kategori == "pakaian":
        return diskon(harga, 20) if VIP else diskon(harga, 5)
    if kategori == "makanan":
        return diskon(harga, 15) if VIP else diskon(harga, 2)


def aturan_hari(harga, hari, kategori, VIP):
    if hari == "Jumat" or hari == "Sabtu":
        return diskon(harga, 5) if VIP else harga
    if hari == "Minggu":
        return pajak(harga, 5)
    if hari == "Rabu" and kategori == "pakaian":
        return diskon(harga, 5)


def aturan_pajak(harga, lokasi):
    if lokasi == "dalam negeri":
        return pajak(harga, 10)
    if lokasi == "luar negeri":
        return pajak(harga, 20)


def hargaAkhir(harga, kategori, VIP, lokasi, hari):
    hargaSetelahDiskon = aturan_diskon(harga, kategori, VIP)
    hargaSetelahHari = aturan_hari(hargaSetelahDiskon, hari, kategori, VIP)
    hargaFinal = aturan_pajak(hargaSetelahHari, lokasi)

    return int(hargaFinal)


"""
**************************************************************
APLIKASI
**************************************************************
"""


print(
    f"{hargaAkhir(1000, 'elektronik', True, 'dalam negeri', 'Jumat')} -> 770000",
    f"{hargaAkhir(500000, 'pakaian', False, 'luar negeri', 'Rabu')} -> 541500",
)
