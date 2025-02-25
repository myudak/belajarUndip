"""
1. {30%} Buatlah definisi, spesifikasi, realisasi, dan aplikasi (dalam notasi fungsional) serta realisasi dalam Python untuk sebuah fungsi yang menerima masukan berupa tiga 3 nilai <d,m,y> yang membentuk sebuah tanggal, kemudian memberikan keluaran berupa string tanggal lahir. Keterangan dari masing-masing masukan tersebut adalah sebagai berikut:
    -  d merupakan hari dari sebuah tanggal yang berupa bilangan bulat positif bernilai 1 sampai dengan 31.
    -  m merupakan bulan dari sebuah tanggal yang berupa bilangan bulat positif bernilai 1 sampai dengan 12.
    -  y merupakan merupakan tahun dari sebuah tanggal berupa bilanga bulat positif mulai dari 1900.
Sebagai contoh jika fungsi tersebut diberi masukan <10,12,2010> maka keluarannya adalah string ’10 Desember 2010’. Terdapat beberapa fungsi yang telah disediakan oleh sistem sebagai berikut: (fungsi-fungsi berikut dapat langsung digunakan tanpa perlu direalisasi karena realisasinya sudah disediakan oleh sistem)
"""

"""
DEFINISI DAN SPESIFIKASI
StrToInt: string -> integer
    {StrToInt(x) mengkonversi string x menjadi nilai integer yang bersesuaian.
        Contoh: StrToInt(’01’) adalah 1 }
IntToStr: integer -> string
    {IntToStr(x) mengkonversi integer x menjadi nilai string yang bersesuaian.
        Contoh: IntToStr(12) adalah ‘12’ }
IntKeBulan : integer -> string
    {IntKeBulan(x) mengembalikan nama bulan berdasarkan nilai integer x yang bersesuaian.
        Contoh: IntKeBulan(1) adalah ‘Januari’ }
tanggalKeDate: 3 integer -> string
    {tanggalKeDate(d,m,y) mengembalikan string tanggal berdasarkan nilai integer d,m,y yang bersesuaian.
        Contoh: tanggalKeDate(10,12,2010) adalah ‘10 Desember 2010’ }
"""


def StrToInt(x):  # BAWAAN
    return int(x)


def IntToStr(x):  # BAWAAN
    return str(x)


def IntKeBulan(x):
    if x == 1:
        return "Januari"
    if x == 2:
        return "Februari"
    if x == 3:
        return "Maret"
    if x == 4:
        return "April"
    if x == 5:
        return "Mei"
    if x == 6:
        return "Juni"
    if x == 7:
        return "Juli"
    if x == 8:
        return "Agustus"
    if x == 9:
        return "September"
    if x == 10:
        return "Oktober"
    if x == 11:
        return "November"
    if x == 12:
        return "Desember"


def tanggalKeDate(d, m, y):
    return IntToStr(d) + " " + IntKeBulan(m) + " " + IntToStr(y)


print(f"tanggalKeDate(’10’, ’12’, ’2010’) = {tanggalKeDate(10,12,2010)}")
print(f"tanggalKeDate(’9’, ’6’, ’2069’) = {tanggalKeDate(9,6,2069)}")
print(f"tanggalKeDate(’6’, ’9’, ’2099’) = {tanggalKeDate(6,9,2099)}")

"""
2. {30%} Buatlah definisi, spesifikasi, realisasi, dan aplikasi (dalam notasi fungsional) serta realisasi dalam Python untuk sebuah fungsi yang menerima masukan berupa tiga 3 nilai <d,m,y> yang membentuk sebuah tanggal seperti soal nomor 1,kemudian mengembalikan hari absolut yang dihitung mulai tanggal 1 Januari 1900 dengan memperhitungkan tahun kabisat.
"""

"""
DEFINISI DAN SPESIFIKASI
Day: 3 integer -> integer
    {Day(d,m,y) mengembalikan hari absolut yang dihitung mulai tanggal 1 Januari 1900 dengan memperhitungkan tahun kabisat }
"""


def Day(d, m, y):
    if y < 1900:
        return 0
    if y == 1900:
        if m < 2:
            return 31
        if m == 2:
            if d < 8:
                return 31
            if d == 8:
                return 30
            if d > 8:
                return 31
        if m > 2:
            return 31
    if y > 1900:
        if m < 3:
            return 31
        if m == 3:
            if d < 1:
                return 31
            if d == 1:
                return 30
            if d > 1:
                return 31
        if m > 3:
            return 31
