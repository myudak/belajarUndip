"""
Program   : Tipe bentukan GARIS
Deskripsi : Program Tipe Bentukan Garis adalah sebuah program yang berfungsi untuk memodelkan dan mengelola garis dalam bidang 2 dimensi menggunakan tipe bentukan (data structures). Program ini memungkinkan pengguna untuk membuat dan mengoperasikan garis berdasarkan titik-titik koordinat, serta menghitung berbagai sifat garis seperti panjang garis, gradien, dan apakah dua garis sejajar. Program ini juga memungkinkan pengguna untuk memeriksa apakah garis-garis tersebut dapat membentuk bangun datar tertentu seperti persegi atau jajaran genjang.
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
    Gradien : garis → real
        { Gradien(g) menghitung gradien (kemiringan) dari garis yang dibentuk}
    Jarak : garis → real
        { Jarak(g) menghitung jarak antara dua titik dari garis yang diberikan menggunakan rumus jarak Euclidean }
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


def FX2(x):
    return x * x


def Jarak(G):
    return (
        FX2(Absis(GarisAwal(G)) - Absis(GarisAkhir(G)))
        + FX2(Ordinat(GarisAwal(G)) - Ordinat(GarisAkhir(G)))
    ) ** 0.5


def Gradien(G):
    return (Ordinat(GarisAwal(G)) - Ordinat(GarisAkhir(G))) / (
        Absis(GarisAwal(G)) - Absis(GarisAkhir(G))
    )


def IsSejajar(G1, G2):
    return Gradien(G1) == Gradien(G2)


def PanjangGaris(G):
    return Jarak(G)


"""
**************************************************************
APLIKASI
**************************************************************
"""
print(
    f"""IsSejajar: <1,3>, <2,3>, <3,3>, <4,3> -> {
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
    f"""PanjangGaris: <1,3>, <2,3> -> {
    PanjangGaris(
        MakeGaris(
            MakePoint(1, 3), 
            MakePoint(2, 3)
            )
        )
    }"""
)
