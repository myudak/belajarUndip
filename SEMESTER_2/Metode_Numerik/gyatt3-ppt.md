<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Teknik Interpolasi: Presentasi Singkat

---

# Slide 1: Judul & Pendahuluan

## Teknik Interpolasi
### Panduan untuk Mahasiswa Tingkat Satu

*   **Apa itu Interpolasi?**
    *   Metode memperkirakan nilai fungsi di antara titik data yang diketahui.
    *   "Mengisi celah" data diskrit untuk mendapatkan perkiraan nilai kontinu.
*   **Mengapa Penting?**
    *   Estimasi nilai di antara data yang terukur.
    *   Aproksimasi fungsi kompleks.
    *   Rekonstruksi data (citra, sinyal).
    *   Dasar untuk integrasi numerik.

---

# Slide 2: Konsep Dasar Interpolasi Numerik

## Konsep Dasar

*   **Definisi:** Teknik matematika untuk estimasi nilai tak diketahui di antara data.
*   **Fungsi Interpolasi:**  Biasanya polinomial, spline, dll.
*   **Pertimbangan Penting:**
    *   Efisiensi Komputasi
    *   Stabilitas Numerik (Fenomena Runge)
    *   Akurasi (tergantung metode dan data)
*   **Tujuan Presentasi:** Memahami metode Newton, Lagrange, dan Neville.

---

# Slide 3: Interpolasi Newton Maju (Forward)

## Interpolasi Newton Maju

*   **Kegunaan:** Estimasi nilai dekat *awal* tabel data.
*   **Metode:** Menggunakan *perbedaan maju* (forward differences).
*   **Rumus Utama:** (Tampilkan rumus utama saja, tanpa detail derivasi)

    ```
    P_n(x) = y_0 + sΔy_0 + ... +  \frac{s(s-1)...(s-n+1)}{n!}\Delta^n y_0
    ```
    di mana  $s = \frac{x - x_0}{h}$

*   **Tabel Perbedaan Maju:** (Tampilkan contoh tabel sederhana)

    | $x$    | $y$      | $\Delta y$ | $\Delta^2 y$ | ... |
    | ------ | -------- | ---------- | ----------- | --- |
    | $x_0$  | $y_0$    | $\Delta y_0$ | $\Delta^2 y_0$ | ... |
    | $x_1$  | $y_1$    | $\Delta y_1$ | ...         |     |
    | $x_2$  | $y_2$    | $\Delta y_2$ |             |     |
    | ...    | ...      |            |             |     |

---

# Slide 4: Contoh Soal - Newton Maju

## Contoh Soal Newton Maju

*   **Data:**

    | $x$    | 0     | 1     | 2     | 3     |
    | ------ | ----- | ----- | ----- | ----- |
    | $y$    | 1     | 2     | 5     | 10    |

*   **Soal:** Perkirakan $y$ pada $x = 0.5$.
*   **Hasil:** $y \approx 1.25$ (Tampilkan hasil akhir, langkah perhitungan bisa diringkas atau dihilangkan di slide)

---

# Slide 5: Interpolasi Newton Mundur (Backward)

## Interpolasi Newton Mundur

*   **Kegunaan:** Estimasi nilai dekat *akhir* tabel data.
*   **Metode:** Menggunakan *perbedaan mundur* (backward differences).
*   **Rumus Utama:** (Tampilkan rumus utama saja)
    ```
    P_n(x) = y_n + s\nabla y_n + ... + \frac{s(s+1)...(s+n-1)}{n!}\nabla^n y_n
    ```
    di mana $s = \frac{x - x_n}{h}$

*   **Tabel Perbedaan Mundur:** (Contoh tabel sederhana)

    | $x$    | $y$      | $\nabla y$ | $\nabla^2 y$ | ... |
    | ------ | -------- | ---------- | ----------- | --- |
    | ...    | ...      |            |             |     |
    | $x_{n-2}$  | $y_{n-2}$  |            |             |     |
    | $x_{n-1}$  | $y_{n-1}$  | $\nabla y_{n-1}$ |             |     |
    | $x_n$  | $y_n$    | $\nabla y_n$ | $\nabla^2 y_n$ | ... |

---

# Slide 6: Contoh Soal - Newton Mundur

## Contoh Soal Newton Mundur

