from typing import List
from tugasRekursif import IsMember


def IsEmpty(S: List[List]) -> bool:
    """IsEmpty(L) mengembalikan True jika list of list kosong"""
    return S == [] or S == [[]]


def IsAtom(S: List[List]) -> bool:
    """IsAtom(L) mengembalikan True jika list of list hanya mempunyai satu elemen"""
    return not isinstance(S, list)


def IsList(S: List[List]) -> bool:
    """IsList(L) mengembalikan True jika list of list berisi list"""
    return isinstance(S, list)


def Konslo(e: List, L: List[List]) -> List[List]:
    """Konslo(e,L) mengisi list of list L dengan elemen e sebagai elemen pertama jika e tidak ada di dalam list of list L"""
    return e + L


def Konsli(L: List[List], e: List) -> List[List]:
    """Konsli(L,e) mengisi list of list L dengan elemen e sebagai elemen terakhir jika e tidak ada di dalam list of list L"""
    return L + e


def FirstList(S: List[List]) -> list:
    """FirstList(L) mengembalikan elemen pertama list of list"""
    return S[0]


def TailList(S: List[List]) -> list:
    """{TailList(S) Menghasilkan  "sisa" list of list S  tanpa elemen pertama list  S"""
    return S[1:]


def HeadList(S: List[List]) -> list:
    """{HeadList(S) Menghasilkan  "sisa" list of list S  tanpa elemen terakhir list  S"""
    return S[:-1]


def LastList(S: List[List]) -> list:
    """LastList(L) mengembalikan elemen terakhir list of list"""
    return S[-1]


def IsEqS(S1: List[List], S2: List[List]) -> bool:
    """IsEqS(S1,S2) mengembalikan True jika S1 dan S2 sama"""
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


def IsMemberS(A: any, S: List[List]) -> bool:
    """IsMember(A,L) mengembalikan True jika A adalah anggota elemen list of list L"""
    if IsEmpty(S):
        return False
    if IsAtom(FirstList(S)):
        return A == FirstList(S)
    if IsList(FirstList(S)):
        return IsMember(A, FirstList(S)) or IsMemberS(A, TailList(S))


def IsMemberLS(L, S):
    """true jika L adalah anggota S"""
    if IsEmpty(L) and IsEmpty(S):
        return True
    if not IsEmpty(L) and IsEmpty(S):
        return False
    if IsEmpty(L) and not IsEmpty(S):
        return False
    if IsAtom(FirstList(S)):
        return IsMemberLS(L, TailList(S))
    if IsEqS(L, FirstList(S)):
        return True
    return IsMemberLS(L, TailList(S))


a = [1, [2, 3]]

print(f"IsEmpty([[]]) = {IsEmpty([[]])}")
print(f"IsAtom(firstList(a)) = {IsAtom((FirstList(a)))}")
print(f"IsList(LastList(a)) = {IsList(LastList(a))}")
print(f"Konslo([4],[2,[6,9]]) = {Konslo([4], [2, [6, 9]])}")
print(f"Konsli([2,[6,9]],[4]) = {Konsli([2, [6, 9]], [4])}")
print(f"IsEqS([1,[2,3]],[1,[2,3]]) = {IsEqS([1, [2, 3]], [1, [2, 3]])}")
print(f"IsMemberS([1,[[2,3],1,[6,9]]) = {IsMemberS(1, ([1,[2,3],1,[6,9]]))}")
print(f"IsMemberS([2,[1,[2,3]]) = {IsMemberS(2, [1, [2, 3]])}")
print(f"IsMemberLS([6,9],[4,[6,9]]) = {IsMemberLS([6, 9], [4, [6, 9]])}")
print(f"IsMemberLS([9,9],[4,[6,9]]) = {IsMemberLS([9, 9], [4, [6, 9]])}")
