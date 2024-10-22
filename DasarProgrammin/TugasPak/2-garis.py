"""
Program   : Tipe Garis
Deskripsi : Menentukan tipe garis yang terdiri dari dua titik yaitu titik awal dan titik akhir
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 29/09/2024

**************************************************************
DEFINISI DAN SPESIFIKASI TYPE
type point : < x : integer, y : integer >
    <x, y> adalah sebuah titik yang mempunyai absis x dan ordinat y
type garis : < p1 : point, p2 : point >
    <p1, p2> adalah sebuah garis yang terdiri dari dua titik yaitu titik awal (p1) dan titik akhir (p2)

**************************************************************
DEFINISI DAN SPESIFIKASI SELEKTOR

absis : point → integer
    absis(P) mengembalikan nilai x atau absis dari titik P
ordinat : point → integer
    ordinat(P) mengembalikan nilai y atau ordinat dari titip P
StartP : garis → point
    StartP(G) mengembalikan titik awal dari garis G
EndP : garis → point
    EndP(G) mengembalikan titik akhir dari garis G

**************************************************************
DEFINISI DAN SPESIFIKASI KONSTRUKTOR

MakePoint: 2 integer → point
    MakePoint(x, y) membuat tipe point dengan absis x dan ordinat y
MakeGaris : 2 point → garis
    MakeGaris(p1,p2) membuat tipe garis dengan titik awal p1 dan titik akhir p2

**************************************************************
DEFINISI DAN SPESIFIKASI OPERATOR

PanjangGaris : garis → real
    PanjangGaris(G) menghitung panjang garis G
Gradien : garis → real
    Gradien(G) menghitung gradien garis G
jarak : 2 point → real
    jarak(p1, p2) mengembalikan jarak antara p1 dengan p2

**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI PREDIKAT

IsSejajar : 2 garis → boolean
    IsSejajar(g1,g2) menentukan apakah garis g1 dan g2 sejajar
IsTegakLurus : 2 garis → boolean
    IsTegakLurus(g1, g2) menentukan apakah garis g1 tegak lurus dengan garis g2

**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI ANTARA

fx2 : integer → integer
    fx2(x) memberikan nilai kuadrat dari x

**************************************************************

REALISASI
**************************************************************
"""

from math import sqrt


def jarak(P1, P2):
    return sqrt(fx2(absis(P2) - absis(P1)) + fx2(ordinat(P2) - ordinat(P1)))


def fx2(x):
    return x * x


def MakePoint(x, y):
    return [x, y]


def absis(P):
    return P[0]


def ordinat(P):
    return P[1]


# Fungsi Utama


# Konstruktor
def MakeGaris(p1, p2):
    return [p1, p2]


# Selektor
def StartP(g):
    return g[0]


def EndP(g):
    return g[1]


# Operator
def PanjangGaris(g):
    return jarak(StartP(g), EndP(g))


def Gradien(g):
    return (ordinat(EndP(g)) - ordinat(StartP(g))) / (absis(EndP(g)) - absis(StartP(g)))


# Predikat
def IsSejajar(g1, g2):
    return Gradien(g1) == Gradien(g2)


def IsTegakLurus(g1, g2):
    return Gradien(g1) * Gradien(g2) == -1


"""
APLIKASI
**************************************************************
"""

print(PanjangGaris(MakeGaris(MakePoint(0, 0), MakePoint(3, 4))))
print(Gradien(MakeGaris(MakePoint(0, 0), MakePoint(3, 4))))
print(
    IsSejajar(
        MakeGaris(MakePoint(0, 0), MakePoint(3, 4)),
        MakeGaris(MakePoint(-3, -4), MakePoint(0, 0)),
    )
)
print(
    IsTegakLurus(
        MakeGaris(MakePoint(-3, 1), MakePoint(3, 0)),
        MakeGaris(MakePoint(1, 3), MakePoint(0, -3)),
    )
)
