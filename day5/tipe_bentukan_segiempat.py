"""
Program   : Tipe bentukan SEGIEMPAT
Deskripsi : sebuah program yang digunakan untuk melakukan berbagai operasi terhadap empat titik (point) pada bidang koordinat kartesius yang membentuk suatu segiempat. Program ini memiliki beberapa fungsi utama, IsBujurSangkar Memeriksa apakah empat titik yang diberikan membentuk bujur sangkar (semua sisi sama panjang dan sudut siku-siku). IsJajargenjang Memeriksa apakah empat titik yang diberikan membentuk jajargenjang (dua pasang sisi berlawanan sejajar dan sama panjang). AreaBujurSangkar Menghitung luas bujur sangkar yang dibentuk oleh empat titik. Jika titik-titik tersebut tidak membentuk bujur sangkar, fungsi akan mengembalikan pesan "BUKAN BUJUR SANGKAR". Fungsi-fungsi ini memanfaatkan operasi dasar pada titik-titik, seperti menghitung jarak antara dua titik dan gradien garis untuk menentukan kemiringan garis. Program ini dapat membantu pengguna memeriksa bentuk geometri berdasarkan titik-titik yang dimasukkan.
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
    type segiempat : <G1: garis, G2: garis, G3: garis, G4: garis>
        { Sebuah segiempat direpresentasikan oleh empat garis G1, G2, G3, dan G4 yang berada dalam bidang dua dimensi }

DEFINISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI
    Absis : point → real
        { Absis(P) memberikan absis (koordinat x) dari titik P }
    Ordinat : point → real
        { Ordinat(P) memberikan ordinat (koordinat y) dari titik P }
    GarisAwal : garis → point
        { GarisAwal(G) memberikan titik awal garis G }
    GarisAkhir : garis → point
        { GarisAkhir(G) memberikan titik akhir garis G }
    GarisSatuSegiempat : segiempat → garis
	    { GarisSatuSegiEmpat(segiempat) memberikan garis ke satu pada bagian bawah segiempat}
    GarisDuaSegiempat : segiempat → garis
	    { GarisDuaSegiEmpat(segiempat) memberikan garis ke dua pada bagian kanan segiempat}
    GarisTigaSegiempat : segiempat → garis
	    { GarisTigaSegiEmpat(segiempat) memberikan garis ke tiga pada bagian atas segiempat}
    GarisEmpatSegiempat : segiempat → garis
	    { GarisEmpatSegiEmpat(segiempat) memberikan garis ke empat pada bagian kiri segiempat}

DEFINISI DAN SPESIFIKASI KONSTRUKTOR
    MakePoint : real, real → point
        { MakePoint(x, y) membentuk sebuah titik dengan koordinat x (absis) dan y (ordinat) }
    MakeGaris : point, point → garis
        { MakeGaris(P1, P2) membentuk sebuah garis dengan titik awal P1 dan titik akhir P2 }
    MakeSegiempat : garis, garis, garis, garis → segiempat
        { MakeSegiempat(G1, G2, G3, G4) membentuk sebuah segiempat dengan garis G1, G2, G3, dan G4 }

DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP SEGIEMPAT
    AreaBujurSangkar : segiempat → real
        { AreaBujurSangkar(segiempat) menghitung luas area dari bujur sangkar yang diberikan menggunakan rumus kuadrat dari panjang garis}

DEFINISI DAN SPESIFIKASI PREDIKAT
    IsBujurSangkar? : segiempat → boolean
        { IsBujurSangkar(segiempat) mengecek apakah segiempat yang diberikan adalah bujur sangkat. Segiempat dikatakan bujur sangkar jika keempat sisinya sama panjang . }
    IsJajarGenjang? : segiempat → boolean
        { IsJajarGenjang(segiempat) mengecek apakah segiempat yang diberikan 	adalah jajar genjang. Segiempat dikatakan jajar genjang jika sisi-sisi yang 	berhadapan sama panjang dan sejajar. }


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


def MakeSegiempat(G1, G2, G3, G4):
    return [G1, G2, G3, G4]


def GarisSatuSegiempat(S):
    return S[0]


def GarisDuaSegiempat(S):
    return S[1]


def GarisTigaSegiempat(S):
    return S[2]


def GarisEmpatSegiempat(S):
    return S[3]


def FX2(x):
    return x * x


def Jarak(P1, P2):
    return (FX2(Absis(P1) - Absis(P2)) + FX2(Ordinat(P1) - Ordinat(P2))) ** 0.5


def Gradien(G):
    return (Ordinat(GarisAwal(G)) - Ordinat(GarisAkhir(G))) / (
        Absis(GarisAwal(G)) - Absis(GarisAkhir(G))
    )


def IsBujurSangkar(segiempat):
    return (
        Jarak(
            GarisAwal(GarisSatuSegiempat(segiempat)),
            GarisAkhir(GarisSatuSegiempat(segiempat)),
        )
        == Jarak(
            GarisAwal(GarisDuaSegiempat(segiempat)),
            GarisAkhir(GarisDuaSegiempat(segiempat)),
        )
        == Jarak(
            GarisAwal(GarisTigaSegiempat(segiempat)),
            GarisAkhir(GarisTigaSegiempat(segiempat)),
        )
        == Jarak(
            GarisAwal(GarisEmpatSegiempat(segiempat)),
            GarisAkhir(GarisEmpatSegiempat(segiempat)),
        )
    )


def IsJajargenjang(segiempat):
    return (
        Gradien(
            MakeGaris(
                GarisAwal(GarisSatuSegiempat(segiempat)),
                GarisAkhir(GarisSatuSegiempat(segiempat)),
            )
        )
        == Gradien(
            MakeGaris(
                GarisAwal(GarisTigaSegiempat(segiempat)),
                GarisAkhir(GarisTigaSegiempat(segiempat)),
            )
        )
        and Gradien(
            MakeGaris(
                GarisAwal(GarisSatuSegiempat(segiempat)),
                GarisAkhir(GarisTigaSegiempat(segiempat)),
            )
        )
        == Gradien(
            MakeGaris(
                GarisAwal(GarisDuaSegiempat(segiempat)),
                GarisAkhir(GarisDuaSegiempat(segiempat)),
            )
        )
        and Jarak(
            GarisAwal(GarisSatuSegiempat(segiempat)),
            GarisAkhir(GarisSatuSegiempat(segiempat)),
        )
        == Jarak(
            GarisAwal(GarisTigaSegiempat(segiempat)),
            GarisAkhir(GarisTigaSegiempat(segiempat)),
        )
        and Jarak(
            GarisAwal(GarisSatuSegiempat(segiempat)),
            GarisAkhir(GarisTigaSegiempat(segiempat)),
        )
        == Jarak(
            GarisAwal(GarisDuaSegiempat(segiempat)),
            GarisAkhir(GarisDuaSegiempat(segiempat)),
        )
    )


def AreaBujurSangkar(segiempat):
    return FX2(
        Jarak(
            GarisAwal(GarisSatuSegiempat(segiempat)),
            GarisAkhir(GarisSatuSegiempat(segiempat)),
        )
    )


"""
**************************************************************
APLIKASI
**************************************************************
"""
print(
    f"""IsJajargenjang: <1,1>, <4,1>, <6,4>, <3,4> -> {
        IsJajargenjang(
            MakeSegiempat(
                MakeGaris(MakePoint(1, 1), MakePoint(4, 1)),
                MakeGaris(MakePoint(4, 1), MakePoint(6, 4)),
                MakeGaris(MakePoint(6, 4), MakePoint(3, 4)),
                MakeGaris(MakePoint(3, 4), MakePoint(1, 1))
            )
        )
    }"""
)
print(
    f"""IsBujurSangkar: <1,3>, <2,3>, <2,2>, <1,2> -> {
        IsBujurSangkar(
            MakeSegiempat(
                MakeGaris(MakePoint(1, 3), MakePoint(2, 3)), 
                MakeGaris(MakePoint(2, 3), MakePoint(2, 2)), 
                MakeGaris(MakePoint(2, 2), MakePoint(1, 2)), 
                MakeGaris(MakePoint(1, 2), MakePoint(1, 3))
             )
        )
    }"""
)
print(
    f"""AreaBujurSangkar: <1,3>, <2,3>, <1,2>, <2,2> -> {
        AreaBujurSangkar(
            MakeSegiempat(
                MakeGaris(MakePoint(1, 3),MakePoint(2, 3)),
                MakeGaris(MakePoint(2, 3),MakePoint(1, 2)),
                MakeGaris(MakePoint(1, 2),MakePoint(2, 2)),
                MakeGaris(MakePoint(2, 2),MakePoint(1, 3))
            )
            )
    }"""
)
