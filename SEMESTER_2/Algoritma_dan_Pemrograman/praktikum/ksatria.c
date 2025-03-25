#include <stdio.h>

int main()
{
    /*Kamus*/

    int N;
    printf("Banyak Ksatria: ");
    scanf("%d", &N);

    int hp[100];
    int alive[100];

    printf("HP KSATRIA:\n");
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &hp[i]);
    }

    // Initialize ksatria hidup
    for (int i = 0; i < N; i++)
    {
        alive[i] = 1;
    }

    int countHidup = N;
    int curentKsatria = 0; // Start with the first knight

    // Continue until only one knight remains
    while (countHidup > 1)
    {
        // Find the next alive knight to attack
        int targetKsatria = curentKsatria;
        do
        {
            targetKsatria = (targetKsatria + 1) % N;
        } while (alive[targetKsatria] == 0);

        // Attack the target knight
        hp[targetKsatria]--;

        // Check if the target knight died
        if (hp[targetKsatria] == 0)
        {
            alive[targetKsatria] = 0;
            countHidup--;
        }

        // Move to the next alive knight
        do
        {
            curentKsatria = (curentKsatria + 1) % N;
        } while (alive[curentKsatria] == 0 && countHidup > 1);
    }

    // Find the last knight standing
    int lastKnight = 0;
    for (int i = 0; i < N; i++)
    {
        if (alive[i] == 1)
        {
            lastKnight = i + 1; // +1 because knights are numbered from 1
            break;
        }
    }

    printf("Ksatria terakhir: %d\n", lastKnight);

    return 0;
}