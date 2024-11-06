from typing import List

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


# PRIMITIVE LIKE TYPE
def IsEmpty(L: List) -> bool:
    """IsEmpty(L) benar jika list kosong"""
    return L == [] or L == [[]] or L == ""


def IsOneElmt(L: List) -> bool:
    """IsOneElmt(L) adalah benar jika list L hanya mempunyai satu elemen"""
    if IsEmpty(L):
        return False
    return Tail(L) == [] and Head(L) == []


def Head(L: List) -> List:
    """Head(L): Menghasilkan list tanpa elemen terakhir list L, mungkin kosong"""
    return L[:-1]


def Konso(e: int, L: List) -> List:
    """Konso(e, L) menghasilkan sebuah List dari e dan L dengan e sebagai elemen pertama"""
    return [e] + L


def SumElmt(L: List) -> int:
    """SumElmt(L) menghasilkan jumlahan dari setiap elemen di dalam list L"""
    if IsEmpty(L):
        return 0
    return FirstElmt(L) + SumElmt(Tail(L))


def FirstElmt(L: List) -> int:
    """FirstElmt(L) mengembalikan elemen pertama dari list L"""
    return L[0]


def Tail(L: List) -> List:
    """Tail(L): Menghasilkan list tanpa elemen pertama list L, mungkin kosong"""
    return L[1:]


def NbElmt(L: List) -> int:
    """NbElmt(L) Menghasilkan banyaknya elemen list, nol jika kosong"""
    if IsEmpty(L):
        return 0
    return 1 + NbElmt(Tail(L))


def max2(a: int, b: int) -> int:
    return ((a + b) + abs(a - b)) // 2


def MaxElmt(L: List) -> int:
    if IsOneElmt(L):
        return FirstElmt(L)
    return max2(FirstElmt(L), MaxElmt(Tail(L)))


# TYPE MAHASISWA
def MakeMhs(nim: str, nama: str, kelas: str, nilai: list):
    return [nim, nama, kelas, nilai]


def SelectNimMhs(Mhs):
    return Mhs[0]


def SelectKelasMhs(Mhs):
    return Mhs[2]


def SelectNilaiMhs(Mhs):
    return Mhs[3]


def HitungRataRata(nilai):
    if IsEmpty(nilai):
        return 0
    return SumElmt(nilai) // NbElmt(nilai)


# TYPE SET OF MAHASISWA
def SetMhs(Mhs):
    """{SetMhs(Mhs) mengembalikan setMhs Mhs"""
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
    if HitungRataRata(SelectNilaiMhs(FirstElmt(SetMhs))) >= 70:
        return Konso(FirstElmt(SetMhs), SetMhsLulus(Tail(SetMhs)))
    return SetMhsLulus(Tail(SetMhs))


def BanyakSetMhsLulus(SetMhs):
    """{SetMhsLulus(Mhs) mengembalikan himpunan mahasiswa yang lulus, yaitu yang memiliki nilai rata-rata lebih dari sama dengan 70"""
    if IsEmpty(SetMhs):
        return 0
    if HitungRataRata(SelectNilaiMhs(FirstElmt(SetMhs))) >= 70:
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
        return 0
    if IsOneElmt(SetMhs):
        return MaxElmt(SelectNilaiMhs(FirstElmt(SetMhs)))
    return max2(
        MaxElmt(SelectNilaiMhs(FirstElmt(SetMhs))), NilaiTertinggi(Tail(SetMhs))
    )


def NilaiTertinggiKelas(kelas, SetMhs):
    """{NilaiTertinggiKelas(kelas, Mhs) mengembalikan nilai tertinggi dari SetMhs yang memiliki kelas kelas"""
    if IsEmpty(SelectNilaiMhs(FirstElmt(SetMhs))) or kelas != SelectKelasMhs(
        FirstElmt(SetMhs)
    ):
        return 0
    if IsOneElmt(SetMhs):
        return MaxElmt(SelectNilaiMhs(FirstElmt(SetMhs)))
    return max2(
        MaxElmt(SelectNilaiMhs(FirstElmt(SetMhs))), NilaiTertinggi(Tail(SetMhs))
    )


# APPLIKASI

"""
a. Konstruktor khusus untuk SetMhs dengan syarat saat menambahkan elemen 
mahasiswa baru harus menggunakan nim yang unik (tidak boleh sama dengan nim 
yang sudah ada). 
"""
print("SET MAHASISA :")
print(
    SetMhs(
        [
            MakeMhs("123", "Caca", "C", [90, 80, 100]),
            MakeMhs("234", "Andi", "C", []),
            MakeMhs("345", "Cahya", "C", [90, 80, 100]),
            MakeMhs("345", "Dimas", "C", [90, 80, 100]),
        ]
    )
)

