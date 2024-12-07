from sympy import symbols, Eq, solve, integrate

# Define variables and functions
x = symbols("x")
f = 48 - x**2
g = -x - 8

# Find intersection points
intersection_eq = Eq(f, g)
intersection_points = solve(intersection_eq, x)

# Define the integrand (f(x) - g(x))
integrand = f - g

print(intersection_points[0])
print(intersection_points[1])

# Calculate the area
area = integrate(integrand, (x, intersection_points[0], intersection_points[1]))
print(float(area))
