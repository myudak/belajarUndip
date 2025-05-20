#include <stdio.h>

int maxTabel(float T[], int N)
{
    int max = 0, i, IX;
    for (i = 0; i < N; i++)
    {
        if (T[i] >= max)
        {
            max = T[i];
            IX = i;
        }
    }

    return IX;
}

int main()
{
    int i, j, sum, b, k, iMax;
    int data_penjualan[3][4] = {{10, 15, 10, 5}, {20, 25, 20, 15}, {10, 5, 14, 3}};

    b = 3;
    k = 4;
    float bulanRataRataTerbesar[b];

    for (j = 0; j < k; j++)
    {
        sum = 0;
        for (i = 0; i < b; i++)
        {
            sum += data_penjualan[i][j];
        }
        bulanRataRataTerbesar[j] = (float)sum / k;
    }

    for (i = 0; i < b; i++)
    {
        printf("%f\n", bulanRataRataTerbesar[i]);
    }

    iMax = maxTabel(bulanRataRataTerbesar, k);
    if (iMax == 0)
    {
        printf("Bulan Januari memiliki rata-rata penjualan tertinggi.");
    }
    else if (iMax == 1)
    {
        printf("Bulan Februari memiliki rata-rata penjualan tertinggi.");
    }
    else if (iMax == 2)
    {
        printf("Bulan Maret memiliki rata-rata penjualan tertinggi.");
    }
    else if (iMax == 3)
    {
        printf("Bulan April memiliki rata-rata penjualan tertinggi.");
    }

    return 0;
}