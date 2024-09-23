"""
Program   : Shop Smart
Deskripsi : Program ini menghitung harga akhir barang di toko Shop Smart berdasarkan kategori produk, 
            status keanggotaan, lokasi pembelian, dan hari transaksi. Sistem ini menerapkan diskon 
            dinamis dan pajak sesuai dengan kebijakan toko, memberikan pelanggan harga yang paling 
            adil dan sesuai dengan aturan promosi yang berlaku.
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 23/09/2024
"""

"""
**************************************************************
DEFINISI DAN SPESIFIKASI
**************************************************************

diskon : integer, float → float
{diskon(harga, persen) menghitung harga setelah penerapan diskon berdasarkan persen yang diberikan.
Fungsi ini mengembalikan harga setelah diskon sebagai float.}

pajak : integer, float → float
{pajak(harga, persen) menghitung harga setelah penambahan pajak berdasarkan persen yang diberikan.
Fungsi ini mengembalikan harga setelah pajak sebagai float.}

aturan_diskon : integer, string, boolean → float
{aturan_diskon(harga, kategori, VIP) menghitung harga setelah penerapan diskon berdasarkan kategori 
barang dan status keanggotaan.
Fungsi ini mengembalikan harga setelah penerapan diskon sebagai float.}

aturan_hari : float, string, string, boolean → float
{aturan_hari(harga, hari, kategori, VIP) menghitung harga setelah penerapan diskon atau pajak tambahan 
berdasarkan hari transaksi dan kategori barang.
Fungsi ini mengembalikan harga setelah penerapan tambahan diskon atau pajak sebagai float.}

aturan_pajak : float, string → float
{aturan_pajak(harga, lokasi) menghitung harga setelah penerapan pajak berdasarkan lokasi pembelian.
Fungsi ini mengembalikan harga setelah penerapan pajak sebagai float.}

hargaAkhir : integer, string, boolean, string, string → integer
{hargaAkhir(harga, kategori, VIP, lokasi, hari) menghitung harga akhir barang dengan mempertimbangkan 
diskon, pajak, dan aturan tambahan berdasarkan kategori barang, status keanggotaan, lokasi, dan hari 
transaksi.
Fungsi ini akan mengembalikan harga akhir barang sebagai integer yang lebih besar dari 0.}

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
    return harga


def aturan_hari(harga, hari, kategori, VIP):
    if hari == "Jumat" or hari == "Sabtu":
        return diskon(harga, 5) if VIP else harga
    if hari == "Minggu":
        return pajak(harga, 5)
    if hari == "Rabu" and kategori == "pakaian":
        return diskon(harga, 5)
    return harga


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
    f"{hargaAkhir(1000, 'elektronik', True, 'dalam negeri', 'Jumat')}",  # -> 770000
    f"{hargaAkhir(500000, 'pakaian', False, 'luar negeri', 'Rabu')}",  # -> 541500
)
