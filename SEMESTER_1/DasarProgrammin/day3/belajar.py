"""
Latihan
Terjemakanlah contoh notasi fungsional pada Diktat berikut ke dalam bahasa pemrograman 
Python (perhatikan aturan standar penulisan program):
"""

"""
1. Ekspresi kondisional: penanggalan versi 1 (tanpa memperhitungkan tahun kabisat)
Definisi dan Spesifikasi
HariKe1900 : integer [1..31], integer [1..12], integer [0..99] → integer [1..366]
{HariKe1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari absolut dihitung mulai 1 Januari tahun 1900+y. 1 Januari tahun 1900+y adalah hari ke 1}

dpm : integer [1..12] → integer [1..366]
{dpm(B) adalah jumlah hari kumulatif dari tanggal 1 Januari hingga tanggal 1 bulan B pada tahun tertentu, tanpa memperhitungkan tahun kabisat.}

Realisasi Spesifikasi:
"""


def dpm(bulan: int) -> int:
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


def HariKe1900(hari: int, bulan: int, tahun: int) -> int:
    return dpm(bulan) + hari - 1


print(HariKe1900(1, 1, 82))  # -> 1
print(HariKe1900(31, 12, 72))  # -> 366
print(HariKe1900(3, 4, 93))  # -> 93

"""
2. Ekspresi kondisional: penanggalan versi 2 (dengan memperhitungkan tahun kabisat)

Definisi dan Spesifikasi
HariKe1900 : integer [1..31], integer [1..12], integer [0..99] → integer [1..366]
{HariKe1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari absolut dihitung mulai 1 Januari tahun 1900+y. Memperhitungkan tahun kabisat.}

dpm : integer [1..12] → integer [1..366]
{dpm(B) adalah jumlah hari kumulatif dari tanggal 1 Januari hingga tanggal 1 bulan B pada tahun tertentu.}

IsKabisat? : integer [0..99] → boolean
{IsKabisat?(y) menghasilkan True jika tahun 1900+y adalah tahun kabisat, yaitu habis dibagi 4 tetapi tidak habis dibagi 100, atau habis dibagi 400.}

Realisasi Spesifikasi:
"""


def IsKabisat(y: int) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def HariKe1900Kabisat(d: int, m: int, y: int) -> int:
    return dpm(m) + d - 1 + (1 if m > 2 and IsKabisat(y) else 0)


print(HariKe1900Kabisat(1, 1, 82))  # -> 1
print(HariKe1900Kabisat(31, 12, 72))  # -> 366
print(HariKe1900Kabisat(3, 4, 93))  # -> 93

"""
3. Tuliskanlah sebuah fungsi yang menerima suatu besaran dalam dalam derajat Celcius dan 
kode konversi ke derajat Reamur, Fahrenheit atau Kelvin, dan mengirimkan nilai derajat 
sesuai kode konversi. (Diktat, halaman 34, no 6)
"""


def UbahCelcius(C: int, kode: str):

    def CelciusKeFahrenheit(C: int) -> int:
        return C * 9 / 5 + 32

    def CelciusKeKelvin(C: int) -> int:
        return C + 273.15

    def CelciusKeReamur(C: int) -> int:
        return C * 4 / 5

    if kode == "C":
        return C
    if kode == "F":
        return CelciusKeFahrenheit(C)
    if kode == "K":
        return CelciusKeKelvin(C)
    if kode == "R":
        return CelciusKeReamur(C)
    return "kode gak valid"


print(UbahCelcius(0, "C"))  # -> 0
print(UbahCelcius(100, "C"))  # -> 100
print(UbahCelcius(0, "F"))  # -> 32
print(UbahCelcius(100, "R"))  # -> 212
print(UbahCelcius(0, "K"))  # -> 273.15

"""
4. Buatlah program fungsional yang menerima masukan suatu besaran yang menyatakan 
temperatur air dalam derajat Celcius dan pada tekanan 1 atm dan menghasilkan
wujudnya, apakah berwujud es (padat), cair atau uap. (Diktat, halaman 34, no 7).
"""


def isPadatCairUap(C: int) -> str:
    if C <= 0:
        return "padat"
    if C >= 100:
        return "uap"
    return "cair"


