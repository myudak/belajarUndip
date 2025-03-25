#include <stdio.h>

int main()
{
    int N;
    int banyakHi = 0;

    scanf("%d", &N);

    int hi[N];

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &hi[i]);
    }

    int rataHi = 0;

    for (int i = 0; i < N; i++)
    {
        rataHi += hi[i];
    }
    rataHi /= N;

    for (int i = 0; i < N; i++)
    {
        if (hi[i] >= rataHi)
        {
            banyakHi++;
        }
    }

    printf(" banyak ksatria yang lebih dari rata-rata: %d\n", banyakHi);

    return 0;
}
