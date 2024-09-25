def diskon(harga, persen):
    return harga - (harga * persen / 100)


def pajak(harga, persen):
    return harga + (harga * persen / 100)


def AturanDiskon(harga, kategori, VIP):
    if kategori == "elektronik":
        if VIP == True:
            return diskon(harga, 30)
        return diskon(harga, 10)

    if kategori == "pakaian":
        if VIP == True:
            return diskon(harga, 20)
        return diskon(harga, 5)

    if kategori == "makanan":
        if VIP == True:
            return diskon(harga, 15)
        return diskon(harga, 2)
    return harga


def AturanPajak(harga, lokasi):
    if lokasi == "dalam negeri":
        return pajak(harga, 10)

    if lokasi == "luar negeri":
        return pajak(harga, 20)


def AturanHari(harga, kategori, VIP, hari):
    if hari == "jumat" or hari == "sabtu":
        if VIP == True:
            return diskon(harga, 5)
        else:
            return harga

    if hari == "minggu":
        return diskon(harga, 5)

    if hari == "rabu":
        if kategori == "pakaian":
            return diskon(harga, 5)


def hargaAkhir(harga, kategori, VIP, lokasi, hari):
    hargaSetelahDiskon = AturanDiskon(harga, kategori, VIP)
    hargaSetelahHari = AturanHari(hargaSetelahDiskon, kategori, VIP, hari)
    hargaSetelahPajak = AturanPajak(hargaSetelahHari, lokasi)
    return hargaSetelahPajak


print(eval(input()))
