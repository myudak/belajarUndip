#include <stdio.h>

/*
NAMA  : Muchammad Yuda Tri Ananda
NIM   : 24060124110142
TUGAS :
-----
6. Penjualan terendah keseluruhan (outputnya kota, bulan, nilai)

Tabel Penjualan:
----------------
| Kota        | Jan | Feb | Mar | Apr |
|-------------|-----|-----|-----|-----|
| Semarang    | 10  | 15  | 10  | 5   |
| Jakarta     | 20  | 25  | 20  | 15  |
| Yogyakarta  | 10  | 5   | 14  | 3   |

Output: Yogyakarta, April, 3
*/

int main()
{
    char kota[3][20] = {"Semarang", "Jakarta", "Yogyakarta"};
    char bulan[4][10] = {"Januari", "Februari", "Maret", "April"};
    int sales[3][4] = {
        {10, 15, 10, 5},
        {20, 25, 20, 15},
        {10, 5, 14, 3}};

    int min_sales = sales[0][0];
    int min_kota = 0;
    int min_bulan = 0;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (sales[i][j] < min_sales)
            {
                min_sales = sales[i][j];
                min_kota = i;
                min_bulan = j;
            }
        }
    }

    printf("%s, %s, %d", kota[min_kota], bulan[min_bulan], min_sales);
    return 0;
}
