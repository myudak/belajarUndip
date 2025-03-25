/*
Nama File 		: Faktorial.c
Deskripsi 		: Menentukan Faktorial dari bilangan N
Pembuat   		: 24060124110142 - Muchammad Yuda Tri Ananda
Tgl Pembuatan   : 13 Maret 2025 - 14:51
*/

#include <stdio.h> /*header file*/

/*Program Utama*/
int main()
{
    /*Kamus*/
    int n, factorial = 1;

    printf("masukkan angka: ");
    scanf("%d", &n);

    /*Algoritma*/
    if (n < 0)
    {
        printf("Faktorial gak boleh negatif.\n  ");
    }
    else
    {
        for (int i = 1; i <= n; i++)
        {
            factorial *= i;
        }

        printf("Faktorial dari %d adalah %d\n", n, factorial);
    }

    return 0;
}
