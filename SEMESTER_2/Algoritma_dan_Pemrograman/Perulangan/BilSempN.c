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
    printf("Bilangan sempurna adalah ");
    for (int i = 1; i <= N; i++)
    {
        int faktor = 0;
        for (int j = 1; j <= i / 2; j++)
        {
            if (i % j == 0)
            {
                faktor += j;
            }
        }
        if (faktor == i)
            printf("%d ", i);
    }
    return 0;
}
