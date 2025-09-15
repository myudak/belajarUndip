---
marp: true
theme: gaia
---

<!-- _class: lead -->
# Metode Newton untuk Sistem Persamaan Non-Linear

**Presentasi oleh:**
*   Muhammad Dimas Arya Putra (24060124130062)
*   Muhammad Kemal Faza (24060124120013)
*   Muhammad Akmal Fazli (24060124130123)
*   Muhammad Zaidaan Ardiansyah (24060124140200)
*   Muchammad Yuda Tri Ananda (24060124110142)

---

# Metode Newton untuk Sistem Persamaan Non-Linear

Metode Newton merupakan sebuah teknik iteratif yang sangat berguna untuk menemukan aproksimasi akar dari suatu sistem persamaan non-linear.

Sistem persamaan non-linear dapat direpresentasikan dalam bentuk vektor $F(x) = 0$, di mana $x$ adalah vektor variabel $(x_1, x_2, \dots, x_n)^t$ dan $F$ adalah fungsi vektor yang setiap komponennya $f_i(x_1, x_2, \dots, x_n)$ merupakan persamaan non-linear.

---

Tujuan metode ini adalah untuk menghasilkan serangkaian aproksimasi $x^{(0)}, x^{(1)}, x^{(2)}, \dots$ yang dimulai dari sebuah tebakan awal $x^{(0)}$, dan diharapkan konvergen menuju solusi sebenarnya $p$ dari sistem tersebut.

---

# Prosedur Iterasi Metode Newton

Secara umum, langkah-langkah untuk melakukan satu iterasi dalam Metode Newton, dari aproksimasi $x^{(k-1)}$ menuju $x^{(k)}$, adalah sebagai berikut:

1.  **Evaluasi Fungsi $F(x^{(k-1)})$**: Hitung nilai dari setiap fungsi dalam sistem menggunakan nilai aproksimasi saat ini $x^{(k-1)}$. Ini akan menghasilkan sebuah vektor $F(x^{(k-1)})$.

---

2.  **Evaluasi Matriks Jacobian $J(x^{(k-1)})$**: Matriks Jacobian, $J(x)$, adalah matriks yang berisi semua turunan parsial orde pertama dari sistem fungsi. Elemen $(i,j)$ dari matriks Jacobian, $J(x)_{i,j}$, didefinisikan sebagai $\frac{\partial f_i}{\partial x_j}$. Matriks ini dievaluasi pada titik aproksimasi saat ini $x^{(k-1)}$.

---


3.  **Selesaikan Sistem Linear untuk Vektor Koreksi $y^{(k-1)}$**: Bentuk dan selesaikan sistem persamaan linear berikut untuk mendapatkan vektor koreksi $y^{(k-1)}$:
    $$J(x^{(k-1)})y^{(k-1)} = -F(x^{(k-1)})$$
    Penyelesaian sistem linear ini merupakan inti dari setiap iterasi. Meskipun formula iterasi dapat ditulis menggunakan invers Jacobian ($y^{(k-1)} = -[J(x^{(k-1)})]^{-1}F(x^{(k-1)})$), perhitungan invers matriks secara eksplisit biasanya dihindari karena kurang efisien dan rentan terhadap galat numerik. Metode seperti eliminasi Gauss sering digunakan.

---

4.  **Perbarui Aproksimasi Solusi $x^{(k)}$**: Hitung aproksimasi solusi berikutnya dengan menambahkan vektor koreksi ke aproksimasi sebelumnya:
    $$x^{(k)} = x^{(k-1)} + y^{(k-1)}$$

Proses iterasi ini (langkah 1 hingga 4) diulangi hingga kriteria konvergensi tertentu terpenuhi.

---

# Contoh Penyelesaian SPNL

Pertimbangkan sistem dua persamaan non-linear dengan dua variabel berikut:
$$
\begin{align*}
    f_1(x_1, x_2) &= 4x_1^2 - 20x_1 + \frac{1}{4}x_2^2 + 8 = 0 \\
    f_2(x_1, x_2) &= \frac{1}{2}x_1x_2^2 + 2x_1 - 5x_2 + 8 = 0
\end{align*}
$$
Akan dicari aproksimasi solusi menggunakan Metode Newton dengan tebakan awal $x^{(0)} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.

---

## 1. Definisi Fungsi Vektor dan Matriks Jacobian

