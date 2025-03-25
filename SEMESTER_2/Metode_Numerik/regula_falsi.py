# Fungsi yang ingin kita cari akarnya
def f(x):
    return 2 * x * np.cos(2 * x) - (x - 2) ** 2

def regula_falsi_method(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) > 0:
        print("Interval yang diberikan tidak memiliki akar atau memiliki akar genap.")
        return None

    print(f"{'Iterasi':<8} {'a':<15} {'b':<15} {'c':<15} {'f(c)':<15}")

    for i in range(1, max_iter + 1):
        c = b - f(b) * (b - a) / (f(b) - f(a))
        f_c = f(c)

        print(f"{i:<8} {a:<15.10f} {b:<15.10f} {c:<15.10f} {f_c:<15.10f}")

        if abs(f_c) < tol:
            print(f"\nAkar ditemukan pada x ≈ {c:.10f} setelah {i} iterasi.\n")
            return c

        if f(a) * f_c < 0:
            b = c  # Akar ada di antara a dan c
        else:
            a = c  # Akar ada di antara c dan b

    print("\nMetode tidak konvergen dalam jumlah iterasi maksimum.")
    return None


# Mencari akar di kedua interval
a1, b1 = 2.0, 3.0
a2, b2 = 3.0, 4.0

print("Mencari akar di interval [2, 3]:")
root_falsi_1 = regula_falsi_method(f, a1, b1)

print("\nMencari akar di interval [3, 4]:")
root_falsi_2 = regula_falsi_method(f, a2, b2)
