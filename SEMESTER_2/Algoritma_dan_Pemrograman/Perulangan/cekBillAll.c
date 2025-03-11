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
    for (int i = 1; i <= N / 2; i++)
    {
        if (N % i == 0)
        {
            faktor += i;
        }
    }

    if (faktor == N)
    {

        printf("Bilangan %d adalah bilangan sempurna", N);
        return 0;
    }
    if (faktor == 1)
    {

        printf("Bilangan %d adalah bilangan prima", N);
        return 0;
    }
    printf("Bilangan %d adalah bilangan biasa", N);
    return 0;
}
