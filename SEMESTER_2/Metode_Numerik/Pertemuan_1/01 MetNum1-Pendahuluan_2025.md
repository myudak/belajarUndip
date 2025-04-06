#   Pendahuluan
#   Metode Numerik
MIK 1624205 ( 3 sks )
Priyo Sidik Sasongko, S.Si, M.Kom.
Prajanto Wahyu Adi M.Kom.
Etna Vianita, S.Mat., M.Mat [cite: 1, 2]

* Metode Numerik:
    * Algoritma yang digunakan untuk mendapatkan solusi numerik dari masalah matematika. [cite: 2]

* Mengapa kita membutuhkannya?
    1.  Tidak ada solusi analitis,
    2.  Solusi analitis sulit diperoleh atau tidak praktis. [cite: 3]

* Kebutuhan Dasar dalam Metode Numerik:
    * Praktis:
        * Dapat dihitung dalam jumlah waktu yang wajar. [cite: 4]
    * Akurat:
        * Perkiraan yang baik terhadap nilai sebenarnya,
        * Informasi tentang kesalahan perkiraan (Batas, urutan kesalahan,...). [cite: 5]

* Contoh
    * Selesaikan integral di bawah ini

    * Metode Analitik

    * Contoh
    * Metode Numerik

    * Error = |7.25-7.33| = 0.0833
    * Nonlinear Equations
    * Perbedaan Metode Numerik dan Metode Analitik

| Metode Numerik                           | Metode Analitik                           |
| :--------------------------------------- | :---------------------------------------- |
| Solusi selalu berbentuk angka             | Solusi dapat berupa fungsi matematik      |
| Solusi yang dihasilkan solusi pendekatan | Solusi yang dihasilkan solusi exact       |
| sehingga terdapat error                  |                                           | [cite: 6]

* Kesalahan Numerik
    * Kesalahan numerik adalah kesalahan yang timbul karena adanya proses pendekatan. [cite: 6]
* Hubungan kesalahan dan penyelesaian adalah :
    * 𝑒=𝑥 −𝑥
    * 𝑥 = nilai yang sebenarnya ( nilai eksak )
    * x = nilai pendekatan yang dihasilkan dari metode numerik
    * e adalah kesalahan numerik. [cite: 7]
* Kesalahan fraksional adalah prosentase antara kesalahan dan nilai sebenarnyanya.

    * ∈ = 𝑒𝑥𝑥 100 % [cite: 8]

* Kesalahan Numerik

    * Pada banyak permasalahan kesalahan fraksional di atas sulit atau tidak bisa dihitung, karena nilai eksaknya tidak diketahui. [cite: 8]
* Sehingga kesalahan fraksional dihitung berdasarkan nilai pendekatan yang diperoleh:

    * dimana e pada waktu ke n adalah selisih nilai pendekatan ke n dan ke n-1
    * Perhitungan kesalahan semacam ini dilakukan untuk mencapai keadaan konvergensi pada suatu proses iterasi. [cite: 9]

* Peranan Komputer dalam Metode Numerik
    * Perhitungan dalam metode numerik berupa operasi aritmatika dan dilakukan berulang kali, sehingga komputer untuk mempercepat proses perhitungan tanpa membuat kesalahan [cite: 10]
    * Dengan komputer kita dapat mencoba berbagai kemungkinan solusi yang terjadi akibat perubahan beberapa parameter. [cite: 10]
    * Solusi yang diperoleh juga dapat ditingkatkan ketelitiannya dengan mengubah nilai parameter. [cite: 11]

* Peran Metode Numerik
    * Metode Numerik merupakan alat bantu pemecahan masalah matematika yang sangat ampuh. [cite: 12]
    * Metode numerik mampu menangani sistem persamaan linier yang besar dan persamaan-persamaan yang rumit. [cite: 13]
    * Merupakan penyederhanaan matematika yang lebih tinggi menjadi operasi matematika yang mendasar. [cite: 14]

