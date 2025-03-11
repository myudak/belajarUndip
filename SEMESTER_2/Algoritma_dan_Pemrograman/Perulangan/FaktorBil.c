/*
Nama File 		: BiayaKirim.c
Deskripsi 		: Menentukan biaya kirim dengan input berat dan jarak berupa bilangan integer
Pembuat   		: 24060124110142 - Muchammad Yuda Tri Ananda
Tgl Pembuatan   : 1 Maret 2025 - 14:51
*/

#include <stdio.h> /*header file*/

/*Program Utama*/
int main()
{
    /*Kamus*/
    int N, faktor;

    printf("Masukkan bilangan N :");
    scanf("%d", &N);

    /*Algoritma*/
    printf("Faktor Bilangannya adalah ");
    for (int i = 1; i <= N; i++)
    {
        if (N % i == 0)
        {
            printf("%d, ", i);
        }
    }
    return 0;
}
