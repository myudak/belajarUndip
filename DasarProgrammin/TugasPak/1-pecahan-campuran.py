"""
Program   : Tipe Pecahan Campuran
Deskripsi : Menentukan tipe pecahan campuran
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 29/09/2024

**************************************************************
DEFINISI DAN SPESIFIKASI TYPE
type pecahanc : < bil: integer, n: integer >= 0, d: integer > 0 >
    <bil, n, d> adalah sebuah pecahan campuran yang terdiri atas bil yang merupakan bilangan bulat positif, nol, atau negatif, n yaitu pembilang atau nominator yang merupakan bilangan non-negatif, dan d yaitu denominator yang merupakan bilangan positif, lalu nilai n pasti lebih kecil daripada nilai d

type pecahan: < pemb: integer, peny: integer > 0 >
    <pemb, peny> adalah sebuah pecahan yang terdiri atas pembilang dan penyebut

**************************************************************
DEFINISI DAN SPESIFIKASI SELEKTOR

Bilangan : pecahanc → integer
    Bilangan(P) mengembalikan nilai bil dari tipe <bil, n, d>
Nominator : pecahanc → integer >= 0
    Nominator(P) mengembalikan nilai n yaitu nominator atau pembilang dari tipe <bil, n, d>
Denominator : pecahanc → integer > 0
    Denominator(P) mengembalikan nilai d yaitu denominator atau penyebut dari tipe <bil, n, d>
Pembilang : pecahan → integer
    Pembilang(P) mengembalikan nilai pemb atau pembilang dari tipe <pemb, peny>
Penyebut : pecahan → integer > 0
    Penyebut(P) mengembalikan nilai peny atau penyebut dari tipe <pemb, peny>

**************************************************************
DEFINISI DAN SPESIFIKASI KONSTRUKTOR

MakePecahanC : integer, integer >= 0, integer > 0 → pecahanc
    MakePecahanC(bil, n, d) membuat tipe pecahan campuran dengan bilangan bil, nominator n, dan denominator d
MakePecahan : integer, integer > 0 → pecahan
    MakePecahan(pemb, peny) membuat tipe pecahan dengan pembilang pemb dan penyebut peny

**************************************************************
DEFINISI DAN SPESIFIKASI OPERATOR

KonversiPecahan : pecahanc → pecahan
    KonversiPecahan(P) mengonversi pecahan campuran menjadi pecahan biasa
KonversiReal : pecahanc → real
    KonversiReal(P) mengonversi pecahan campuran menjadi bilangan real
AddP : 2 pecahanc → pecahanc
    AddP(P1, P2) menambah P1 dengan P2
SubP : 2 pecahanc → pecahanc
    SubP(P1, P2) mengurang P1 dengan P2
DivP : 2 pecahanc → pecahanc
    DivP(P1, P2) membagi P1 dengan P2
MulP : 2 pecahanc → pecahanc
    MulP(P1, P2) mengalikan P1 dengan P2

**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI PREDIKAT

IsEqP : 2 pecahanc → boolean
    IsEqP(P1, P2) memeriksa apakah P1 sama dengan P2
IsLtP : 2 pecahanc → boolean
    IsLtP(P1, P2) memeriksa apakah P1 lebih kecil daripada P2
IsGtP : 2 pecahanc → boolean
    IsGtP(P1, P2) memeriksa apakah P1 lebih besar daripada P2

**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI ANTARA

KaliDenominator : 2 pecahanc → integer
    KaliDenominator(P1, P2) mengalikan nilai denominator P1 dengan P2
KaliNoDe : 2 pecahanc → integer
    KaliNoDe(P1, P2) mengalikan nilai nominator P1 dengan denominator P2
KaliPembPeny : 2 pecahanc → integer
    KaliPembPeny(P1, P2) mengalikan nilai pembilang P1 dengan penyebut P2 setelah keduanya dikonversi menjadi pecahan biasa
KaliPemb : 2 pecahanc → integer
    KaliPemb(P1, P2) mengalikan nilai pembilang P1 dengan pembilang P2 setelah keduanya dikonversi menjadi pecahan biasa
SimpNom : integer, 2 pecahanc → integer
    SimpNom(hasilOp, P1, P2) memberikan nilai nominator yang bergantung pada nilai perkalian denominator
SimpPemb : integer, 2 pecahanc → integer
    SimpPemb(hasilOp, P1, P2) memberikan nilai nominator yang bergantung pada nilai perkalian antara pembilang dan penyebut 

**************************************************************

REALISASI
**************************************************************
"""


