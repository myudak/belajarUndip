/*
Nama File 		: hitungTahanan.c
Deskripsi 		: Menjumlahkan 3 buah input tahanan berupa bilangan integer positif dan tidak boleh ada inputan yang negatif
Pembuat   		: 24060124110142 - Muchammad Yuda Tri Ananda
Tgl Pembuatan   : 3 Maret 2025 - 16:55
*/

#include <stdio.h> /*header file*/

/*Program Utama*/
int main()
{
    /*Kamus*/
    int a, b, c;
    printf("Masukkan tahanan 1 = ");
    scanf("%d", &a);
    printf("Masukkan tahanan 2 = ");
    scanf("%d", &b);
    printf("Masukkan tahanan 3 = ");
    scanf("%d", &c);

    /*Algoritma*/
    if (a < 0 || b < 0 || c < 0)
    {
        printf("Masukan tahanan tidak boleh negatif");
        return 0;
    }

    printf("Hasil tahanan = %d", a + b + c);

    return 0;
}