#include "gelas.h"
#include <stdio.h>

// MUCHAMMAD YUDA TRI ANANDA
//  NIM : 24060124110142

int main()
{
    Gelas gelas1 = {500, 0};
    Gelas gelas2 = {300, 0};

    printf("=== Demo Fungsi Gelas ===\n\n");

    printf("Status awal:\n");
    printf("Gelas 1:\n");
    tampilkanStatus(&gelas1);
    printf("\nGelas 2:\n");
    tampilkanStatus(&gelas2);

    printf("\n--- Mengisi gelas 1 hingga penuh ---\n");
    isiPenuh(&gelas1);
    tampilkanStatus(&gelas1);

    printf("\n--- Mengisi gelas 2 dengan 150ml ---\n");
    isiDengan(&gelas2, 150);
    tampilkanStatus(&gelas2);

    printf("\n--- Menuangkan dari gelas 1 ke gelas 2 ---\n");
    tuangKe(&gelas1, &gelas2);
    printf("Setelah menuang:\n");
    printf("Gelas 1:\n");
    tampilkanStatus(&gelas1);
    printf("\nGelas 2:\n");
    tampilkanStatus(&gelas2);

    printf("\n--- Mengosongkan gelas 1 ---\n");
    kosongkan(&gelas1);
    tampilkanStatus(&gelas1);

    printf("\n--- Mencoba mengisi gelas 2 dengan 200ml lagi ---\n");
    isiDengan(&gelas2, 200);
    tampilkanStatus(&gelas2);

    return 0;
}
