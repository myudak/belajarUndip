# Break it Up! - Praktikum 4 Daspro 24 EZ

"""
Program   : Jam Pasir Ajaib
"""


def jam(j, m, s):
    return (
        f"Jam: {j}, Menit: {m}, Detik: {s}"
        if j <= 24 and m <= 59 and s <= 59
        else "Waktu tidak valid"
    )


print(
    f"{jam(12,30,45)} -> Jam: 12, Menit: 30, Detik: 45",
    f"{jam(12,45,60)} -> Waktu tidak valid",
)

"""
Program   : Lalu Lintas Langit
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


print(
    f"{monitor_pesawat(4000,850,55)} -> Aman untuk Mendarat",
    f"{monitor_pesawat(5000,950,70)} -> Kecepatan Berbahaya",
)

"""
Program   : Jalan Semut
"""


def jalanSemut(x, y, z):
    jarak1 = ((x + y) ** 2 + z**2) ** 0.5
    jarak2 = ((x + z) ** 2 + y**2) ** 0.5
    jarak3 = ((y + z) ** 2 + x**2) ** 0.5

    return round(min(jarak1, jarak2, jarak3), 3)


print(
    f"{jalanSemut(3,4,5)} -> 8.602",
    f"{jalanSemut(1,2,7)} -> 7.616",
)

"""
Program   : Belajar Tenang
"""


def BelajarTenang(dB, m):
    return (
        "Isi bensin dulu, bang"
        if round(15 * 10 ** ((dB - 40) / 20), 3) > m
        else f"{round(15 * 10 ** ((dB - 40) / 20), 3)} meter"
    )


print(
    f"{BelajarTenang(102, 20000)} -> 18883.881 meter",
    f"{BelajarTenang(100, 1300)} -> Isi bensin dulu, bang",
)

"""
Program   : Sequence Bilangan Penyebut
"""


def denumeratorSeq(x):
    sembilan = 10 ** len(x) - 1
    return f"Ada: { sembilan // int(x)}" if sembilan % int(x) == 0 else "Tidak ada"


print(f"{denumeratorSeq('3')} -> Ada: 3", f"{denumeratorSeq('166')} -> Tidak ada")

"""
Program   : Gradien Magis
"""


def gradien(a, b):
    def f(x):
        return 3 * x**2 + 2 * x - 5

    return (f(a) - f(b)) / (a - b)


print(f"{gradien(3,1)} -> 14.0")


"""
Program   : Shop Smart
"""


# ====================NORMAL==============================
def diskon(harga, persen):
    return harga - (harga * persen / 100)


def pajak(harga, persen):
    return harga + (harga * persen / 100)


def hargaAkhir(harga, kategori, VIP, lokasi, hari):
    hargaAkhir = harga

    # ATURAN DISKON
    if kategori == "elektronik":
        if VIP:
            hargaAkhir = diskon(hargaAkhir, 30)
        else:
            hargaAkhir = diskon(hargaAkhir, 10)
    if kategori == "pakaian":
        if VIP:
            hargaAkhir = diskon(hargaAkhir, 20)
        else:
            hargaAkhir = diskon(hargaAkhir, 5)
    if kategori == "makanan":
        if VIP:
            hargaAkhir = diskon(hargaAkhir, 15)
        else:
            hargaAkhir = diskon(hargaAkhir, 2)
    # ==================================================

    # DISKON/PAJAK HARI
    if hari == "Jumat" or hari == "Sabtu":
        if VIP:
            hargaAkhir = diskon(hargaAkhir, 5)
    if hari == "Minggu":
        hargaAkhir = pajak(hargaAkhir, 5)
    if hari == "Rabu":
        if kategori == "pakaian":
            hargaAkhir = diskon(hargaAkhir, 5)
    # ==================================================

    # ATURAN PAJAK
    if lokasi == "dalam negeri":
        hargaAkhir = pajak(hargaAkhir, 10)
    if lokasi == "luar negeri":
        hargaAkhir = pajak(hargaAkhir, 20)
    # ==================================================
    return int(hargaAkhir)


print(
    f"{hargaAkhir(1000, 'elektronik', True, 'dalam negeri', 'Jumat')} -> 770000",
    f"{hargaAkhir(500000, 'pakaian', False, 'luar negeri', 'Rabu')} -> 541500",
)


# ===================FUNCTIONAL===============================
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


print(
    f"{hargaAkhir(1000, 'elektronik', True, 'dalam negeri', 'Jumat')} -> 770000",
    f"{hargaAkhir(500000, 'pakaian', False, 'luar negeri', 'Rabu')} -> 541500",
)

"""
Program   : Perpustakaan Agung
"""


def TabelHari(Hari):
    if Hari == "senin":
        return (5000 + 6000 + 4000) / 3
    if Hari == "selasa":
        return (7000 + 5000 + 2000) / 3
    if Hari == "rabu":
        return (4500 + 3500 + 3000) / 3
    if Hari == "kamis":
        return (2900 + 2100 + 2000) / 3
    if Hari == "jumat":
        return (3000 + 3000 + 3000) / 3
    if Hari == "sabtu":
        return (2000 + 2500 + 2300) / 3
    if Hari == "minggu":
        return (1100 + 900 + 1000) / 3


def EstimateGreatLib(
    Hari,
    JamAwal,
    JamAkhir,
    Terbenam,
    Terbit,
    AhliStatistika,
    AhliMatematika,
    AhliIlmpuPerpustakaan,
    R,
):
    rataPengunjung = TabelHari(Hari)
    rangeNy = max(AhliStatistika, AhliMatematika, AhliIlmpuPerpustakaan) - min(
        AhliStatistika, AhliMatematika, AhliIlmpuPerpustakaan
    )

    # FULL SIANG
    if JamAwal >= Terbit and JamAkhir <= Terbenam:
        lamaWaktu = JamAkhir - JamAwal
        return round(lamaWaktu * rangeNy / rataPengunjung, 5)
    # ==================================================

    # FULL MALEM
    if JamAkhir <= Terbit or JamAwal >= Terbenam:
        lamaWaktu = JamAkhir - JamAwal
        return round((lamaWaktu * rangeNy / rataPengunjung) * (R / 100), 5)
    # ==================================================

    # LEWAT TERBIT
    if JamAwal < Terbit and JamAkhir > Terbit and JamAkhir <= Terbenam:
        siang = JamAkhir - Terbit
        malem = Terbit - JamAwal
        return round(
            (
                (siang * rangeNy / rataPengunjung)
                + (malem * rangeNy / rataPengunjung) * (R / 100)
            )
            / 2,
            5,
        )
    # ==================================================

    # LEWAT TERBENAM
    if (
        JamAwal >= Terbit
        and JamAkhir > Terbenam
        and JamAkhir > JamAwal
        and JamAwal < Terbenam
    ):
        siang = Terbenam - JamAwal
        malem = JamAkhir - Terbenam
        return round(
            (
                (siang * rangeNy / rataPengunjung)
                + (malem * rangeNy / rataPengunjung) * (R / 100)
            )
            / 2,
            5,
        )
    # ==================================================

    # FULL DUA DUA NY
    if JamAwal < Terbit and JamAkhir > Terbenam:
        siang = Terbenam - Terbit
        malemSebelum = Terbit - JamAwal
        malemSesudah = JamAkhir - Terbenam
        return round(
            (
                (siang * rangeNy / rataPengunjung)
                + (malemSebelum * rangeNy / rataPengunjung) * (R / 100)
                + (malemSesudah * rangeNy / rataPengunjung) * (R / 100)
            )
            / 3,
            5,
        )
    # ==================================================
    return "error gblh"


print(
    EstimateGreatLib("jumat", 7, 8, 17, 6, 4000, 5500, 5000, 3),
    EstimateGreatLib("senin", 12, 17, 18, 9, 6000, 5000, 4500, 50),
    EstimateGreatLib("selasa", 8, 16, 20, 12, 7000, 5000, 2000, 75),
)
