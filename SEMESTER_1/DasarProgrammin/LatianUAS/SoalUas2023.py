from typing import List


def Konso(e: int, L: List) -> List:
    """Konso(e, L) menghasilkan sebuah List dari e dan L dengan e sebagai elemen pertama"""
    return [e] + L


"""
Konsi: List, elemen → List
  {Konsi(L,e) menghasilkan sebuah List dari L dan e dengan e sebagai elemen terakhir}
Realisasi
"""


def Konsi(L: List, e: int) -> List:
    """Konsi(L,e) menghasilkan sebuah List dari L dan e dengan e sebagai elemen terakhir <L,e>"""
    return L + [e]


"""
DEFINISI DAN SPESIFIKASI SELEKTOR
FirstElmt: List tidak kosong → elemen
  {FirstElmt(L) mengembalikan elemen pertama dari list L}
Realisasi
"""


def FirstElmt(L: List) -> int:
    """FirstElmt(L) mengembalikan elemen pertama dari list L"""
    return L[0]


def LastElmt(L: List) -> int:
    """LastElmt(L): mengembalikan elemen terakhir terakhir list L"""
    return L[-1]


"""
Head: List tidak kosong → List
  {Head(L): Menghasilkan list tanpa elemen terakhir list L, mungkin kosong}
Realisasi
"""


def Head(L: List) -> List:
    """Head(L): Menghasilkan list tanpa elemen terakhir list L, mungkin kosong"""
    return L[:-1]


"""
Tail: List tidak kosong → List
  {Tail(L): Menghasilkan list tanpa elemen pertama list L, mungkin kosong}
Realisasi
"""


def Tail(L: List) -> List:
    """Tail(L): Menghasilkan list tanpa elemen pertama list L, mungkin kosong"""
    return L[1:]


"""
DEFINISI DAN SPESIFIKASI PREDIKAT
IsEmpty: List → boolean
  {IsEmpty(L) benar jika list kosong}
Realisasi
"""


def IsEmpty(L: List) -> bool:
    """IsEmpty(L) benar jika list kosong"""
    return L == [] or L == ""


"""
IsOneElmt: List → boolean
  {IsOneElmt(L) adalah benar jika list L hanya mempunyai satu elemen}
Realisasi
"""


def IsOneElmt(L: List) -> bool:
    """IsOneElmt(L) adalah benar jika list L hanya mempunyai satu elemen"""
    if IsEmpty(L):
        return False
    return Tail(L) == [] and Head(L) == []


def IsList(S):
    return type(S) is list


def makePN(A, PN):
    return [A, PN]


# DEFINISI DAN SPESIFIKASI SELEKTOR
# Akar : PohonN-ner tidak kosong -> elemen
#   {Akar(P) adalah akar dari P. Jika P adalah (A, PN) = Akar(P) adalah A}
def Akar(PN):
    return PN[0]


def isOneElmt(PN):
    return (isTreeNEmpty(PN) is False) and (isTreeNEmpty(Anak(PN)) is True)


def Copy(L: List) -> List:
    if IsEmpty(L):
        return []
    return Konso(FirstElmt(L), Copy(Tail(L)))


# print(f"Copy([1,2,3,4]) = {Copy([1, 2, 3, 4])}")

"""
Invers: List → List
  {Invers(L) menghasilkan List L yang dibalik}
"""


def Invers(L: List) -> List:
    """Invers(L) menghasilkan List L yang dibalik"""
    if IsEmpty(L):
        return []
    return Konso(LastElmt(L), Head(L))


"""
Konkat : 2 List → List
  {Konkat(L1,L2) menghasilkan konketasi 2 buah list, dengan list L2 "sesudah" list L1}
Realisasi
"""


def Konkat(L1: List, L2: List) -> List:
    """Konkat(L1,L2) menghasilkan konketasi 2 buah list, dengan list L2 "sesudah" list L1"""
    return Copy(L1) + Copy(L2)


# Anak: PohonN-ner tidak kosong → list of PohonN-ner
# #{ Anak(P) adalah list of pphon N-ner yang merupakan anak-anak (sub phon) # dari P. Jika P adalah (A, PN) = Anak (P) adalah PN }
def Anak(PN):
    return PN[1]


# DEFINISI DAN SPESIFIKASI PREDIKAT
# #IsTreeNEmpty : PohonN-ner → boolean_
# # {IsTreeNEmpty(PN) true jika PN kosong : () }
def isTreeNEmpty(PN):
    return PN == []


def MakeBST(A, L, R):
    return [A, L, R]


def Akar(P):
    return P[0]


def Left(P):
    return P[1]


def Right(P):
    return P[2]


def IsTreeEmpty(P):
    return P == []


def IsOneElmtBST(T):
    return not IsTreeEmpty(T) and IsTreeEmpty(Left(T)) and IsTreeEmpty(Right(T))


def IsBiner(P):
    return not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))


def IsUnerLeft(P):
    return not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))


def IsUnerRight(P):
    return not IsTreeEmpty(P) and IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))


"""

< MAIN >

"""


def FilterGenap(x: List[int]) -> List[int]:
    if IsEmpty(x):
        return []
    if FirstElmt(x) % 2 != 0:
        return FilterGenap(Tail(x))
    return Konso(FirstElmt(x), FilterGenap(Tail(x)))


