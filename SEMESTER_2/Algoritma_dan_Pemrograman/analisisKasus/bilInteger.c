/*
Nama File       : bilInteger.c
Deskripsi       : Mengecek input bilangan integer apakah bilangan positif atau nol atau negatif
Pembuat         : 24060124110142 - Muchammad Yuda Tri Ananda
Tgl Pembuatan   : 3 Maret 2025 - 16:52
*/

#include <stdio.h> /*header file*/

/*Program Utama*/
int main()
{
    /*Kamus*/
    int i;
    printf("Masukkan angka = ");
    scanf("%d", &i);

    /*Algoritma*/
    if (i < 0)
    {
        printf("Angka ini negatif");
        return 0;
    }

    if (i > 0)
    {
        printf("Angka ini positif");
        return 0;
    }

    printf("Angka ini bernilai 0");

    return 0;
}