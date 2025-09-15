#include "gelas.h"
#include <stdio.h>

// Mengisi gelas hingga penuh
void isiPenuh(Gelas *g)
{
    if (g != NULL)
    {
        g->isi = g->kapasitas;
    }
}

// Mengosongkan gelas
void kosongkan(Gelas *g)
{
    if (g != NULL)
    {
        g->isi = 0;
    }
}

// Mengisi gelas dengan sejumlah volume tertentu
void isiDengan(Gelas *g, int volume)
{
    if (g != NULL && volume >= 0)
    {

        int totalIsi = g->isi + volume;
        if (totalIsi <= g->kapasitas)
        {
            g->isi = totalIsi;
        }
        else
        {
            g->isi = g->kapasitas;
        }
    }
}

// Menuangkan isi dari satu gelas ke gelas lain
void tuangKe(Gelas *dari, Gelas *ke)
{
    if (dari != NULL && ke != NULL && dari->isi > 0)
    {

        int ruangKosong = ke->kapasitas - ke->isi;
        int volumeTuang;

        if (dari->isi <= ruangKosong)
        {

            volumeTuang = dari->isi;
        }
        else
        {

            volumeTuang = ruangKosong;
        }

        dari->isi -= volumeTuang;
        ke->isi += volumeTuang;
    }
}

// Menampilkan status gelas (kapasitas dan isi)
void tampilkanStatus(const Gelas *g)
{
    if (g != NULL)
    {
        printf("Status Gelas:\n");
        printf("  Kapasitas: %d ml\n", g->kapasitas);
        printf("  Isi saat ini: %d ml\n", g->isi);
        printf("  Ruang kosong: %d ml\n", g->kapasitas - g->isi);

        if (g->isi == 0)
        {
            printf("  Status: Kosong\n");
        }
        else if (g->isi == g->kapasitas)
        {
            printf("  Status: Penuh\n");
        }
        else
        {
            printf("  Status: Terisi sebagian\n");
        }
    }
}
