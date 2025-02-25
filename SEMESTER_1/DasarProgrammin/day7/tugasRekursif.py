"""
Deskripsi : TUGAS LIST
Pembuat   : Muchammad Yuda Tri Ananda
NIM       : 24060124110142
Tanggal   : 29 Oktober 2024 
"""

"""
DEFINISI DAN SPESIFIKASI TYPE
Konstruktor menambahkan elemen di awal, notasi prefix
type List: [] atau  [e o List]
Konstruktor menambahkan elemen di akhir, notasi postfix
type List: [] atau [List o e]
"""

from typing import List

"""
DEFINISI DAN SPESIFIKASI KONSTRUKTOR
Konso: elemen, List → List
  {Konso(e,L) menghasilkan sebuah List dari e dan L dengan e sebagai elemen pertama}
REALISASI
"""


def Konso(e: int, L: List) -> List:
    return [e] + L


"""
Konsi: List, elemen → List
  {Konsi(L,e) menghasilkan sebuah List dari L dan e dengan e sebagai elemen terakhir}
Realisasi
"""


def Konsi(L: List, e: int) -> List:
    return L + [e]


"""
DEFINISI DAN SPESIFIKASI SELEKTOR
FirstElmt: List tidak kosong → elemen
  {FirstElmt(L) mengembalikan elemen pertama dari list L}
Realisasi
"""


def FirstElmt(L: List) -> int:
    return L[0]


"""
LastElmt: List tidak kosong → elemen
  {LastElmt(L): mengembalikan elemen terakhir terakhir list L}
Realisasi
"""


def LastElmt(L: List) -> int:
    return L[-1]


"""
Head: List tidak kosong → List
  {Head(L): Menghasilkan list tanpa elemen terakhir list L, mungkin kosong}
Realisasi
"""


def Head(L: List) -> List:
    return L[:-1]


"""
Tail: List tidak kosong → List
  {Tail(L): Menghasilkan list tanpa elemen pertama list L, mungkin kosong}
Realisasi
"""


def Tail(L: List) -> List:
    return L[1:]


"""
DEFINISI DAN SPESIFIKASI PREDIKAT
IsEmpty: List → boolean
  {IsEmpty(L) benar jika list kosong}
Realisasi
"""


def IsEmpty(L: List) -> bool:
    return L == [] or L == ""


"""
IsOneElmt: List → boolean
  {IsOneElmt(L) adalah benar jika list L hanya mempunyai satu elemen}
Realisasi
"""


def IsOneElmt(L: List) -> bool:
    if IsEmpty(L):
        return False
    return Tail(L) == [] and Head(L) == []


"""
DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
NbElmt: List → integer
  {NbElmt(L) Menghasilkan banyaknya elemen list, nol jika kosong}
Realisasi
"""


def NbElmt(L: List) -> int:
    if IsEmpty(L):
        return 0
    return 1 + NbElmt(Tail(L))


print(f"NbElmt([1,2,3,4]) = {NbElmt([1, 2, 3, 4])}")


"""
ElmtKeN: integer >= 0, List → elemen
  {ElmtKeN(N,L) mengembalikan elemen ke N dari list L, N <= NbElmt(L) dan N>=0}
Realisasi
"""


def ElmtKeN(N: int, L: List) -> int:
    if N == 1:
        return FirstElmt(L)
    return ElmtKeN(N - 1, Tail(L))


print(f"ElmtKeN(2,[1,2,3,4]) = {ElmtKeN(2, [1, 2, 3, 4])}")


"""
IsMember: elemen, List → boolean
  {IsMember(X,L) adalah benar jika X adalah anggota elemen List L}
Realisasi
"""


def IsMember(X: int, L: List) -> bool:
    if IsEmpty(L):
        return False
    if X == FirstElmt(L):
        return True
    return IsMember(X, Tail(L))


print(f"IsMember(2,[1,2,3,4]) = {IsMember(2, [1, 2, 3, 4])}")
print(f"IsMember(5,[1,2,3,4]) = {IsMember(5, [1, 2, 3, 4])}")

"""
Copy: List → List
  {Copy(L) menghasilkan list yang identik dengan list L}
Realisasi
"""


