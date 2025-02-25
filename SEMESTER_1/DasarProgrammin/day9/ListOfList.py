"""
Deskripsi : TUGAS LIST OF LIST
Pembuat   : Muchammad Yuda Tri Ananda
NIM       : 24060124110142
Tanggal   : 19 November 2024 
"""

from tugasRekursif import IsEqual, max2, IsOneElmt, NbElmt

# KONSTRUKTOR

"""
DEFINISI DAN SPESIFIKASI
    KonsLo(e, L): elemen, List of List --> List of List
    KonsLo(e, L) Menambahkan elemen di baris awal List of List
"""


def KonsLo(e, L):
    return [e] + L


"""
DEFINISI DAN SPESIFIKASI
    KonsLi(L, e): List of List, elemen --> List of List
    KonsLi(L, e) Menambahkan elemen di baris akhir List of List
"""


def KonsLi(L, e):
    return L + [e]


# SELEKTOR

"""
DEFINISI DAN SPESIFIKASI
    FirstList(L): List of List --> elemen
    FirstList(L) Menampilkan elemen pertama dari List of List
"""


def FirstList(L):
    return L[0]


"""
DEFINISI DAN SPESIFIKASI
    LastList(L): List of List --> elemen
    LastList(L) Menampilkan elemen terakhir dari List of List
"""


def LastList(L):
    return L[-1]


"""
DEFINISI DAN SPESIFIKASI
    HeadList(L): List of List --> List of List
    HeadList(L) List of List dengan menghilangkan elemen terakhirnya
"""


def HeadList(L):
    return L[:-1]


"""
DEFINISI DAN SPESIFIKASI
    TailList(L): List of List --> List of List
    TailList(L) List of List dengan menghilangkan elemen pertamanya
"""


def TailList(L):
    return L[1:]


# PREDIKAT KHUSUS PADA LIST OF LIST

"""
DEFINISI DAN SPESIFIKASI
    isEmpty(L): List of List --> boolean
    isEmpty(L) mengecek apakah List of List kosong
"""


def IsEmpty(L):
    return L == []


"""
DEFINISI DAN SPESIFIKASI
    IsAtom: List of List --> boolean
    IsAtom Cek apakah S adalah atom atau bukan sebuah list
"""


def IsAtom(S):
    return type(S) is not list


"""
DEFINISI DAN SPESIFIKASI
    IsList: List of List --> boolean
    IsList Cek apakah S adalah List
"""


def IsList(S):
    return type(S) is list


# PREDIKAT LOL

"""
DEFINISI DAN SPESIFIKASI
    IsList: 2 List of List --> boolean
    IsList Cek apakah S adalah List
"""


def IsMemberLS(L, S):
    if IsEmpty(S):
        return False
    if IsAtom(FirstList(S)):
        return IsMemberLS(L, TailList(S))
    if IsEqual(FirstList(S), L):
        return True
    return IsMemberLS(L, TailList(S))


# APLIKASI
print(f"IsMemberLS([3, 1], [1, 2, [3, 1]]) = {IsMemberLS([3, 1], [1, 2, [3, 1]])}")
print(f"IsMemberLS([1], [1, 2, 3, [4, 5]]) = {IsMemberLS([1], [1, 2, 3, [4, 5]])}")

"""
DEFINISI DAN SPESIFIKASI
    IsList: 2 List of List --> boolean
    IsList Cek apakah S adalah List
"""


def IsEqS(S1, S2):
    if IsEmpty(S1) and IsEmpty(S2):
        return True
    if not IsEmpty(S1) and IsEmpty(S2):
        return False
    if IsEmpty(S1) and not IsEmpty(S2):
        return False
    if IsAtom(FirstList(S1)) and IsAtom(FirstList(S2)):
        if FirstList(S1) == FirstList(S2):
            return IsEqS(TailList(S1), TailList(S2))
        return False
    if IsList(FirstList(S1)) and IsList(FirstList(S2)):
        return IsEqS(FirstList(S1), FirstList(S2)) and IsEqS(TailList(S1), TailList(S2))
    return False


