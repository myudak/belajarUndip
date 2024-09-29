"""
Program   : Tipe bentukan GARIS
Deskripsi : Didefinisikan suatu type bernama Pecahan, yang terdiri dari pembilang dan penyebut. Berikut ini adalah teks dalam notasi fungsional untuk type pecahan tersebut. Perhatikanlah bahwa realisasi fungsi hanya dilakukan untuk operator aritmatika dan relasional terhadap pecahan. Realisasi selektor hanya diberikan secara konseptual, karena nantinya akan diserahkan implementasinya ke bahasa pemrograman 
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 29/09/2024
"""

"""
**************************************************************
DEFINISI DAN SPESIFIKASI
    type point : <x: real, y: real>
        { <x: real, y: real> merepresentasikan sebuah titik dalam bidang dua dimensi. x adalah absis (horizontal) dan y adalah ordinat (vertical) }
    type garis : <P1: point, P2: point>
        { Sebuah garis direpresentasikan oleh dua titik P1 dan P2 yang berada dalam bidang dua dimensi }

DEFINISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI
    Absis : point → real
        { Absis(P) memberikan absis (koordinat x) dari titik P }
    Ordinat : point → real
        { Ordinat(P) memberikan ordinat (koordinat y) dari titik P }
    GarisAwal : garis → point
        { GarisAwal(G) memberikan titik awal garis G }
    GarisAkhir : garis → point
        { GarisAkhir(G) memberikan titik akhir garis G }

DEFINISI DAN SPESIFIKASI KONSTRUKTOR
    MakePoint : real, real → point
        { MakePoint(x, y) membentuk sebuah titik dengan koordinat x (absis) dan y (ordinat) }
    MakeGaris : point, point → garis
        { MakeGaris(P1, P2) membentuk sebuah garis dengan titik awal P1 dan titik akhir P2 }

DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP GARIS
    PanjangGaris : garis → real
        { PanjangGaris(garis) menghitung panjang garis antara dua titik Absis(garis) dan Ordinat(garis) menggunakan rumus jarak Euclidean }

DEFINISI DAN SPESIFIKASI PREDIKAT
    IsSejajar : garis, garis → boolean
        { IsSejajar(garisAwal, garisAkhir) mengecek apakah garis yang dibentuk oleh Absis(garisAwal)-Ordinat(garisAwal) dan Absis(GarisAkhir)-Ordinat(GarisAkhir) sejajar. Dua garis sejajar jika dan hanya jika gradien (kemiringan) kedua garis sama }

DEFINISI DAN SPESIFIKASI FUNGSI TAMBAHAN
    Gradien : point, point → real
        { Gradien(P1, P2) menghitung gradien (kemiringan) dari garis yang dibentuk oleh dua titik P1 dan P2 }
    Jarak : point, point → real
        { Jarak(P1, P2) menghitung jarak antara dua titik P1 dan P2 menggunakan rumus jarak Euclidean }

**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def MakePoint(x, y):
    return [x, y]


def Absis(P):
    return P[0]


def Ordinat(P):
    return P[1]


def MakeGaris(P1, P2):
    return [P1, P2]


def GarisAwal(G):
    return G[0]


def GarisAkhir(G):
    return G[1]


def IsOrigin(P):
    return Absis(P) == 0 and Ordinat(P) == 0


def FX2(x):
    return x * x


def Jarak(P1, P2):
    return (FX2(Absis(P1) - Absis(P2)) + FX2(Ordinat(P1) - Ordinat(P2))) * 0.5


def Jarak0(P):
    return (FX2(Absis(P)) + FX2(Ordinat(P))) * 0.5


def Kuadran(P):
    if Absis(P) > 0 and Ordinat(P) > 0:
        return "Kuadran 1"
    if Absis(P) < 0 and Ordinat(P) > 0:
        return "Kuadran 2"
    if Absis(P) < 0 and Ordinat(P) < 0:
        return "Kuadran 3"
    if Absis(P) > 0 and Ordinat(P) < 0:
        return "Kuadran 4"
    return "Gk ad"


def Gradien(P1, P2):
    return (Ordinat(P2) - Ordinat(P1)) / (Absis(P2) - Absis(P1))


def IsSejajar(G1, G2):
    return Gradien(GarisAwal(G1), GarisAkhir(G1)) == Gradien(
        GarisAwal(G2), GarisAkhir(G2)
    )


def PanjangGaris(G):
    return Jarak(GarisAwal(G), GarisAkhir(G))


"""
**************************************************************
APLIKASI
**************************************************************
"""
print(
    f"""IsSejajar: <1,3>, <2,3>, <3,3>, <4,3> -> 
    {
        IsSejajar(
            MakeGaris(
                MakePoint(1, 3), 
                MakePoint(2, 3)
                ), 
            MakeGaris(
                MakePoint(3, 3),
                MakePoint(4, 3)
                )
            )
    }"""
)
print(
    f"""PanjangGaris: <1,3>, <2,3> -> 
    {
    PanjangGaris(
        MakeGaris(
            MakePoint(1, 3), 
            MakePoint(2, 3)
            )
        )
    }"""
)
