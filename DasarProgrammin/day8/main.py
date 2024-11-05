from typing import List
from tugasRekursif import (
    IsEmpty,
    Konsi,
    Konso,
    FirstElmt,
    LastElmt,
    Head,
    NbElmt,
    Tail,
    IsMember,
)

"""
Deskripsi : TUGAS LIST
Pembuat   : Muchammad Yuda Tri Ananda
NIM       : 24060124110142
Tanggal   : 5 November 2024 
"""

"""
DEFINISI DAN SPESIFIKASI TYPE
Set adalah sebuah list dengan syarat setiap elemen harus unik
Semua konstruktor, selektor, dan operasi yang telah didefinisikan untuk list juga berlaku pada set
"""

"""
DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN
Rember: elemen, list ➜ list
Rember(x, L) menghapus sebuah elemen x dari list L
    Jika x ada di list L, maka elemen L berkurang 1.
    Jika x tidak ada di list L maka L tetap.
    List kosong tetap menjadi list kosong.
"""


def rember(x, L: List) -> List:
    if IsEmpty(L):
        return []
    if x == FirstElmt(L):
        return Tail(L)
    return Konso(FirstElmt(L), rember(x, Tail(L)))


# APPLIKASI
print(f"rember(2,[1,2,3,4]) = {rember(2,[1,2,3,4])}")
print(f"rember(2,[1,2,3,2]) = {rember(2,[1,2,3,2])}")
print(f"rember(2,[3]) = {rember(2,[3])}")

"""
TUGAS / LATIhAN
"""

"""
1. Realisasi fungsi Rember(x,L) yang dicontohkan akan menghapus elemen x yang ditemui pertama kali dari list L. Buatlah realisasi versi 2 untuk menghapus elemen x yang ditemui terakhir kali pada list L, beri nama dengan Rember2(x,L). 
"""

"""
Rember: elemen, list ➜ list 
    Rember(x,L) menghapus sebuah elemen x dari list L 
    Jika x ada di list L, maka elemen L berkurang 1.  
    Jika x tidak ada di list L maka L tetap. 
    List kosong tetap menjadi list kosong. 
"""


def Rember2(x: any, L: List) -> List:
    """Realisasi 2 untuk menghapus elemen x yang ditemui terakhir kali pada list L"""
    if IsEmpty(L):
        return []
    if x == LastElmt(L):
        return Head(L)
    return Konsi(Rember2(x, Head(L)), LastElmt(L))


# APPLIKASI
print(f"Rember2(2,[1,2,3,4]) = {Rember2(2,[1,2,3,4])}")
print(f"Rember2(2,[1,2,3,4,4,6,9]) = {Rember2(2,[1,2,3,4,4,6,9])}")
print(f"Rember2(2,[3]) = {Rember2(2,[3])}")

"""
2. Buatlah realisasi dari fungsi MultiRember(x,L). 
"""

"""
MultiRember: elemen, list ➜ list 
    MultiRember(x,L) menghapus semua kemunculan elemen x dari list L.  
    List baru yang dihasilkan tidak lagi memiliki elemen x.  
    List kosong tetap menjadi list kosong. 
"""


def MultiRember(x: any, L: List) -> List:
    """MultiRember (x,L)  menghapus semua elemen bernilai x dari list"""
    if IsEmpty(L):
        return []
    if x == FirstElmt(L):
        return MultiRember(x, Tail(L))
    return Konso(FirstElmt(L), MultiRember(x, Tail(L)))


# APPLIKASI
print(f"MultiRember(2,[1,2,3,4,2]) = {MultiRember(2,[1,2,3,4,2])}")


"""
3. Buatlah realisasi fungsi MakeSet(L) dalam dua versi: 
    a. Versi 1: dengan memanfaatkan fungsi IsMember(x,L) untuk mengecek duplikasi elemen. 
    b. Versi 2: dengan memanfaatkan fungsi MultiRember(x,L) untuk menghapus duplikasi elemen.   
"""

"""
MakeSet: list ➜ set  
    MakeSet(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali list kosong tetap menjadi himpunan kosong 
"""


def MakeSet(L: List) -> List:
    if IsEmpty(L):
        return []
    if IsMember(FirstElmt(L), Tail(L)):
        return MakeSet(Tail(L))
    return Konso(FirstElmt(L), MakeSet(Tail(L)))


def MakeSet2(L: List) -> List:
    if IsEmpty(L):
        return []
    return Konso(FirstElmt(L), MakeSet2(MultiRember(FirstElmt(L), Tail(L))))


# APPLIKASI
print(f"MakeSet([1,2,3,4,2]) = {MakeSet([1,2,3,4,2])}")
print(f"MakeSet2([1,2,3,4,2]) = {MakeSet2([1,2,3,4,2])}")

"""
Perhatikan output yang dihasilkan dari kedua versi tersebut. Bagaimana perbedaannya?  
"""


