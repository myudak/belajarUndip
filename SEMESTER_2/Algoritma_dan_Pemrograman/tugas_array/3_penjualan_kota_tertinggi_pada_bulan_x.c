#include <stdio.h>
#include <string.h>

/*
NAMA  : Muchammad Yuda Tri Ananda
NIM   : 24060124110142
TUGAS :
-----
3. penjualan (kota) tertinggi pada bulan x

Tabel Penjualan:
----------------
| Kota        | Jan | Feb | Mar | Apr |
|-------------|-----|-----|-----|-----|
| Semarang    | 10  | 15  | 10  | 5   |
| Jakarta     | 20  | 25  | 20  | 15  |
| Yogyakarta  | 10  | 5   | 14  | 3   |

Contoh Input: "Feb"
Contoh Output: Saat: Feb penjualan tertinggi pada kota: Jakarta (25)
*/

int main()
{
    char input_bulan[3];
    char kota[3][20] = {"Semarang", "Jakarta", "Yogyakarta"};
    char bulan[4][10] = {"Jan", "Feb", "Mar", "Apr"};
    int sales[3][4] = {
        {10, 15, 10, 5},
        {20, 25, 20, 15},
        {10, 5, 14, 3}};

    printf("Masukkan nama bulan: ");
    scanf("%s", input_bulan);

    int index_bulan = -1;

    for (int i = 0; i < 3; i++)
    {
        if (strcmp(input_bulan, bulan[i]) == 0)
        {
            index_bulan = i;
            break;
        }
    }

    if (index_bulan == -1)
    {
        printf("Bulan gak ada");
        return 1;
    }

    int max_penjualan = sales[index_bulan][0];
    int index_bulan = 0;

    for (int j = 0; j < 3; j++)
    {
        if (sales[index_bulan][j] > max_penjualan)
        {
            max_penjualan = sales[index_bulan][j];
            index_bulan = j;
        }
    }

    printf("Saat: %s penjualan tertinggi pada kota: %s (25)\n", kota[index_bulan], bulan[index_bulan], max_penjualan);
    return 0;
}
