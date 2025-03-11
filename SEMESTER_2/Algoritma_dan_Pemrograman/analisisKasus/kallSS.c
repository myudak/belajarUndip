/*
Nama File 		: kallSS.c
Deskripsi 		: Membuat kalkulator sederhana dengan 2 buah inputan berupa bilangan integer dan 1 input berupa character sebagai operator aritmatika
Pembuat   		: 24060124110142 - Muchammad Yuda Tri Ananda
Tgl Pembuatan   : 3 Maret 2025 - 11:28
*/

#include <stdio.h> /*header file*/

/*Program Utama*/
int main()
{
    /*Kamus*/
    int a, b;
    char operator;
    printf("Masukkan angka pertama = ");
    scanf("%d", &a);
    printf("Masukkan angka kedua = ");
    scanf("%d", &b);
    printf("Operator :\na = +\nb = -\nc = *\nd = /\ne = div\nf = mod\nMasukkan operator = ");
    scanf(" %c", &operator);

    /*Algoritma*/
    if (operator!= 'a' && operator!= 'b' && operator!= 'c' && operator!= 'd' && operator!= 'e' && operator!= 'f')
    {
        printf("Bukan pilihan menu yang benar");
        return 0;
    }

    switch (operator)
    {
    case 'a':
        printf("Hasil = %d", a + b);
        break;
    case 'b':
        printf("Hasil = %d", a - b);
        break;
    case 'c':
        printf("Hasil = %d", a * b);
        break;
    case 'd':
        if (b == 0)
        {
            printf("Pembagi tidak boleh 0!");
            break;
        }
        printf("Hasil = %.2f", (float)a / b);
        break;
    case 'e':
        if (b == 0)
        {
            printf("Pembagi tidak boleh 0!");
            break;
        }
        printf("Hasil = %d", a / b);
        break;
    case 'f':
        printf("Hasil = %d", a % b);
        break;
    }
    return 0;
}