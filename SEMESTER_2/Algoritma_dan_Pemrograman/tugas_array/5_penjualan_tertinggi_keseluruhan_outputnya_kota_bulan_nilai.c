#include <stdio.h>

/*
NAMA  : Muchammad Yuda Tri Ananda
NIM   : 24060124110142
TUGAS :
-----
5. Penjualan tertinggi keseluruhan (outputnya kota, bulan, nilai)

Tabel Penjualan:
----------------
| Kota        | Jan | Feb | Mar | Apr |
|-------------|-----|-----|-----|-----|
| Semarang    | 10  | 15  | 10  | 5   |
| Jakarta     | 20  | 25  | 20  | 15  |
| Yogyakarta  | 10  | 5   | 14  | 3   |

Output: Jakarta, Februari, 25
*/

int main()
{
    char kota[3][20] = {"Semarang", "Jakarta", "Yogyakarta"};
    char bulan[4][10] = {"Januari", "Februari", "Maret", "April"};
    int sales[3][4] = {
        {10, 15, 10, 5},
        {20, 25, 20, 15},
        {10, 5, 14, 3}};

    int max_sales = sales[0][0];
    int max_kota = 0;
    int max_bulan = 0;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (sales[i][j] > max_sales)
            {
                max_sales = sales[i][j];
                max_kota = i;
                max_bulan = j;
            }
        }
    }

    printf("%s, %s, %d\n", kota[max_kota], bulan[max_bulan], max_sales);
    return 0;
}
