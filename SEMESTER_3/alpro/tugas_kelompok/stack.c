/* Program   : stack.c */
/* Deskripsi : file BODY modul stack karakter */
/* NIM/Nama  : 24060124120013/Muhamad Kemal Faza */
/* Tanggal   : 21-09-2025 */
/***********************************/

#include "stack.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NUM_STACK 50

typedef struct
{
    double wadah[MAX_NUM_STACK + 1];
    int top;
} TNumStack;

static void createNumStack(TNumStack *S)
{
    S->top = 0;
}

static boolean isEmptyNumStack(TNumStack S)
{
    return S.top == 0;
}

static boolean isFullNumStack(TNumStack S)
{
    return S.top == MAX_NUM_STACK;
}

static boolean pushNum(TNumStack *S, double value)
{
    if (isFullNumStack(*S))
    {
        return false;
    }
    S->top++;
    S->wadah[S->top] = value;
    return true;
}

static boolean popNum(TNumStack *S, double *value)
{
    if (isEmptyNumStack(*S))
    {
        return false;
    }
    *value = S->wadah[S->top];
    S->top--;
    return true;
}

/* KONSTRUKTOR */
/* procedure createStack(output S: Tstack)
    {I.S.: - }
    {F.S.: Stack S terdefinisi}
    {Proses mengisi elemen wadah kosong dengan '_', top 0} */
void createStack(Tstack *S)
{
    (*S).top = 0;
    for (int i = 1; i <= 10; i++)
    {
        (*S).wadah[i] = '_';
    }
}

/* SELEKTOR */
/* function infoTop(S: Tstack) -> character
    {mengembalikan nilai elemen puncak} */
int infoTop(Tstack S)
{
    if (S.top > 0)
    {
        return S.wadah[top(S)];
    }
    return -1; // Menandakan stack kosong
}

/* function top(S: Tstack) -> integer
    {mengembalikan posisi puncak} */
int top(Tstack S)
{
    return S.top;
}

/* PREDIKAT */
/* function isEmptyStack(S: Tstack) -> boolean
    {mengembalikan True jika matriks M kosong } */
boolean isEmptyStack(Tstack S)
{
    return (S.top == 0);
}

/* function isFullStack(S: Tstack) -> boolean
    {mengembalikan True jika matriks M penuh } */
boolean isFullStack(Tstack S)
{
    return (S.top == 10);
}

/* MUTATOR */
/* procedure push(input/output S:Tstack, input e:character)
    {I.S.: S, e terdefinisi, S mungkin kosong}
    {F.S.: S tetap, atau infoTop(S) = e}
    {Proses: mengisi elemen e ke puncak S, bila belum penuh} */
void push(Tstack *S, char e)
{
    if (!isFullStack(*S))
    {
        (*S).top++;
        (*S).wadah[(*S).top] = e;
    }
}

/* procedure push(input/output S:Tstack, output e:character)
    {I.S.: S terdefinisi, mungkin kosong}
    {F.S.: S tetap, atau e berisi infoTop(S) lama}
    {Proses: menghapus elemen e dari puncak S, bila belum kosong} */
void pop(Tstack *S, char *e)
{
    if (!isEmptyStack(*S))
    {
        *e = (*S).wadah[(*S).top];
        (*S).wadah[(*S).top] = '_';
        (*S).top--;
    }
}

/* procedure printStack(input S:Tstack)
    {I.S.: S terdefinisi}
    {F.S.: -}
    {Proses: menampilkan semua elemen S ke layar} */
void printStack(Tstack S)
{
    for (int i = 1; i <= 10; i++)
    {
        printf("%c ", S.wadah[i]);
    }
    printf("\n");
}

/* procedure viewStack (input S:Tstack)
    {I.S.: M terdefinisi}
    {F.S.: -}
    {Proses: menampilkan elemen S yang terisi ke layar} */
void viewStack(Tstack S)
{
    for (int i = 1; i <= S.top; i++)
    {
        printf("%c ", S.wadah[i]);
    }
    printf("\n");
}

/* OPERASI LAINNYA */
boolean isValidKurung(char *str)
{
    Tstack S;
    createStack(&S);
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == '(' || str[i] == '{' || str[i] == '[')
        {
            push(&S, str[i]);
        }
        else if (str[i] == ')' || str[i] == '}' || str[i] == ']')
        {
            if (isEmptyStack(S))
            {
                return false;
            }
            char temp;
            pop(&S, &temp);

            if ((str[i] == ')' && temp != '(') ||
                (str[i] == '}' && temp != '{') ||
                (str[i] == ']' && temp != '['))
            {
                return false;
            }
        }
    }
    return isEmptyStack(S);
}
boolean evaluatePostfix(const char *expr, double *result)
{
    if (expr == NULL || result == NULL)
    {
        return false;
    }

    size_t length = strlen(expr);
    char *buffer = (char *)malloc(length + 1);
    if (buffer == NULL)
    {
        return false;
    }
    strcpy(buffer, expr);

    TNumStack stack;
    createNumStack(&stack);

    char *token = strtok(buffer, " \t\r\n");
    while (token != NULL)
    {
        if (strlen(token) == 1 && strchr("+-*/", token[0]) != NULL)
        {
            double right;
            double left;
            if (!popNum(&stack, &right) || !popNum(&stack, &left))
            {
                free(buffer);
                return false;
            }

            double value = 0.0;
            switch (token[0])
            {
            case '+':
                value = left + right;
                break;
            case '-':
                value = left - right;
                break;
            case '*':
                value = left * right;
                break;
            case '/':
                if (right == 0.0)
                {
                    free(buffer);
                    return false;
                }
                value = left / right;
                break;
            default:
                free(buffer);
                return false;
            }

            if (!pushNum(&stack, value))
            {
                free(buffer);
                return false;
            }
        }
        else
        {
            char *endPtr;
            double value = strtod(token, &endPtr);
            if (token == endPtr || *endPtr != '\0')
            {
                free(buffer);
                return false;
            }

            if (!pushNum(&stack, value))
            {
                free(buffer);
                return false;
            }
        }

        token = strtok(NULL, " \t\r\n");
    }

    free(buffer);

    double finalValue;
    if (!popNum(&stack, &finalValue) || !isEmptyNumStack(stack))
    {
        return false;
    }

    *result = finalValue;
    return true;
}
