# DEFINISI DAN SPESIFIKASI SELEKTOR
# Absis : point --> real
# Absis(P) memberikan absis point P
# Realisasi dalam Phyton
def Absis(P):
    return P[0]


# Ordinat : point --> real
# Ordinat(P) memberikan ordinat point P
# Realisasi dalam Phyton
def Ordinat(P):
    return P[1]


# GarisSatu : garis --> point
# GarisSatu(G) memberikan titik awal garis G
# Realisasi dalam Phyton
def GarisSatu(G):
    return G[0]


# GarisDua : garis --> point
# GarisDua(G) memberikan titik akhir garis G
# Realisasi dalam Phyton
def GarisDua(G):
    return G[1]


# GarisSatuSegiempat : segiempat --> garis
# GarisSatuSegiempat(SE) memberikan garis pertama pada bagian bawah segiempat
# Realisasi dalam Phyton
def GarisSatuSegiempat(SE):
    return SE[0]


# GarisDuaSegiempat : segiempat --> garis
# GarisDuaSegiempat(SE) memberikan garis kedua pada bagian kanan segiempat
# Realisasi dalam Phyton
def GarisDuaSegiempat(SE):
    return SE[1]


# GarisTigaSegiempat : segiempat --> garis
# GarisTigaSegiempat(SE) memberikan garis ketiga pada bagian atas segiempat
# Realisasi dalam Phyton
def GarisTigaSegiempat(SE):
    return SE[2]


# GarisEmpatSegiempat :segiempat --> garis
# GarisEmpatSegiempat(SE) memberikan garis keempat pada bagian kiri segiempat
# Realisasi dalam Phyton
def GarisEmpatSegiempat(SE):
    return SE[3]


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint  : 2 real  → point
# MakePoint(a,b) membentuk sebuah point dari a dan b dengan a sebagai absis dan b sebagai ordinat
# Realisasi dalam Phyton
def MakePoint(a, b):
    return [a, b]


# MakeGaris  : 2 point  → garis
# MakeGaris(P1, P2) membentuk sebuah garis dengan titik awal P1 dan titik akhir P2
# Realisasi dalam Phyton
def MakeGaris(P1, P2):
    return [P1, P2]


# MakeSegiempat  : 4 garis → segiempat
# MakeSegiempat(G1, G2, G3, G4) membentuk sebuah segiempat dengan: garis kesatu G1 pada bagian bawah, garis kedua G2 pada bagian kanan, garis ketiga G3 pada bagian atas, garis keempat G4 pada bagian kiri
# Realisasi dalam Phyton
def MakeSegiempat(G1, G2, G3, G4):
    return [G1, G2, G3, G4]


# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsBujurSangkar? : segiempat → boolean
# IsBujurSangkar(SE) mengecek apakah segiempat yang diberikan adalah bujur sangkat. Segiempat dikatakan bujur sangkar jika keempat sisinya sama panjang
# IsJajarGenjang? : segiempat → boolean
# IsJajarGenjang(SE) mengecek apakah segiempat yang diberikan  adalah jajar genjang. Segiempat dikatakan jajar genjang jika sisi-sisi yang berhadapan sama panjang dan sejajar

# DEFINISI DAN SPESIFIKASI FUNGSI TAMBAHAN
# FX2 : real --> real
# FX2(x) adalah hasil kuadrat dari x


# REALISASI
def FX2(x):
    return x * x


def SQRT(y):
    return y**0.5


def Jarak(P1, P2):
    return SQRT(FX2(Absis(P1) - Absis(P2)) + FX2(Ordinat(P1) - Ordinat(P2)))


def Gradien(P1, P2):
    return (Ordinat(P2) - Ordinat(P1)) / (Absis(P2) - Absis(P1))


def IsBujurSangkar(SE):
    if (
        Jarak(
            GarisSatu(GarisSatuSegiempat(SE)),
            GarisDua(GarisSatuSegiempat(SE)),
        )
        == Jarak(
            GarisSatu(GarisDuaSegiempat(SE)),
            GarisDua(GarisDuaSegiempat(SE)),
        )
        == Jarak(
            GarisSatu(GarisTigaSegiempat(SE)),
            GarisDua(GarisTigaSegiempat(SE)),
        )
        == Jarak(
            GarisSatu(GarisEmpatSegiempat(SE)),
            GarisDua(GarisEmpatSegiempat(SE)),
        )
    ):
        return True
    else:
        return False


def IsJajargenjang(SE):
    if (
        Gradien(GarisSatu(GarisSatuSegiempat(SE)), GarisDua(GarisSatuSegiempat(SE)))
        == Gradien(GarisSatu(GarisTigaSegiempat(SE)), GarisDua(GarisTigaSegiempat(SE)))
        and Gradien(GarisSatu(GarisSatuSegiempat(SE)), GarisDua(GarisTigaSegiempat(SE)))
        == Gradien(GarisSatu(GarisDuaSegiempat(SE)), GarisDua(GarisDuaSegiempat(SE)))
        and Jarak(GarisSatu(GarisSatuSegiempat(SE)), GarisDua(GarisSatuSegiempat(SE)))
        == Jarak(GarisSatu(GarisTigaSegiempat(SE)), GarisDua(GarisTigaSegiempat(SE)))
        and Jarak(GarisSatu(GarisSatuSegiempat(SE)), GarisDua(GarisTigaSegiempat(SE)))
        == Jarak(GarisSatu(GarisDuaSegiempat(SE)), GarisDua(GarisDuaSegiempat(SE)))
    ):
        return True
    else:
        return False


def AreaBujurSangkar(SE):
    return FX2(
        Jarak(GarisSatu(GarisSatuSegiempat(SE)), GarisDua(GarisSatuSegiempat(SE)))
    )


# APLIKASI
print(
    IsBujurSangkar(
        MakeSegiempat(
            MakeGaris(MakePoint(1, 3), MakePoint(2, 3)),
            MakeGaris(MakePoint(2, 3), MakePoint(1, 2)),
            MakeGaris(MakePoint(1, 2), MakePoint(2, 2)),
            MakeGaris(MakePoint(2, 2), MakePoint(1, 3)),
        )
    )
)