Fungsi vektor $F(x)$ adalah:
$$F(x) = \begin{pmatrix} f_1(x_1, x_2) \\ f_2(x_1, x_2) \end{pmatrix} = \begin{pmatrix} 4x_1^2 - 20x_1 + \frac{1}{4}x_2^2 + 8 \\ \frac{1}{2}x_1x_2^2 + 2x_1 - 5x_2 + 8 \end{pmatrix}$$

---

Turunan parsial yang dibutuhkan untuk Matriks Jacobian adalah:
$$
\begin{align*}
    \frac{\partial f_1}{\partial x_1} &= 8x_1 - 20 \\
    \frac{\partial f_1}{\partial x_2} &= \frac{1}{2}x_2 \\
    \frac{\partial f_2}{\partial x_1} &= \frac{1}{2}x_2^2 + 2 \\
    \frac{\partial f_2}{\partial x_2} &= x_1x_2 - 5
\end{align*}
$$
Sehingga, Matriks Jacobian $J(x_1, x_2)$ adalah:
$$J(x_1, x_2) = \begin{pmatrix} 8x_1 - 20 & \frac{1}{2}x_2 \\ \frac{1}{2}x_2^2 + 2 & x_1x_2 - 5 \end{pmatrix}$$

---

## 2. Iterasi ke-1

Dimulai dengan $x^{(0)} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.

*   **Evaluasi $F(x^{(0)})$**:
    $$
    \begin{align*}
        f_1(0,0) &= 4(0)^2 - 20(0) + \frac{1}{4}(0)^2 + 8 = 8 \\
        f_2(0,0) &= \frac{1}{2}(0)(0)^2 + 2(0) - 5(0) + 8 = 8
    \end{align*}
    $$
    Jadi, $F(x^{(0)}) = \begin{pmatrix} 8 \\ 8 \end{pmatrix}$.

---

*   **Evaluasi $J(x^{(0)})$**:
    $$J(0,0) = \begin{pmatrix} 8(0) - 20 & \frac{1}{2}(0) \\ \frac{1}{2}(0)^2 + 2 & (0)(0) - 5 \end{pmatrix} = \begin{pmatrix} -20 & 0 \\ 2 & -5 \end{pmatrix}$$

---

## 2. Iterasi ke-1 (Lanjutan)

*   **Selesaikan $J(x^{(0)})y^{(0)} = -F(x^{(0)})$ untuk $y^{(0)}$**:
    $$\begin{pmatrix} -20 & 0 \\ 2 & -5 \end{pmatrix} \begin{pmatrix} y_1^{(0)} \\ y_2^{(0)} \end{pmatrix} = -\begin{pmatrix} 8 \\ 8 \end{pmatrix} = \begin{pmatrix} -8 \\ -8 \end{pmatrix}$$
    Sistem linear:
    $$
    \begin{align*}
        -20y_1^{(0)} + 0y_2^{(0)} &= -8 \quad &(1) \\
        2y_1^{(0)} - 5y_2^{(0)} &= -8 \quad &(2)
    \end{align*}
    $$
---

*    Dari (1): $-20y_1^{(0)} = -8 \implies y_1^{(0)} = 0.4$.
    Substitusi ke (2): $2(0.4) - 5y_2^{(0)} = -8 \implies 0.8 - 5y_2^{(0)} = -8 \implies -5y_2^{(0)} = -8.8 \implies y_2^{(0)} = 1.76$.
    Jadi, $y^{(0)} = \begin{pmatrix} 0.4 \\ 1.76 \end{pmatrix}$.

*   **Perbarui Aproksimasi $x^{(1)} = x^{(0)} + y^{(0)}$**:
    $$x^{(1)} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 0.4 \\ 1.76 \end{pmatrix} = \begin{pmatrix} 0.4 \\ 1.76 \end{pmatrix}$$

---

## 3. Iterasi ke-2

Menggunakan $x^{(1)} = \begin{pmatrix} 0.4 \\ 1.76 \end{pmatrix}$.

*   **Evaluasi $F(x^{(1)})$**:
    $$
    \begin{align*}
        f_1(0.4, 1.76) &= 4(0.4)^2 - 20(0.4) + \frac{1}{4}(1.76)^2 + 8 \\
                       &= 0.64 - 8 + 0.7744 + 8 = 1.4144 \\
        f_2(0.4, 1.76) &= \frac{1}{2}(0.4)(1.76)^2 + 2(0.4) - 5(1.76) + 8 \\
                       &= 0.61952 + 0.8 - 8.8 + 8 = 0.61952
    \end{align*}
    $$
    Jadi, $F(x^{(1)}) = \begin{pmatrix} 1.4144 \\ 0.61952 \end{pmatrix}$.

