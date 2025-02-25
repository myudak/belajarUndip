[github.com/myudak/belajarUndip/main/DasarSistem/LatianUTS/SOAL_UTS_DASIS_2023.md](https://github.com/myudak/belajarUndip/blob/main/DasarSistem/LatianUTS/SOAL_UTS_DASIS_2023.md)
# UJIAN TENGAH SEMESTER DASAR SISTEM 2023/2024

- Mata Kuliah : Dasar Sistem
- Kelas : A/B/C/D/E
- Pengampu :

  - Rismiyati, B.Eng, M.Cs
  - Muharnmad Malik Hakim S.T., M.T.I
  - Dr. Sutikno, S.T, M.Cs

- Departemen/Program Studi : Ilmu Komputer / Informatika
- Hari/Tanggal : Jumat, 13 Oktober 2023
- Jam/Ruang : 13:30 - 15:10 WIB (100 menit)/ E101, E102, E103, A103
- Sifat Ujian : Buku Tertutup

# SOAL URAIAN

## 1. [CPMK07-1(1-2) bobot 25%]

a. Hitunglah nilai decimal, biner, octal, atau hexa decimal untuk melengkapi tabel{15} berikut :

| Decimal | Biner   | Octal | HexaDecimal |
| ------- | ------- | ----- | ----------- |
| 54.25   | ...     | ...   | ..          |
| ...     | 1101011 | ..    | ..          |

b. Hitunglah hasil dari operasi aritmatika berikut dalam aritmatika bilangan biner. Rubah masih-masing angka ke bilangan 4 bit {10}

1. 5+2
2. 5-2

## 2. [CPMK07-1(3) bobot 25%] Deskripsi soal

a. Dengan menggunakan aljabar Boolean, buktikan bahwa

$$
\overline{W}\\overline{X}\,\overline{Z} + \overline{W}X\overline{Y} + \overline{W}XY + W\overline{Y}\,\overline{Z}
$$

Tuliskan dengan jelas teorema mana yang anda pakai untuk membuktikan kedua
Eptersi tersebut! {15}

b. Gambarkan tabel kebenaran dari fungsi berikut dan nyatakan fungsi F dalam
bentuk sum of minterm!

$$
F(W,X,Y,Z)= WX+\overline{W}\,\overline{X}\,\overline{Z}\,+\overline{W}\,X\,Y
$$

{10}

## 3. [CPMK07-1(4) bobot 30%]

7 segment display digunakan untuk menampilkan bilangan dari 0 sampai 9. Output sistem tersebut adalah digit yang direpresentasikan oleh input. Output untuk input yang tidak valid (selain nilai 0-9) adalah menampilkan huruf E untuk menyatakan error.

![](https://github.com/myudak/myudak/blob/9ea56c3312d475a4ef3efb4ef062ead5005ba2e0/public/Screenshot%202024-10-09%20034853.png?raw=true)

Desainlah rangkaian kombinasional tersebut **dengan mengikuti langkah-langkah pembuatan rangkaian kombinasional**. <u>Untuk karnaugh map dan penyederhanaan serta penggambaran rangkaian, lakukan hanya untuk output f. {30}</u>

## 4. [CPMK07-1(4) bobot 20%]

a. Sebuah Multiplexer 8 ke 1 sebagaimana ditunjukkan pada gambar, jika Data bernilai 10101010, dan select line bernilai 101, tentukan berapa nilai Y. Jelaskan bagaimana anda mendapatkan jawaban tersebut! {10}

b. dekoder 2-ke-4 dengan Enable. Jika Enable aktif dan A bernilai 0, B bernilai 1, berapakah nilai keluaran Y1 Y2 Y3 Y4 {10}

![](https://github.com/myudak/myudak/blob/d18e4889d2abb0013ff5dcb723444a0a4139a42b/public/Screenshot%202024-10-09%20030627.png?raw=true)

# JAWABAN URAIAN

## 1. [CPMK07-1(1-2) bobot 25%]
a. Hitunglah nilai decimal, biner, octal, atau hexa decimal untuk melengkapi tabel{15} berikut : 
| Decimal | Biner     | Octal | HexaDecimal |
| ------- | --------- | ----- | ----------- |
| 54.25   | 110110.01 | 66.2  | 36.4        |
| 107     | 1101011   | 153   | 6B          |

 
---
 
### $54.25_{10} = 110110.01_2$
- 54 ÷ 2 = 27 sisa 0
- 27 ÷ 2 = 13 sisa 1
- 13 ÷ 2 = 6 sisa 1
- 6 ÷ 2 = 3 sisa 0
- 3 ÷ 2 = 1 sisa 1
- 1 ÷ 2 = 0 sisa 1

$$
54_{10} = 110110_2
$$

  - 0.25 × 2 = 0.5 → ambil 0
  - 0.5 × 2 = 1.0 → ambil 1

$$
0.25_{10} = 01_2
$$
 
---
 
### $54.25_{10} = 66.2_8$
- 54 ÷ 8 = 6 sisa 6

$$
54_{10} = 66_8
$$
- 0.25 × 8 = 2.0 → ambil 2

$$
0.25_{10} = 2_8
$$
 
---
 
### $54.25_{10} = 36.4_{16}$
- 54 ÷ 16 = 3 sisa 6

$$
54_{10} = 36_{16}
$$
- 0.25 × 16 = 4.0 → ambil 4

$$ 
0.25_{10} = 4_{16}
$$
 
---
 
### $1101011_{2} = 107_{10}$

$$
(1 \times 2^6) + (1 \times 2^5) + (0 \times 2^4) + (1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (1 \times 2^0) 
$$

$$
= 64 + 32 + 8 + 2 + 1 = 107_{10}
$$

---

### $1101011_2 = 153_8$
1101011

= 1 101 011

= 1 5 3

= 153

---

### $1101011_2 = 6B_{16}$
1101011

= 110 1011

= 6 B

= 6B

---

b. Hitunglah hasil dari operasi aritmatika berikut dalam aritmatika bilangan biner. Rubah masih-masing angka ke bilangan 4 bit {10}

1. 5+2
2. 5-2
---
1. **5 + 2** dalam biner 4 bit:

- 5 dalam biner: `0101`
- 2 dalam biner: `0010`
dijumlah  = 0111

2. **5 - 2** dalam biner 4 bit:
- 5 dalam biner: `0101`
- 2 dalam biner: `0010`
dikurang = 0011

Jadi:
- 5 + 2 = `0111` (7 dalam desimal)
- 5 - 2 = `0011` (3 dalam desimal)

## 2. [CPMK07-1(3) bobot 25%] Deskripsi soal

a. Dengan menggunakan aljabar Boolean, buktikan bahwa

$$
\overline{W}\\overline{X}\,\overline{Z} + \overline{W}X\overline{Y} + \overline{W}XY + W\overline{Y}\,\overline{Z}
$$

Tuliskan dengan jelas teorema mana yang anda pakai untuk membuktikan kedua
Eptersi tersebut! {15}


mager ajg



$\overline{W}\,\overline{X}\,\overline{Z}\left(Y+\overline{Y}\right)+\overline{W}X\overline{Y}\left(Z+\overline{Z}\right)+\overline{W}XY\left(Z+\overline{Z}\right)+W\overline{Y}\,\overline{Z}\left(X+\overline{X}\right)$

---

b. Gambarkan tabel kebenaran dari fungsi berikut dan nyatakan fungsi F dalam
bentuk sum of minterm!

$$
F(W,X,Y,Z)= WX+\overline{W}\,\overline{X}\,\overline{Z}\,+\overline{W}\,X\,Y
$$

{10}

---

Truth Table
| W | X | Y | Z | Output |
|---|---|---|---|--------|
| 0 | 0 | 0 | 0 | T      |
| 0 | 0 | 0 | 1 | F      |
| 0 | 0 | 1 | 0 | T      |
| 0 | 0 | 1 | 1 | F      |
| 0 | 1 | 0 | 0 | F      |
| 0 | 1 | 0 | 1 | F      |
| 0 | 1 | 1 | 0 | T      |
| 0 | 1 | 1 | 1 | T      |
| 1 | 0 | 0 | 0 | F      |
| 1 | 0 | 0 | 1 | F      |
| 1 | 0 | 1 | 0 | F      |
| 1 | 0 | 1 | 1 | F      |
| 1 | 1 | 0 | 0 | T      |
| 1 | 1 | 0 | 1 | T      |
| 1 | 1 | 1 | 0 | T      |
| 1 | 1 | 1 | 1 | T      |

![](https://github.com/myudak/myudak/blob/bb267f7c6a6a4c5dd8b06f0241051d7ab070eab2/public/Screenshot%202024-10-09%20202015.png?raw=true)

## 3. [CPMK07-1(4) bobot 30%]

Desainlah rangkaian kombinasional tersebut **dengan mengikuti langkah-langkah pembuatan rangkaian kombinasional**. <u>Untuk karnaugh map dan penyederhanaan serta penggambaran rangkaian, lakukan hanya untuk output f. {30}</u>

### Steps {dari ppt dasis}

1. Determine required number of inputs and outputs from the specifications.
2. Derive the truth table for each of the outputs based on their relationships to the input.
3. Simplify the boolean expression for each output. Use Karnaugh Maps or Boolean algebra.
4. Draw a logic diagram that represents the simplified Boolean expression. Verify the design by analysing or simulating the circuit.

---

#### 1. Determine required number of inputs and outputs from the specifications.

- **Input:**
  - Karena display akan menampilkan angka 0 hingga 9, kita membutuhkan 4 input (representasi biner dari angka 0–9), yang dapat dilambangkan sebagai `A`, `B`, `C`, dan `D`, di mana:
    - `A` = Most Significant Bit (MSB)
    - `D` = Least Significant Bit (LSB)
  - Ini memberikan 16 kemungkinan kombinasi (0000 hingga 1111).

- **Output:**
  - 7-segment display memiliki 7 output (`a`, `b`, `c`, `d`, `e`, `f`, `g`) yang mengendalikan setiap segmen display.
  - Kita diminta untuk menyederhanakan dan mendesain logika hanya untuk output `f` (segmen horizontal tengah).

#### 2. Derive the truth table for each of the outputs based on their relationships to the input.

Berdasarkan kombinasi input (0–15), kita dapat menentukan segmen mana yang menyala untuk setiap angka. Untuk input yang tidak valid (nilai 10–15), display akan menampilkan "E", yang menyalakan segmen tertentu pada 7-segment display.

Untuk segmen tengah `f`, tabel kebenaran untuk input biner (`A, B, C, D`) adalah sebagai berikut:

| A  | B  | C  | D  | Angka | f (segmen) |
|----|----|----|----|-------|------------|
| 0  | 0  | 0  | 0  |   0   |      1     |
| 0  | 0  | 0  | 1  |   1   |      0     |
| 0  | 0  | 1  | 0  |   2   |      0     |
| 0  | 0  | 1  | 1  |   3   |      0     |
| 0  | 1  | 0  | 0  |   4   |      1     |
| 0  | 1  | 0  | 1  |   5   |      1     |
| 0  | 1  | 1  | 0  |   6   |      1     |
| 0  | 1  | 1  | 1  |   7   |      0     |
| 1  | 0  | 0  | 0  |   8   |      1     |
| 1  | 0  | 0  | 1  |   9   |      1     |
| 1  | 0  | 1  | 0  |   E   |      1     |
| 1  | 0  | 1  | 1  |   E   |      1     |
| 1  | 1  | 0  | 0  |   E   |      1     |
| 1  | 1  | 0  | 1  |   E   |      1     |
| 1  | 1  | 1  | 0  |   E   |      1     |
| 1  | 1  | 1  | 1  |   E   |      1     |

- Segmen `f` menyala untuk input yang sesuai dengan angka: 0, 2, 3, 4, 5, 6, 8, 9, dan untuk semua nilai yang tidak valid (menampilkan "E").

#### 3. Simplify the boolean expression for each output. Use Karnaugh Maps or Boolean algebra.

$$
f(A, B, C, D) = \Sigma_{m}(0, 4,5, 6, 8,9)
$$

![](https://github.com/myudak/myudak/blob/491f66f9ed8c754427272c95e1845faea9f88ded/public/Screenshot%202024-10-09%20155822.png?raw=true)

#### 4. Draw a logic diagram that represents the simplified Boolean expression. Verify the design by analysing or simulating the circuit.

$$
\overline{A}\,B\,\overline{C}\,+\,\overline{B}\,\overline{C}\,\overline{D}\,+A\,\overline{B}\,\overline{C}\,+\,\overline{A}\,B\,\overline{D}
$$

![](https://github.com/myudak/myudak/blob/5332b66b523b5f8f0e255646a5bc71f2c5b0b4d9/public/Main%20(28).png?raw=true)
https://circuitverse.org/users/255105/projects/soal_uts_dasis_20234a

## 4. [CPMK07-1(4) bobot 20%]

a. Sebuah Multiplexer 8 ke 1 sebagaimana ditunjukkan pada gambar, jika Data bernilai 10101010, dan select line bernilai 101, tentukan berapa nilai Y. Jelaskan bagaimana anda mendapatkan jawaban tersebut! {10}

Data inputs: 10101010, Artinya:

- A0 = 1
- A1 = 0
- A2 = 1
- A3 = 0
- A4 = 1
- A5 = 0
- A6 = 1
- A7 = 0

Select lines: 101, yang dalam binary yang sama dengan 5 dalam decimal.

Dalam multiplexer 8:1, baris select yang digunakan untuk memilih satu dari 8 input data untuk menerima output Y. Baris select 101 (binary) sesuai dengan A5, sehingga nilai Y adalah A5.

Dari data input, A5 = 0.

**Jadi, value dari Y adalah 0.**


![](<https://github.com/myudak/myudak/blob/8b646aedfa5d44a0e55b7e6e6555a4cb442d5149/public/Main%20(26).png?raw=true>)
https://circuitverse.org/users/255105/projects/soal_uts_dasis_20234a

b. dekoder 2-ke-4 dengan Enable. Jika Enable aktif dan A bernilai 0, B bernilai 1, berapakah nilai keluaran Y1 Y2 Y3 Y4 {10}

Enbale (E) aktif, maka dekoder akan berfungsi.
Inputs:

- A = 0
- B = 1

Untuk dekoder 2-ke-4:

A = 0 dan B = 1 sesuai dengan output kedua yang aktif, yaitu Y1.
Jadi output akan adalah:

- Y0 = 0
- Y1 = 1
- Y2 = 0
- Y3 = 0


![](<https://github.com/myudak/myudak/blob/994b3b90f09af47963d4c3f653288b913198af43/public/Main%20(24).png?raw=true>)
https://circuitverse.org/users/255105/projects/soal_uts_dasis_20234a
