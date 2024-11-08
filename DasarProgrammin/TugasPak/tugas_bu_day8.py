from pprint import pprint

"""
Deskripsi : TUGAS DASAR PEMROGRAMAN KOLEKSI OBJEK
Pembuat   : Muchammad Yuda Tri Ananda
NIM       : 24060124110142
Tanggal   : 5 November 2024 
"""

"""
TUGAS DASAR PEMROGRAMAN  KOLEKSI OBJEK 
BAGIAN 1 
Dalam suatu kelas pemrograman terdapat kumpulan mahasiswa. Di dalam kelas tersebut  mahasiswa diminta untuk mengerjakan kuis dengan jumlah kesempatan submit maksimal 10 kali.  Nilai yang diambil adalah nilai rata-rata dari semua submission yang pernah dilakukan. Untuk mewakili mahasiswa dibuatlah tipe bentukan mahasiswa yang memiliki komponen berupa nama, nim, kelas, dan nilai (berbentuk list), seperti berikut:
"""

"""
BAGIAN 2 
Buatlah type kolektif berupa Set of Mhs yang merupakan himpunan mahasiswa yang ada di dalam suatu program studi di suatu universitas, seperti berikut: 
1. Buatlah definisi dan spesifikasi untuk Set of Mhs. Konstruktor dan selektor yang ada pada list 
dapat langsung digunakan, tidak perlu dituliskan lagi. 
2. Buatlah definsi, spesifikasi, realisasi, dan aplikasi fungsi atau operasi yang menggunakan Set of 
Mhs seperti berikut: 
a. Konstruktor khusus untuk SetMhs dengan syarat saat menambahkan elemen 
mahasiswa baru harus menggunakan nim yang unik (tidak boleh sama dengan nim 
yang sudah ada). 
b. Fungsi yang mengembalikan himpunan mahasiswa yang lulus, yaitu yang memiliki nilai 
rata-rata lebih dari sama dengan 70. 
c. Fungsi yang mengembalikan himpunan mahasiswa yang tidak mengerjakan kuis sama 
sekali di suatu kelas tertentu sesuai dengan nama kelas di-input-kan sebagai parameter. 
d. Fungsi yang mengembalikan nilai tertinggi dari semua kelas. 
e. Fungsi yang mengembalikan mahasiswa yang mendapatkan nilai tertinggi dari suatu 
kelas tertentu sesuai dengan nama kelas di-input-kan sebagai parameter. 
f. 
Fungsi yang mengembalikan banyaknya mahasiswa yang tidak mengerjakan kuis dari 
semua kelas. 
g. Fungsi yang mengembalikan banyaknya mahasiswa yang lulus dari semua kelas.
"""

"""
TYPE MAHASISWA (MHS) 
DEFINISI DAN SPESIFIKASI TYPE 
    type Mhs: <nim: string, nama: string, kelas: character, nilai: list of integer> 
    {type Mhs terdiri atas nim, nama, dan kelas mahasiswa, serta kumpulan nilai kuis yang pernah dikerjakan, dengan maksimal jumlah mengerjakan adalah 10 kali. Nilai mahasiswa memiliki rentang antara 0-100} 

DEFINISI DAN SPESIFIKASI KONSTRUKTOR 
    MakeMhs: <string, string, character, list of integer>  → Mhs 
    {MakeMhs(nim, nama, kelas, nilai) membentuk sebuah mahasiswa dengan dengan nim, nama, kelas dan nilai berbentuk list of integer. 
    Contoh:  
    MakeMhs('234', 'Andi', 'C', []) membentuk mahasiswa dengan nim '234', nama 'Andi' dari kelas C, dan belum pernah mengerjakan kuis (nilainya berupa list kosong). MakeMhs('123', 'Caca', 'C', [90,80,100]) membentuk mahasiswa dengan nim '123', nama 'CC' dari kelas C, dan telah mengerjakan kuis sebanyak tiga kali dengan nilai masing-masing adalah 90, 80, dan 100. } 
"""


# PRIMITIVE LIKE FUNCTIONs
def IsEmpty(L):
    """IsEmpty(L) benar jika list kosong"""
    return L == [] or L == [[]] or L == ""


def IsOneElmt(L):
    """IsOneElmt(L) adalah benar jika list L hanya mempunyai satu elemen"""
    if IsEmpty(L):
        return False
    return Tail(L) == [] and Head(L) == []


def Head(L):
    """Head(L): Menghasilkan list tanpa elemen terakhir list L, mungkin kosong"""
    return L[:-1]


