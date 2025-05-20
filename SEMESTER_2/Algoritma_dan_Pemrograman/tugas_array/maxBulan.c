#include <stdio.h>
#include <string.h>

int main() {
    int i, j, maxJual, iBulan, iKota;
    int tabel[3][4] = {{10, 15, 10, 5}, {20, 25, 20, 15}, {10, 5, 14, 3}};
    char inputKota[20];
    char bulan[4][10] = {"Januari", "Februari", "Maret", "April"};
    char kota[3][20] = {"Semarang", "Jakarta", "Yogyakarta"};

    printf("Masukkan nama kota: ");
    scanf("%s", inputKota);

    iKota = -1;
    for (i = 0; i < 3; i++) {
        if (strcmp(inputKota, kota[i]) == 0) {
            iKota = i;
            break;
        }
    }

    if (iKota == -1) {
        printf("Kota tidak ditemukan.");
        return 1;
    }

    maxJual = tabel[iKota][0];
    iBulan = 0;

    for (i = 1; i < 4; i++) {
        if (maxJual < tabel[iKota][i]) {
            maxJual = tabel[iKota][i];
            iBulan = i;
        }
    }

    printf("Penjualan tertinggi pada Kota %s adalah bulan %s dengan jumlah %d.", inputKota, bulan[iBulan], maxJual);

    return 0;
}