#include <stdio.h>

int main() {
    // Kamus
    float uang_sekarang, bunga, tahun, uang_masa_depan;

    // Algo
    // printf("=== Kalkulator Uang Masa Depan ===\n");
    // printf("Masukkan jumlah uang saat ini (Rp): ");
    scanf("%f", &uang_sekarang);

    // printf("Masukkan bunga per tahun (%%): ");
    scanf("%f", &bunga);

    // printf("Masukkan jumlah tahun: ");
    scanf("%f", &tahun);

    uang_masa_depan = uang_sekarang + (uang_sekarang * (bunga / 100) * tahun);

    printf("Uang Lu setelah %.0f tahun adalah: Rp %.2f", tahun, uang_masa_depan);

    return 0;
}
