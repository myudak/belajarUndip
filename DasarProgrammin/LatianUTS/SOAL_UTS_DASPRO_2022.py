"""
=================================================================================================================================================
SOAL URAIAN :
"""

"""
1. {30%} Buatlah definisi, spesifikasi, realisasi, dan realisasi dalam python untuk sebuah fungsi
yang menghitung biaya panggilan dari sebuah provider telekomunikasi berdasarkan kode
wilayah dan lama bicara dalam satuan detik seperti tabel berikut ini:

Kode Wilayah | Tarif Pulsa (30 detik pertama) | Tarif pulsa setelah 30 detik berikutnya

A Rp. 200,- Rp. 10,- / detik
B Rp. 300,- Rp. 20,- / detik
C Rp. 350,- Rp. 25,- / detik

Contoh: seseorang berada di kode wilayah A melakukan panggilan selama 40 detik, maka
biayanya adalah: 200 + (10 x 10) = 300.
"""


def tagihanBulan(kode, detik):
    if kode == "A":
        if detik <= 30:
            return 200
        return 200 + (10 * (detik - 30))
    if kode == "B":
        if detik <= 10:
            return 300
        return 300 + (20 * (detik - 30))
    if kode == "C":
        if detik <= 10:
            return 350
        return 350 + (25 * (detik - 30))


"""
**************************************************************
APLIKASI
**************************************************************
"""


print(f"tagihanBulan('A', 10) = {tagihanBulan('A', 10)}")
print(f"tagihanBulan('B', 34) = {tagihanBulan('B', 34)}")
print(f"tagihanBulan('C', 40) = {tagihanBulan('C', 40)}")

# Nomer 2


def Day(D):
    return D[0]


def Month(D):
    return D[1]


def Year(D):
    return D[2]


def MakeDate(d, m, y):
    return [d, m, y]


def MakeDiskon(kategori, diskon):
    return [kategori, diskon]


def DiskonUsia(TglLahir, TglBrkt):
    if (
        Year(TglBrkt) - Year(TglLahir) < 2
        or Year(TglBrkt) - Year(TglLahir) == 2
        and Month(TglBrkt) < Month(TglLahir)
        or Year(TglBrkt) - Year(TglLahir) == 2
        and Month(TglBrkt) == Month(TglLahir)
        and Day(TglBrkt) <= Day(TglLahir)
    ):
        return MakeDiskon("infant", 75)
    if (
        Year(TglBrkt) - Year(TglLahir) < 12
        or Year(TglBrkt) - Year(TglLahir) == 12
        and Month(TglBrkt) < Month(TglLahir)
        or Year(TglBrkt) - Year(TglLahir) == 12
        and Month(TglBrkt) == Month(TglLahir)
        and Day(TglBrkt) <= Day(TglLahir)
    ):
        return MakeDiskon("child", 25)
    return MakeDiskon("adult", 0)


print(DiskonUsia(MakeDate(10, 1, 2000), MakeDate(1, 1, 2002)))
print(DiskonUsia(MakeDate(10, 1, 2000), MakeDate(1, 1, 2004)))
print(DiskonUsia(MakeDate(10, 1, 2000), MakeDate(1, 1, 2024)))

# Nomer 3
# DEFSPEK TYPE
# type Waktu : <string, 3 integer>


# DEFSPEK SELEKTOR
# hari: Waktu -> string
def hari(w):
    return w[0]


# jam: Waktu -> integer
def jam(w):
    return w[1]


# menit: Waktu -> integer
def menit(w):
    return w[2]


# detik: Waktu -> integer
def detik(w):
    return w[3]


# DEFSPEK KONSTRUKTOR
def MakeWaktu(h, j, m, s):
    return [h, j, m, s]


# DEFSPEK OPERATOR
# GetSelisihWaktu: 2 Waktu -> integer
def GetSelisihWaktu(w1, w2):
    return abs(
        (jam(w1) * 3600 + menit(w1) * 60 + detik(w1))
        - (jam(w2) * 3600 + menit(w2) * 60 + detik(w2))
    )


# APLIKASI
print(
    GetSelisihWaktu(
        MakeWaktu("Senin", 6, 45, 49),
        MakeWaktu("Selasa", 8, 30, 59),
    )
)
