#include <stdio.h>

int main()
{

    int kartu, suit;

    if (kartu == 11)
        printf("Jack");
    else if (kartu == 12)
        printf("Queen");
    else if (kartu == 13)
        printf("King");
    else if (kartu == 14)
        printf("Ace");
    else
        printf("%d", kartu);

    if (suit == 1)
        printf("Diamond");
    else if (suit == 2)
        printf("Spade");
    else if (suit == 3)
        printf("Heart");
    else if (suit == 4)
        printf("Club");

    int kartuka, kartuki;

    scanf("%d %d", &kartuka, &kartuki);

    int kartu1 = kartuka / 10, suit1 = kartuka % 10;
    int kartu2 = kartuki / 10, suit2 = kartuki % 10;

    printf("masukkan kartu kanan:\n");
    scanf("%d", &kartu1);
    printf("masukkan kartu kiri:\n");
    scanf("%d", &kartu2);

    if (kartu1 > kartu2)
    {
        printf("%d", kartu1);
        printf("of");
        printf(suit1);
        return 0;
    }
    if (kartu1 == kartu2)
    {
        printf(kartu1);
        printf("of");
        printf(suit1, suit2);
        return 0;
    }
    if (kartu2 > kartu1)
    {
        printf(kartu2);
        printf("of");
        printf(suit2);
        return 0;
    }
}