# APLIKASI
print(
    f"IsEqS([[1, 2], 3, 4, 5], [[1, 2], 3, 4, 5]) = {IsEqS([[1, 2], 3, 4, 5], [[1, 2], 3, 4, 5])}"
)
print(
    f"IsEqS([[1, 2], 3, 4, 5], [[1], 3, 4, 5]) = {IsEqS([[1, 2], 3, 4, 5], [[1], 3, 4, 5])}"
)

"""
DEFINISI DAN SPESIFIKASI
    IsMemberS: elemen, list of list-> boolean
    IsMemberS(x,S) mengembalikan true jika elemen x ada di dalam list of list S
"""


def IsMemberS(x, S):
    if IsEmpty(S):
        return False
    if IsAtom(FirstList(S)):
        if x == FirstList(S):
            return True
        return IsMemberS(x, TailList(S))
    if IsList(FirstList(S)):
        return IsMemberS(x, FirstList(S)) or IsMemberS(x, TailList(S))


# APLIKASI
print(f"IsMemberS(3, []) = {IsMemberS(3, [])}")
print(f"IsMemberS(3, [2, 4, 3, [1], [4, 5]]) = {IsMemberS(3, [2, 4, 3, [1], [4, 5]])}")
print(f"IsMemberS(3, [2, 4, 7, [1], [3, 5]]) = {IsMemberS(3, [2, 4, 7, [1], [3, 5]])}")

# OPERASI/FUNGSI LOL

"""
DEFINISI DAN SPESIFIKASI
Rember: elemen, list of list -> list of list
Rember(x,S) menghapus semua elemen x yang ada di list of list S
"""


def Rember(x, S):
    if IsEmpty(S):
        return []
    if IsAtom(FirstList(S)):
        if FirstList(S) == x:
            return Rember(x, TailList(S))
        return KonsLo(FirstList(S), Rember(x, TailList(S)))
    if IsList(FirstList(S)):
        if FirstList(S) == x:
            return Rember(x, TailList(S))
        return KonsLo(Rember(x, FirstList(S)), Rember(x, TailList(S)))


# APLIKASI
print(f"Rember(3, []) = {Rember(3, [])}")
print(f"Rember(3, [4, 3, [2, 4], 3]) = {Rember(3, [4, 3, [2, 4], 3])}")
print(f"Rember(3, [2, 4, [3, 6, 9], 5, 3]) = {Rember(3, [2, 4, [3, 6, 9], 5, 3])}")

"""
DEFINISI DAN SPESIFIKASI
Max: list of list -> elemen
Max(S) mengembalikan elemen maksimum di dalam list of list S
"""


def Max(S):
    if IsEmpty(S):
        return []
    if IsAtom(S):
        return S
    if IsOneElmt(S):
        return Max(FirstList(S))
    return max2(Max(FirstList(S)), Max(TailList(S)))


# APLIKASI
print(
    f"Max([4, 5, 6, [8, 9, 10], [12, 0], 8]) = {Max([4, 5, 6, [8, 9, 10], [12, 0], 8])}"
)
print(
    f"Max([4, 15, 6, [8, 9, 10], [12, 0], 8]) = {Max([4, 15, 6, [8, 9, 10], [12, 0], 8])}"
)

"""
DEFINISI DAN SPESIFIKASI
    NBElmtAtom: list of list -> integer
    NBElmtAtom(S) mengembalikan banyaknya elemen list of list S yang berupa atom
"""


def NBElmtAtom(S):
    if IsEmpty(S):
        return 0
    if IsAtom(FirstList(S)):
        return 1 + NBElmtAtom(TailList(S))
    if IsList(FirstList(S)):
        return 0 + NBElmtAtom(TailList(S))


# APLIKASI
print(
    f"NBElmtAtom([4, 5, 6, [8, 9, 10], [12, 0], 8]) = {NBElmtAtom([4, 5, 6, [8, 9, 10], [12, 0], 8])}"
)
print(
    f"NBElmtAtom([4, 15, 6, [8, 9], 10, [12], 8]) = {NBElmtAtom([4, 15, 6, [8, 9], 10, [12], 8])}"
)
print(f"NBElmtAtom([[8, 9, 10]]) = {NBElmtAtom([[8, 9, 10]])}")

