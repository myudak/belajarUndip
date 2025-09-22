#include <stdio.h>
#include "tabel.h"

/* Deskripsi : driver ADT tabel integer */
/* NIM/Nama : 24060124110142 / Muchammad Yuda Tri Ananda */
/* Tanggal : 12/09/2025*/

int main()
{
	// kamus
	Tabel T, U, INV, P;
	int pos, N;

	// algoritma
	printf("== kondisi awal ==\n");
	createTable(&T);
	printf("size = %d, empty=%d, full=%d\n", getSize(T), isEmptyTable(T), isFullTable(T));
	printTable(T);

	printf("\n== Add elemen (D,A,B,A,C) ==\n");
	addXTable(&T, 'D');
	addXTable(&T, 'A');
	addXTable(&T, 'B');
	addXTable(&T, 'A');
	addXTable(&T, 'C');
	viewTable(T);

	printf("cari 'B' -> ");
	searchX(T, 'B', &pos);
	printf("pos=%d\n", pos);
	printf("cari 'Z' -> ");
	searchX(T, 'Z', &pos);
	printf("pos=%d (harusnya -999)\n", pos);

	printf("jumlah 'A' = %d\n", countX(T, 'A'));
	printf("jumlah huruf vokal = %d\n", countVocal(T));

	printf("\n== addUniqueXTable('C') dan addUniqueXTable('E') ==\n");
	addUniqueXTable(&T, 'C'); // duplikat, diabaikan
	addUniqueXTable(&T, 'E'); // baru, ditambahkan
	viewTable(T);
	printf("ukuran = %d\n", getSize(T));

	printf("\n== delXTable('A') (hapus 'A' pertama) ==\n");
	delXTable(&T, 'A');
	viewTable(T);

	printf("\n== delTable(indeks=2) ==\n");
	delTable(&T, 2);
	viewTable(T);

	printf("\n== Tambah 'B','B' terus delAllXTable('B') ==\n");
	addXTable(&T, 'B');
	addXTable(&T, 'B');
	viewTable(T);
	delAllXTable(&T, 'B');
	viewTable(T);

	printf("\nModus(T) = '%c'\n", (char)Modus(T));

	printf("\n== isEqualTable(T,U) ==\n");
	createTable(&U);
	addXTable(&U, 'D');
	addXTable(&U, 'A');
	addXTable(&U, 'C');
	addXTable(&U, 'E');

	printf("T = ");
	viewTable(T);
	printf("U = ");
	viewTable(U);

	printf("sama? %d\n", isEqualTable(T, U));
	addXTable(&U, 'Z');
	printf("setelah tambah 'Z' ke U, sama? %d\n", isEqualTable(T, U));

	printf("\n== getInverseTable dan inverseTable ==\n");
	INV = getInverseTable(T);
	printf("T   = ");
	viewTable(T);
	printf("INV = ");
	viewTable(INV);
	inverseTable(&T);
	printf("T setelah dibalik = ");
	viewTable(T);

	printf("\n== sortAsc terus sortDesc ==\n");
	sortAsc(&T);
	viewTable(T);
	sortDesc(&T);
	viewTable(T);

	printf("\n== printTable (10 slot tetap) ==\n");
	printTable(T);

	printf("\n== populateTable demo ==\n");
	createTable(&P);
	printf("Masukkan N (1..10): ");
	scanf("%d", &N);
	printf("Masukkan %d karakter (pisahkan dengan spasi/newline): ", N);
	populateTable(&P, N);
	printf("P = ");
	viewTable(P);

	return 0;
}
