# Nama : Muchamad Yuda Tri Ananda
# Tanggal : 12/3/2024


from typing import List


def FirstElmt(L):
    return L[0]


def LastElmt(L):
    return L[-1]


def Head(L):
    return L[:-1]


def Tail(L: List) -> List:
    """Tail(L): Menghasilkan list tanpa elemen pertama list L, mungkin kosong"""
    return L[1:]


def Konso(e, L):
    return [e] + L


def isEmpty(L):
    return L == []


def dimensi(L):  # atau NbElmt()
    if isEmpty(L):
        return 0
    else:
        return 1 + dimensi(Tail(L))


def CompareDmg(dmgS, dmgM, skorS=0, skorM=0):
    if dmgS > dmgM:
        return skorS + 1
    if dmgS < dmgM:
        return skorM + 1


def DuelSihir(S, M, skorS=0, skorM=0):
    if isEmpty(S):
        if skorS > skorM:
            return "Snape Menang"
        if skorS < skorM:
            return "McGonagall Menang"
        return "Keduanya Seri"
    if FirstElmt(S) == FirstElmt(M):
        return DuelSihir(Tail(S), Tail(M), skorS + 1, skorM + 1)
    if FirstElmt(S) > FirstElmt(M):
        return DuelSihir(Tail(S), Tail(M), skorS + 1, skorM)
    if FirstElmt(S) < FirstElmt(M):
        return DuelSihir(Tail(S), Tail(M), skorS, skorM + 1)


# Tulis algoritma di sini


# PRINT
# print(eval(input()))
print(DuelSihir([10, 20], [15, 10]))


# Selamat Menikmati
