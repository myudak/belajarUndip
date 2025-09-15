#ifndef KALKULATOR_H
#define KALKULATOR_H

// Prosedur untuk menjumlahkan *a dengan b, hasil disimpan di *a
void tambah(int* a, int b);

// Prosedur untuk mengurangkan *a dengan b, hasil disimpan di *a
void kurang(int* a, int b);

// Prosedur untuk membagi *a dengan b, hasil disimpan di *a
void bagi(int* a, int b);

// Prosedur untuk mengalikan *a dengan b, hasil disimpan di *a
void kali(int* a, int b);

// Prosedur untuk menampilkan nilai a ke layar
void output(int a);

// Prosedur untuk menerima input operator (belum digunakan di main)
void inputOperator(char* x);

// Prosedur untuk menerima input nilai dan menyimpannya ke parameter
void inputNilai(int* x);

#endif // KALKULATOR_H