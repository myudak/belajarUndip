# Definisi variabel simbolik
X = Symbol("x")

# FUNGSI
f = X**3 - 7 * X**2 + 14 * X - 6

# INTERVAL
a, b = 3.2, 4

# TOLERANSI
tol = 1e-2

def bisection_method(f, a, b, tol=1e-2):
    print("=== Metode Bisection ===")
    for i in range(100):
        c = (a + b) / 2  # Titik tengah
        f_c = f.subs(X, c)
        f_a = f.subs(X, a)
        f_b = f.subs(X, b)

        print(f"Iterasi {i+1}:")
        print(f"  Titik Tengah: c_{i+1} = ({a} + {b}) / 2 = {c}")
        print(f"  |a - b| = |{a} - {b}| = {abs(a - b)}")
        print(f"  f(c_{i+1}) = f({c}) = {f_c}")

        # Jika akar ditemukan atau sudah mencapai toleransi, berhenti
        if abs(f_c) < tol or abs(a - b) < tol:
            print(f"  Konvergen: Akar ditemukan pada x ≈ {c}\n")
            return c

        # Perbarui interval berdasarkan tanda f(c)
        if f_c * f_a < 0:
            print(f"  Karena f(c) * f(a) < 0, interval baru: [{a}, {c}]")
            b = c
        else:
            print(f"  Karena f(c) * f(b) < 0, interval baru: [{c}, {b}]")
            a = c

        print("-" * 50)

    return c  # Estimasi terbaik setelah iterasi maksimum

# Menjalankan metode bisection
akar_bisection = bisection_method(f, a, b, tol)
print("SOLUSI Akar (Metode Bisection):", akar_bisection)
