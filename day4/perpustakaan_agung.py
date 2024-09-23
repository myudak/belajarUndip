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


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(
    EstimateGreatLib("jumat", 7, 8, 17, 6, 4000, 5500, 5000, 3),
    EstimateGreatLib("senin", 12, 17, 18, 9, 6000, 5000, 4500, 50),
    EstimateGreatLib("selasa", 8, 16, 20, 12, 7000, 5000, 2000, 75),
)
