# Latihan Ekspresi Dasar

"""
1. hitungKelilingPersegiPanjang
Definisi dan Spesifikasi:
    hitungKelilingPersegiPanjang : real, real → real
    {hitungKelilingPersegiPanjang(p, l) adalah fungsi yang menghitung keliling persegi panjang dengan panjang p dan lebar l }
Realisasi Spesifikasi:
"""


def hitungKelilingPersegiPanjang(p: float, l: float) -> float:
    return 2 * (p + l)


"""
2. hitungVolumeKubus
Definisi dan Spesifikasi:
    hitungVolumeKubus : real → real
    {hitungVolumeKubus(s) adalah fungsi yang menghitung volume kubus dengan panjang sisi s }
Realisasi Spesifikasi:
"""


def hitungVolumeKubus(s: float) -> float:
    return s**3


"""
3. hitungRataRata
Definisi dan Spesifikasi:
    hitungRataRata : 8 real → real
    {hitungRataRata(a, b, c, d, w1, w2, w3, w4) adalah fungsi yang menghitung rata-rata dari 4 buah nilai a, b, c, d dengan bobot w1, w2, w3, dan w4 }
Realisasi Spesifikasi:
"""


def hitungRataRata(
    a: float, b: float, c: float, d: float, w1: float, w2: float, w3: float, w4: float
) -> float:
    return (a * w1 + b * w2 + c * w3 + d * w4) / (w1 + w2 + w3 + w4)


"""
4. Mencari nilai tengah dari tiga bilangan
Definisi dan Spesifikasi:
nilaiTengah : real, real, real → real
{nilaiTengah(x, y, z) adalah fungsi yang mencari nilai tengah dari tiga bilangan x, y, z }
Realisasi Spesifikasi:
"""


def max2(a: int, b: int) -> int:
    return (a + b + abs(a - b)) // 2


def min2(a: int, b: int) -> int:
    return (a + b - abs(a - b)) // 2


def max3(a: int, b: int, c: int) -> int:
    return max2(max2(a, b), c)


def min3(a: int, b: int, c: int) -> int:
    return min2(min2(a, b), c)


def nilaiTengahGW(x: int, y: int, z: int) -> int:
    return sorted([x, y, z])[1]


def nilaiTengah(x: int, y: int, z: int) -> int:
    return x + y + z - min3(x, y, z) - max3(x, y, z)


"""
5. kecepatanRataRata
Definisi dan Spesifikasi:
    kecepatanRataRata : real, real, real, real → real
    {kecepatanRataRata(jarakTempuh1, waktuTempuh1, jarakTempuh2, waktuTempuh2) adalah fungsi yang menghitung kecepatan rata-rata dari dua perjalanan }
Realisasi Spesifikasi:
"""


def hitungCepat(x: int, y: int) -> int:
    return x / y


def kecRataAmeng(
    jaraktempuh1: int, waktutempuh1: int, jaraktempuh2: int, waktutempuh2: int
) -> int:
    return (
        hitungCepat(jaraktempuh1, waktutempuh1)
        + hitungCepat(jaraktempuh2, waktutempuh2)
    ) / 2


def kecepatanRataRata(
    jarakTempuh1: float, waktuTempuh1: float, jarakTempuh2: float, waktuTempuh2: float
) -> float:
    total_jarak = jarakTempuh1 + jarakTempuh2
    total_waktu = waktuTempuh1 + waktuTempuh2
    return total_jarak / total_waktu


"""
6. jumlahDigit
Definisi dan Spesifikasi:
    jumlahDigit : integer, integer, integer → integer
    {jumlahDigit(angka1, angka2, angka3) adalah fungsi yang menghitung jumlah digit dari tiga angka }
Realisasi Spesifikasi:
"""


def jumlahDigitGampang(angka1: int, angka2: int, angka3: int) -> int:
    return len(str(angka1)) + len(str(angka2)) + len(str(angka3))


def jumlahDigit(angka1: int, angka2: int, angka3: int) -> int:
    from math import log10

    return int(log10(angka1) + 1) + int(log10(angka2) + 1) + int(log10(angka3) + 1)


"""
7. volumeBola
Definisi dan Spesifikasi:
    volumeBola : real, real, real → real
    {volumeBola(jariJari1, jariJari2, jariJari3) adalah fungsi yang menghitung volume tiga bola dengan jari-jari yang berbeda }
Realisasi Spesifikasi:
"""


def volumeBola(jariJari1, jariJari2, jariJari3):
    from math import pi

    return (4 / 3) * pi * (jariJari1**3 + jariJari2**3 + jariJari3**3)


"""
8. jumlahKombinasi
Definisi dan Spesifikasi:
    jumlahKombinasi : integer, integer → integer
    {jumlahKombinasi(n, r) adalah fungsi yang menghitung jumlah kombinasi dari n dan r }
Realisasi Spesifikasi:
"""


def jumlahKombinasi(n, r):
    from math import factorial

    return factorial(n) // (factorial(r) * factorial(n - r))


print(
    f"""\
Keliling persegi panjang (p=5, l=3): {hitungKelilingPersegiPanjang(5, 3)} -> 16

Volume kubus (s=4): {hitungVolumeKubus(4)} -> 64

Rata-rata bobot (a=80, b=90, c=70, d=85, w1=0.25, w2=0.25, w3=0.25, w4=0.25) : {hitungRataRata(80, 90, 70, 85, 0.25, 0.25, 0.25, 0.25)} -> 81.25

Nilai tengah dari (x=5, y=7, z=3): {nilaiTengah(5, 7, 3)} -> 5

Kecepatan rata-rata (jarakTempuh1=120, waktuTempuh1=2, jarakTempuh2=180, waktuTempuh2=3): {kecRataAmeng(120, 2, 180, 3)} -> 60

Jumlah digit dari angka (angka1=123, angka2=4567, angka3=89): {jumlahDigit(123, 4567, 89)} ->  9

Volume bola dengan jari-jari (jariJari1=3, jariJari2=4, jariJari3=5): {volumeBola(3, 4, 5)}

Jumlah kombinasi (n=5, r=3): {jumlahKombinasi(5, 3)} -> 10
"""
)
