#ifndef GELAS_H
#define GELAS_H

// Mendefinisikan tipe data Gelas
typedef struct {
    int kapasitas;   // Kapasitas maksimum gelas (ml)
    int isi;         // Isi saat ini (ml)
} Gelas;

// Mengisi gelas hingga penuh
void isiPenuh(Gelas* g);

// Mengosongkan gelas
void kosongkan(Gelas* g);

// Mengisi gelas dengan sejumlah volume tertentu
void isiDengan(Gelas* g, int volume);

// Menuangkan isi dari satu gelas ke gelas lain
void tuangKe(Gelas* dari, Gelas* ke);

// Menampilkan status gelas (kapasitas dan isi)
void tampilkanStatus(const Gelas* g);

#endif // GELAS_H