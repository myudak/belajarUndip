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
    int N;

    printf("Masukkan bilangan N :");
    scanf("%d", &N);

    /*Algoritma*/
    printf("Bilangan Primanya Adalah ");
    for (int i = 2; i <= N; i++)
    {
        int isPrima = 1;
        for (int j = 2; j * j <= i; j++)
        {
            if (i % j == 0)
            {
                isPrima = 0;
                break;
            }
        }
        if (isPrima)
            printf("%d ", i);
    }
    return 0;
}
