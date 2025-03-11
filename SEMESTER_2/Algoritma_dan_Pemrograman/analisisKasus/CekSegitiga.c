/*
Nama File 		: CekSegitiga.c
Deskripsi 		: Menentukan bentuk segitiga sama kaki atau sama sisi atau sembarang dari inputan 3 buah sisi segitiga berupa bilangan integer
Pembuat   		: 24060124110142 - Muchammad Yuda Tri Ananda
Tgl Pembuatan   : 3 Maret 2025 - 16:55
*/

#include <stdio.h> /*header file*/

/*Program Utama*/
int main()
{
    /*Kamus*/
    int sisi1, sisi2, sisi3;
    printf("Masukkan sisi 1 = ");
    scanf("%d", &sisi1);
    printf("Masukkan sisi 2 = ");
    scanf("%d", &sisi2);
    printf("Masukkan sisi 3 = ");
    scanf("%d", &sisi3);

    /*Algoritma*/
    if (sisi1 <= 0 || sisi2 <= 0 || sisi3 <= 0)
    {
        printf("Terdapat nilai yang bukan sisi segitiga!");
        return 0;
    }

    if (sisi1 == sisi2 && sisi2 == sisi3 && sisi1 == sisi3)
    {
        printf("Segitiga sama sisi");
        return 0;
    }

    if (sisi1 == sisi2 || sisi1 == sisi3 || sisi2 == sisi3)
    {
        printf("Segitiga sama kaki");
        return 0;
    }

    printf("Segitiga sembarang");

    return 0;
}