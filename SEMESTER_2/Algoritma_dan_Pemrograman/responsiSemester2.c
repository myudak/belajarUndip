#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

/*
Nama Nim: 24060124110142 - Muchammad Yuda Tri Ananda
*/

void bubbleSort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

float median(int arr[], int jumlah)
{
    if (jumlah == 0)
    {
        return 0.0;
    }
    bubbleSort(arr, jumlah);

    if (jumlah % 2 == 1)
    {
        return arr[jumlah / 2];
    }
    float tengah1 = arr[jumlah / 2 - 1];
    float tengah2 = arr[jumlah / 2];
    return (tengah1 + tengah2) / 2.0;
}

int main()
{
    int N;

    scanf("%d", &N);

    int angka_genap[9999];
    int angka_ganjil[9999];

    int jumlah_genap = 0;
    int jumlah_ganjil = 0;

    for (int i = 0; i < N; i++)
    {
        int A;
        scanf("%d", &A);

        if (A % 2 == 0)
        {
            angka_genap[jumlah_genap] = A;
            jumlah_genap++;
        }
        else
        {
            angka_ganjil[jumlah_ganjil] = A;
            jumlah_ganjil++;
        }
    }

    if (jumlah_genap == 0)
        printf("%.3f\n", median(angka_ganjil, jumlah_ganjil));
    else if (jumlah_ganjil == 0)
        printf("%.3f\n", median(angka_genap, jumlah_genap));
    else
        printf("%.3f\n", (median(angka_genap, jumlah_genap) + median(angka_ganjil, jumlah_ganjil)) / 2.0);

    return 0;
}