def Konso(e, L):
    """Konso(e, L) menghasilkan sebuah List dari e dan L dengan e sebagai elemen pertama"""
    return [e] + L


def SumElmt(L):
    """SumElmt(L) menghasilkan jumlahan dari setiap elemen di dalam list L"""
    if IsEmpty(L):
        return 0
    return FirstElmt(L) + SumElmt(Tail(L))


def FirstElmt(L):
    """FirstElmt(L) mengembalikan elemen pertama dari list L"""
    return L[0]


def Tail(L):
    """Tail(L): Menghasilkan list tanpa elemen pertama list L, mungkin kosong"""
    return L[1:]


def NbElmt(L):
    """NbElmt(L) Menghasilkan banyaknya elemen list, nol jika kosong"""
    if IsEmpty(L):
        return 0
    return 1 + NbElmt(Tail(L))


def max2(a, b):
    return ((a + b) + abs(a - b)) // 2


def MaxElmt(L):
    """MaxElmt(L) mengembalikan elemen maksimum dari list L"""
    if IsOneElmt(L):
        return FirstElmt(L)
    return max2(FirstElmt(L), MaxElmt(Tail(L)))


# TYPE MAHASISWA
def MakeMhs(nim, nama, kelas, nilai):
    return [nim, nama, kelas, nilai]


def SelectNimMhs(Mhs):
    return Mhs[0]


def SelectKelasMhs(Mhs):
    return Mhs[2]


def SelectNilaiMhs(Mhs):
    return Mhs[3]


def HitungRataRataNilaiMhs(nilaiMhs):
    if IsEmpty(nilaiMhs):
        return 0
    return SumElmt(nilaiMhs) // NbElmt(nilaiMhs)


# TYPE SET OF MAHASISWA
def SetMhs(Mhs):
    """{SetMhs(Mhs) mengembalikan setMhs NIM harus unik"""
    if IsEmpty(Mhs):
        return []
    if IsNimMemberSetMhs(SelectNimMhs(FirstElmt(Mhs)), Tail(Mhs)):
        return SetMhs(Tail(Mhs))
    return Konso(FirstElmt(Mhs), SetMhs(Tail(Mhs)))


def IsNimMemberSetMhs(nim, SetMhs):
    """{IsNimMemberSetMhs(nim, Mhs) mengembalikan True jika nim adalah anggota Mhs"""
    if IsEmpty(SetMhs):
        return False
    if nim == SelectNimMhs(FirstElmt(SetMhs)):
        return True
    return IsNimMemberSetMhs(nim, Tail(SetMhs))


def SetMhsLulus(SetMhs):
    """{SetMhsLulus(Mhs) mengembalikan himpunan mahasiswa yang lulus, yaitu yang memiliki nilai rata-rata lebih dari sama dengan 70"""
    if IsEmpty(SetMhs):
        return []
    if HitungRataRataNilaiMhs(SelectNilaiMhs(FirstElmt(SetMhs))) >= 70:
        return Konso(FirstElmt(SetMhs), SetMhsLulus(Tail(SetMhs)))
    return SetMhsLulus(Tail(SetMhs))


def BanyakSetMhsLulus(SetMhs):
    """{SetMhsLulus(Mhs) mengembalikan himpunan mahasiswa yang lulus, yaitu yang memiliki nilai rata-rata lebih dari sama dengan 70"""
    if IsEmpty(SetMhs):
        return 0
    if HitungRataRataNilaiMhs(SelectNilaiMhs(FirstElmt(SetMhs))) >= 70:
        return 1 + BanyakSetMhsLulus(Tail(SetMhs))
    return BanyakSetMhsLulus(Tail(SetMhs))


def SetMhsTidakMengerjakanKuisKelas(kelas, SetMhs):
    """{SetMhsTidakMengerjakanKuis(kelas, Mhs) mengembalikan himpunan mahasiswa yang tidak mengerjakan kuis sama sekali di suatu kelas tertentu sesuai dengan nama kelas di-input-kan sebagai parameter"""
    if IsEmpty(SetMhs):
        return []
    if kelas == SelectKelasMhs(FirstElmt(SetMhs)) and IsEmpty(
        SelectNilaiMhs(FirstElmt(SetMhs))
    ):
        return Konso(
            FirstElmt(SetMhs), SetMhsTidakMengerjakanKuisKelas(kelas, Tail(SetMhs))
        )
    return SetMhsTidakMengerjakanKuisKelas(kelas, Tail(SetMhs))


