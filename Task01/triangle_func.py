class IncorrectTriangleSides(Exception):
    """Исключение для некорректных сторон треугольника."""
    pass


def get_triangle_type(a, b, c):
    """
    Определяет тип треугольника по длинам сторон.

    >>> get_triangle_type(3, 3, 3)
    'equilateral'
    >>> get_triangle_type(3, 3, 2)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
    ...
    triangle_func.IncorrectTriangleSides
    >>> get_triangle_type(-1, 2, 2)
    Traceback (most recent call last):
    ...
    triangle_func.IncorrectTriangleSides
    >>> get_triangle_type(0, 1, 1)
    Traceback (most recent call last):
    ...
    triangle_func.IncorrectTriangleSides
    """

    for side in (a, b, c):
        if not isinstance(side, (int, float)):
            raise IncorrectTriangleSides

    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides

    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides

    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