print(f"{FilterGenap([1,2,3,4,5,6,7,8,9,10])=}")  # > [2,4,6,8,10]
print(f"{FilterGenap([6, 3, 1, 28, 12, 9, 4])=}")  # > [6, 28, 12, 4]


def IsContainList(L: List) -> bool:
    if IsEmpty(L):
        return False
    return IsList(FirstElmt(L)) or IsContainList(Tail(L))


print(f"{IsContainList([6, [3, 1], [28, 12, 9], 4])=}")  # > true
print(f"{IsContainList([6, 3, 1, 28, 12, 9, 4])=}")  # > false


def SubTreeElemt(x, PN):
    if IsTreeEmpty(PN):
        return []
    if Akar(PN) == x:
        return PN
    if Anak(PN) == []:
        return []
    if not IsTreeEmpty(SubTreeElemt(x, Akar(Anak(PN)))):
        return SubTreeElemt(x, Akar(Anak(PN)))
    return SubTreeElemt(x, Konso(Akar(PN), [Tail(Anak(PN))]))


print(f"{SubTreeElemt(3, [2, [[3, [[4, []], [5, []]]], [6, []]]])=}")
print(f"{SubTreeElemt(2, [2, [[3, [[4, []], [5, []]]], [6, []]]])=}")
print(f"{SubTreeElemt(4, [2, [[3, [[4, []], [5, []]]], [6, []]]])=}")
print(f"{SubTreeElemt(5, [2, [[3, [[4, []], [5, []]]], [6, []]]])=}")
print(f"{SubTreeElemt(10, [2, [[3, [[4, []], [5, []]]], [6, []]]])=}")
print(f"{SubTreeElemt(2, [2, [[3, []], [4, []], [5, []]]])=}")
print(f"{SubTreeElemt(3, [2, [[3, []], [4, []], [5, []]]])=}")
print(f"{SubTreeElemt(4, [2, [[3, []], [4, []], [5, []]]])=}")
print(f"{SubTreeElemt(5, [2, [[3, []], [4, []], [5, []]]])=}")
print(f"{SubTreeElemt(1, [1, [[2, []], [3, []], [4, []], [5, []]]])=}")
print(f"{SubTreeElemt(2, [1, [[2, []], [3, []], [4, []], [5, []]]])=}")
print(f"{SubTreeElemt(3, [1, [[2, []], [3, []], [4, []], [5, []]]])=}")
print(f"{SubTreeElemt(5, [1, [[2, []], [3, []], [4, []], [5, []]]])=}")
print(
    f"{SubTreeElemt(3, [1, [[2, [[5, []], [6, []], [7, []]]], [3, [[8, []], [9, []]]], [4, [[10, []]]]]])=}"
)
print(
    f"{SubTreeElemt(2, [1, [[2, [[5, []], [6, []], [7, []]]], [3, [[8, []], [9, []]]], [4, [[10, []]]]]])=}"
)
print(
    f"{SubTreeElemt(7, [1, [[2, [[5, []], [6, []], [7, []]]], [3, [[8, []], [9, []]]], [4, [[10, []]]]]])=}"
)


def IsBST4(BST, F):
    if IsTreeEmpty(BST):
        return False
    if IsOneElmtBST(BST) or IsUnerLeft(BST):
        return F(Akar(BST))
    return IsBST4(Right(BST), F)


print(
    f"{IsBST4(MakeBST(8, MakeBST(4, MakeBST(3, [], []), MakeBST(6, [], [])), MakeBST(10, [], MakeBST(12, [], []))), lambda x: x % 4 == 0)=}"
)
print(f"{IsBST4(MakeBST(8, MakeBST(4, [], []), []), lambda x: x % 4 == 0)=}")
print(
    f"{IsBST4(MakeBST(10, MakeBST(6, [], []), MakeBST(15, [], [])), lambda x: x % 4 == 0)=}"
)
print(
    f"{IsBST4(MakeBST(12, MakeBST(8, [], []), MakeBST(16, [], [])), lambda x: x % 4 == 0)=}"
)
print(f"{IsBST4([], lambda x: x % 4 == 0)=}")
print(
    f"{IsBST4(MakeBST(7, MakeBST(4, [], []), MakeBST(9, [], [])), lambda x: x % 4 == 0)=}"
)
print(f"{IsBST4(MakeBST(16, [], []), lambda x: x % 4 == 0)=}")
print(f"{IsBST4(MakeBST(15, [], []), lambda x: x % 4 == 0)=}")
print(
    f"{IsBST4(MakeBST(20, MakeBST(10, [], []), MakeBST(25, [], [])), lambda x: x % 4 == 0)=}"
)
print(
    f"{IsBST4(MakeBST(10, MakeBST(8, [], []), MakeBST(18, [], [])), lambda x: x % 4 == 0)=}"
)
print(
    f"{IsBST4(MakeBST(8, MakeBST(4, MakeBST(3, [], []), MakeBST(6, MakeBST(5, [], []), MakeBST(7, [], []))), MakeBST(10, MakeBST(9, [], []), MakeBST(12, [], []))),lambda x: x % 4 == 0)=}"
)