def BanyakSetMhsTidakMengerjakanKuis(SetMhs):
    """{SetMhsTidakMengerjakanKuis(kelas, Mhs) mengembalikan himpunan mahasiswa yang tidak mengerjakan kuis sama sekali di suatu kelas tertentu sesuai dengan nama kelas di-input-kan sebagai parameter"""
    if IsEmpty(SetMhs):
        return 0
    if IsEmpty(SelectNilaiMhs(FirstElmt(SetMhs))):
        return 1 + BanyakSetMhsTidakMengerjakanKuis(Tail(SetMhs))
    return BanyakSetMhsTidakMengerjakanKuis(Tail(SetMhs))


def NilaiTertinggi(SetMhs):
    """{NilaiTertinggi(Mhs) mengembalikan nilai tertinggi dari SetMhs"""
    if IsEmpty(SelectNilaiMhs(FirstElmt(SetMhs))):
        return NilaiTertinggi(Tail(SetMhs))
    if IsOneElmt(SetMhs):
        return HitungRataRataNilaiMhs(SelectNilaiMhs(FirstElmt(SetMhs)))
    return max2(
        HitungRataRataNilaiMhs(SelectNilaiMhs(FirstElmt(SetMhs))),
        NilaiTertinggi(Tail(SetMhs)),
    )


def NilaiTertinggiKelas(kelas, SetMhs):
    """{NilaiTertinggiKelas(kelas, Mhs) mengembalikan nilai tertinggi dari SetMhs yang memiliki kelas kelas"""
    if IsEmpty(SetMhs):
        return 0
    if IsEmpty(SelectNilaiMhs(FirstElmt(SetMhs))) or not kelas == SelectKelasMhs(
        FirstElmt(SetMhs)
    ):
        return NilaiTertinggiKelas(kelas, Tail(SetMhs))
    return max2(
        HitungRataRataNilaiMhs(SelectNilaiMhs(FirstElmt(SetMhs))),
        NilaiTertinggiKelas(kelas, Tail(SetMhs)),
    )


def MhsNilaiTertinggiKelas(kelas, SetMhs, MaxNilai):
    if IsEmpty(SetMhs):
        return []
    if IsEmpty(SelectNilaiMhs(FirstElmt(SetMhs))):
        return MhsNilaiTertinggiKelas(kelas, Tail(SetMhs), MaxNilai)
    if kelas == SelectKelasMhs(
        FirstElmt(SetMhs)
    ) and MaxNilai == HitungRataRataNilaiMhs(SelectNilaiMhs(FirstElmt(SetMhs))):
        return Konso(
            FirstElmt(SetMhs), MhsNilaiTertinggiKelas(kelas, Tail(SetMhs), MaxNilai)
        )
    return MhsNilaiTertinggiKelas(kelas, Tail(SetMhs), MaxNilai)


def NilaiMahasiswaTertinggiKelas(Kelas, SetMhs):
    return MhsNilaiTertinggiKelas(Kelas, SetMhs, NilaiTertinggiKelas(Kelas, SetMhs))


# APPLIKASI

"""
a. Konstruktor khusus untuk SetMhs dengan syarat saat menambahkan elemen 
mahasiswa baru harus menggunakan nim yang unik (tidak boleh sama dengan nim 
yang sudah ada). 
"""
print("SET MAHASISWA :")
pprint(
    SetMhs(
        [
            MakeMhs("001", "Budi", "A", [88, 75, 92]),
            MakeMhs("002", "Siti", "B", [60, 58]),
            MakeMhs("003", "Agus", "A", []),
            MakeMhs("004", "Rina", "C", [85, 90, 78]),
            MakeMhs("005", "Dewi", "B", [72, 65, 80]),
            MakeMhs("006", "Toni", "A", [50, 60, 40]),
            MakeMhs("007", "Mira", "D", []),
            MakeMhs("008", "Rudi", "C", [100, 95, 90]),
            MakeMhs("009", "Linda", "D", [55, 65]),
            MakeMhs("010", "Rahmat", "A", [95, 98, 99]),
            MakeMhs("011", "Fahmi", "B", []),
            MakeMhs("123", "Kemal", "A", [90, 69, 90]),
            MakeMhs("2001", "Zaki", "E", [85, 80, 92]),
            MakeMhs("3001", "Faris", "F", [45, 55, 60]),
            MakeMhs("5001", "Alvin", "G", [92, 94, 96]),
            MakeMhs("9999", "Nina", "H", [72, 80, 88]),
            MakeMhs("69", "Ambasing", "C", [69, 42, 100]),
        ]
    )
)

