"""
UJIAN TENGAH SEMESTER GASAL 2023/2024
Mata Kuliah : PAIK6102/ AIK21311- Dasar Pemrograman
Kelas       : A, B, C, D, E
Pengampu    : Helmie Arif Wibawa, S.Si., M.Cs/ Khadijah, S.Kom., M.Cs / Dr. Eng. Adi Wibowo, S.Si., M.Kom

Departemen/Program Studi    : Ilmu Komputer / Informatika
Hari/Tanggal                : Senin, 9 Oktober 2023
Jam/Ruang                   : 08:00 - 09:30 WIB (90 menit)/E101, E102, E103, A303
Sifat Ujian                 : Buku Terbuka

Capaian Pembelajaran Lulusan (CPL)
CPL-P05:
Mampu menerapkan konsep teoretis bidang ilmu komputer dalam
mengidentifikasi solusi permasalahan kompleks dengan prinsip
komputasi dan ilmu lain yang relevan.

Capaian Pembelajaran Mata Kuliah (CPMK) dan Sub-CPMK
CPMK05-2:
Mampu menerapkan (C3) konsep teoretis bidang pengetahuan dan
keterampilan Ilmu Komputer dalam menyelesaikan permasalahan
(P4) kompleks dengan pemikiran komputasional untuk pengambilan
keputusan.
Sub CPMKX05-2:
1. Mampu memahami dan menerapkan konsep pemrograman
fungsional untuk membangun fungsi menggunakan ekspresi
dasar sebagai solusi dari suatu permasalahan.
2. Mampu memahami dan menerapkan konsep analisa kasus dalam
pemrograman fungsional.
3. Mampu memahami dan menerapkan konsep tipe bentukan
dalam pemrograman fungsional.
"""

"""
Petunjuk Pengerjaan:
A. Tuliskan identitas NIM, Nama, pada setiap lembar jawab!
B. Jawablah soal-soal berikut pada lembar jawab dan bila perlu disertai asumsi/gambar!
"""

"""
=================================================================================================================================================
SOAL URAIAN :
"""


"""
1. [CPMK05-2 (1,2) bobot 25%] Buatlah definisi, spesifikasi, realisasi, dan realisasi untuk
sebuah fungsi yang menghitung biaya tagihan bulanan dari sebuah perusahaan air
berdasarkan kode pelanggan seperti tabel berikut ini:

Kode Pelanggan| Tarif 10 m3 pertama | Tarif setelah 10 m3 berikutnya
A             | Rp. 30.000,-        | Rp. 2.500,- / m3
B             | Rp. 50.000,-        | Rp. 3.000,- / m3
C             | Rp. 50.000,-        | Rp. 3.500,- / m3

Contoh: seseorang pelanggan dengan kode pelanggan A dan penggunaan air selama bulan
tersebut sebanyak 25 m3, maka tagihannya adalah:
Rp 30.000,- + (15 x Rp. 2.500,-) = Rp. 67.500,-
"""

"""
**************************************************************
BIAYA TAGIHAN BULANAN   | biaya_tagihan_bulanan(kode_pelanggan, penggunaan_air)
**************************************************************

**************************************************************
DEFINISI DAN SPESIFIKASI
    biaya_tagihan_bulanan : string, real → real
        { biaya_tagihan_bulanan(kode_pelanggan, penggunaan_air) menghitung biaya tagihan bulanan dari pelanggan dengan kode pelanggan kode_pelanggan dan penggunaan air penggunaan_air }
**************************************************************

**************************************************************
REALISASI
**************************************************************
"""


def biaya_tagihan_bulanan(kode_pelanggan, penggunaan_air):
    if kode_pelanggan == "A":
        if penggunaan_air > 10:
            return 30000 + (penggunaan_air - 10) * 2500
        return 30000
    if kode_pelanggan == "B":
        if penggunaan_air > 10:
            return 50000 + (penggunaan_air - 10) * 3000
        return 50000
    if kode_pelanggan == "C":
        if penggunaan_air > 10:
            return 50000 + (penggunaan_air - 10) * 3500
        return 50000


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(f"biaya_tagihan_bulanan('A', 10) = {biaya_tagihan_bulanan('A', 10)}")
print(f"biaya_tagihan_bulanan('A', 25) = {biaya_tagihan_bulanan('A', 25)}")
print(f"biaya_tagihan_bulanan('B', 25) = {biaya_tagihan_bulanan('B', 25)}")

"""
2. [CPMK05-2 (2) bobot 35%] Buatlah definisi, spesifikasi dan realisasi dari suatu predikat IsNextDayFriday? yang akan memeriksa apakah nama hari pada esok harinya setelah tanggal yang diberikan adalah hari Jum'at, jika diketahui suatu data masukan yang berupa tanggal bulan dan tahun, dan diketahui bahwa pada tanggal 1 Januari pada tahun yang bersangkutan adalah hari Senin, dengan memperhatikan tahun kabisatnya!

Contoh aplikasi:
Is TomorrowFriday?(2,1,1990) → False
IsTomorrowFriday?(4,1,1990)  → True
IsTomorrowFriday?(9,3,1993)  → True
"""