"""
4. Buatlah realisasi fungsi KonsoSet(e,H) yang menambahkan sebuah elemen e sebagai elemen  pertama set H dengan syarat e belum ada di dalam himpunan H.
"""

"""
KonsoSet: elemen,set ➜ set  
    konsoSet(e,H) menambahkan sebuah elemen e sebagai elemen pertama set H  
    dengan syarat e belum ada di dalam himpunan H 
"""


def KonsoSet(e: any, H: List) -> List:
    """KonsoSet(e,H) mengisi set H dengan elemen e sebagai elemen pertama jika e tidak ada di dalam set H"""
    if IsEmpty(H):
        return e
    if FirstElmt(e) == LastElmt(H):
        return H
    return Konsi(KonsoSet(e, Head(H)), LastElmt(H))


# APPLIKASI
print(f"KonsoSet([2],[1,2,3,4,2]) = {KonsoSet([2],[1,2,3,4,2])}")
print(f"KonsoSet([2],[1,2,3,4]) = {KonsoSet([2],[1,2,3,4])}")
print(f"KonsoSet([2],[1,3,4]) = {KonsoSet([2],[1,3,4])}")

"""
5. Buatlah realisasi fungsi IsSet(L). 
"""

"""
IsSet: list ➜ boolean 
    IsSet(L) mengembalikan true jika L adalah sebuah set 
"""


def IsSet(L: List) -> bool:
    if IsEmpty(L):
        return True
    if IsMember(FirstElmt(L), Tail(L)):
        return False
    return IsSet(Tail(L))


# APPLIKASI
print(f"IsSet([1,2,3,4,2]) = {IsSet([1,2,3,4,2])}")

"""
6. Buatlah realisasi fungsi IsSubset(H1,H2) 
"""

"""
IsSubset: 2 set ➜ boolean 
    IsSubset(H1,H2) mengembalikan true jika H1 merupakan subset dari H2
"""


def IsSubset(H1: List, H2: List) -> bool:
    """true jika H1 merupakan subset dari H2"""
    if IsEmpty(H1):
        return True
    if not IsMember(FirstElmt(H1), H2):
        return False
    return IsSubset(Tail(H1), H2)


# APPLIKASI
print(f"IsSubset([1,2,3], [1,2,3,4,5]) == {IsSubset([1, 2, 3], [1, 2, 3, 4, 5])}")
print(f"IsSubset([1,2,6], [1,2,3,4,5]) == {IsSubset([1, 2, 6], [1, 2, 3, 4, 5])}")

"""
7. Buatlah realisasi fungsi IsEqualSet dalam dua versi: 
a. Versi 1: memanfaatkan fungsi IsSubset(H1,H2). 
b. Versi 2: dengan mengecek satu persatu elemen pada H1 dan H2. 
"""

"""
IsEqualSet: 2 set ➜ boolean 
    IsEqualSet(H1,H2} benar jika H1 adalah set yang sama dengan H2
"""


def IsEqualSet(H1: List, H2: List) -> bool:
    return IsSubset(H1, H2) and IsSubset(H2, H1)


def IsEqualSet2(H1: List, H2: List) -> bool:
    if IsEmpty(H1):
        return True
    if IsMember(FirstElmt(H1), H2):
        return IsEqualSet2(Tail(H1), H2)
    return False


# APPLIKASI
print(f"IsEqualSet([1,2,3], [1,2,3]) = {IsEqualSet([1, 2, 3], [1, 2, 3])}")
print(f"IsEqualSet([1,2,3], [1,2,4]) = {IsEqualSet([1, 2, 3], [1, 2, 4])}")
print(f"IsEqualSet2([1,2,3], [1,2]) = {IsEqualSet2([1, 2, 3], [1, 2])}")
print(f"IsEqualSet2([1,2,3,4], [1,3,2,4]) = {IsEqualSet([1, 2, 3,4], [1, 3, 2,4])}")
print(f"IsEqualSet([1,2,3], [2,3]) = {IsEqualSet([1, 2, 3], [2, 3])}")
print(f"IsEqualSet([1,2,3], [3,2]) = {IsEqualSet([1, 2, 3], [3, 2])}")


"""
8. Buatlah realisasi fungsi IsIntersect(H1,H2). 
"""

"""
IsIntersect: 2 set ➜ boolean 
    IsIntersect(H1,H2) benar jika H1 beririsan dengan H2
"""


def IsIntersect(H1: List, H2: List) -> bool:
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

"""
9. Buatlah realisasi fungsi MakeIntersect(H1,H2) dalam 2 versi: 
    a. Versi 1: rekursif terhadap H1 
    b. Versi 2: rekursif terhadap H2 
"""

"""
MakeIntersect: 2 set ➜ set 
    MakeIntersect(H1,H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2
"""


