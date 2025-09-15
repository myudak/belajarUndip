#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

/*
    NAMA : Muchammad Yuda Tri Ananda
    NIM : 24060124110142
    KELAS : D
    LAB : D2
*/

int main()
{

    int N, X;
    scanf("%d %d", &N, &X);
    int A[N];

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
    }

    int jawaban = A[0];

    int selisih_min = 0;
    if (A[0] > X)
    {
        selisih_min = A[0] - X;
    }
    else
    {
        selisih_min = X - A[0];
    }

    for (int i = 1; i < N; i++)
    {
        int selising_skrg = 0;
        if (A[i] > X)
        {
            selising_skrg = A[i] - X;
        }
        else
        {
            selising_skrg = X - A[i];
        }

        if (selising_skrg < selisih_min)
        {
            jawaban = A[i];
            selisih_min = selising_skrg;
        }
        else if (selising_skrg == selisih_min)
        {
            if (A[i] < jawaban)
            {
                jawaban = A[i];
            }
        }
    }
    printf("%d\n", jawaban);

    return 0;
}