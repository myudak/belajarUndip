# Nama File : set.py
# deskripsi : berisi type dsan operasi list
# Pembuat : Novelya Cherina
# Tanggal : 5 November 2024

# Nama File : List_24060124140174
# Deskripsi :
# Pembuat : Novelya Cherina
# Tanggal : 29 Oktober 2024


# ElmtkeN : integer ≥ 0 , List → elemen
# ElmtkeN (N, L) : Mengirimkan elemen list yang ke N, N ≤ NbELmt(L) dan N>=0
def ElmtkeN(N, L):
    if N == 1:
        return FirstElmt(L)
    else:
        return ElmtkeN(N - 1, Tail(L))


# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: list tidak kosong -> elemen
# FirstElmt(l) menghasilkan elemen pertama dari list l
# Realisasi
def FirstElmt(L):
    return L[0]


# LastElmt: list tidak kosong -> elemen
# LastElmt(l) menghasilkan elemen terakhir dari list l
# Realisasi
def LastElmt(l):
    return l[-1]


# Tail: list tidak kosong -> List
# Tail(l) mengembalikan list tanpa elemen pertama dari list l, mungkin kosong
# Realisasi
def Tail(L):
    return L[1:]


# Head: list tidak kosong -> List
# Head(l) mengembalikan list tanpa elemen terakhir dari list l, mungkin kosong
# Realisasi
def Head(L):
    return L[:-1]


# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: List -> boolean
# IsEmpty(L) benar jika list kosong
# Realisasi
def IsEmpty(L):
    return L == []


# IsOneElmt: List -> boolean
# IsOneElmt(L) adalah benar jika list L hanya mempunyai satu elemen
# Realisasi
def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, List -› List
# Konso(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# Realisasi
def Konso(e, L):
    return [e] + L


# Konsi: List, elemen -› List
# Konsi(L,e) -> menghasilkan sebah list dari L dan e dengan e sebagai elemen terakhir
def Konsi(L, e):
    return L + [e]


# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# NbElmt: List -> integer
# NbElmt(L) menghasilkan banyaknya elemen list, nol jika kosong
# Realisasi
def NbElmt(L, N):
    if IsEmpty(L):
        return 0
    elif FirstElmt(L) == N:
        return 1 + NbElmt(Tail(L), N)
    else:
        return NbElmt(Tail(L), N)


# Copy : List → List
# Copy(L) : Menghasilkan list yang identik dengan list asal
def Copy(L):
    if IsEmpty(L):
        return []
    else:
        Konso(FirstElmt(L), Copy(Tail(L)))


# Inverse : List → List
# Inverse(L) : Menghasilkan list L yang dibalik, yaitu yang urutan elemennya
#   adalah kebalikan dari list asal# invers: List -> List
# Realisasi
def inverse(L):
    if IsEmpty(L):
        return []
    else:
        Konsi(inverse(Tail(L)), FirstElmt(L))


# Konkat : 2 List → List
# Konkat(L1,L2) : Menghasilkan konkatenasi 2 buah list, dengan list L2 "sesudah" list L1
# Realisasi terhadap L1
def Konkat1(L1, L2):
    if IsEmpty(L2):
        return []
    else:
        return Konsi(L1, FirstElmt(L2)) + Konkat1(L1, Tail(L2))


L = [1, 2, 3, 5]
L2 = [6, 5, 4, 3]
print(Konkat1(L, L2))


# Realisasi terhadap L2
def Konkat2(L1, L2):
    if IsEmpty(L1):
        return L2
    else:
        Konkat2(Konsi(L1, FirstElmt(L2)), Tail(L2))


# SumElmt: List of integer -› integer
# SumElmt(L) menghasilkan jumlahan dari setiap elemen di list L
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))


# AvgElmt: List of integer -› integer
# AvgEmlt(L) menghasilkan nilai rata-rata
def AvgElmt(L):
    return SumElmt(L) / NbElmt(L)