"""
b. Fungsi yang mengembalikan himpunan mahasiswa yang lulus, yaitu yang memiliki nilai 
rata-rata lebih dari sama dengan 70.
"""
print("SET MAHASISWA LULUS :")
pprint(
    SetMhsLulus(
        SetMhs(
            [
                MakeMhs("001", "Budi", "A", [88, 75, 92]),
                MakeMhs("002", "Siti", "B", [60, 58]),
                MakeMhs("003", "Agus", "A", []),
                MakeMhs("004", "Rina", "C", [85, 90, 78]),
                MakeMhs("005", "Dewi", "B", [72, 65, 80]),
                MakeMhs("006", "Toni", "A", [50, 60, 40]),
                MakeMhs("007", "Mira", "D", []),
                MakeMhs("008", "Rudi", "C", [100, 95, 90]),
                MakeMhs("009", "Linda", "D", [55, 65]),
                MakeMhs("010", "Rahmat", "A", [95, 98, 99]),
                MakeMhs("011", "Fahmi", "B", []),
                MakeMhs("123", "Kemal", "A", [90, 69, 90]),
                MakeMhs("2001", "Zaki", "E", [85, 80, 92]),
                MakeMhs("3001", "Faris", "F", [45, 55, 60]),
                MakeMhs("5001", "Alvin", "G", [92, 94, 96]),
                MakeMhs("9999", "Nina", "H", [72, 80, 88]),
                MakeMhs("69", "Ambasing", "C", [69, 42, 100]),
            ]
        )
    )
)

"""
c. Fungsi yang mengembalikan himpunan mahasiswa yang tidak mengerjakan kuis sama 
sekali di suatu kelas tertentu sesuai dengan nama kelas di-input-kan sebagai parameter.
"""
print("SET MAHASISWA TIDAK MENGERJAKAN KUIS DI KELAS A :")
print(
    SetMhsTidakMengerjakanKuisKelas(
        "A",
        SetMhs(
            [
                MakeMhs("001", "Budi", "A", [88, 75, 92]),
                MakeMhs("002", "Siti", "B", [60, 58]),
                MakeMhs("003", "Agus", "A", []),
                MakeMhs("004", "Rina", "C", [85, 90, 78]),
                MakeMhs("005", "Dewi", "B", [72, 65, 80]),
                MakeMhs("006", "Toni", "A", [50, 60, 40]),
                MakeMhs("007", "Mira", "D", []),
                MakeMhs("008", "Rudi", "C", [100, 95, 90]),
                MakeMhs("009", "Linda", "D", [55, 65]),
                MakeMhs("010", "Rahmat", "A", [95, 98, 99]),
                MakeMhs("011", "Fahmi", "B", []),
                MakeMhs("123", "Kemal", "A", [90, 69, 90]),
                MakeMhs("2001", "Zaki", "E", [85, 80, 92]),
                MakeMhs("3001", "Faris", "F", [45, 55, 60]),
                MakeMhs("5001", "Alvin", "G", [92, 94, 96]),
                MakeMhs("9999", "Nina", "H", [72, 80, 88]),
            ]
        ),
    )
)

"""
d. Fungsi yang mengembalikan nilai tertinggi dari semua kelas. 
"""

print("NILAI TERTINGGI DARI SEMUA KELAS :")
print(
    NilaiTertinggi(
        SetMhs(
            [
                MakeMhs("001", "Budi", "A", [88, 75, 92]),
                MakeMhs("002", "Siti", "B", [60, 58]),
                MakeMhs("003", "Agus", "A", []),
                MakeMhs("004", "Rina", "C", [85, 90, 78]),
                MakeMhs("005", "Dewi", "B", [72, 65, 80]),
                MakeMhs("006", "Toni", "A", [50, 60, 40]),
                MakeMhs("007", "Mira", "D", []),
                MakeMhs("008", "Rudi", "C", [100, 95, 90]),
                MakeMhs("009", "Linda", "D", [55, 65]),
                MakeMhs("010", "Rahmat", "A", [95, 98, 99]),
                MakeMhs("011", "Fahmi", "B", []),
                MakeMhs("123", "Kemal", "A", [90, 69, 90]),
                MakeMhs("2001", "Zaki", "E", [85, 80, 92]),
                MakeMhs("3001", "Faris", "F", [45, 55, 60]),
                MakeMhs("5001", "Alvin", "G", [92, 94, 96]),
                MakeMhs("9999", "Nina", "H", [72, 80, 88]),
            ]
        )
    )
)

"""
e. Fungsi yang mengembalikan mahasiswa yang mendapatkan nilai tertinggi dari suatu 
kelas tertentu sesuai dengan nama kelas di-input-kan sebagai parameter. 
"""

