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

DEFINISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI
    Pemb : pecahan → integer >=0 
        { Pemb(p) memberikan numerator pembilang n dari pecahan tsb } 
    Peny : pecahan → integer > 0 
        { Peny(p) memberikan denumerator penyebut d dari pecahan tsb }

DEFINISI DAN SPESIFIKASI KONSTRUKTOR
    MakeP : integer >=0, integer > 0 → pecahan 
        { MakeP(x,y) membentuk sebuah pecahan dari pembilang x dan penyebut y, dengan x 
        dan y integer} 

DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP PECAHAN { Operator aritmatika Pecahan } 
    AddP : 2 pecahan → pecahan 
        { AddP(P1,P2) : Menambahkan dua buah pecahan P1 dan P2 : 
        n1/d1 + n2/d2 = (n1*d2 + n2*d1)/d1*d2 }
    SubP : 2 pecahan → pecahan 
        { SubP(P1,P2) : Mengurangkan dua buah pecahan P1 dan P2 
        Mengurangkan dua pecahan : n1/d1 - n2/d2 = (n1*d2 - n2*d1)/d1*d2 } 
    MulP : 2 pecahan → pecahan 
        {MulP(P1,P2) : Mengalikan dua buah pecahan P1 dan P2 
        Mengalikan dua pecahan : n1/d1 * n2/d2 = n1*n2/d1*d2 } 
    DivP : 2 pecahan → pecahan 
        { DivP(P1,P2) : Membagi dua buah pecahan P1 dan P2 
        Membagi dua pecahan : (n1/d1)/(n2/d2) = n1*d2/d1*n2 } 
    RealP : pecahan → real
        {Menuliskan bilangan pecahan dalam notasi desimal }

DEFINISI DAN SPESIFIKASI PREDIKAT { Operator relasional Pecahan } 
    IsEqP?: 2 pecahan → boolean
        {IsEqP?(p1,p2) true jika p1 = p2 
        Membandingkan apakah dua buah pecahan samanilainya: n1/d1 = n2/d2 jika dan 
        hanya jika n1d2=n2d1 }
    IsLtP?: 2 pecahan → boolean
        {IsLtP?(p1,p2) true jika p1 < p2 
        Membandingkan dua buah pecahan, apakah p1 lebih kecil nilainya dari p2: n1/d1 < 
        n2/d2 jika dan hanya jika n1d2 < n2d1 }
    IsGtP?: 2 pecahan → boolean
        {IsGtP?(p1,p2) tue jika p1 > p2 
        Membandingkan nilai dua buah pecahan,, apakah p1 lebih besar nilainya dari p2: 
        n1/d1 > n2/d2 jika dan hanya jika n1d2 > n2d1 }
**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def MakeP(x, y):
    return [x, y]


def Pemb(P):
    return P[0]


def Peny(P):
    return P[1]


def AddP(P1, P2):
    return MakeP(Pemb(P1) * Peny(P2) + Pemb(P2) * Peny(P1), Peny(P1) * Peny(P2))


def SubP(P1, P2):
    return MakeP(Pemb(P1) * Peny(P2) - Pemb(P2) * Peny(P1), Peny(P1) * Peny(P2))


def MulP(P1, P2):
    return MakeP(Pemb(P1) * Pemb(P2), Peny(P1) * Peny(P2))


def DivP(P1, P2):
    return MakeP(Pemb(P1) * Peny(P2), Peny(P1) * Pemb(P2))


def RealP(P):
    return Pemb(P) / Peny(P)


def IsEqP(P1, P2):
    return RealP(SubP(P1, P2)) == 0


def IsLtp(P1, P2):
    return RealP(SubP(P1, P2)) < 0


def IsGtP(P1, P2):
    return RealP(SubP(P1, P2)) > 0


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(
    f"AddP: <3,1>, <2,1> -> {AddP(MakeP(3, 1), MakeP(2, 1))}",
)
print(
    f"IsGtP: <3,1>, <2,1> -> {IsGtP(MakeP(3, 1), MakeP(2, 1))}",
)
print(
    f"IsLtp: <3,1>, <2,1> -> {IsLtp(MakeP(3, 1), MakeP(2, 1))}",
)
print(
    f"IsEqP: <3,1>, <3,1> -> {IsEqP(MakeP(3, 1), MakeP(3, 1))}",
)
