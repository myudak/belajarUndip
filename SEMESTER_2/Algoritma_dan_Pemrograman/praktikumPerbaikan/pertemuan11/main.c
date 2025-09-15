#include <stdio.h>
#include "kalkulator.h"

int main()
{
    // Kamus
    char op;
    int a, b;
    // algoritma
    while (1)
    {
        printf("Masukkan operator (+, -, *, /) atau Q untuk keluar: ");
        inputOperator(&op);
        if (op == 'Q' || op == 'q') {
            break;
        }
        printf("Operator yang dimasukkan: %c\n", op);
        printf("Masukkan dua angka: ");
        inputNilai(&a);
        inputNilai(&b);

        switch (op) {
            case '+':
                tambah(&a, b);
                output(a);
                break;
            case '-':
                kurang(&a, b);
                output(a);
                break;
            case '*':
                kali(&a, b);
                output(a);
                break;
            case '/':
                if (b != 0) {
                    bagi(&a, b);
                    output(a);
                } else {
                    printf("Error: Pembagi tidak boleh nol!\n");
                }
                break;
            default:
                printf("Operator tidak dikenali!\n");
        }
    }
    printf("Terima kasih!\n");
    return 0;
}