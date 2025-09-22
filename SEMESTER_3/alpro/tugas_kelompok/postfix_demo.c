#include <stdio.h>
#include "stack.h"

int main(void)
{
    const char *expression = "9 3 * 8 + 4 /";
    double result;

    if (evaluatePostfix(expression, &result))
    {
        printf("Ekspresi: %s\n", expression);
        printf("Hasil: %.2f\n", result);
    }
    else
    {
        printf("Ekspresi tidak valid.\n");
    }

    return 0;
}
