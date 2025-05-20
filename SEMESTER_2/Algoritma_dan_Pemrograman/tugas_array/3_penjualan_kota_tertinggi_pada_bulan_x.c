#include <stdio.h>
#include <string.h>

/*
NAMA  : Muchammad Yuda Tri Ananda
NIM   : 24060124110142
TUGAS :
-----
3. Penjualan (kota) tertinggi pada bulan x

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
    char input_bulan[10];
    char bulan[4][10] = {"Jan", "Feb", "Mar", "Apr"};
    char kota[3][10] = {"Semarang", "Jakarta", "Yogyakarta"};
    int sales[3][4] = {
        {10, 15, 10, 5},
        {20, 25, 20, 15},
        {10, 5, 14, 3}};

    printf("Masukkan nama bulan (Jan/Feb/Mar/Apr): ");
    scanf("%s", input_bulan);

    int index_bulan = -1;
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(input_bulan, bulan[i]) == 0)
        {
            index_bulan = i;
            break;
        }
    }

    if (index_bulan == -1)
    {
        printf("Bulan gk ada");
        return 1;
    }

    int max_penjualan = sales[0][index_bulan];
    int index_kota = 0;

    for (int i = 1; i < 3; i++)
    {
        if (sales[i][index_bulan] > max_penjualan)
        {
            max_penjualan = sales[i][index_bulan];
            index_kota = i;
        }
    }

    printf("Saat: %s penjualan tertinggi pada kota: %s (%d)", input_bulan, kota[index_kota], max_penjualan);
    return 0;
}