def MakeIntersect(H1: List, H2: List) -> List:
    if IsEmpty(H1):
        return []
    if IsMember(FirstElmt(H1), H2):
        return Konso(FirstElmt(H1), MakeIntersect(Tail(H1), H2))
    return MakeIntersect(Tail(H1), H2)


def MakeIntersect2(H1: List, H2: List) -> List:
    if IsEmpty(H2):
        return []
    if IsMember(FirstElmt(H2), H1):
        return Konso(FirstElmt(H2), MakeIntersect2(Tail(H2), H1))
    return MakeIntersect2(Tail(H2), H1)


print(f"MakeIntersect([1,2,3], [1,2,3,4,5]) = {MakeIntersect([1,2,3], [1,2,3,4,5])}")
print(
    f"MakeIntersect([6,9,1,3,2], [1,2,3,4,5]) = {MakeIntersect([6,9,1,3,2], [1,2,3,4,5])}"
)
print(f"MakeIntersect2([1,2,3], [1,2,3,4,5]) = {MakeIntersect2([1,2,3], [1,2,3,4,5])}")
print(
    f"MakeIntersect2([6,9,1,3,2], [1,2,3,4,5]) = {MakeIntersect2([6,9,1,3,2], [1,2,3,4,5])}"
)

"""
Perhatikan output yang dihasilkan dari kedua versi tersebut. Bagaimana perbedaannya?  
"""

"""
10. Buatlah realisasi fungsi MakeUnion(H1,H2) dalam 2 versi: 
    a. Versi 1: rekursif terhadap H1 
    b. Versi 2: rekursif terhadap H2 
"""

"""
MakeUnion: 2 set ➜ set 
    MakeUnion(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2 
"""


def MakeUnion(H1: List, H2: List) -> List:
    if IsEmpty(H1):
        return H2
    if IsMember(FirstElmt(H1), H2):
        return MakeUnion(Tail(H1), H2)
    return Konso(FirstElmt(H1), MakeUnion(Tail(H1), H2))


def MakeUnion2(H1: List, H2: List) -> List:
    if IsEmpty(H2):
        return H1
    if IsMember(FirstElmt(H2), H1):
        return MakeUnion2(H1, Tail(H2))
    return Konso(FirstElmt(H2), MakeUnion2(H1, Tail(H2)))


print(f"MakeUnion([1,2,3], [1,2,3,4,5]) = {MakeUnion([1,2,3], [1,2,3,4,5])}")
print(f"MakeUnion([3,2,1], [1,2,3,4,5]) = {MakeUnion([3,2,1], [1,2,3,4,5])}")
print(f"MakeUnion([6,9,3,2,1], [1,2,3,4,5]) = {MakeUnion([6,9,3,2,1], [1,2,3,4,5])}")

print(f"MakeUnion2([1,2,3], [1,2,3,4,5]) = {MakeUnion2([1,2,3], [1,2,3,4,5])}")
print(f"MakeUnion2([3,2,1], [1,2,3,4,5]) = {MakeUnion2([3,2,1], [1,2,3,4,5])}")
print(f"MakeUnion2([6,9,3,2,1], [1,2,3,4,5]) = {MakeUnion2([6,9,3,2,1], [1,2,3,4,5])}")

"""
Perhatikan output yang dihasilkan dari kedua versi tersebut. Bagaimana perbedaannya?  
"""

"""
11. Buatlah realisasi fungsi NBIntersect(H1,H2). 
"""

"""
NBIntersect: 2 set ➜ integer 
    NBIntersect(H1,H2) menghasilkan jumlah elemen yang beririsan pada H1 dan H2 
    tanpa memanfaatkan fungsi MakeIntersect(H1,H2). 
"""


def NBIntersect(H1, H2):
    if IsEmpty(H1):
        return 0
    if IsMember(FirstElmt(H1), H2):
        return 1 + NBIntersect(Tail(H1), H2)
    return NBIntersect(Tail(H1), H2)


print(f"NBIntersect([1,2,3], [1,2,3,4,5]) = {NBIntersect([1,2,3], [1,2,3,4,5])}")

"""
12. Buatlah realisasi fungsi NBUnion(H1,H2).
"""

"""
NBUnion: 2 set ➜ integer 
    NBUnion(H1,H2) menghasilkan jumlah elemen hasil gabungan antara H1 dan H2 
    tanpa memanfaatkan fungsi MakeUnion(H1,H2).
"""


def NBUnion(H1, H2):
    if IsEmpty(H1):
        return NbElmt(H2)
    if IsMember(FirstElmt(H1), H2):
        return NBUnion(Tail(H1), H2)
    return 1 + NBUnion(Tail(H1), H2)


print(f"NBUnion([3,2,1], [1,2,3,4,5]) = {NBUnion([3,2,1], [1,2,3,4,5])}")
print(f"NBUnion([6,9,3,2,1], [1,2,3,4,5]) = {NBUnion([6,9,3,2,1], [1,2,3,4,5])}")
