#include <stdio.h>
#include <string.h>

int main()
{
    int i, j, sum, b, k, min, iMin, jMin;
    int data_penjualan[3][4] = {{10, 15, 10, 5}, {20, 25, 20, 15}, {10, 5, 14, 3}};
    char dataBulan[4][10] = {"Januari", "Februari", "Maret", "April"};
    char dataKota[3][20] = {"Semarang", "Jakarta", "Yogyakarta"};
    char *kota, *bulan;

    b = 3;
    k = 4;

    min = data_penjualan[0][0];
    for (i = 0; i < b; i++)
    {
        for (j = 0; j < k; j++)
        {
            if (data_penjualan[i][j] <= min)
            {
                min = data_penjualan[i][j];
                iMin = i;
                jMin = j;
            }
        }
    }

    for (i = 0; i < b; i++)
    {
        if (i == iMin)
        {
            kota = dataKota[i];
        }
    }

    for (j = 0; j < k; j++)
    {
        if (j == jMin)
        {
            bulan = dataBulan[j];
        }
    }

    printf("%s, %s, %d\n", kota, bulan, min);

    return 0;
}