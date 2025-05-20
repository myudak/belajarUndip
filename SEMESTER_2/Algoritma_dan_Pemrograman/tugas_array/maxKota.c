#include <stdio.h>
#include <string.h>

int main()
{
    int i, j, maxJual, iBulan, iKota;
    int tabel[3][4] = {{10, 15, 10, 5}, {20, 25, 20, 15}, {10, 5, 14, 3}};
    char inputBulan[20];
    char bulan[4][10] = {"Januari", "Februari", "Maret", "April"};
    char kota[3][20] = {"Semarang", "Jakarta", "Yogyakarta"};

    printf("Masukkan nama bulan: ");
    scanf("%s", inputBulan);

    iBulan = -1;
    for (i = 0; i < 4; i++)
    {
        if (strcmp(inputBulan, bulan[i]) == 0)
        {
            iBulan = i;
            break;
        }
    }

    if (iBulan == -1)
    {
        printf("Bulan tidak ditemukan.");
        return 1;
    }

    maxJual = tabel[0][iBulan];
    iKota = 0;

    for (i = 1; i < 3; i++)
    {
        if (maxJual < tabel[i][iBulan])
        {
            maxJual = tabel[i][iBulan];
            iKota = i;
        }
    }

    printf("Penjualan tertinggi pada bulan %s adalah Kota %s dengan jumlah %d.", inputBulan, kota[iKota], maxJual);

    return 0;
}