"""
**************************************************************
Is Tomorrow Friday   | IsTomorrowFriday(d,m,y)
**************************************************************

**************************************************************
DEFINISI DAN SPESIFIKASI
    IsTomorrowFriday : 3 integer → boolean
        { IsTomorrowFriday(d,m,y) memeriksa apakah nama hari pada esok harinya setelah tanggal yang diberikan adalah hari Jum'at,}

DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
    HariKe1900 : integer [1..31], integer [1..12], integer [0..99] → integer [1..366]
        {HariKe1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari absolut dihitung mulai 1 Januari tahun 1900+y. 1 Januari tahun 1900+y adalah hari ke 1}
    dpm : integer [1..12] → integer [1..366]
        {dpm(B) adalah jumlah hari kumulatif dari tanggal 1 Januari hingga tanggal 1 bulan B pada tahun tertentu, tanpa memperhitungkan tahun kabisat.}
    IsKabisat? : integer [0..99] → boolean
        {IsKabisat?(y) menghasilkan True jika tahun 1900+y adalah tahun kabisat, yaitu habis dibagi 4 tetapi tidak habis dibagi 100, atau habis dibagi 400.}
**************************************************************

**************************************************************
REALISASI
**************************************************************
"""


def dpm(bulan):
    if bulan == 1:
        return 1
    if bulan == 2:
        return 32
    if bulan == 3:
        return 60
    if bulan == 4:
        return 91
    if bulan == 5:
        return 121
    if bulan == 6:
        return 152
    if bulan == 7:
        return 182
    if bulan == 8:
        return 213
    if bulan == 9:
        return 244
    if bulan == 10:
        return 274
    if bulan == 11:
        return 305
    if bulan == 12:
        return 335


def IsKabisat(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def HariKe1900(d, m, y):
    return dpm(m) + d - 1 + (1 if m > 2 and IsKabisat(y) else 0)


def IsTomorrowFriday(d, m, y):
    return HariKe1900(d, m, y) % 7 + 1 == 5


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(f"IsTomorrowFriday(2,1,1990) = {IsTomorrowFriday(2, 1, 1990)}")
print(f"IsTomorrowFriday(4,1,1990) = {IsTomorrowFriday(4, 1, 1990)}")
print(f"IsTomorrowFriday(9,3,1993) = {IsTomorrowFriday(9, 3, 1993)}")

"""
3. [CPMK05-2 (2,3) bobot 40%] Definisikan sebuah tipe bentukan untuk garis yang terdiri atas 2 tipe
point <P1: point, P2:point>

Tuliskan notasi fungsionalnya untuk:
a. Definisi dan spesifikasi tipe garis tersebut
b. Definisi dan spesifikasi selektor
c. Definisi dan spesifikasi konstruktor
d. Definisi, spesifikasi, realisasi dan aplikasi operator/fungsi berikut:
PanjangGaris(G) yang menghitung panjang garis G
e. Definisi, spesifikasi,realisasi dan aplikasi predikat berikut:
IsKuadran3?(G) di mana predikat tersebut memberikan nilai True apabila keseluruhan garis berada pada kuadran III
"""

"""
**************************************************************
TYPE GARIS
**************************************************************

**************************************************************
DEFINISI TYPE
    type point : <x: real, y: real>
        { <x: real, y: real> merepresentasikan sebuah titik dalam bidang dua dimensi. x adalah absis (horizontal) dan y adalah ordinat (vertical) }
    type garis : <P1: point, P2: point>
        { Sebuah garis direpresentasikan oleh dua titik P1 dan P2 yang berada dalam bidang dua dimensi }
**************************************************************

**************************************************************
DEFINISI DAN SPESIFIKASI SELEKTOR 
    Absis : point  → real 
        { Absis(P) Memberikan Absis Point P } 
    Ordinat : point  → real 
        { Ordinat(P) Memberikan ordinat Point P } 
    GarisAwal : garis → point 
        { GarisAwal(G) memberikan titik awal garis G } 
    GarisAkhir : garis → point 
        { GarisAkhir(G) memberikan titik akhir garis G }
**************************************************************

**************************************************************
DEFINISI DAN SPESIFIKASI KONSTRUKTOR 
    MakePoint  : 2 real  → point 
        { MakePoint(a,b) membentuk sebuah point dari a dan b dengan a sebagai absis dan b sebagai ordinat } 
    MakeGaris  : 2 point  → garis 
        { MakeGaris(P1, P2) membentuk sebuah garis dengan titik awal P1 dan titik akhir P2 }
**************************************************************

**************************************************************
DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP GARIS 
    PanjangGaris : garis → boolean 
        { PanjangGaris(garis) menghitung panjang garis antara dua titik Absis(garis) dan Ordinat(garis) menggunakan rumus jarak Euclidean }
**************************************************************

**************************************************************
DEFINISI DAN SPESIFIKASI PREDIKAT
    IsKuadran3 : point → boolean
        { IsKuadran3(P) mengecek apakah point P adalah kuadran 3 }
**************************************************************

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


def PanjangGaris(G):
    return (
        FX2(Absis(GarisAwal(G)) - Absis(GarisAkhir(G)))
        + FX2(Ordinat(GarisAwal(G)) - Ordinat(GarisAkhir(G)))
    ) ** 0.5


def IsKuadran3(P):
    return Absis(P) < 0 and Ordinat(P) < 0


"""
**************************************************************
APLIKASI
**************************************************************
"""
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
