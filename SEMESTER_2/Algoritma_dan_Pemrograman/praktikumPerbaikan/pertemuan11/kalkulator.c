#include <stdio.h>
#include "kalkulator.h"


void tambah(int* a, int b) {
    *a += b;
}
void kurang(int* a, int b) {
    *a -= b;
}
void bagi(int* a, int b) {
    *a /= b;
}
void kali(int* a, int b) {
    *a *= b;
}

void output(int a) {
    printf("%d\n", a);
}

void inputOperator(char* x) {
    scanf(" %c", x);
}

void inputNilai(int* x) {
    scanf("%d", x);
}