def Copy(L: List) -> List:
    if IsEmpty(L):
        return []
    return Konso(FirstElmt(L), Copy(Tail(L)))


print(f"Copy([1,2,3,4]) = {Copy([1, 2, 3, 4])}")

"""
Invers: List → List
  {Invers(L) menghasilkan List L yang dibalik}
"""


def Invers(L: List) -> List:
    if IsEmpty(L):
        return []
    return Konso(LastElmt(L), Head(L))


print(f"Invers([1,2,3]) = {Invers([1, 2, 3])}")

"""
Konkat : 2 List → List
  {Konkat(L1,L2) menghasilkan konketasi 2 buah list, dengan list L2 "sesudah" list L1}
Realisasi
"""


def Konkat(L1: List, L2: List) -> List:
    return Copy(L1) + Copy(L2)


print(f"Konkat([1,2,3],[4,5,6]) = {Konkat([1, 2, 3], [4, 5, 6])}")

"""
SumElmt: List of integer → integer
  {SumElmt(L) menghasilkan jumlahan dari setiap elemen di dalam list L}
Realisasi
"""


def SumElmt(L: List) -> int:
    if IsEmpty(L):
        return 0
    return FirstElmt(L) + SumElmt(Tail(L))


print(f"SumElmt([1,2,3]) = {SumElmt([1, 2, 3])}")

"""
AvgElmt: List of integer → integer
  {AvgElmt(L) menghasilkan nilai rata-rata}
Realisasi
"""


def AvgElmt(L: List) -> int:
    return SumElmt(L) // NbElmt(L)


print(f"AvgElmt([1,2,3]) = {AvgElmt([1, 2, 3])}")


"""
MaxElmt: List of integer → integer
  {MaxElmt(L) mengembalikan elemen maksimum dari list L}
"""


def max2(a: int, b: int) -> int:
    return ((a + b) + abs(a - b)) // 2


# Realisasi
def MaxElmt(L: List) -> int:
    if IsOneElmt(L):
        return FirstElmt(L)
    return max2(FirstElmt(L), MaxElmt(Tail(L)))


print(f"MaxElmt([1,2,3,4,5,6,7,8,9,10]) = {MaxElmt([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")

"""
MaxNB: List of integer → <integer, integer>
  {MaxNB(L) menghasilkan <max,countMax}
      dengan max adalah elemen maksimum list L
      dan countMax adalah banyaknya kemunculan max di list L
Realisasi
"""


def countNList(L: List, n: int) -> int:
    if IsEmpty(L):
        return 0
    if n == FirstElmt(L):
        return 1 + countNList(Tail(L), n)
    return countNList(Tail(L), n)


def MaxNB(L: List) -> tuple:
    return MaxElmt(L), countNList(L, MaxElmt(L))


print(f"MaxNB([1,2,3,4,5,6,7,8,9,10,10]) = {MaxNB([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,10])}")

"""
AddList: 2 List of integer → List of integer
  {AddList(L1,L2) menghaislkan list baru yang setiap elemennya adalah hasil
   penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama}
Realisasi
"""


def AddList(L1: List, L2: List) -> List:
    if IsEmpty(L1):
        return L2
    if IsEmpty(L2):
        return L1
    return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))


print(
    f"""AddList([1,2,3,4,5,6,7,8,9,10,10],[1,2,3,4,5,6,7,8,9,10,10]) = {
        AddList(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
            ),
        }"""
)

"""
IsPalindrom(L): List of character → boolean
    IsPalindrom(L) benar jika L merupakan kata palindrom
    yaitu kata yang sama jika dibaca dari kiri atau kanan
contoh: KASUR RUSAK, NABABAN
"""


def IsPalindrom(L: str) -> bool:
    if IsEmpty(L):
        return True
    if FirstElmt(L) != LastElmt(L):
        return False
    return IsPalindrom(Tail(Head(L)))


print(f"""IsPalindrom("KASUR RUSAK") = {IsPalindrom("KASUR RUSAK")}""")
print(f"""IsPalindrom("NABANAN") = {IsPalindrom("NABANAN")}""")
print(f"""IsPalindrom("TENET") = {IsPalindrom("TENET")}""")
