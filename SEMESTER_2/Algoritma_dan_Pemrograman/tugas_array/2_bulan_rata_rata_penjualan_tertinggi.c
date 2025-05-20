#include <stdio.h>

/*
NAMA  : Muchammad Yuda Tri Ananda
NIM   : 24060124110142
TUGAS :
-----
2. Bulan rata rata penjualan tertinggi

Tabel Penjualan:
----------------
| Kota        | Jan | Feb | Mar | Apr |
|-------------|-----|-----|-----|-----|
| Semarang    | 10  | 15  | 10  | 5   |
| Jakarta     | 20  | 25  | 20  | 15  |
| Yogyakarta  | 10  | 5   | 14  | 3   |

Expected Output:
---------------
Bulan dengan rata-rata penjualan tertinggi: Februari (15.00)
*/

int main()
{
    char bulan[4][10] = {"Januari", "Februari", "Maret", "April"};
    int sales[3][4] = {
        {10, 15, 10, 5},
        {20, 25, 20, 15},
        {10, 5, 14, 3}};
    float rata_max = 0.0;
    int index_max = 0;

    for (int i = 0; i < 4; i++)
    {
        float jumlah = 0;
        for (int j = 0; j < 3; j++)
        {
            jumlah += sales[j][i];
        }

        float rata = jumlah / 3.0;
        if (rata > rata_max)
        {
            rata_max = rata;
            index_max = i;
        }
    }

    printf("Bulan dengan rata-rata penjualan tertinggi: %s (%.2f)\n", bulan[index_max], rata_max);
    return 0;
}