# Nama File: matematika_gura.py
# Pembuat:
# Tanggal:
# Deskripsi: Mengembalikan list hasil tambah-tambah dua buah list sebagai representasi integer.

# DEFINISI DAN SPESIFIKASI
# shrimp --> list: integer
# shrimp(X, Y) mengembalikan list hasil tambah-tambah dua buah list sebagai representasi integer.


# REALISASI


def konso(e, L):
    return [e] + L


def konsi(L, e):
    return L + [e]


def first_elmt(L):
    return L[0]


def last_elmt(L):
    return L[-1]


def Head(L):
    """Head(L): Menghasilkan list tanpa elemen terakhir list L, mungkin kosong"""
    return L[:-1]


def Tail(L):
    """Tail(L): Menghasilkan list tanpa elemen pertama list L, mungkin kosong"""
    return L[1:]


def concatList(L1, L2):
    return L1 + L2


def is_empty(L):
    return len(L) == 0


def shrimp(X, Y):
    def is_negative(L):
        return not is_empty(L) and first_elmt(L) == "-"

    def make_positive(L):
        return Tail(L) if is_negative(L) else L

    def prepend_negative(L):
        return konso("-", L)

    def add_lists(X, Y, carry=0, result=[]):
        if is_empty(X) and is_empty(Y) and carry == 0:
            return result

        X_tail = Head(X) if not is_empty(X) else []
        Y_tail = Head(Y) if not is_empty(Y) else []

        total = (
            last_elmt(X if not is_empty(X) else [0])
            + last_elmt(Y if not is_empty(Y) else [0])
            + carry
        )

        carry_next = total // 10
        digit = total % 10

        return add_lists(X_tail, Y_tail, carry_next, konso(digit, result))

    def subtract_lists(X, Y, borrow=0, result=[]):
        if is_empty(X) and is_empty(Y) and borrow == 0:
            return result

        X_tail = Head(X) if not is_empty(X) else []
        Y_tail = Head(Y) if not is_empty(Y) else []

        diff = (
            last_elmt(X if not is_empty(X) else [0])
            - last_elmt(Y if not is_empty(Y) else [0])
            - borrow
        )

        if diff < 0:
            borrow_next = 1
            digit = diff + 10
        else:
            borrow_next = 0
            digit = diff

        return subtract_lists(X_tail, Y_tail, borrow_next, konso(digit, result))

    # Main Logic
    X_neg = is_negative(X)
    Y_neg = is_negative(Y)

    X_abs = make_positive(X)
    Y_abs = make_positive(Y)

    if X_neg and Y_neg:
        # Both are negative: Add absolute values and prepend '-'
        return prepend_negative(add_lists(X_abs, Y_abs))
    elif X_neg:
        # X is negative, Y is positive: Subtract absolute values
        if X_abs > Y_abs:
            return prepend_negative(subtract_lists(X_abs, Y_abs))
        else:
            return subtract_lists(Y_abs, X_abs)
    elif Y_neg:
        # X is positive, Y is negative: Subtract absolute values
        if Y_abs > X_abs:
            return prepend_negative(subtract_lists(Y_abs, X_abs))
        else:
            return subtract_lists(X_abs, Y_abs)
    else:
        # Both are positive: Add absolute values
        return add_lists(X_abs, Y_abs)


# APLIKASI
print(shrimp([1, 3], [1, 2]))
print(shrimp([1, 2, 3], [9]))  # -> [1, 3, 2]
print(shrimp([1, 2, 2], [1, 0]))  # -> [1, 3, 2]
print(
    shrimp(
        [
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
        ],
        [1],
    )
)
# print(eval(input()))
print(shrimp([1, 3], [1, 2]))  # Output: [2, 5]
print(shrimp([1, 3], ["-", 1, 2]))  # Output: [1]
print(shrimp(["-", 1, 3], [1, 2]))  # Output: ['-', 1]
print(shrimp(["-", 3], ["-", 3]))  # Output: ['-', 6]
print(shrimp(["-", 9], [1]))  # Output: ['-', 8]
print(shrimp([1, 2, 3], ["-", 4, 5]))  # Output: [7, 8]