*   **Data:** (Sama seperti sebelumnya)

    | $x$    | 0     | 1     | 2     | 3     |
    | ------ | ----- | ----- | ----- | ----- |
    | $y$    | 1     | 2     | 5     | 10    |

*   **Soal:** Perkirakan $y$ pada $x = 2.5$.
*   **Hasil:** $y \approx 7.25$ (Tampilkan hasil akhir)

---

# Slide 7: Interpolasi Lagrange

## Interpolasi Lagrange

*   **Keunggulan:**
    *   Formula *langsung*.
    *   Data *tidak harus berjarak sama*.
*   **Rumus Utama:** (Tampilkan rumus utama)
    ```
    P_n(x) = \sum_{i=0}^{n} y_i L_i(x)
    ```
    dengan
    ```
    L_i(x) = \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}
    ```

*   **Konsep:** Kombinasi polinomial basis $L_i(x)$.

---

# Slide 8: Contoh Soal - Lagrange

## Contoh Soal Lagrange

*   **Data:** (Sama seperti sebelumnya)

    | $x$    | 0     | 1     | 2     | 3     |
    | ------ | ----- | ----- | ----- | ----- |
    | $y$    | 1     | 2     | 5     | 10    |

*   **Soal:** Perkirakan $y$ pada $x = 0.5$.
*   **Hasil:** $y \approx 1.25$ (Tampilkan hasil akhir)

---

# Slide 9: Algoritma Neville

## Algoritma Neville

*   **Metode:** *Rekursif* untuk interpolasi polinomial.
*   **Keunggulan:**
    *   Efisien Komputasi
    *   Data tidak harus berjarak sama.
    *   Estimasi error (dengan membandingkan iterasi).
*   **Rumus Rekursif:** (Tampilkan rumus utama)
    ```
    P_{i,j}(x) = \frac{(x - x_i)P_{i+1,j}(x) - (x - x_j)P_{i,j-1}(x)}{x_j - x_i}
    ```

---

# Slide 10: Contoh Soal - Neville

## Contoh Soal Neville

*   **Data:** (Sama seperti sebelumnya)

    | $x$    | 0     | 1     | 2     | 3     |
    | ------ | ----- | ----- | ----- | ----- |
    | $y$    | 1     | 2     | 5     | 10    |

*   **Soal:** Perkirakan $y$ pada $x = 0.5$.
*   **Hasil:** $y \approx 1.25$ (Tampilkan hasil akhir, tabel Neville bisa diringkas atau dihilangkan di slide jika terlalu panjang)

---

# Slide 11: Perbandingan Metode

## Perbandingan Metode Interpolasi

*   **Newton (Maju, Mundur, Pusat):**
    *   Efisien, baik untuk data *berjarak sama*.
    *   Spesialisasi wilayah data (awal, akhir, tengah).
*   **Lagrange:**
    *   Formula langsung, mudah dipahami.
    *   Data *tidak harus berjarak sama*.
    *   Kurang efisien untuk data besar.
*   **Neville:**
    *   Rekursif, efisien.
    *   Data *tidak harus berjarak sama*.
    *   Estimasi error.

---

# Slide 12: Aplikasi Interpolasi

## Aplikasi Interpolasi

*   **Rekonstruksi CT Scan (Medis):** Interpolasi linear untuk mengisi data hilang.
*   **Komputasi Ilmiah:** Solusi persamaan diferensial, analisis data.
*   **Grafika Komputer:** Texture mapping, animasi, rendering.
*   **Pemodelan Keuangan:** Estimasi nilai keuangan.
*   **Analisis Geospasial:** Pemetaan permukaan kontinu.

---

# Slide 13: Kesimpulan

## Kesimpulan

*   **Interpolasi:** Alat penting untuk representasi data kontinu dari data diskrit.
*   **Metode Newton, Lagrange, Neville:**  Berbagai pendekatan dengan kelebihan dan kekurangan.
*   **Pemilihan Metode:** Tergantung pada data, efisiensi, dan akurasi yang dibutuhkan.
*   **Penting untuk Mahasiswa:**  Dasar penting dalam metode numerik dan aplikasi rekayasa.

---

# Slide 14: Daftar Pustaka (Optional)

## Daftar Pustaka

*   (Jika perlu, daftar pustaka bisa diringkas atau dihilangkan untuk presentasi, dan diberikan sebagai handout terpisah)

<div style="text-align: center">⁂</div>