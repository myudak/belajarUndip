# 3.1. Ekspresi rekursif: Factorial (Versi 1)

"""
Menghitung faktorial dari angka yang diberikan.

DEFINISI DAN SPESIFIKASI
    fac : integer > 0 → integer
        { fac(n) = n! sesuai dengan definisi rekursif factorial, versi 1 }

REALISASI
"""


def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


"""
APPLIKASI
"""

print(fac(1))

# 3.2. Ekspresi rekursif: Factorial (Versi 2)

"""
Menghitung faktorial dari angka yang diberikan.

DEFINISI DAN SPESIFIKASI
    fac : integer > 0 → integer
        { fac(n) = n! sesuai dengan definisi rekursif factorial, versi 1 }

REALISASI
"""


def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


"""
APPLIKASI
"""

print(fac(1))
