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
    int Y[Q];

    for (int i = 0; i < Q; i++)
    {
        scanf("%d %d", &X[i], &Y[i]);
    }

    for (int i = 0; i < Q; i++)
    {
        int count = 0;
        for (int j = 0; j < N; j++)
        {
            if (A[j] > X[i] && A[j] <= Y[i])
            {
                count++;
            }
        }
        printf("%d\n", count);
    }

    return 0;
}