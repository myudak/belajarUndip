/* TULIS NAMA DAN NIM DI SINI (WAJIB)
jika tidak ditulis nilai -2%
Nama : Muchammad Yuda Tri Ananda
NIM  : 24060124110142
Deskripsi :*/

/*======================= SELAMAT DATANG DI SOAL SUITLESS ===========================*/
/* Pada soal suitless, kalian diminta untuk meemperbaiki kode di bawah ini, setelah
Kode kalian selesai lengkapi, cobalah untuk men-tracing semua sample input yang diberikan,
berikan pula penjelasan mengapa algoritma ini dipakai ? apakah ada alternatif lain?
Perhatikan penulisan algoritma, algoritma bukanlah sebah blok kode bahasa pemrograman
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    /* Kamus */
    int N;
    int T[100];
    int A[100];
    int KingMax, QueenMax;

    /* Algoritma */
    scanf("%d", &N);

    KingMax = 0;
    QueenMax = 0;

    for (int i = 0; i < N; i++)
    {
        scanf("%d %d", &A[i], &T[i]);
        if (T[i] == 1)
        {
            KingMax += A[i];
        }
        else if (T[i] == 2)
        {
            QueenMax += A[i];
        }
        else
        {
            QueenMax += A[i];
            KingMax += A[i];
        }
    }

    if (KingMax >= QueenMax)
        printf("%d", KingMax);
    else
        printf("%d", QueenMax);
    return 0;
}

/* Tulis Hasil Tracing Kalian di sini , Menggunakan Komentar */

/*
=== Sample Input 0 ===

ada 3 pasukan

Total Power :
Raja = 7         (dari input 1: 7 1)
Ratu = 5         (dari input 2: 5 2)
bebas = 4        (dari input 3: 4 3)

Maksimal = max(Raja + bebas, Ratu + bebas)
Maksimal = max(7 + 4, 5 + 4)
Maksimal = max(11, 9)
Maksimal = 11

Hasil Akhir: 11

=== Sample Input 1 ===

ada 15 pasukan

Total Power :
Raja = 51        (dari 5 1, 8 1, 7 1, 15 1, 6 1, 9 1, 1 1)
Ratu = 66        (dari 10 2, 12 2, 20 2, 11 2, 13 2)
bebas = 9        (dari 3 0, 4 3, 2 3)

Maksimal = max(Raja + bebas, Ratu + bebas)
Maksimal = max(51 + 9, 66 + 9)
Maksimal = max(60, 75)
Maksimal = 75

Hasil Akhir: 75
*/

/* Tulis Alasan Kalian di sini , Menggunakan Komentar */
/*
algoritma ini dipakai karena hanya tinggal memperbaiki template, yang diperbaiki

menambahkan kamus A[100] kekuatan, mengubah input menjadi scanf, mengganti inisialisasi kingMax QeenMax menjadi 0, mengubah int j dalam for loop menjadi i, j + 2 menjadi i + 1, mengubah scanf T T menjadi scanf A T, mengubah logika jika tipe 0 kingMax ditambah kekuatan, terakhir mengubah output menjadi printf angkanya saja dan menambahkan else.

algoritma ini dipakai karena hanya tinggal memperbaiki logika / template yang sudah ada jadi tidak perlu logika alternatif walaupun ada logika alternatif

*/