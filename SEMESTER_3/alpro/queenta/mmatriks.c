/* Program   : mmatriks.c */
/* Deskripsi : driver ADT matriks integer */
/* NIM/Nama  : 24060124120016 / Quinta Aurabiansyah */
/* Tanggal   : 19-09-2025 */
/***********************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "matriks.h"


void show_matriks(Matriks M, char *matrixName)
{
	printf("--- Isi Matriks %s (%dx%d) ---\n", matrixName, getNBaris(M), getNKolom(M));
	if (isEmptyMatriks(M))
	{
		printf("(Kosong)\n");
		return;
	}
	for (int i = 1; i <= getNBaris(M); i++)
	{
		for (int j = 1; j <= getNKolom(M); j++)
		{
			printf("%d\t", M.cell[i][j]);
		}
		printf("\n");
	}
}

int main()
{
	/* KAMUS */
	Matriks M1, M2, M3, MHasil;
	int r, c;

	printf("1. UJI KONSTRUKTOR & PENGISIAN");
	initMatriks(&M1);
	printf("M1 dibuat. Apakah kosong? %s\n", isEmptyMatriks(M1) ? "Ya" : "Tidak");

	printf("\nMengisi M1 3x3 dengan isiMatriksRandom...\n");
	isiMatriksRandom(&M1, 3, 3);
	show_matriks(M1, "M1");

	initMatriks(&M2);
	printf("\nMengisi M2 3x3 dengan matriks identitas...\n");
	isiMatriksIdentitas(&M2, 3);
	show_matriks(M2, "M2");

	printf("2. UJI OPERASI ARITMATIKA");
	MHasil = addMatriks(M1, M2);
	show_matriks(MHasil, "M1 + M2");

	MHasil = subMatriks(M1, M2);
	show_matriks(MHasil, "M1 - M2");

	initMatriks(&M3);
	isiMatriksRandom(&M3, 3, 2); // Buat matriks 3x2
	show_matriks(M1, "M1 (3x3)");
	show_matriks(M3, "M3 (3x2)");
	MHasil = kaliMatriks(M1, M3);
	show_matriks(MHasil, "M1 * M3");

	MHasil = kaliSkalarMatriks(M1, 10);
	show_matriks(MHasil, "M1 * 10");

	
	return 0;
}