---

*   **Evaluasi $J(x^{(1)})$**:
    $$
    \begin{align*}
    J(0.4, 1.76) &= \begin{pmatrix} 8(0.4) - 20 & \frac{1}{2}(1.76) \\ \frac{1}{2}(1.76)^2 + 2 & (0.4)(1.76) - 5 \end{pmatrix} \\
                 &= \begin{pmatrix} -16.8 & 0.88 \\ 3.5488 & -4.296 \end{pmatrix}
    \end{align*}
    $$

---

## 3. Iterasi ke-2 (Lanjutan)

*   **Selesaikan $J(x^{(1)})y^{(1)} = -F(x^{(1)})$ untuk $y^{(1)}$**:
    $$\begin{pmatrix} -16.8 & 0.88 \\ 3.5488 & -4.296 \end{pmatrix} \begin{pmatrix} y_1^{(1)} \\ y_2^{(1)} \end{pmatrix} = -\begin{pmatrix} 1.4144 \\ 0.61952 \end{pmatrix}$$
    Penyelesaian sistem linear ini menghasilkan:
    $y_1^{(1)} \approx 0.0959057$
    $y_2^{(1)} \approx 0.223654$
    Jadi, $y^{(1)} \approx \begin{pmatrix} 0.0959057 \\ 0.223654 \end{pmatrix}$.

---

*   **Perbarui Aproksimasi $x^{(2)} = x^{(1)} + y^{(1)}$**:
    $$x^{(2)} = \begin{pmatrix} 0.4 \\ 1.76 \end{pmatrix} + \begin{pmatrix} 0.0959057 \\ 0.223654 \end{pmatrix} = \begin{pmatrix} 0.4959057 \\ 1.983654 \end{pmatrix}$$

---

## 4. Kondisi Berhenti Iterasi

Iterasi biasanya dihentikan jika salah satu kondisi berikut terpenuhi:
*   Norma dari vektor koreksi $y^{(k-1)}$ (atau selisih $x^{(k)} - x^{(k-1)}$) lebih kecil dari toleransi (TOL).
    Misalnya, $||y^{(k-1)}||_{\infty} < \text{TOL}$.
*   Jumlah maksimum iterasi (N) telah tercapai.


---

Dalam contoh:
*   Akhir iterasi 1: $||y^{(0)}||_{\infty} = \max(|0.4|, |1.76|) = 1.76$.
*   Akhir iterasi 2: $||y^{(1)}||_{\infty} = \max(|0.0959057|, |0.223654|) = 0.223654$.

Jika $\text{TOL} = 10^{-5}$, maka karena $0.223654 \not< 10^{-5}$, iterasi akan dilanjutkan jika akurasi lebih tinggi diperlukan dan batas maksimum iterasi belum tercapai.
Untuk contoh ini, kita berhenti pada $x^{(2)}$.

---

## 5. Analisis Galat untuk Aproksimasi $x^{(2)}$

Solusi eksak: $x_{\text{eksak}} = \begin{pmatrix} 0.5 \\ 2 \end{pmatrix}$.
Aproksimasi: $x^{(2)} = \begin{pmatrix} 0.4959057 \\ 1.983654 \end{pmatrix}$.

*   **Vektor Galat Absolut**:
    $$E_{\text{abs\_vec}} = x_{\text{eksak}} - x^{(2)} = \begin{pmatrix} 0.5 - 0.4959057 \\ 2 - 1.983654 \end{pmatrix} = \begin{pmatrix} 0.0040943 \\ 0.016346 \end{pmatrix}$$

*   **Galat Absolut** ($l_{\infty}$ norma):
    $$||E_{\text{abs\_vec}}||_{\infty} = \max(|0.0040943|, |0.016346|) = 0.016346$$

---

*   **Galat Relatif** ($l_{\infty}$ norma):
    $$||x_{\text{eksak}}||_{\infty} = \max(|0.5|, |2|) = 2$$
    $$E_{\text{rel}} = \frac{||E_{\text{abs\_vec}}||_{\infty}}{||x_{\text{eksak}}||_{\infty}} = \frac{0.016346}{2} = 0.008173$$

Setelah dua iterasi, aproksimasi $x^{(2)}$ memiliki galat absolut sekitar $0.016346$. Jika iterasi dilanjutkan, diharapkan galat ini akan menurun dengan cepat (konvergensi kuadratik).

---

<!-- _class: lead invert -->
# Terima Kasih

## Ada Pertanyaan?