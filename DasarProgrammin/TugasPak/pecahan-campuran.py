"""
Program   : Tipe bentukan PECAHAN
Deskripsi : Didefinisikan suatu type bernama Pecahan, yang terdiri dari pembilang dan penyebut. Berikut ini adalah teks dalam notasi fungsional untuk type pecahan tersebut. Perhatikanlah bahwa realisasi fungsi hanya dilakukan untuk operator aritmatika dan relasional terhadap pecahan. Realisasi selektor hanya diberikan secara konseptual, karena nantinya akan diserahkan implementasinya ke bahasa pemrograman 
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 29/09/2024
"""

"""
**************************************************************
DEFINISI DAN SPESIFIKASI
    type pecahan : <n: integer >=0 ,d: integer >0> 
        {<n:integer >=0, d:integer >0> n adalah pembilang (numerator) dan d adalah penyebut 
        (denumerator). Penyebut sebuah pecahan tidak boleh nol }
    type pecahancampuran : <bil: integer, n: integer >= 0, d: integer > 0 >
        {<bil, n, d> adalah sebuah pecahan campuran yang terdiri atas bilangan bil,

DEFINISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI
    PembPecahan : pecahan → integer >=0 
        { Pemb(p) memberikan numerator pembilang n dari pecahan tsb } 
    PenyPecahan : pecahan → integer > 0 
        { Peny(p) memberikan denumerator penyebut d dari pecahan tsb }
    BilanganPecahanCampuran : pecahancampuran → integer >=0 
        { BilanganPecahanCampuran(Pc) memberikan bilangan bil dari pecahan campuran tsb }
    PembPecahanCampuran : pecahancampuran → integer >=0 
        { PembPecahanCampuran(Pc) memberikan numerator pembilang n dari pecahan campuran tsb }
    PenyPecahanCampuran : pecahancampuran → integer > 0 
        { PenyPecahanCampuran(Pc) memberikan denumerator penyebut d dari pecahan campuran tsb }

DEFINISI DAN SPESIFIKASI KONSTRUKTOR
    MakePecahan : integer >=0, integer > 0 → pecahan 
        { MakeP(pemb,peny) membentuk sebuah pecahan dari pembilang pemb dan penyebut peny, dengan pemb dan peny integer} 
    MakePecahanCampuran : integer, integer >= 0, integer > 0 → pecahancampuran
        { MakePecahanCampuran(bilangan,pemb,peny) membentuk sebuah pecahan campuran dari pembilang bilangan, pembilang pemb dan penyebut peny, dengan pemb, peny dan bilangan integer }

DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP PECAHAN { Operator aritmatika Pecahan } 
    AddPecahan : 2 pecahan → pecahan 
        { AddPecahan(P1,P2) : Menambahkan dua buah pecahan P1 dan P2 }
    SubPecahan : 2 pecahan → pecahan 
        { SubPecahan(P1,P2) : Mengurangkan dua buah pecahan P1 dan P2 } 
    MulPecahan : 2 pecahan → pecahan 
        {MulPecahan(P1,P2) : Mengalikan dua buah pecahan P1 dan P2 } 
    DivPecahan : 2 pecahan → pecahan 
        { DivPecahan(P1,P2) : Membagi dua buah pecahan P1 dan P2 } 
    RealPecahan : pecahan → real
        {Menuliskan bilangan pecahan dalam notasi desimal }

DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP PECAHAN CAMPURAN { Operator aritmatika PecahanCampuran } 
    AddPecahanCampuran : 2 pecahancampuran → pecahancampuran 
        { AddPecahanCampuran(Pc1,Pc2) : Menambahkan dua buah pecahan campuran Pc1 dan Pc2 }
    SubPecahanCampuran : 2 pecahancampuran → pecahancampuran 
        { SubPecahanCampuran(Pc1,Pc2) : Mengurangkan dua buah pecahan campuran Pc1 dan Pc2 } 
    DivPecahanCampuran : 2 pecahancampuran → pecahancampuran 
        { DivPecahanCampuran(Pc1,Pc2) : Membagi dua buah pecahan campuran Pc1 dan Pc2 } 
    MulPecahanCampuran : 2 pecahancampuran → pecahancampuran 
        {MulPecahanCampuran(Pc1,Pc2) : Mengalikan dua buah pecahan campuran Pc1 dan Pc2 }
    RealPecahanCampuran : pecahancampuran → real
        {Menuliskan bilangan pecahan campuran dalam notasi desimal }

DEFINISI DAN SPESIFIKASI PREDIKAT
    IsEqPecahan?: 2 pecahan → boolean
        {IsEqP?(p1,p2) true jika p1 = p2 
        Membandingkan apakah dua buah pecahan saman ilainya: n1/d1 = n2/d2 jika dan 
        hanya jika n1d2=n2d1 }
    IsLtPecahan?: 2 pecahan → boolean
        {IsLtP?(p1,p2) true jika p1 < p2 
        Membandingkan dua buah pecahan, apakah p1 lebih kecil nilainya dari p2: n1/d1 < 
        n2/d2 jika dan hanya jika n1d2 < n2d1 }
    IsGtPecahan?: 2 pecahan → boolean
        {IsGtP?(p1,p2) tue jika p1 > p2 
        Membandingkan nilai dua buah pecahan,, apakah p1 lebih besar nilainya dari p2: 
        n1/d1 > n2/d2 jika dan hanya jika n1d2 > n2d1 }
    IsEqPecahanCampuran?: 2 pecahancampuran → boolean
        {IsEqP?(p1,p2) true jika p1 = p2 
        Membandingkan apakah dua buah pecahan campuran saman ilainya: n1/d1 = n2/d2 jika dan 
        hanya jika n1d2=n2d1 }
    IsLtPecahanCampuran?: 2 pecahancampuran → boolean
        {IsLtP?(p1,p2) true jika p1 < p2 
        Membandingkan dua buah pecahan campuran, apakah p1 lebih kecil nilainya dari p2: n1/d1 < 
        n2/d2 jika dan hanya jika n1d2 < n2d1 }
    IsGtPecahanCampuran?: 2 pecahancampuran → boolean
        {IsGtP?(p1,p2) tue jika p1 > p2 
        Membandingkan nilai dua buah pecahan campuran,, apakah p1 lebih besar nilainya dari p2: 
        n1/d1 > n2/d2 jika dan hanya jika n1d2 > n2d1 }

DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
    PecahanCampuranKePecahan : pecahancampuran → pecahan
        { PecahanCampuranKePecahan(Pc) mengonversi pecahan campuran menjadi pecahan biasa }
    PecahanKePecahanCampuran : pecahan → pecahancampuran
        { PecahanKePecahanCampuran(P) mengonversi pecahan biasa menjadi pecahan campuran }
**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


# Konstruktor Pecahan
def MakePecahan(Pemb, Peny):
    return [Pemb, Peny]


# Selektor Pecahan
def PembPecahan(P):
    return P[0]


def PenyPecahan(P):
    return P[1]


# Konstruktor PecahanCampuran
def MakePecahanCampuran(bilangan, pemb, peny):
    return [bilangan, pemb, peny]


# Selektor PecahanCampuran
def BilanganPecahanCampuran(Pc):
    return Pc[0]


def PembPecahanCampuran(Pc):
    return Pc[1]


def PenyPecahanCampuran(Pc):
    return Pc[2]


# Operator Pecahan
def AddPecahan(P1, P2):
    return MakePecahan(
        PembPecahan(P1) * PenyPecahan(P2) + PembPecahan(P2) * PenyPecahan(P1),
        PenyPecahan(P1) * PenyPecahan(P2),
    )


def SubPecahan(P1, P2):
    return MakePecahan(
        PembPecahan(P1) * PenyPecahan(P2) - PembPecahan(P2) * PenyPecahan(P1),
        PenyPecahan(P1) * PenyPecahan(P2),
    )


def MulPecahan(P1, P2):
    return MakePecahan(
        PembPecahan(P1) * PembPecahan(P2), PenyPecahan(P1) * PenyPecahan(P2)
    )


def DivPecahan(P1, P2):
    return MakePecahan(
        PembPecahan(P1) * PenyPecahan(P2), PenyPecahan(P1) * PembPecahan(P2)
    )


def RealPecahan(P):
    return PembPecahan(P) / PenyPecahan(P)


# Predikat
def IsEqPecahan(P1, P2):
    return RealPecahan(SubPecahan(P1, P2)) == 0


def IsLtPecahan(P1, P2):
    return RealPecahan(SubPecahan(P1, P2)) < 0


def IsGtPecahan(P1, P2):
    return RealPecahan(SubPecahan(P1, P2)) > 0


# Fungsi Antara
def PecahanCampuranKePecahan(Pc):
    return (
        MakePecahan(
            PenyPecahanCampuran(Pc) * BilanganPecahanCampuran(Pc)
            + PembPecahanCampuran(Pc),
            PenyPecahanCampuran(Pc),
        )
        if BilanganPecahanCampuran(Pc) >= 0
        else MakePecahan(
            PenyPecahanCampuran(Pc) * BilanganPecahanCampuran - PembPecahanCampuran(Pc),
            PenyPecahanCampuran(Pc),
        )
    )


def PecahanKePecahanCampuran(P):
    return (
        MakePecahanCampuran(
            PembPecahan(P) // PenyPecahan(P),
            PembPecahan(P),
            PenyPecahan(P),
        )
        if PembPecahan(P) // PenyPecahan(P) == 0
        else MakePecahanCampuran(
            PembPecahan(P) // PenyPecahan(P),
            PembPecahan(P) % PenyPecahan(P),
            PenyPecahan(P),
        )
    )


# Operator PecahanCampuran
def AddPecahanCampuran(Pc1, Pc2):
    return PecahanKePecahanCampuran(
        AddPecahan(
            PecahanCampuranKePecahan(Pc1),
            PecahanCampuranKePecahan(Pc2),
        )
    )


def SubPecahanCampuran(Pc1, Pc2):
    return PecahanKePecahanCampuran(
        SubPecahan(
            PecahanCampuranKePecahan(Pc1),
            PecahanCampuranKePecahan(Pc2),
        )
    )


def DivPecahanCampuran(Pc1, Pc2):
    return PecahanKePecahanCampuran(
        DivPecahan(
            PecahanCampuranKePecahan(Pc1),
            PecahanCampuranKePecahan(Pc2),
        )
    )


def MulPecahanCampuran(Pc1, Pc2):
    return PecahanKePecahanCampuran(
        MulPecahan(
            PecahanCampuranKePecahan(Pc1),
            PecahanCampuranKePecahan(Pc2),
        )
    )


def RealPecahanCampuran(Pc):
    return RealPecahan(PecahanCampuranKePecahan(Pc))


# Predikat
def IsEqPecahanCampuran(Pc1, Pc2):
    return RealPecahanCampuran(SubPecahanCampuran(Pc1, Pc2)) == 0


def IsLtPecahanCampuran(Pc1, Pc2):
    return RealPecahanCampuran(SubPecahanCampuran(Pc1, Pc2)) < 0


def IsGtPecahanCampuran(Pc1, Pc2):
    return RealPecahanCampuran(SubPecahanCampuran(Pc1, Pc2)) > 0


"""
**************************************************************
APLIKASI
**************************************************************
"""

# Pecahan
print(
    f"AddPecahan: <3,1>, <2,1> -> {AddPecahan(MakePecahan(3, 1), MakePecahan(2, 1))}",
)
print(
    f"SubPecahan: <3,1>, <2,1> -> {SubPecahan(MakePecahan(3, 1), MakePecahan(2, 1))}",
)
print(
    f"DivPecahan: <3,1>, <2,1> -> {DivPecahan(MakePecahan(3, 1), MakePecahan(2, 1))}",
)
print(
    f"MulPecahan: <3,1>, <2,1> -> {MulPecahan(MakePecahan(3, 1), MakePecahan(2, 1))}",
)
print(
    f"IsGtPecahan: <3,1>, <2,1> -> {IsGtPecahan(MakePecahan(3, 1), MakePecahan(2, 1))}",
)
print(
    f"IsLtPecahan: <3,1>, <2,1> -> {IsLtPecahan(MakePecahan(3, 1), MakePecahan(2, 1))}",
)
print(
    f"IsEqPecahan: <3,1>, <3,1> -> {IsEqPecahan(MakePecahan(3, 1), MakePecahan(3, 1))}",
)

# PecahanCampuran
print(
    f"AddPecahanCampuran: <1,4,5>, <1,2,5> -> {AddPecahanCampuran(MakePecahanCampuran(1, 4, 5), MakePecahanCampuran(1, 2, 5))}",
)
print(
    f"SubPecahanCampuran: <1,4,5>, <1,2,5> -> {SubPecahanCampuran(MakePecahanCampuran(1, 4, 5), MakePecahanCampuran(1, 2, 5))}",
)
print(
    f"DivPecahanCampuran: <1,4,5>, <1,2,5> -> {DivPecahanCampuran(MakePecahanCampuran(1, 4, 5), MakePecahanCampuran(1, 2, 5))}",
)
print(
    f"MulPecahanCampuran: <1,4,5>, <1,2,5> -> {MulPecahanCampuran(MakePecahanCampuran(1, 4, 5), MakePecahanCampuran(1, 2, 5))}",
)
print(
    f"IsGtPecahanCampuran: <1,4,5>, <1,2,5> -> {IsGtPecahanCampuran(MakePecahanCampuran(1, 4, 5), MakePecahanCampuran(1, 2, 5))}",
)
print(
    f"IsLtPecahanCampuran: <1,4,5>, <1,2,5> -> {IsLtPecahanCampuran(MakePecahanCampuran(1, 4, 5), MakePecahanCampuran(1, 2, 5))}",
)
print(
    f"IsEqPecahanCampuran: <1,4,5>, <1,2,5> -> {IsEqPecahanCampuran(MakePecahanCampuran(1, 4, 5), MakePecahanCampuran(1, 2, 5))}",
)