"""
5. Buatlah program fungsional yang menerima sebuah masukan berupa 3 buah bilangan 
integer lebih besar dari 0, yaitu a,b dan c yang menyatakan panjang setiap sisi pada 
sebuah segitiga. Tentukanlah apakah segitiga tersebut sama sisi, sama kaki atau 
sembarang.
"""


def cekSamaSisi(a: int, b: int, c: int) -> str:
    if a == b == c:
        return "sama sisi"
    if a == b or a == c or b == c:
        return "sama kaki"
    return "sembarang"


"""
6. Buatlah program fungsional untuk menghitung hasil pembagian antara akar-akar
persamaan kuadrat ax2
+ bx + c = 0 menggunakan rumus abc dengan masukan berupa 3 
buah koefisien, yaitu a, b dan c . (pembagian dihitung dari akar persamaan kuadrat yang 
lebih besar dibagi dengan akar persamaan kuadrat yang lebih kecil)
"""


def mboh():
    "mboh"


# TUGAS PAKNYA **************************************************************

"""
Program   : Ekspresi Kondisional: Penanggalan dari paknya
Deskripsi : Program ini menghitung hari ke-n dari suatu tanggal berdasarkan tahun 1900+y dan memeriksa apakah lusa (hari setelah besok) adalah hari Kamis.
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 15/09/2024
"""

"""
**************************************************************
DEFINISI DAN SPESIFIKASI
HariKe1900 : integer [1..31], integer [1..12], integer [0..99] → integer [1..366]
{HariKe1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari absolut dihitung mulai 1 Januari tahun 1900+y. 1 Januari tahun 1900+y adalah hari ke 1}

dpm : integer [1..12] → integer [1..366]
{dpm(B) adalah jumlah hari kumulatif dari tanggal 1 Januari hingga tanggal 1 bulan B pada tahun tertentu, tanpa memperhitungkan tahun kabisat.}

totalKabisat : integer [0..99] → integer [0..366]
{totalKabisat(y) menghitung jumlah tahun kabisat dari tahun 1900 hingga tahun 1900+y-1.}

ApakahLusaHariKamis : integer [1..31], integer [1..12], integer [0..99] → boolean
{ApakahLusaHariKamis(d, m, y) memeriksa apakah lusa (hari setelah besok) dari tanggal <d,m,y> adalah hari Kamis.}
**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def dpm(bulan: int) -> int:
    """Menghitung jumlah hari kumulatif dari tanggal 1 Januari hingga tanggal 1 bulan B pada tahun tertentu"""
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


def HariKe1900(hari: int, bulan: int, tahun: int) -> int:
    """Menghitung hari ke-n dari tanggal <hari, bulan, tahun> dari 1 Januari 1900+y"""
    return dpm(bulan) + hari - 1


def totalKabisat(y: int) -> int:
    """Menghitung jumlah tahun kabisat dari 1900 hingga tahun 1900+y-1"""
    return (
        (y - 1) // 4
        - (y - 1) // 100
        + (y - 1) // 400
        - (1900 // 4 - 1900 // 100 + 1900 // 400)
    )


def ApakahLusaHariKamis(d: int, m: int, y: int) -> bool:
    """Memeriksa apakah lusa (hari setelah besok) dari tanggal <d, m, y> adalah hari Kamis"""
    totalHari = HariKe1900(d + 2, m, y)
    # totalHariSejak1900
    return (totalHari + (y - 1900) * 365 + totalKabisat(y)) % 7 == 3


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(f"Apakah Lusa hari Kamis: {ApakahLusaHariKamis(17, 9, 2024)}")

"""
**************************************************************
NOTASI FUNGSIONAL??
**************************************************************

totalKabisat(y):
  (y - 1) // 4 
  - (y - 1) // 100
  + (y - 1) // 400
  - (1900 // 4 - 1900 // 100 + 1900 // 400)

ApakahLusaHariKamis(d, m, y) = 
  let totalHari = HariKe1900(d + 2, m, y) in
  let totalHariSejak1900 = totalHari + (y - 1900) * 365 + totalKabisat(y) in
  totalHariSejak1900 mod 7 = 3
"""