"""
b. Fungsi yang mengembalikan himpunan mahasiswa yang lulus, yaitu yang memiliki nilai 
rata-rata lebih dari sama dengan 70.
"""
print("SET MAHASISWA LULUS :")
print(
    SetMhsLulus(
        SetMhs(
            [
                MakeMhs("123", "Caca", "C", [90, 69, 100]),
                MakeMhs("234", "Andi", "C", []),
                MakeMhs("345", "Cahya", "C", [90, 22, 100]),
                MakeMhs("345", "anton", "C", [90, 80, 100]),
                MakeMhs("69", "Aku", "C", [90, 80, 100]),
                MakeMhs("345", "Cahya", "C", [90, 10, 100]),
            ]
        )
    )
)

"""
c. Fungsi yang mengembalikan himpunan mahasiswa yang tidak mengerjakan kuis sama 
sekali di suatu kelas tertentu sesuai dengan nama kelas di-input-kan sebagai parameter.
"""
print("SET MAHASISWA TIDAK MENGERJAKAN KUIS :")
print(
    SetMhsTidakMengerjakanKuisKelas(
        "C",
        SetMhs(
            [
                MakeMhs("123", "Caca", "C", [90, 69, 100]),
                MakeMhs("234", "Andi", "C", []),
                MakeMhs("345", "Cahya", "C", [90, 22, 100]),
                MakeMhs("345", "anton", "C", [90, 80, 100]),
                MakeMhs("69", "Aku", "C", [90, 80, 100]),
                MakeMhs("345", "Cahya", "C", [90, 10, 100]),
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
                MakeMhs("123", "Caca", "C", [90, 69, 100]),
                MakeMhs("234", "Andi", "C", []),
                MakeMhs("345", "Cahya", "C", [90, 22, 100]),
                MakeMhs("345", "anton", "C", [90, 80, 100]),
                MakeMhs("69", "Aku", "C", [90, 80, 100]),
                MakeMhs("345", "Cahya", "C", [90, 10, 100]),
            ]
        )
    )
)

"""
e. Fungsi yang mengembalikan mahasiswa yang mendapatkan nilai tertinggi dari suatu 
kelas tertentu sesuai dengan nama kelas di-input-kan sebagai parameter. 
"""

print("NILAI TERTINGGI DARI SEMUA KELAS :")
print(
    NilaiTertinggiKelas(
        "C",
        SetMhs(
            [
                MakeMhs("123", "Caca", "C", [90, 69, 90]),
                MakeMhs("234", "Andi", "C", []),
                MakeMhs("345", "Cahya", "C", [90, 22, 90]),
                MakeMhs("345", "anton", "C", [90, 80, 90]),
                MakeMhs("69", "Aku", "C", [90, 80, 90]),
                MakeMhs("345", "TOL", "D", [90, 10, 100]),
            ]
        ),
    )
)

"""
f. Fungsi yang mengembalikan banyaknya mahasiswa yang tidak mengerjakan kuis dari 
semua kelas. 
"""

print("BANYAK MAHASISWA YANG TIDAK MENGERJAKAN KUIS DARI SEMUA KELAS")
print(
    BanyakSetMhsTidakMengerjakanKuis(
        SetMhs(
            [
                MakeMhs("123", "Caca", "C", [90, 69, 90]),
                MakeMhs("234", "Andi", "E", []),
                MakeMhs("89", "Kemal", "L", []),
                MakeMhs("345", "Cahya", "C", [90, 22, 90]),
                MakeMhs("345", "anton", "C", [90, 80, 90]),
                MakeMhs("69", "Aku", "C", [90, 80, 90]),
                MakeMhs("345", "TOL", "D", [90, 10, 100]),
            ]
        )
    )
)

"""
g. Fungsi yang mengembalikan banyaknya mahasiswa yang lulus dari semua kelas. 
"""

print("BANYAK MAHASISWA YANG LULUS DARI SEMUA KELAS")
print(
    BanyakSetMhsLulus(
        SetMhs(
            [
                MakeMhs("123", "Caca", "C", [90, 69, 90]),
                MakeMhs("234", "Andi", "E", []),
                MakeMhs("89", "Kemal", "L", []),
                MakeMhs("345", "Cahya", "C", [90, 22, 90]),
                MakeMhs("345", "anton", "C", [90, 80, 90]),
                MakeMhs("69", "Aku", "C", [90, 80, 90]),
                MakeMhs("345", "TOL", "D", [90, 10, 100]),
            ]
        )
    )
)
