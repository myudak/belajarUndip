/*
Nama File 		: namaBulan.c
Deskripsi 		: Menentukan nama bulan sesuai dengan nomor bulan dan jika tidak sesuai maka muncul pesan "Masukan nomor bulan tidak tepat!"
Pembuat   		: 24060124110142 - Muchammad Yuda Tri Ananda
Tgl Pembuatan   : 3 Maret 2025 - 17:01
*/

#include <stdio.h> /*header file*/

/*Program Utama*/
int main()
{
    /*Kamus*/
    int bulan;
    printf("Masukkan angka untuk mengetahui nama bulan : ");
    scanf("%d", &bulan);

    /*Algoritma*/
    if (bulan > 12 || bulan < 1)
    {
        printf("Masukan nomor bulan tidak tepat!");
        return 0;
    }

    switch (bulan)
    {
    case 1:
        printf("Bulan Januari");
        break;
    case 2:
        printf("Bulan Februari");
        break;
    case 3:
        printf("Bulan Maret");
        break;
    case 4:
        printf("Bulan April");
        break;
    case 5:
        printf("Bulan Mei");
        break;
    case 6:
        printf("Bulan Juni");
        break;
    case 7:
        printf("Bulan Juli");
        break;
    case 8:
        printf("Bulan Agustus");
        break;
    case 9:
        printf("Bulan September");
        break;
    case 10:
        printf("Bulan Oktober");
        break;
    case 11:
        printf("Bulan November");
        break;
    case 12:
        printf("Bulan Desember");
        break;
    }

    return 0;
}