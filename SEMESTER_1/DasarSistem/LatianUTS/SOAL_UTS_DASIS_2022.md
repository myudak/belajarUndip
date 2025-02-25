# UJIAN TENGAH SEMESTER GASAL 2022/2023

- Mata Kuliah : Dasar Sistem
- Kelas : A/B/C/D/E
- Pengampu :

  - Rismiyati, B.Eng, M.Cs
  - Muharnmad Malik Hakim S.T., M.T.I

- Departemen : Ilmu Komputer/Informatika
- Program Studi : Informatika
- Hari/Tanggal : Rabu/ 12 Oktober 2023
- Jam/Ruang : 09.20 - 11.00 WIB (100 menit)/
- Sifat Ujian : Buku Tertutup

# SOAL URAIAN

## 1. {Bobot: 25}

a. Hitunglah nilai decimal, biner, octal, atau hexa decimal untuk melengkapi tabel{12} berikut :

| Decimal | Biner   | Octal | HexaDecimal |
| ------- | ------- | ----- | ----------- |
| 54.25   | ...     | ...   | ..          |
| ...     | 1101011 | ..    | ..          |

b. Hitunglah
aritmatika berikut dalam aritmatika bilangan biner. Rubah masih - masing angka ke bilangan 4 bit {9}

    1.  3+4
    2.  3-4

c. Diketahui tabel bilangan ASCII dan kata dalam biner sebagai berikut, bagaimanakah bunyi kaya tersebut!

1001001 1101110 1100110 1101111 1110010

1101101 1100001 1110100 1101001 1101111

1101110

## 2. {Bobot: 25}
a. Dengan menggunakan aljabar Boolean, buktikan bahwa

Tuliskan dengan jelas teorema mana yang anda pakai untuk membuktikan kedua Eptersi tersebut! {13}

---

b. Gambarkan tabel kebenaran dari fungsi berikut dan nyatakan fungsi F dalam bentuk sum of minterm! 





## 3. {30}

7 segment display digunakan untuk menampilkan bilangan dari 0 sampai 9. Output sistem tersebut adalah digit yang direpresentasikan oleh input. Output untuk input yang tidak valid (selain nilai 0-9) adalah lambing - (led yang tengah menyala).

Desainlah rangkaian kombinasional tersebut dengan mengikuti langkah-langkah pembuatan rangkaian kombinasional. Untuk karnaugh map dan penyederhanaan, lakukan hanya untuk output g. {301}



## 4 {20}

a. Sebuah Multiplexer sebagaimana ditunjukkan pada gambar, jika Data bernilai 10101110, dan select line bernilai 011, tentukan berapa nilai Y.Jelaskan dengan cara bagaimana anda mendapatkan jawaban tersebut! {10}

b. Rancang dekoder 4-ke-16 dengan Enable menggunakan lima dekoder 2-ke-4 dengan Enable yang ditunjukkan pada Gambar {10}

# JAWABAN URAIAN


## 3. {30}

7 segment display digunakan untuk menampilkan bilangan dari 0 sampai 9. Output sistem tersebut adalah digit yang direpresentasikan oleh input. Output untuk input yang tidak valid (selain nilai 0-9) adalah lambang - (led yang tengah menyala).

Desainlah rangkaian kombinasional tersebut dengan mengikuti langkah-langkah pembuatan rangkaian kombinasional. Untuk karnaugh map dan penyederhanaan, lakukan hanya untuk output g. {301}

---

### Steps {dari ppt dasis}

1. Determine required number of inputs and outputs from the specifications.
2. Derive the truth table for each of the outputs based on their relationships to the input.
3. Simplify the boolean expression for each output. Use Karnaugh Maps or Boolean algebra.
4. Draw a logic diagram that represents the simplified Boolean expression. Verify the design by analysing or simulating the circuit.


#### 1. Determine required number of inputs and outputs from the specifications.

- **Input:**
  - Karena display akan menampilkan angka 0 hingga 9, kita membutuhkan 4 input (representasi biner dari angka 0–9), yang dapat dilambangkan sebagai `A`, `B`, `C`, dan `D`, di mana:
    - `A` = Most Significant Bit (MSB)
    - `D` = Least Significant Bit (LSB)
  - Ini memberikan 16 kemungkinan kombinasi (0000 hingga 1111).

- **Output:**
  - 7-segment display memiliki 7 output (`a`, `b`, `c`, `d`, `e`, `f`, `g`) yang mengendalikan setiap segmen display.
  - Kita diminta untuk menyederhanakan dan mendesain logika hanya untuk output `g` (segmen horizontal tengah).

#### 2. Derive the truth table for each of the outputs based on their relationships to the input.

Berdasarkan kombinasi input (0–15), kita dapat menentukan segmen mana yang menyala untuk setiap angka. Untuk input yang tidak valid (nilai 10–15), display akan menampilkan "-" strip, yang led yang tengah menyala.

Untuk segmen tengah `g`, tabel kebenaran untuk input biner (`A, B, C, D`) adalah sebagai berikut:

| A  | B  | C  | D  | Angka | g (segmen) |
|----|----|----|----|-------|------------|
| 0  | 0  | 0  | 0  |   0   |      0     |
| 0  | 0  | 0  | 1  |   1   |      0     |
| 0  | 0  | 1  | 0  |   2   |      1     |
| 0  | 0  | 1  | 1  |   3   |      1     |
| 0  | 1  | 0  | 0  |   4   |      1     |
| 0  | 1  | 0  | 1  |   5   |      1     |
| 0  | 1  | 1  | 0  |   6   |      1     |
| 0  | 1  | 1  | 1  |   7   |      0     |
| 1  | 0  | 0  | 0  |   8   |      1     |
| 1  | 0  | 0  | 1  |   9   |      1     |
| 1  | 0  | 1  | 0  |   -   |      1     |
| 1  | 0  | 1  | 1  |   -   |      1     |
| 1  | 1  | 0  | 0  |   -   |      1     |
| 1  | 1  | 0  | 1  |   -   |      1     |
| 1  | 1  | 1  | 0  |   -   |      1     |
| 1  | 1  | 1  | 1  |   -   |      1     |

- Segmen `f` menyala untuk input yang sesuai dengan angka: 0, 2, 3, 4, 5, 6, 8, 9, dan untuk semua nilai yang tidak valid (menampilkan "E").

#### 3. Simplify the boolean expression for each output. Use Karnaugh Maps or Boolean algebra.

$$
g(A, B, C, D) = \Sigma_{m}(2, 3,4,5, 6, 8,9)
$$

#### 4. Draw a logic diagram that represents the simplified Boolean expression. Verify the design by analysing or simulating the circuit.
asd


## 4 {20}

a. Sebuah Multiplexer sebagaimana ditunjukkan pada gambar, jika Data bernilai 10101110, dan select line bernilai 011, tentukan berapa nilai Y.Jelaskan dengan cara bagaimana anda mendapatkan jawaban tersebut! {10}

jawaban == 1

---

b. Rancang dekoder 4-ke-16 dengan Enable menggunakan lima dekoder 2-ke-4 dengan Enable yang ditunjukkan pada Gambar {10}



---

Selamat mengerjakan dan semoga sukses. ~when the going gets tough, the tough gets going~ =\)