print("MAHASISWA NILAI TERTINGGI DARI KELAS C :")
print(
    NilaiMahasiswaTertinggiKelas(
        "C",
        SetMhs(
            [
                MakeMhs("001", "Budi", "A", [88, 75, 92]),
                MakeMhs("002", "Siti", "B", [60, 58]),
                MakeMhs("003", "Agus", "A", []),
                MakeMhs("004", "Rina", "C", [85, 90, 78]),
                MakeMhs("005", "Dewi", "B", [72, 65, 80]),
                MakeMhs("006", "Toni", "A", [50, 60, 40]),
                MakeMhs("007", "Mira", "D", []),
                MakeMhs("008", "Rudi", "C", [100, 95, 90]),
                MakeMhs("009", "Linda", "D", [55, 65]),
                MakeMhs("010", "Rahmat", "A", [95, 98, 99]),
                MakeMhs("011", "Fahmi", "B", []),
                MakeMhs("123", "Kemal", "A", [90, 69, 90]),
                MakeMhs("2001", "Zaki", "E", [85, 80, 92]),
                MakeMhs("3001", "Faris", "F", [45, 55, 60]),
                MakeMhs("5001", "Alvin", "G", [92, 94, 96]),
                MakeMhs("9999", "Nina", "H", [72, 80, 88]),
                MakeMhs("69", "Ambasing", "C", [90, 100, 95]),
            ]
        ),
    )
)

"""
f. Fungsi yang mengembalikan banyaknya mahasiswa yang tidak mengerjakan kuis dari 
semua kelas. 
"""

print("BANYAK MAHASISWA YANG TIDAK MENGERJAKAN KUIS DARI SEMUA KELAS :")
pprint(
    BanyakSetMhsTidakMengerjakanKuis(
        SetMhs(
            [
                MakeMhs("001", "Budi", "A", [88, 75, 92]),
                MakeMhs("002", "Siti", "B", [60, 58]),
                MakeMhs("003", "Agus", "A", []),
                MakeMhs("004", "Rina", "C", [85, 90, 78]),
                MakeMhs("005", "Dewi", "B", [72, 65, 80]),
                MakeMhs("006", "Toni", "A", [50, 60, 40]),
                MakeMhs("007", "Mira", "D", []),
                MakeMhs("008", "Rudi", "C", [100, 95, 90]),
                MakeMhs("009", "Linda", "D", [55, 65]),
                MakeMhs("010", "Rahmat", "A", [95, 98, 99]),
                MakeMhs("011", "Fahmi", "B", []),
                MakeMhs("123", "Kemal", "A", [90, 69, 90]),
                MakeMhs("2001", "Zaki", "E", [85, 80, 92]),
                MakeMhs("3001", "Faris", "F", [45, 55, 60]),
                MakeMhs("5001", "Alvin", "G", [92, 94, 96]),
                MakeMhs("9999", "Nina", "H", [72, 80, 88]),
                MakeMhs("69", "Ambasing", "C", [69, 42, 100]),
            ]
        ),
    )
)

"""
g. Fungsi yang mengembalikan banyaknya mahasiswa yang lulus dari semua kelas. 
"""

print("BANYAK MAHASISWA YANG LULUS DARI SEMUA KELAS :")
print(
    BanyakSetMhsLulus(
        SetMhs(
            [
                MakeMhs("001", "Budi", "A", [88, 75, 92]),
                MakeMhs("002", "Siti", "B", [60, 58]),
                MakeMhs("003", "Agus", "A", []),
                MakeMhs("004", "Rina", "C", [85, 90, 78]),
                MakeMhs("005", "Dewi", "B", [72, 65, 80]),
                MakeMhs("006", "Toni", "A", [50, 60, 40]),
                MakeMhs("007", "Mira", "D", []),
                MakeMhs("008", "Rudi", "C", [100, 95, 90]),
                MakeMhs("009", "Linda", "D", [55, 65]),
                MakeMhs("010", "Rahmat", "A", [95, 98, 99]),
                MakeMhs("011", "Fahmi", "B", []),
                MakeMhs("123", "Kemal", "A", [90, 69, 90]),
                MakeMhs("2001", "Zaki", "E", [85, 80, 92]),
                MakeMhs("3001", "Faris", "F", [45, 55, 60]),
                MakeMhs("5001", "Alvin", "G", [92, 94, 96]),
                MakeMhs("9999", "Nina", "H", [72, 80, 88]),
                MakeMhs("69", "Ambasing", "C", [69, 42, 100]),
            ]
        ),
    )
)