# MaxElmt(L): List of integer -› integer
# MaxElmt(L) mengembalikan elemen maksimum dari list L
#             def MaxElmt(L) :
#    return

# MaxNB: List of integer -› <integer, integer›
# MaxNB(L) menghasilkan <max,countMax>
#   dengan max adalah elemen maksimum list L
#   dan countMax adalah banyaknya kemunculan max di list L


# IsMember: elemen, List → boolean
# IsMember (X,L) adalah benar jika X adalah elemen list L
def IsMember(X, L):
    if IsEmpty(L):
        return False
    elif FirstElmt(L) == X:
        return True
    else:
        return IsMember(X, Tail(L))


# AddList: 2 List of integer -› List of integer
# AddList(L1,L2) menghasilkan list baru yang setiap elemennya
#   adalah hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama
# Realisasi
def addlist(l1, l2):
    if NbElmt(l1) == NbElmt(l2):
        if IsEmpty(l1) and IsEmpty(l2):
            return []
        else:
            return Konso(FirstElmt(l1) + FirstElmt(l2), addlist(Tail(l1), Tail(l2)))
    else:
        return False


# IsPalindrom(L): List of character -› boolean
# IsPalindrom(L) benar jika L merupakan kata palindrom
#   yaitu kata yang sama jika dibaca dari kiri atau kanan
#   contoh: RUSAK, KASUR RUSAK, NABABAN
def IsPalindrom(l):
    return inverse(l) == l


def IsPalindrom(L):
    if L == []:
        return True
    elif L == FirstElmt(L):
        return True
    elif FirstElmt(L) == LastElmt(L):
        return IsPalindrom(Head(Tail(L)))


# print(IsMember(2,[1,2,4,6,8]))
print(IsPalindrom(["r", "u", "m", "u", "r"]))


# DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN
# Rember: elemen, list -> list
# Rember(x,L) menghapus sebuah elemen x dari list L
# Jika x ada di list L, maka elemen L berkurang 1.
# Jika x tidak ada di list L maka L tetap.
# List kosong tetap menjadi list kosong.
def rember(x, L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L), rember(x, Tail(L)))


# APLIKASI
print(rember(2, []))
print(rember(2, [3]))
print(rember(2, [3, 4, 5, 2, 3, 5, 7, 8, 2]))


