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
    int N, jumlah;

    printf("Masukkan deret N :");
    scanf("%d", &N);

    /*Algoritma*/
    for (int i = 1; i <= N; i++)
    {
        jumlah += i;
    }
    printf("Jumlah deret N = %d", jumlah);
    return 0;
}
