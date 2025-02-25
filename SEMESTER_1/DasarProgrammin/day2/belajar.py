"""
1. Diberikan masukan berupa waktu yang terdiri atas jam berupa integer[0..24], menit berupa 
integer [0..59], dan detik berupa integer [0..59]. Buatlah sebuah program untuk mengkonversi 
sebuah waktu tersebut ke dalam satuan detik terhitung mulai waktu 00:00:00 pada tanggal 
yang bersangkutan.
"""


def ubahWaktu(j: int, m: int, d: int) -> int:
    if j < 0 or j > 24:
        return "SALAH JAM"
    if m < 0 or m > 59:
        return "SALAH MENIT"
    if d < 0 or d > 59:
        return "SALAH DETIK"
    return j * 60 * 60 + m * 60 + d


print(f"Waktu Detik {ubahWaktu(14, 0, 0)}     ")

"""
2. Sebuah persamaan kuadrat ax2 + bx + c = 0 mempunyai akar-akar berupa x1 dan x2. Buatlah 
program untuk menghitung jumlahan kuadrat dari akar-akar persamaan kuadrat (x1
2 + x2
2
) 
tersebut jika diberikan nilai a, b, dan c. 
"""


def jumlahKuadrat(a: int, b: int, c: int) -> int:
    return (-b / a) ** 2 - 2 * c / a


print(f"Jumlah Kuadrat {jumlahKuadrat(1, 5, 6)}")

"""
3. Seorang mahasiswa berhak mendapat gelar cumlaude jika masa studi tidak lebih dari 4,5 tahun 
dan memiliki nilai IPK minimal 3.50. Buatlah program untuk mengecek apakah seorang 
mahasiswa cumluade berdasarkan masa studi yang dinyatakan dalam bulan dan nilai IPK 
dengan range [0..4].

"""


def cekCumlaude(m: int, i: float) -> bool:
    return m < 4.5 and i >= 3.5


print(f"Mahasiswa Cumlaude {cekCumlaude(3, 3.5)}")

"""
4. Buatlah sebuah program untuk mengecek apakah sebuah tahun merupakan tahun kabisat. 
Sebuah tahun dinyatakan kabisat jika angka tahun tersebut memenuhi salah satu syarat berikut:
◦ Angka tahun habis dibagi 400, atau
◦ Angka tahun habis dibagi 4, tetapi tidak habis dibagi 100.
Contoh: 
Tahun 2000 adalah tahun kabisat
Tahun 1996 adalah tahun kabisat
Tahun 1900 bukan tahun kabisat
"""


def cekKabisat(t: int) -> bool:
    return t % 400 == 0 or (t % 4 == 0 and t % 100 != 0)


print(f"CEK KABISAT 2000 {cekKabisat(2000)}")

"""
Carilah contoh sebuah kasus yang dapat diselesaikan dengan ekspresi fungsional dasar selain 
contoh yang diberikan di tugas ini atau contoh yang ada di Diktat Kuliah.   
"""