def Bilangan(P):
    return P[0]


def Nominator(P):
    return P[1]


def Denominator(P):
    return P[2]


def Pembilang(P):
    return P[0]


def Penyebut(P):
    return P[1]


# Konstruktor
def MakePecahanC(bil, n, d):
    return [bil, n, d]


def MakePecahan(n, d):
    return [n, d]


# Fungsi Antara
def KaliDenominator(P1, P2):
    return (
        Denominator(P1) * Denominator(P2)
        if Denominator(P1) != Denominator(P2)
        else Denominator(P1)
    )


def KaliNoDe(P1, P2):
    return Nominator(P1) * Denominator(P2)


def KaliPembPeny(P1, P2):
    return Pembilang(KonversiPecahan(P1)) * Penyebut(KonversiPecahan(P2))


def KaliPemb(P1, P2):
    return Pembilang(KonversiPecahan(P1)) * Pembilang(KonversiPecahan(P2))


def SimpNom(hasilOp, P1, P2):
    return (
        hasilOp
        if abs(hasilOp) < KaliDenominator(P1, P2)
        else hasilOp % KaliDenominator(P1, P2)
    )


def SimpPemb(hasilOp, P1, P2):
    return (
        hasilOp * -1
        if hasilOp < abs(KaliPembPeny(P2, P1))
        else hasilOp % abs(KaliPembPeny(P2, P1))
    )


# Predikat
def IsEqP(P1, P2):
    return (KaliPembPeny(P1, P2)) == (KaliPembPeny(P2, P1))


def IsLtP(P1, P2):
    return (KaliPembPeny(P1, P2)) < (KaliPembPeny(P2, P1))


def IsGtP(P1, P2):
    return (KaliPembPeny(P1, P2)) > (KaliPembPeny(P2, P1))


# Operator
def KonversiPecahan(P):
    if Bilangan(P) < 0:
        return MakePecahan(
            (Bilangan(P) * Denominator(P)) - Nominator(P), Denominator(P)
        )
    else:
        return MakePecahan(
            (Bilangan(P) * Denominator(P)) + Nominator(P), Denominator(P)
        )


def KonversiReal(P):
    return Pembilang(KonversiPecahan(P)) / Penyebut(KonversiPecahan(P))


def AddP(P1, P2):
    return MakePecahanC(
        Bilangan(P1)
        + Bilangan(P2)
        + ((KaliNoDe(P1, P2) + KaliNoDe(P2, P1)) // KaliDenominator(P1, P2)),
        SimpNom((KaliNoDe(P1, P2) + KaliNoDe(P2, P1)), P1, P2),
        KaliDenominator(P1, P2),
    )


def SubP(P1, P2):
    return MakePecahanC(
        Bilangan(P1)
        - Bilangan(P2)
        - (abs(KaliNoDe(P1, P2) - KaliNoDe(P2, P1)) // KaliDenominator(P1, P2)),
        SimpNom((KaliNoDe(P1, P2) - KaliNoDe(P2, P1)), P1, P2),
        KaliDenominator(P1, P2),
    )


def DivP(P1, P2):
    return MakePecahanC(
        (KaliPembPeny(P1, P2) // KaliPembPeny(P2, P1))
        + (1 if KaliPembPeny(P2, P1) < 0 else 0),
        SimpPemb(KaliPembPeny(P1, P2), P1, P2),
        abs(KaliPembPeny(P2, P1)),
    )


def MulP(P1, P2):
    return MakePecahanC(
        (KaliPemb(P1, P2) // KaliDenominator(P1, P2))
        + (1 if KaliPemb(P1, P2) < 0 else 0),
        (KaliPemb(P1, P2)) % KaliDenominator(P1, P2),
        KaliDenominator(P1, P2),
    )


"""
APLIKASI
**************************************************************
"""

print(AddP(MakePecahanC(1, 1, 2), MakePecahanC(1, 2, 4)))
print(SubP(MakePecahanC(1, 1, 2), MakePecahanC(1, 3, 4)))
print(DivP(MakePecahanC(1, 1, 2), MakePecahanC(-1, 1, 4)))
print(MulP(MakePecahanC(1, 1, 2), MakePecahanC(1, 1, 4)))
print(IsEqP(MakePecahanC(1, 1, 2), MakePecahanC(1, 2, 4)))
print(IsLtP(MakePecahanC(1, 1, 2), MakePecahanC(1, 1, 4)))
print(IsGtP(MakePecahanC(1, 1, 2), MakePecahanC(1, 1, 4)))
