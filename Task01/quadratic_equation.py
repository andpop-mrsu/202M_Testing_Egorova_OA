import math

def solve_quadratic(a, b, c):

    def r(x):
        return round(x, 4)

    if a == 0:
        if b == 0:
            return []
        return [r(-c / b)]

    d = b * b - 4 * a * c

    if d < 0:
        return []

    if d == 0:
        return [r(-b / (2 * a))]

    sqrt_d = math.sqrt(d)
    x1 = (-b - sqrt_d) / (2 * a)
    x2 = (-b + sqrt_d) / (2 * a)

    return sorted([r(x1), r(x2)])

if __name__ == "__main__":
    print("Решение уравнения ax² + bx + c = 0")

    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))

    roots = solve_quadratic(a, b, c)

    if not roots:
        print("Действительных корней нет")
    elif len(roots) == 1:
        print(f"x₁ = {roots[0]}")
    else:
        print(f"x₁ = {roots[0]}, x₂ = {roots[1]}")
