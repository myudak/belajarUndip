# Definisi fungsi f(x) dan turunannya f'(x)
def f(x):
    return (x - 2) ** 2 - np.log(x)

def df(x):
    return 2 * (x - 2) - 1 / x

def metode_newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    x = x0
    print(f"\n=== Metode Newton-Raphson (x0 = {x0}) ===")

    for i in range(1, max_iter + 1):
        f_x = f(x)
        df_x = df(x)

        # Cek jika turunan nol (hindari pembagian oleh nol)
        if df_x == 0:
            print(f"Iterasi {i}: Turunan nol! Newton-Raphson gagal.")
            return None

        x_new = x - f_x / df_x

        print(
            f"Iterasi {i}: x = {x:.6f}, f(x) = {f_x:.6f}, f'(x) = {df_x:.6f}, x_baru = {x_new:.6f}"
        )

        if abs(x_new - x) < tol:
            print(f"Konvergen: Akar ditemukan pada x ≈ {x_new:.6f}\n")
            return x_new

        x = x_new

    print("Maksimum iterasi tercapai, hasil terakhir:", x)
    return x

# Interval pertama: 1 ≤ x ≤ 2 (ambil x0 = 1.5)
akar1 = metode_newton_raphson(f, df, x0=1.5)

# Interval kedua: e ≤ x ≤ 4 (ambil x0 = 3)
akar2 = metode_newton_raphson(f, df, x0=3)
