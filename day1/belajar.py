# NAMA FILE : Praktikum 1.py
# Deskropsi : Menghitung nilai pangkat
# Taggal : 27 Agustus 2024
# Pemuat : myudakk - NIM


# CONTOH =>>
def kuadrat(x: int) -> int:
    return x * x


def kubik(x: int) -> int:
    return x * kuadrat(x)


def duaKali(x: int) -> int:
    return x + x


def max2(x: int, y: int) -> int:
    return ((x + y) + abs(x - y)) // 2


def max3(x: int, y: int, z: int) -> int:
    return max2(max2(x, y), z)


def is_origin(x: int, y: int) -> bool:
    return x == 0 and y == 0


#  LATIHAN ==>>


def mean_olympikGue(w: int, x: int, y: int, z: int) -> float:
    a = sorted([w, x, y, z])
    return (a[1] + a[2]) / 2


# Contoh-4 Ekspresi numeric: Mean Olympique (MO)
def mean_olympique(data: list) -> float:
    sorted_data = sorted(data)
    n = len(sorted_data)

    return (
        (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        if n % 2 == 0
        else sorted_data[n // 2]
    )


# Contoh-5 Ekspresi Boolean: POSITIF
def isPositive(x: int) -> bool:
    return x > 0


# Contoh-6 Ekspresi Boolean: APAKAH HURUF A
def isHurufA(x: str) -> bool:
    return x == "A"


def isValid(x: int) -> bool:
    return x < 5 or x > 500


# Ekspresi numeric: Least Square (Jarak 2 Titik)
