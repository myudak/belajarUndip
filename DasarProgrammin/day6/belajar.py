"""
# BELAJAR REKURSIP

Ekspresi rekursif adalah sebuah ekspresi yang di dalam definisinya menngandung
terminology dirinya sendiri.
"""

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

## LATIAN

# 1. Operasi aritmatika pengurangan


def pengurangan(a, b):
    if b == 0:
        return a
    else:
        return pengurangan(a - 1, b - 1)


print(f"pengurangan(5, 3) = {pengurangan(5, 3)}")

# 2. Operasi aritmatika perkalian


def perkalian(a, b):
    if b == 0:
        return 0
    return a + perkalian(a, b - 1)  # -> 15


print(f"perkalian(5, 3) = {perkalian(5, 3)}")

# 3. Operasi aritmatika pembagian


def pembagian(a, b):
    if b == 0:
        return 0
    return 1 + pembagian(a - b, b - 1)


print(f"pembagian(15, 3) = {pembagian(15, 3)}")

# 5. Operasi aritmatika perpangkatan


def perpangkatan(a, b):
    if b == 0:
        return 1
    return a * perpangkatan(a, b - 1)


print(f"perpangkatan(5, 3) = {perpangkatan(5, 3)}")

"""
6. Menghitung perkalian dengan 3 atau f(n) = 3 \* n
   - f(1) = 3
   - f(n+1) = f(n) = 3
"""


def menghitung_perkalian(n):
    if n == 1:
        return 3
    return 3 + menghitung_perkalian(n - 1)


print(f"menghitung_perkalian(5) = {menghitung_perkalian(5)}")

"""
7. Menghitung deret bilangan integer: 1 + 2 + 3 + 4 + ….
   - S(1) = 1
   - S(2) = 1 + 2
   - S(3) = 1 + 2 + 3
"""


def menghitung_deret_123(n):
    if n == 1:
        return 1
    return n + menghitung_deret_123(n - 1)


print(f"menghitung_deret_123(3) = {menghitung_deret_123(3)}")

"""
8. Menghitung deret aritmatika: 3 + 6 + 9 + 12 + …
   - S(1) = 3
   - S(2) = 3 + 6
   - S(3) = 3 + 6 + 9
"""


def menghitung_deret_aritmatika_369(n):
    if n == 1:
        return 3
    return 3 * (n) + menghitung_deret_aritmatika_369(n - 1)


print(f"menghitung_deret_aritmatika_369(3) = {menghitung_deret_aritmatika_369(3)}")

"""
9. Menghitung deret geometri: 1 + 3 + 9 + 27 + …
   - S(1) = 1
   - S(2) = 1 + 3
   - S(3) = 1 + 3 + 9
"""


def menghitung_deret_geometri_139(n):
    if n == 1:
        return 1
    return 3 ** (n - 1) + menghitung_deret_geometri_139(n - 1)


print(f"menghitung_deret_geometri_139(3) = {menghitung_deret_geometri_139(3)}")

"""
10. Menghitung deret : 1 + 4 + 9 + 16 + …
    - S(1) = 1
    - S(2) = 1 + 4
    - S(3) = 1 + 4 + 9
"""


def menghitung_deret_149(n):
    if n == 1:
        return 1
    return n**2 + menghitung_deret_149(n - 1)


print(f"menghitung_deret_149(3) = {menghitung_deret_149(3)}")
