#include <stdio.h>
#include <string.h>

/*
NAMA  : Muchammad Yuda Tri Ananda
NIM   : 24060124110142
TUGAS :
-----
4. penjualan (bulan) tertinggi pada kota x


Tabel Penjualan:
----------------
| Kota        | Jan | Feb | Mar | Apr |
|-------------|-----|-----|-----|-----|
| Semarang    | 10  | 15  | 10  | 5   |
| Jakarta     | 20  | 25  | 20  | 15  |
| Yogyakarta  | 10  | 5   | 14  | 3   |

Contoh Input: "Jakarta"
Contoh Output: Kota: Jakarta dengan penjualan tertinggi saat: Februari (25)
*/

int main()
{
    char input_kota[20];
    char kota[3][20] = {"Semarang", "Jakarta", "Yogyakarta"};
    char bulan[4][10] = {"Januari", "Februari", "Maret", "April"};
    int sales[3][4] = {
        {10, 15, 10, 5},
        {20, 25, 20, 15},
        {10, 5, 14, 3}};

    printf("Masukkan nama kota (Jakarta/Semarang/Yogyakarta): ");
    scanf("%s", input_kota);

    int index_kota = -1;

    for (int i = 0; i < 3; i++) {
        if (strcmp(input_kota, kota[i]) == 0) {
            index_kota = i;
            break;
        }
    }

    if (index_kota == -1) {
        printf("Kota gak ada");
        return 1;
    }

    int max_penjualan = sales[index_kota][0];
    int index_bulan = 0;

    for (int j = 1; j < 4; j++) {
        if (sales[index_kota][j] > max_penjualan) {
            max_penjualan = sales[index_kota][j];
            index_bulan = j;
        }
    }

    printf("Kota: %s dengan penjualan tertinggi saat: %s (%d)", kota[index_kota], bulan[index_bulan], max_penjualan);
    return 0;
}
