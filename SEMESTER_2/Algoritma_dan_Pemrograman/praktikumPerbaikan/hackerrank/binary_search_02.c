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
    int N;
    scanf("%d", &N);

    int A[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
    }

    int Q;
    scanf("%d", &Q);

    int X[Q];
    for (int i = 0; i < Q; i++)
    {
        scanf("%d", &X[i]);
    }

    for (int i = 0; i < Q; i++)
    {
        int jawaban = 0;

        int kanan = 1;
        for (int kiri = 0; kiri < N; kiri++)
        {
            if (X[i] <= A[kiri])
            {
                jawaban = kiri + 1;
                break;
            }
            else if (X[i] - A[kiri] <= A[kanan])
            {
                jawaban = kanan + 1;
                break;
            }
            else
            {
                kanan++;
                X[i] -= A[kiri];
            }
        }
        printf("%d\n", jawaban);
    }

    return 0;
}