"""
    Program   : Ekspresi numeric: Mean Olympique (MO)
    Deskripsi : menghitung rata-rata dari dua buah bilangan integer, yang bukan maksimum dan bukan minimum dari 4 buah integer
    NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
    Tanggal   : 02/09/2024
    **************************************************************
    DEFINISI DAN SPESIFIKASI
    MO : 4 integer > 0 → real
        { MO (u,v,w,x): menghitung rata-rata dari dua buah bilangan integer, yang bukan  maksimum dan bukan minimum dari 4 buah integer: (u+v+w+x-min4 (u,v,w,x)-max4  (u,v,w,x))/2 

    max4 : 4 integer >0 → integer 
        {max4 (i,j,k,l) menentukan maksimum dari 4 buah bilangan integer} 
    
    min4 : 4 integer > 0 → integer 
        {min4 (i,j,k,l) menentukan minimum dari 4 buah bilangan integer} 

    max2 : 2 integer >0 → integer 
        {max2 (a,b) menentukan maksimum dari 2 bilangan intege, hanya dengan ekspresi aritmatika: jumlah dari kedua bilangan ditambah denganselisih kedua bilangan, hasilnya dibagi 2} 
    
    min2 : 2 integer > 0 → integer 
        {min2 (a,b) menentukan minimum dari 2 bilangan integer, , hanya dengan ekspresi aritmatika :jumlah dari kedua bilangan – selisih kedua bilangan , hasilnya dibagi 2} 
    **************************************************************

"""

"""
    **************************************************************
    REALISASI
    **************************************************************
"""


def max2(a: int, b: int) -> int:
    return (a + b + abs(a - b)) // 2


def min2(a: int, b: int) -> int:
    return (a + b - abs(a - b)) // 2


def max4(i: int, j: int, k: int, l: int) -> int:
    return max2(max2(i, j), max2(k, l))


def min4(i: int, j: int, k: int, l: int) -> int:
    return min2(min2(i, j), min2(k, l))


def MO(u: int, v: int, w: int, x: int) -> float:
    return (u + v + w + x - max4(u, v, w, x) - min4(u, v, w, x)) / 2


"""
    **************************************************************
    APPLIKASI
    **************************************************************
"""
print(MO(10, 8, 12, 14))
