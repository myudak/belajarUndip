# Fungsi yang ingin kita cari akarnya
def f(x):
    return x - np.cos(x)

def secant_method(f, x0, x1, tol=1e-4, max_iter=100):
    print(f"{'Iterasi':<8} {'x0':<15} {'x1':<15} {'x_baru':<15} {'f(x_baru)':<15}")

    for i in range(1, max_iter + 1):
        f_x0, f_x1 = f(x0), f(x1)
        if f_x1 - f_x0 == 0:
            print("Dibagi dengan nol! Metode gagal.")
            return None

        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        f_xnew = f(x_new)

        print(f"{i:<8} {x0:<15.10f} {x1:<15.10f} {x_new:<15.10f} {f_xnew:<15.10f}")

        if abs(x_new - x1) < tol:
            print(f"\nAkar ditemukan pada x ≈ {x_new:.10f} setelah {i} iterasi.\n")
            return x_new

        x0, x1 = x1, x_new

    print("\nMetode tidak konvergen dalam jumlah iterasi maksimum.")
    return None


# Mencari akar di interval [0, pi/2]
x0, x1 = 0, np.pi / 2

print("Mencari akar dengan metode Secant di interval [0, π/2]:")
root_secant = secant_method(f, x0, x1)
