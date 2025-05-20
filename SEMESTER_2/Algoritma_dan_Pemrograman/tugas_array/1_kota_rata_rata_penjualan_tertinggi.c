#include <stdio.h>

/*
NAMA  : Muchammad Yuda Tri Ananda
NIM   : 24060124110142
TUGAS :
-----
1. kota rata rata penjualan tertinggi

Tabel Penjualan:
----------------
| Kota        | Jan | Feb | Mar | Apr |
|-------------|-----|-----|-----|-----|
| Semarang    | 10  | 15  | 10  | 5   |
| Jakarta     | 20  | 25  | 20  | 15  |
| Yogyakarta  | 10  | 5   | 14  | 3   |

Expected Output:
---------------
Kota dengan rata-rata penjualan tertinggi: Jakarta (20.00)
*/

int main()
{
    char kota[3][10] = {"Semarang", "Jakarta", "Yogyakarta"};
    int sales[3][4] = {
        {10, 15, 10, 5},
        {20, 25, 20, 15},
        {10, 5, 14, 3}};
    float rata_max = 0.0;
    int index_max = 0;

    for (int i = 0; i < 3; i++)
    {
        float jumlah = 0;
        for (int j = 0; j < 4; j++)
        {
            jumlah += sales[i][j];
        }

        float rata = jumlah / 4.0;
        if (rata > rata_max)
        {
            rata_max = rata;
            index_max = i;
        }
    }

    printf("Kota dengan rata-rata penjualan tertinggi: %s (%.2f)\n", kota[index_max], rata_max);
    return 0;
}