# MultiRember: elemen, list -> list
# MultiRember(x,L) menghapus semua kemunculan elemen x dari list L.
# List baru yang dihasilkan tidak lagi memiliki elemen x.
# List kosong tetap menjadi list kosong.
def MultiRember(x, L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return MultiRember(x, Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(x, Tail(L)))


# APLIKASI
print(MultiRember(2, [1, 2, 2, 3]))


# DEFINISI DAN SPESIKASI KONSTRUKTOR SET DARI LIST
# MakeSet: list -> set
# MakeSet(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali
# list kosong tetap menjadi himpunan kosong
def MakeSet1(l):
    if IsEmpty(l):
        return []
    else:
        if IsMember(FirstElmt(l), Tail(l)):
            return MakeSet1(Tail(l))
        else:
            return Konso(FirstElmt(l), MakeSet1(l))


# APLIKASI
print(MakeSet1([3, 4, 5, 3, 6]))


def MakeSet2(L):
    if IsEmpty(L):
        return L
    else:
        return Konso(FirstElmt(L), MakeSet2(MultiRember(FirstElmt(L), Tail(L))))


# APLIKASI
print(MakeSet2([3, 4, 5, 3, 6]))


# DEFINISI DAN SPESIKASI KONSTRUKTOR SET
# KonsoSet: elemen,set -> set
# konsoSet(e,H) menambahkan sebuah elemen e sebagai elemen pertama set H
#   dengan syarat e belum ada di dalam himpunan H
def KonsoSet(e, H):
    if IsMember(e, H):
        return H
    else:
        return Konso(e, H)


# APLIKASI
print(KonsoSet(2, [3, 2, 1]))


# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSet: list -> boolean
# IsSet(L) mengembalikan true jika L adalah sebuah set
def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return False
        else:
            return IsSet(Tail(L))


# APLIKASI
print(IsSet([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(IsSet([2, 2, 3, 4, 5, 6, 7, 8, 9]))


# IsSubset: 2 set -> boolean
# IsSubset(H1,H2) mengembalikan true jika H1 merupakan subset dari H2
def IsSubset(H1, H2):
    if IsEmpty(H1):
        return True
    else:
        if not IsMember(FirstElmt(H1), H2):
            return False
        else:
            return IsSubset(Tail(H1), H2)


# APLIKASI
print(IsSubset([2, 3, 4], [6, 5, 4, 3, 2]))
print(IsSubset([1, 2, 3], [5, 6, 7, 8, 9]))


# IsEqualSet: 2 set -> boolean
# IsEqualSet(H1,H2} benar jika H1 adalah set yang sama dengan H2
def IsEqualSet(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    else:
        return IsSubset(H1, H2) and IsSubset(H2, H1)


# APLIKASI
print(IsEqualSet([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
print(IsEqualSet([1, 2, 3], [5, 4, 3, 2, 1]))


# IsIntersect: 2 set -> boolean
# IsIntersect(H1,H2) benar jika H1 beririsan dengan H2
def IsIntersect(H1, H2) -> bool:
    if IsEmpty(H1) and IsEmpty(H2):
        return False
    if not IsEmpty(H1) and IsEmpty(H2):
        return False
    if IsEmpty(H1) and not IsEmpty(H2):
        return False
    if IsMember(FirstElmt(H1), H2):
        return True
    return IsIntersect(Tail(H1), H2)


# APPLIKASI
print(f"IsIntersect([1,2],[1,2,3]) = {IsIntersect([1,2],[1,2,3])}")
print(f"IsIntersect([6,9],[1,2,3]) = {IsIntersect([6,9],[1,2,3])}")


# DEFINISI DAN SPESIFIKASI OPERASI TERHADAP HIMPUNAN
# MakeIntersect: 2 set -> set
# MakeUnion: 2 set -> set
# MakeUnion(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2
def MakeUnion(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif IsEmpty(H1) and not IsEmpty(H2):
        return H2
    elif not IsEmpty(H1) and IsEmpty(H2):
        return H1
    else:
        return Konso(FirstElmt(H1), MakeUnion(Tail(H1), H2))


print(MakeUnion([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))


def MakeIntersect(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif IsEmpty(H1) and not IsEmpty(H2):
        return []
    elif not IsEmpty(H1) and IsEmpty(H2):
        return []
    else:
        return (
            Konso(FirstElmt(H1), MakeIntersect(Tail(H1), H2))
            if IsMember(FirstElmt(H1), H2)
            else MakeIntersect(Tail(H1), H2)
        )


print(MakeIntersect([1, 2, 3], [1, 3, 4]))
# NBIntersect: 2 set -> integer
# NBIntersect(H1,H2) menghasilkan jumlah elemen yang beririsan pada H1 dan H2
#   tanpa memanfaatkan fungsi MakeIntersect(H1,H2).


# NBUnion: 2 set -> integer
# NBUnion(H1,H2) menghasilkan jumlah elemen hasil gabungan antara H1 dan H2
#   tanpa memanfaatkan fungsi MakeUnion(H1,H2).
def NBUnion(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return 0
    if not IsEmpty(H1) and IsEmpty(H2):
        return NbElmt(H1)
    if IsEmpty(H1) and not IsEmpty(H2):
        return NbElmt(H2)
    else:
        if IsMember(FirstElmt(H1), H2):
            return NBUnion(Tail(H1), H2)
        return 1 + NBUnion(Tail(H1), H2)


# APLIKASI
print(NBUnion())