"""
DEFINISI DAN SPESIFIKASI
NBElmtList: list of list -> integer
NBElmtList(S) mengembalikan banyaknya elemen list of list S yang berupa list
"""


def NBElmtList(S):
    if IsEmpty(S):
        return 0
    if IsAtom(FirstList(S)):
        return 0 + NBElmtList(TailList(S))
    if IsList(FirstList(S)):
        return 1 + NBElmtList(TailList(S))


# APLIKASI
print(
    f"NBElmtList([4, 5, 6, [8, 9, 10], [12, 0], 8]) = {NBElmtList([4, 5, 6, [8, 9, 10], [12, 0], 8])}"
)
print(
    f"NBElmtList([[4, 15], 6, [8, 9], 10, [12], 8]) = {NBElmtList([[4, 15], 6, [8, 9], 10, [12], 8])}"
)
print(f"NBElmtList([[8, 9, 10]]) = {NBElmtList([[8, 9, 10]])}")

"""
DEFINISI DAN SPESIFIKASI
    SumLoL: list of list -> integer
    SumLoL(S) mengembalikan jumlah semua elemen dalam list of list S
"""


def SumLoL(S):
    if IsEmpty(S):
        return 0
    if IsEmpty(FirstList(S)):
        return 0
    if IsAtom(FirstList(S)):
        return FirstList(S) + SumLoL(TailList(S))
    if IsList(FirstList(S)):
        return SumLoL(FirstList(S)) + SumLoL(TailList(S))


# APLIKASI
print(f"SumLoL([[]]) = {SumLoL([[]])}")
print(f"SumLoL([4, 5, 6, [2, 3, 1]]) = {SumLoL([4, 5, 6, [2, 3, 1]])}")
print(f"SumLoL([[2, 3, 4]]) = {SumLoL([[2, 3, 4]])}")

"""
DEFINISI DAN SPESIFIKASI
MaxNBElmtList: list of list -> integer
MaxNBElmtList(S) mengembalikan banyaknya elemen list maksimum yang ada pada list of list S
"""


def MaxNBElmtList(S):
    if IsEmpty(S):
        return 0
    if IsAtom(FirstList(S)):
        return MaxNBElmtList(TailList(S))
    if IsList(FirstList(S)):
        return max2(NbElmt(FirstList(S)), MaxNBElmtList(TailList(S)))


# APPLIKASI
print(
    f"MaxNBElmtList([[4, 5, 6, 7], [8, 9, 10], [12, 0], 8]) = {MaxNBElmtList([[4, 5, 6, 7], [8, 9, 10], [12, 0], 8])}"
)
print(
    f"MaxNBElmtList([[4, 15], 6, [8, 9], 10, [12], 8]) = {MaxNBElmtList([[4, 15], 6, [8, 9], 10, [12], 8])}"
)
print(f"MaxNBElmtList([8, 9, 10]) = {MaxNBElmtList([8, 9, 10])}")

"""
DEFINISI DAN SPESIFIKASI
    MaxSumElmt: list of list -> integer
    MaxSumElmt(S) mengembalikan elemen maksimum pada list of list S
    jika elemen berupa list, maka dihitung jumlahan elemen dalam list tersebut5
    jika elemen atom, maka nilainya adalah elemen tersebut
"""


def MaxSumElmt(S):
    if IsEmpty(S):
        return 0
    if IsAtom(FirstList(S)):
        return max2(FirstList(S), MaxSumElmt(TailList(S)))
    if IsList(FirstList(S)):
        return max2(SumLoL(FirstList(S)), MaxSumElmt(TailList(S)))


# APLIKASI
print(
    f"MaxSumElmt([[1, 2], 9, [4, 5, 6], 8]) = {MaxSumElmt([[1, 2], 9, [4, 5, 6], 8])}"
)
print(
    f"MaxSumElmt([[1, 2], 90, [4, 5, 6], 8]) = {MaxSumElmt([[1, 2], 90, [4, 5, 6], 8])}"
)
print(f"MaxSumElmt([8, 9, 10]) = {MaxSumElmt([8, 9, 10])}")
print(f"MaxSumElmt([[8, 9, 10]]) = {MaxSumElmt([[8, 9, 10]])}")
