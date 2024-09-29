# 1. Tipe bentukan pecahan (diktat)
"""
Kasus-2: Type PECAHAN 
Didefinisikan suatu type bernama Pecahan, yang terdiri dari pembilang dan penyebut. 
Berikut ini adalah teks dalam notasi fungsional untuk type pecahan tersebut. 
Perhatikanlah bahwa realisasi fungsi hanya dilakukan untuk operator aritmatika dan 
relasional terhadap pecahan. Realisasi selektor hanya diberikan secara konseptual, karena 
nantinya akan diserahkan implementasinya ke bahasa pemrograman
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


print(
    f"IsGtP: <3,1>, <2,1> -> {IsGtP(MakeP(3, 1), MakeP(2, 1))}",
)

"""
2. Tipe bentukan tanggal (diktat)
KASUS-3 : PENANGGALAN 
Didefinisikan suatu type Date yang terdiri dari thari, bulan dan tahun dan membentuk 
komposisi <Hr,Bln,Thn >. Dalam contoh ini, sebuah nama type bukan merupakan nama 
type bentukan, melainkan sebuah subdomain (sebagian dari nilai domain). Penamaan 
semacam ini akan mempermudah pembacaan teks 

DEFINISI DAN SPESIFIKASI TYPE
type Hr : integer [1...31] 
 {definisi ini hanyalah untuk “menamakan” type integer dengan nilai tertentu supaya 
mewakili hari, sehingga jika dipunyai suatu nilai integer, kita dapat memeriksa apakah 
nilai integer tersebut mewakili Hari yang absah } 
type Bln : integer [1...12] 
 {definisi ini hanyalah untuk “menamakan” type integer dengan daerah nilai tertentu 
supaya mewakili Bulan } 
type Thn : integer > 0 
 {definisi ini hanyalah untuk “menamakan“ type integer dengan daerah nilai tertentu 
supaya mewakili tahun } 
type date <d: Hr, m:Bln,y:Thn> 
 { <d,m,y> adalah tanggal d bulan m tahun y } 


 DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP DATE
