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
\overline{W}\,\overline{X}\,\overline{Z} + \overline{W}X\overline{Y} + \overline{W}XY + W\overline{Y}\,\overline{Z}
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
 
### $$ 54.25_{10} = 110110.01_2 $$
- 54 ÷ 2 = 27 sisa 0
- 27 ÷ 2 = 13 sisa 1
- 13 ÷ 2 = 6 sisa 1
- 6 ÷ 2 = 3 sisa 0
- 3 ÷ 2 = 1 sisa 1
- 1 ÷ 2 = 0 sisa 1
$$ 54_{10} = 110110_2 $$
  - 0.25 × 2 = 0.5 → ambil 0
  - 0.5 × 2 = 1.0 → ambil 1
$$0.25_{10} = 01_2 $$
 
---
 
### $$ 54.25_{10} = 66.2_8 $$
- 54 ÷ 8 = 6 sisa 6
$$ 54_{10} = 66_8 $$
- 0.25 × 8 = 2.0 → ambil 2
$$ 0.25_{10} = 2_8 $$
 
---
 
### $$ 54.25_{10} = 36.4_{16} $$
- 54 ÷ 16 = 3 sisa 6
$$ 54_{10} = 36_{16} $$
- 0.25 × 16 = 4.0 → ambil 4
$$0.25_{10} = 4_{16} $$
 
---
 
### $$ 1101011_{2} = 107_{10} $$

$$
(1 \times 2^6) + (1 \times 2^5) + (0 \times 2^4) + (1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (1 \times 2^0) 
$$
$$
= 64 + 32 + 8 + 2 + 1 = 107_{10}
$$

---

### $$ 1101011_2 = 153_8 $$
1101011

= 1 101 011

= 1 5 3

= 153

---

### $$ 1101011_2 = 6B_{16} $$
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
## 4. [CPMK07-1(4) bobot 20%]

a. Sebuah Multiplexer 8 ke 1 sebagaimana ditunjukkan pada gambar, jika Data bernilai 10101010, dan select line bernilai 101, tentukan berapa nilai Y. Jelaskan bagaimana anda mendapatkan jawaban tersebut! {10}

Data inputs: 10101010, which means:

- A7 = 1
- A6 = 0
- A5 = 1
- A4 = 0
- A3 = 1
- A2 = 0
- A1 = 1
- A0 = 0

Select lines: 101, which in binary is equivalent to 5 in decimal.

In a multiplexer 8:1, the select lines choose one of the eight data inputs to pass through to the output Y. The select lines 101 (binary) correspond to A5, so the value of Y will be A5.

From the data inputs, A5 = 1.

**Thus, the value of Y is 1.**
![](<https://github.com/myudak/myudak/blob/e29003f9e5650a36f4ecf7cb22a70e352a0533db/public/Main%20(23).png?raw=true>)
https://circuitverse.org/users/255105/projects/soal_uts_dasis_20234a

b. dekoder 2-ke-4 dengan Enable. Jika Enable aktif dan A bernilai 0, B bernilai 1, berapakah nilai keluaran Y1 Y2 Y3 Y4 {10}

Enable (E) is active, so the decoder will function.
Inputs:

- A = 0
- B = 1

For a 2-to-4 decoder:

A = 0 and B = 1 correspond to the second output line being active, which is Y1.
Thus, the output will be:

- Y0 = 0
- Y1 = 1
- Y2 = 0
- Y3 = 0

![](<https://github.com/myudak/myudak/blob/994b3b90f09af47963d4c3f653288b913198af43/public/Main%20(24).png?raw=true>)
https://circuitverse.org/users/255105/projects/soal_uts_dasis_20234a
