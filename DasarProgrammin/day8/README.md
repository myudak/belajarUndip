# PRAKTIKUM DASAR PEMROGRAMAN PERTEMUAN KE-8 SET

Set (himpunan) merupakan sebuah koleksi objek. Set merupakan list dengan syarat bahwa setiap elemennya harus unik (tidak boleh ada elemen yang sama). Dalam set urutan kemunculan elemen tidak diperhatikan.

## TUJUAN PRAKTIKUM 
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu merealisasikan set ke dalam bahasa pemrograman Python serta mengaplikasikan masalah/kasus yang perlu diselesaikan dengan menggunakan set. 

## TOOLS 
Tools yang diperlukan untuk melakukan praktikum ini adalah interpreter Python yang telah terinstall di komputer. Set merupakan list dengan syarat bahwa setiap elemennya harus unik. Dalam set, urutan kemunculan elemen tidak diperhatikan. Himpunan A sama dengan himpunan B jika himpunan A memiliki elemen yang sama dengan B, meskipun urutan/posisi elemennya berbeda.  Pada praktikum ini mahasiswa akan belajar merealisasikan type kolektif set ke dalam bahasa Python dalam paradigma fungsional. Dalam paradigma fungsional, set didefinisikan sebagaimana list dengan syarat tambahan bahwa setiap elemennya harus unik. Oleh karena itu, set juga dapat didefinisikan secara rekursif seperti pada list.  Meskipun bahasa Python memiliki type bawaan berupa set, namun set dalam praktikum ini akan tetap direalisasikan (dalam paradigma fungsional/ secara rekursif) sebagai list dengan syarat khusus sebagaimana yang dipelajari dalam kuliah atau Diktat.  Semua konstruktor, selektor, dan fungsi lainnya yang telah dibuat pada list dapat digunakan di dalam set.

## TUGAS/LATIHAN 
Buatlah realisasi python untuk fungsi-fungsi lainnya sebagai berikut: 
1. Realisasi fungsi Rember(x,L) yang dicontohkan akan menghapus elemen x yang ditemui pertama 
kali dari list L. Buatlah realisasi versi 2 untuk menghapus elemen x yang ditemui terakhir kali pada 
list L, beri nama dengan Rember2(x,L). 
2. Buatlah realisasi dari fungsi MultiRember(x,L). 
3. Buatlah realisasi fungsi MakeSet(L) dalam dua versi: 
a. Versi 1: dengan memanfaatkan fungsi IsMember(x,L) untuk mengecek duplikasi elemen. 
b. Versi 2: dengan memanfaatkan fungsi MultiRember(x,L) untuk menghapus duplikasi elemen.   
Perhatikan output yang dihasilkan dari kedua versi tersebut. Bagaimana perbedaannya?  
4. Buatlah realisasi fungsi KonsoSet(e,H) yang menambahkan sebuah elemen e sebagai elemen 
pertama set H dengan syarat e belum ada di dalam himpunan H. 
5. Buatlah realisasi fungsi IsSet(L). 
6. Buatlah realisasi fungsi IsSubset(H1,H2) 
7. Buatlah realisasi fungsi IsEqualSet dalam dua versi: 
a. Versi 1: memanfaatkan fungsi IsSubset(H1,H2). 
b. Versi 2: dengan mengecek satu persatu elemen pada H1 dan H2. 
8. Buatlah realisasi fungsi IsIntersect(H1,H2). 
9. Buatlah realisasi fungsi MakeIntersect(H1,H2) dalam 2 versi: 
a. Versi 1: rekursif terhadap H1 
b. Versi 2: rekursif terhadap H2 
Perhatikan output yang dihasilkan dari kedua versi tersebut. Bagaimana perbedaannya?  
10. Buatlah realisasi fungsi MakeUnion(H1,H2) dalam 2 versi: 
a. Versi 1: rekursif terhadap H1 
b. Versi 2: rekursif terhadap H2 
Perhatikan output yang dihasilkan dari kedua versi tersebut. Bagaimana perbedaannya?  
11. Buatlah realisasi fungsi NBIntersect(H1,H2). 
12. Buatlah realisasi fungsi NBUnion(H1,H2). 
Untuk setiap fungsi yang telah direalisasikan buatlah aplikasinya dengan berbagai variasi input untuk 
menguji apakah output fungsi sudah sesuai dengan yang seharusnya.