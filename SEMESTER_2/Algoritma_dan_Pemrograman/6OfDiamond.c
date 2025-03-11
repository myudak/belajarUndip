/*
Nama File 		: 6OfDiamond.c
Deskripsi 		:
Pembuat   		: 24060124110142 - Muchammad Yuda Tri Ananda
Tgl Pembuatan   : 5 Maret 2025 - 14:51
*/

#include <stdio.h> /*header file*/

/*Program Utama*/
int main()
{
    /*Kamus*/
    int kartu1, kartu2;

    printf("Masukan Kartu Kanan : ");
    scanf("%d", &kartu1);
    printf("Masukan Kartu Kiri : ");
    scanf("%d", &kartu2);

    int angka1 = kartu1 / 10, gambar1 = kartu1 % 10;
    int angka2 = kartu2 / 10, gambar2 = kartu2 % 10;

    /*Algoritma*/
    if (angka1 > angka2)
    {
        if (angka1 == 11)
            printf("Jack");
        else if (angka1 == 12)
            printf("Queen");
        else if (angka1 == 13)
            printf("King");
        else if (angka1 == 14)
            printf("Ace");
        else
            printf("%d", angka1);

        printf(" of ");

        if (gambar1 == 1)
            printf("Diamond");
        else if (gambar1 == 2)
            printf("Spade");
        else if (gambar1 == 3)
            printf("Heart");
        else if (gambar1 == 4)
            printf("Club");

        return 0;
    }
    if (angka2 > angka1)
    {
        if (angka2 == 11)
            printf("Jack");
        else if (angka2 == 12)
            printf("Queen");
        else if (angka2 == 13)
            printf("King");
        else if (angka2 == 14)
            printf("Ace");
        else
            printf("%d", angka2);

        printf(" of ");

        if (gambar2 == 1)
            printf("Diamond");
        else if (gambar2 == 2)
            printf("Spade");
        else if (gambar2 == 3)
            printf("Heart");
        else if (gambar2 == 4)
            printf("Club");

        return 0;
    }
    if (angka1 == 11)
        printf("Jack");
    else if (angka1 == 12)
        printf("Queen");
    else if (angka1 == 13)
        printf("King");
    else if (angka1 == 14)
        printf("Ace");
    else
        printf("%d", angka1);

    printf(" of ");

    if (gambar1 == 1)
        printf("Diamond");
    else if (gambar1 == 2)
        printf("Spade");
    else if (gambar1 == 3)
        printf("Heart");
    else if (gambar1 == 4)
        printf("Club");

    printf(" and ");

    if (gambar2 == 1)
        printf("Diamond");
    else if (gambar2 == 2)
        printf("Spade");
    else if (gambar2 == 3)
        printf("Heart");
    else if (gambar2 == 4)
        printf("Club");

    return 0;
}