Nextday : date → date 
 {NextDay(D): menghitung date yang merupakan keesokan hari dari date D yang 
diberikan: 
 Nextday (<1,1,80>) adalah (<2,1,80>) 
 Nextday (<31,1,80>) adalah (<1,2,80> 
 Nextday (<30,4,80>) adalah (<1,5,80> 
 Nextday (<31,12,80>) adalah (<1,1,81> 
 Nextday (<28,2,80>) adalah (<29,2,80> 
 Nextday (<28,2,81>) adalah (<1,3,82> } 

Yesterday : date → date 
 { Yesterday(D): Menghitung date yang merupakan 1 hari sebelum date D yang 
diberikan: 
 Yesterday (<1,1,80>) adalah <31,12,79> 
 Yesterday (<31,1,80>) adalah <30,1,80> 
 Yesterday (<1,5,80>) adalah <30,4,80> 
 Yesterday (<31,12,80>) adalah <30,12,80> 
 Yesterday (<29,2,80>) adalah <28,2,80> 
 Yesterday (<1,3,80>) adalah <29,2,80> } 
NextNday : date,integer → date 
{ NextNDay(D,N) : Menghitung date yang merupakan N hari (N adalah nilai integer) 
sesudah dari date D yang diberikan} 
HariKe1900: date → integer [0..366] 
{HariKe1900(D) : Menghitung jumlah hari terhadap 1 Januari pada tahun y, dengan 
memperhitungkan apakah y adalah tahun kabisat } 
PREDIKAT
IsEqD?: 2 date → boolean
 {IsEqD?(d1,d2) benar jika d1=d2, mengirimkan true jika d1=d2 and m1=m2 and 
y1=y2. Contoh : EqD(<1,1,90>,<1,1,90>) adalah true
 EqD(<1,2,90>,<1,1,90>) adalah false } 
IsBefore? : 2 date → boolean
 {IsBefore?(d1,d2) benar e jika d1 adalah sebelum d2 mengirimkan true jika D1 adalah 
"sebelum" D2: 
 HariKe1900 dari D1 adalah lebih kecil dari HariKe1900 D2 } 
 {Contoh : Before (<1,1,80>,<1,2,80>) adalah false } 
 Before (<1,1,80>,<2,1,80>) adalah true } 
IsAfter? : 2 date → boolean
 {IsAfter?(d1,d2) benar jika d1 adalah sesudah d2 mengirimkan true jika D1 adalah 
"sesudah" D2: HariKe1900 dari D1 adalah lebih besar dari HariKe1900 dari D2. 
 Contoh : After (<1,11,80>,<1,2,80>) adalah true 
 After (<1,1,80>,<2,1,80>) adalah false
 After (<1,1,80>,<1,1,80>) adalah false} 
IsKabisat? : integer → boolean
{IsKabisat?(a) true jika tahun 1900+a adalah tahun kabisat: habis dibagi 4 tetapi tidak 
habis dibagi 100, atau habis dibagi 400 }
"""


def Day(date):
    return date[0]


def Month(date):
    return date[1]


def Year(date):
    return date[2]


def MakeDate(Hr, Bln, Thn):
    if Hr < 1 or Hr > 31:
        return f"Error Hr: {Hr}"
    if Bln < 1 or Bln > 12:
        return f"Error Bln: {Bln}"
    if Thn < 1:
        return f"Error Thn: {Thn}"
    return [Hr, Bln, Thn]


def NextDay(date):
    if Month(date) in [1, 3, 5, 7, 8, 10]:
        if Day(date) < 31:
            return MakeDate(Day(date) + 1, Month(date), Year(date))
        return MakeDate(1, Month(date) + 1, Year(date))
    if Month(date) in [4, 6, 9, 11]:
        if Month(date) < 30:
            return MakeDate(Day(date) + 1, Month(date), Year(date))
        return MakeDate(1, Month(date) + 1, Year(date))
    if Month(date) == 2:
        if IsKabisat(Year(date)):
            if Day(date) == 28:
                return MakeDate(Day(date) + 1, Month(date), Year(date))
            return MakeDate(1, Month(date) + 1, Year(date))
        if Day(date) < 28:
            return MakeDate(Day(date) + 1, Month(date), Year(date))
        return MakeDate(1, Month(date) + 1, Year(date))
    if Month(date) == 12:
        if Day(date) < 31:
            return MakeDate(Day(date) + 1, Month(date), Year(date))
        return MakeDate(1, 1, Year(date) + 1)


def Yesterday(date):
    if Day(date) == 1:
        if Month(date) in [5, 7, 8, 10, 12]:
            return MakeDate(30, Month(date) - 1, Year(date))
        if Month(date) in [2, 4, 6, 9, 11]:
            return MakeDate(31, Month(date) - 1, Year(date))
        if Month(date) == 1:
            return MakeDate(31, 12, Year(date) - 1)
        if Month(date) == 3:
            if IsKabisat(Year(date)):
                return MakeDate(29, 2, Year(date))
            return MakeDate(28, 2, Year(date))
    return MakeDate(Day(date) - 1, Month(date), Year(date))


def NextNDay(date, n):  # rekursiv gk di bolehin kakakny anjfskdjk
    if n == 0:
        return date
    return NextNDay(NextDay(date), n - 1)


def NextNDay(date, N):
    if (
        dpm(Month(date))
        + Day(date)
        - 1
        + (1 if Month(date) > 2 and IsKabisat(Year(date)) else 0)
    ) + N > (366 if IsKabisat(Year(date)) else 365):
        return HrKeDate(
            Year(date) + 1,
            (
                (
                    dpm(Month(date))
                    + Day(date)
                    - 1
                    + (1 if Month(date) > 2 and IsKabisat(Year(date)) else 0)
                )
                + N
                - (366 if IsKabisat(Year(date)) else 365)
            ),
        )
    return HrKeDate(
        Year(date),
        (
            dpm(Month(date))
            + Day(date)
            - 1
            + (1 if Month(date) > 2 and IsKabisat(Year(date)) else 0)
        )
        + N,
    )


def HrKeDate(Thn, TotalHr):
    if TotalHr <= 31:
        return MakeDate(TotalHr, 1, Thn)
    if TotalHr <= (31 + (29 if IsKabisat(Thn) else 28)):
        return MakeDate(TotalHr - 31, 2, Thn)
    if TotalHr <= (62 + (29 if IsKabisat(Thn) else 28)):
        return MakeDate(TotalHr - (31 + (29 if IsKabisat(Thn) else 28)), 3, Thn)
    if TotalHr <= (92 + (29 if IsKabisat(Thn) else 28)):
        return MakeDate(TotalHr - (62 + (29 if IsKabisat(Thn) else 28)), 4, Thn)
    if TotalHr <= (123 + (29 if IsKabisat(Thn) else 28)):
        return MakeDate(TotalHr - (92 + (29 if IsKabisat(Thn) else 28)), 5, Thn)
    if TotalHr <= (153 + (29 if IsKabisat(Thn) else 28)):
        return MakeDate(TotalHr - (123 + (29 if IsKabisat(Thn) else 28)), 6, Thn)
    if TotalHr <= (184 + (29 if IsKabisat(Thn) else 28)):
        return MakeDate(TotalHr - (153 + (29 if IsKabisat(Thn) else 28)), 7, Thn)
    if TotalHr <= (215 + (29 if IsKabisat(Thn) else 28)):
        return MakeDate(TotalHr - (184 + (29 if IsKabisat(Thn) else 28)), 8, Thn)
    if TotalHr <= (245 + (29 if IsKabisat(Thn) else 28)):
        return MakeDate(TotalHr - (215 + (29 if IsKabisat(Thn) else 28)), 9, Thn)
    if TotalHr <= (276 + (29 if IsKabisat(Thn) else 28)):
        return MakeDate(TotalHr - (245 + (29 if IsKabisat(Thn) else 28)), 10, Thn)
    if TotalHr <= (306 + (29 if IsKabisat(Thn) else 28)):
        return MakeDate(TotalHr - (276 + (29 if IsKabisat(Thn) else 28)), 11, Thn)
    if TotalHr <= (337 + (29 if IsKabisat(Thn) else 28)):
        return MakeDate(TotalHr - (306 + (29 if IsKabisat(Thn) else 28)), 12, Thn)


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


def IsKabisat(y: int) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def HariKe1900(d: int, m: int, y: int) -> int:
    return dpm(m) + d - 1 + (1 if m > 2 and IsKabisat(y) else 0)


def IsEqD(D1, D2):
    return Day(D1) == Day(D2) and Month(D1) == Month(D2) and Year(D1) == Year(D2)


def IsBefore(D1, D2):
    return (
        Day(D1) < Day(D2)
        or (Day(D1) == Day(D2) and Month(D1) < Month(D2))
        or (Day(D1) == Day(D2) and Month(D1) == Month(D2) and Year(D1) < Year(D2))
    )


def IsAfter(D1, D2):
    return (
        Day(D1) > Day(D2)
        or (Day(D1) == Day(D2) and Month(D1) > Month(D2))
        or (Day(D1) == Day(D2) and Month(D1) == Month(D2) and Year(D1) > Year(D2))
    )


print(f"NextDay: <28,2,2024> -> {NextDay(MakeDate(28, 2, 2024))}")
print(f"Yesterday: <1,3,2024> ->{Yesterday(MakeDate(1, 3, 2024))}")
print(
    f"IsEqD: <1,1,2024>, <1,1,2024> -> {IsEqD(MakeDate(1, 1, 2024), MakeDate(1, 1, 2024))}"
)
print(
    f"IsBefore: <1,1,2024>, <2,1,2024> -> {IsBefore(MakeDate(1, 1, 2024), MakeDate(2, 1, 2024))}"
)
print(
    f"IsAfter: <1,11,2024>, <2,1,2024> -> {IsAfter(MakeDate(1, 11, 2024), MakeDate(2, 1, 2024))}"
)
print(f"IsKabisat: 2024 -> {IsKabisat(2024)}")
print(f"NextNDay: <1,1,2023>, 100 -> {NextNDay(MakeDate(1, 1, 2023), 100)}")
print(f"NextNDay: <31,12,2023>, 1 -> {NextNDay(MakeDate(31, 12, 2023), 1)}")
print(f"NextNDay: <15,6,2023>, 0 -> {NextNDay(MakeDate(15, 6, 2023), 0)}")
print(f"NextNDay: <10,4,2023>, 5 -> {NextNDay(MakeDate(10, 4, 2023), 5)}")
print(f"NextNDay: <28,2,2024>, 2 -> {NextNDay(MakeDate(28, 2, 2024), 2)}")
print(f"NextNDay: <28,2,2024>, 1 -> {NextNDay(MakeDate(28, 2, 2024), 1)}")
print(f"NextNDay: <31,12,2023>, 365 -> {NextNDay(MakeDate(31, 12, 2023), 365)}")
print(f"NextNDay: <1,1,2024>, 366 -> {NextNDay(MakeDate(1, 1, 2024), 730)}")

"""
3. Tipe bentukan garis (isSejajar, panjang garis)

"""


def Absis(P):
    return P[0]


def Ordinat(P):
    return P[1]


def MakePoint(x, y):
    return [x, y]


def IsOrigin(P):
    return Absis(P) == 0 and Ordinat(P) == 0


def FX2(x):
    return x * x


def Jarak(P1, P2):
    return (FX2(Absis(P1) - Absis(P2)) + FX2(Ordinat(P1) - Ordinat(P2))) * 0.5


def Jarak0(P):
    return (FX2(Absis(P)) + FX2(Ordinat(P))) * 0.5


def Kuadran(P):
    if Absis(P) > 0 and Ordinat(P) > 0:
        return "Kuadran 1"
    if Absis(P) < 0 and Ordinat(P) > 0:
        return "Kuadran 2"
    if Absis(P) < 0 and Ordinat(P) < 0:
        return "Kuadran 3"
    if Absis(P) > 0 and Ordinat(P) < 0:
        return "Kuadran 4"
    return "Gk ad"


def Gradien(P1, P2):
    return (Ordinat(P2) - Ordinat(P1)) / (Absis(P2) - Absis(P1))


def IsSejajar(P1, P2, P3, P4):
    return Gradien(P1, P2) == Gradien(P3, P4)


def PanjangGaris(P1, P2):
    return Jarak(P1, P2)


print(
    f"IsSejajar: <1,3>, <2,3>, <3,3>, <4,3> -> {IsSejajar(MakePoint(1, 3), MakePoint(2, 3), MakePoint(3, 3), MakePoint(4, 3))}"
)
print(f"PanjangGaris: <1,3>, <2,3> -> {PanjangGaris(MakePoint(1, 3), MakePoint(2, 3))}")

"""
4. Tipe bentukan segiempat (isBujurSangkar, isJajargenjang, AreaBujurSangkar)

"""


def IsBujurSangkar(P1, P2, P3, P4):
    return Jarak(P1, P2) * Jarak(P3, P4) == Jarak(P1, P3) * Jarak(P2, P4)


def IsJajargenjang(P1, P2, P3, P4):
    return (
        Gradien(P1, P2) == Gradien(P3, P4)
        and Gradien(P1, P4) == Gradien(P2, P3)
        and Jarak(P1, P2) == Jarak(P3, P4)
        and Jarak(P1, P4) == Jarak(P2, P3)
    )


def AreaBujurSangkar(P1, P2, P3, P4):
    if not IsBujurSangkar(P1, P2, P3, P4):
        return "BUKAN BUJUR SANGKAR"
    return Jarak(P1, P2) * Jarak(P3, P4)


print(
    f"IsBujurSangkar: <1,3>, <2,3>, <1,2>, <2,2> -> {IsBujurSangkar(MakePoint(1, 3), MakePoint(2, 3), MakePoint(1, 2), MakePoint(2, 2))}"
)
print(
    f"IsJajargenjang: <1,1>, <4,1>, <6,4>, <3,4> -> {IsJajargenjang(MakePoint(1, 1), MakePoint(4, 1), MakePoint(6, 4), MakePoint(3, 4))}"
)
print(
    f"AreaBujurSangkar: <1,3>, <2,3>, <1,2>, <2,2> -> {AreaBujurSangkar(MakePoint(1, 3), MakePoint(2, 3), MakePoint(1, 2), MakePoint(2, 2))}"
)

"""
5. Buatlah tipe bentukan yang merepresentasikan data mahasiswa, nilai, dan mata kulah. Gunakan tipe bentukan tersebut untuk menyelesaikan masalah berikut:
   Definisi Tipe Bentukan
   Tipe bentukan MHS1 yang berisi informasi dasar NIM, Nama, dan Tanggal Lahir.
   Tipe bentukan MHS2 yang berisi informasi nilai, yaitu NIM, KodeMatkul, Nilai.
   Tipe bentukan MHS3 yang berisi informasi matkul, yaitu KodeMatkul, NamaMatkul.
   Buat Fungsi Operator :
   Fungsi hitungRangeNilai : fungsi ini menggunakan tipe bentukan MHS2 dan akan menghasilkan range (selisih nilai tertinggi dan terendah) dari nilai mahasiswa tersebut. Fungsi ini harus mengembalikan sebuah nilai tipe bentukan yang memuat:
   KodeMatkul, NilaiTertinggi, NilaiTertinggi, NilaiTerendah, RangeNilai.
"""


def MakeMHS1(NIM, Nama, TanggalLahir):
    return [NIM, Nama, TanggalLahir]


def MakeMHS2(NIM, KodeMatkul, Nilai):
    return [NIM, KodeMatkul, Nilai]


def MHS2Nim(MHS2):
    return MHS2[0]


def MHS2KodeMatkul(MHS2):
    return MHS2[1]


def MHS2Nilai(MHS2):
    return MHS2[2]


def MakeMHS3(KodeMatkul, NamaMatkul):
    return [KodeMatkul, NamaMatkul]


def MakeRangeNilai(KodeMatkul, NilaiTertinggi, NilaiTerendah, RangeNilai):
    return [KodeMatkul, NilaiTertinggi, NilaiTerendah, RangeNilai]


def hitungRangeNilai(MHS2):  # gk boleh rekursiv anjhhjsdhjs
    return RangeNilai(MHS2, MHS2Nilai(MHS2[0]), MHS2Nilai(MHS2[0]), 0)


def RangeNilai(MHS2, MaxSkrg, MinSkrg, i):
    if i == len(MHS2):
        return [MHS2KodeMatkul(MHS2[0]), MaxSkrg, MinSkrg, MaxSkrg - MinSkrg]
    return RangeNilai(
        MHS2, max(MaxSkrg, MHS2Nilai(MHS2[i])), min(MinSkrg, MHS2Nilai(MHS2[i])), i + 1
    )


def hitungRangeNilai(MHS2):
    return MakeRangeNilai(
        MHS2KodeMatkul(MHS2[0]),
        max4(
            MHS2Nilai(MHS2[0]),
            MHS2Nilai(MHS2[1]),
            MHS2Nilai(MHS2[2]),
            MHS2Nilai(MHS2[3]),
        ),
        min4(
            MHS2Nilai(MHS2[0]),
            MHS2Nilai(MHS2[1]),
            MHS2Nilai(MHS2[2]),
            MHS2Nilai(MHS2[3]),
        ),
        max4(
            MHS2Nilai(MHS2[0]),
            MHS2Nilai(MHS2[1]),
            MHS2Nilai(MHS2[2]),
            MHS2Nilai(MHS2[3]),
        )
        - min4(
            MHS2Nilai(MHS2[0]),
            MHS2Nilai(MHS2[1]),
            MHS2Nilai(MHS2[2]),
            MHS2Nilai(MHS2[3]),
        ),
    )


def max2(a: int, b: int) -> int:
    return (a + b + abs(a - b)) // 2


def max4(i: int, j: int, k: int, l: int) -> int:
    return max2(max2(i, j), max2(k, l))


def min2(a: int, b: int) -> int:
    return (a + b - abs(a - b)) // 2


def min4(i: int, j: int, k: int, l: int) -> int:
    return min2(min2(i, j), min2(k, l))


print(
    f"""Range Nilai: {
        hitungRangeNilai(
            [
    MakeMHS2(24060124110142, "69", 100),
    MakeMHS2(24060124110142, "69", 43),
    MakeMHS2(24060124110142, "69", 76),
    MakeMHS2(24060124110142, "69", 69),
            ]
    )}"""
)  # -> Range Nilai: ['69', 100, 43, 57]
