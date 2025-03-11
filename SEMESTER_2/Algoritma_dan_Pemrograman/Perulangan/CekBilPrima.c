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
    for (int i = 2; i * i <= N; i++)
    {
        if (N % i == 0)
        {
            printf("Bilangan %d bukan prima, ", N);
            return 0;
        }
    }
    printf("Bilangan %d adalah prima", N);
    return 0;
}
