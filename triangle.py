def area(a, h):
    """
    Возвращает площадь треугольника по заданной стороне и высоте, проведённой к этой стороне.

    Параметры:
        a (float): сторона треугольника
        h (float): высота треугольника, проведённая к указанной стороне

    Возвращаемое значение:
        s (float): площадь треугольника со стороной a и высотой h, проведённой к этой стороне.

    Пример вызова:
        area(3.0, 10.0) --> 15.0
    """

    if type(a) not in [int, float] or type(h) not in [int, float]:
        raise TypeError

    if a <= 0 or h <= 0:
        raise ValueError

    return a * h / 2


def perimeter(a, b, c):
    """
    Возвращает периметр треугольника по трём заданным сторонам.

    Параметры:
        a (float): первая сторона треугольника
        b (float): вторая сторона треугольника
        c (float): третья сторона треугольника


    Возвращаемое значение:
        p (float): периметр треугольника со сторонами a, b и с

    Пример вызова:
        perimeter(3.0, 10.0, 5.5) --> 18.5
    """

    if type(a) not in [int, float] or type(b) not in [int, float] or type(c) not in [int, float]:
        raise TypeError

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError

    return a + b + c
