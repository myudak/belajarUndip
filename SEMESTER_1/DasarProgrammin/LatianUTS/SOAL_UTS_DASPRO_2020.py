"""
1. {30%} Buatlah definisi, spesifikasi, realisasi, dan aplikasi (dalam notasi fungsional) serta realisasi dalam Python untuk sebuah fungsi yang menerima masukan berupa tiga 3 nilai <bil, n, d> yang membentuk pecahan campuran dan menghasilkan nilai berupa bilangan desimal yang ekuivalen dengan pecahan campuran tersebut. Keterangan dari masing-masing
masukan tersebut adalah sebagai berikut:
    - bil merupakan bilangan bulat dari sebuah pecahan campuran yang berupa bilangan bulat positif, 0, atau negatif.
    - n merupakan pembilang dari sebuah pecahan campuran yang berupa bilangan bulat 0 atau positif.
    - d merupakan penyebut dari sebuah pecahan campuran yang berupa bilangan bulat positif bukan 0.
"""

"""
DEFINISI DAN SPESIFIKASI
    pecahan_campuran : 3 integer → real
        { pecahan_campuran(bil, n, d) mengembalikan nilai real yang berupa pecahan campuran dari bil, n, d }
"""


def pecahan_campuran(bil, n, d):
    return bil + n / d


"""
APPLIKASI
"""

print(f"pecahan_campuran(10, 3, 5) = {pecahan_campuran(10, 3, 5)}")
print(f"pecahan_campuran(10, 0, 5) = {pecahan_campuran(10, 0, 5)}")
print(f"pecahan_campuran(10, -3, 5) = {pecahan_campuran(10, -3, 5)}")

"""
2. {30%} Tanggal lahir seseorang dapat dilihat dari NIK (Nomor Induk Kependudukan) pada digit 7 s.d.12 dengan format ddmmyy (dd adalah tanggal lahir, mm adalah bulan dan yy adalah 2 digit tahun angka tahun dari belakang). Jika jenis kelamin wanita, maka tanggal lahir (dd) ditambah 40. Jika angka tahun (yy) ditambah 2000 melebihi tahun saat ini, maka tahun lahir diawali dengan ‘19’, sebaliknya tahun diawali dengan ‘20’. Sebagai contoh:
    - seseorang memiliki NIK 3374025012900003 maka orang tersebut berjenis kelamin perempuan dan memiliki tanggal lahir 10 Desember 1990.
    - seseorang memiliki NIK 3374021012100003 maka orang tersebut berjenis kelamin laki-laki dan memiliki tanggal lahir 10 Desember 2010.
Buatlah definisi, spesifikasi, realisasi dan aplikasi (dalam notasi fungsional) untuk sebuah fungsi yang menerima masukan berupa string NIK kemudian memberikan keluaran berupa


"""

"""
DEFINISI DAN SPESIFIKASI
    NIK : string → string
        { NIK(NIK) mengembalikan string tanggal lahir seseorang berdasarkan NIK }
"""


def NIK(NIK):
    if len(NIK) != 12:
        return "Error"
