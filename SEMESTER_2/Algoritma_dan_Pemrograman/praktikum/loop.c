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
    int i, n, skor, jumlahSkor = 0, maxSkor = 0;

    /*Algoritma*/
    printf("jumlah siswa: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        printf("Skor siswa %d: ", i);
        scanf("%d", &skor);

        jumlahSkor += skor;
        if (skor > maxSkor)
            maxSkor = skor;
    }

    printf("Skor rata rata: %.2f\n", jumlahSkor / (float)n);
    printf("Skor tertinggi: %d\n", maxSkor);

    return 0;
}