* Persoalan yang diselesaikan dengan Metode Numerik
    * Menyelesaikan pers non-linier
        * M. Tertutup : Tabel, Biseksi, Regula Falsi,
        * M Terbuka : Secant, Newton Raphson
    * Menyelesaikan pers linier
        * Eliminasi Gauss, Eliminasi Gauss Jordan, Gauss Seidel
    * Interpolasi
        * Interpolasi Linier, Quadrat, Kubik, Polinom Lagrange, Polinom Newton, Polinomial Neville
    * Regresi (Pencocokan Kurva)
        * Linear ( Tunggal dan Ganda )
        * Nonlinear (Tunggal dan Ganda )
    * Differensiasi NumerikType equation here.
        * Selisih Maju, Selisih Tengahan, Selisih Mundur
    * Integrasi Numerik
        * Integral Reimann, Integrasi Trapezoida, Simpson, Gauss
    * Penyelesaian Persamaan Differensial
        * Euler, Taylor, Runge Kutta
    * Sistem persamaan linier menggunakan teknik iterasi
    * Aproksimasi dan kasus komputasi numerik aproksimasi
    * Metode Numerik  untuk sistem persamaan non linier

* Pendahuluan
    * Persoalan yang melibatkan model matematika banyak muncul dalam berbagai disiplin ilmu pengetahuan (bidang fisika, kimia, Teknik Sipil, Teknik Mesin, Elektro dsb) [cite: 15, 16]
    * Sering model matematika tersebut rumit dan tidak dapat diselesaikan dengan metode analitik [cite: 16]
    * Metode Analitik adalah metode penyelesaian model matematika dengan rumus-rumus aljabar yang sudah lazim. [cite: 16]
* Optimasi
    * Tak berkendala
    * Berkendala
    * Transformasi Fourier Cepat
    * Aproksimasi Discrete dan Polynomial
    * Aproksimasi Eigen Value
    * Persoalan yang diselesaikan dengan Metode Numerik (Lanjutan )
    * Penulisan Metode Numerik ke dalam Bahasa Python ( Google colab )
    * 3
    * Bagaimana memecahkan masalah teknik? [cite: 17]

* Deskripsi Masalah

* Model Matematika

* Solusi Model Matematika

* Implementasi (Menggunakan Solusi)

* Penilaian :
    * TERIMA KASIH
    * 4
    * A mathematical model is represented as a functional relationship of the form

    * Dependent independent forcing
        Variable = f variables , parameters, functions

    * Dependent variable: Characteristic that usually reflects the state of the system
    * Independent variables: Dimensions such as time and space along which the systems behavior is being determined
    * Parameters: reflect the system’s properties or composition
    * Forcing functions: external influences acting upon the system [cite: 18]

* 5
* Solusi Persamaan Nonlinear
    * Persamaan sederhana dan diselesaikan secara analitik:

    * Ada beberapa persamaan tidak ada solusi analitik:
    * To solve problems that cannot be solved exactly

    * Persoalan matematika
    * Bagaimana cara menyelesaikannya ?
        * Tentukan akar2 persamaan polinom
            * 23.4x7 - 1.25x6+ 120x4 + 15x3 – 120x2 – x + 100 = 0
        * 2.  Selesaikan sistem persamaan linier
            * 1.2a – 3b – 12c + 12d + 4.8e – 5.5f  + 100g = 18
            * 0.9a + 3b – c + 16d + 8e – 5f  - 10g = 17
            * 4.6a + 3b – 6c - 2d  + 4e + 6.5f  - 13g = 19 [cite: 18, 19, 20]
            * 3.  7a – 3b  + 8c  - 7d + 14e + 8.4f  + 16g = 6
            * 2.  2a + 3b  + 17c + 6d  + 12e – 7.5f + 18g = 9
            * 5.  9a + 3b  + 11c + 9d  - 5e – 25f + 10g = 0
            * 1.  6a + 3b  + 1.8c + 12d - 7e + 2.5f + g = -5
* Metode Analitik vs Metode [cite: 20, 21]
* Numerik
    * Kebanyakan persoalan matematika tidak dapat diselesaikan dengan metode analitik. [cite: 21]
    * Metode analitik disebut juga metode exact yang menghasilkan solusi exact (solusi sejati). [cite: 21]

* Metode analitik ini unggul untuk sejumlah persoalan yang terbatas. [cite: 22]
* Padahal kenyataan persoalan matematis banyak yang rumit, sehingga tidak dapat diselesaikan dengan metode analitik. [cite: 22]

* Metode Analitik vs Metode Numerik
    * Kalau metode analitik tidak dapat diterapkan, maka solusi dapat dicari dengan metode numerik. [cite: 23]
* Metode Numerik adalah teknik yang digunakan untuk memformulasikan persoalan matematika sehingga dapat dipecahkan dengan operasi perhitungan biasa (+, - , / , *) [cite: 24]