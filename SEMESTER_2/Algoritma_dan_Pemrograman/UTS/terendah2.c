#include <stdio.h>

int main()
{
    int T[100];     // tabel T maximal size 100
    int N;          // jumlah elemen tabel T
    int count;      // variabel untuk menampilkan elemen tabel T yang frekuensi kemunculannya lebih dari satu kali
    int i, j, k;    // variabel untuk menjalankan loop
    int sudahPrint; // variabel untuk menampilkan elemen tabel T yang frekuensi kemunculannya lebih dari satu kali
    int sum;        // variabel untuk menampilkan jumlah nilai-nilai elemen tabel T yang frekuensi kemunculannya lebih dari satu kali

    printf("Masukkan jumlah data T: ");
    scanf("%d", &N);

    for (i = 0; i < N; i++)
    {
        printf("Masukkan data T[%d]: ", i);
        scanf("%d", &T[i]);
    }

    for (i = 0; i < N; i++)
    {
        count = 0;
        for (j = 0; j < N; j++)
        {
            if (T[i] == T[j])
                count++;
        }

        if (count > 1)
        {
            sudahPrint = 0;
            for (k = 0; k < i; k++)
            {
                if (T[i] == T[k])
                {
                    sudahPrint = 1;
                    break;
                }
            }
            if (!sudahPrint)
            {
                sum += T[i] * count;
            }
        }
    }

    printf("jumlah elemen tabel T yang frekuensi kemunculannya lebih dari satu kali adalah %d", sum);

    return 0;
}