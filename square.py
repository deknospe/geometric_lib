def area(a):
    """
    Возвращает площадь квадрата по заданной стороне.

    Параметры:
        a (float): сторона квадрата

    Возвращаемое значение:
        s (float): площадь квадрата со стороной a

    Пример вызова:
        area(3.0) --> 9.0
    """

    if type(a) not in [int, float]:
        raise TypeError

    if a <= 0:
        raise ValueError

    return a * a


def perimeter(a):
    """
    Возвращает периметр квадрата по заданной стороне.

    Параметры:
        a (float): сторона квадрата

    Возвращаемое значение:
        p (float): периметр квадрата со стороной a

    Пример вызова:
        perimeter(3.0) --> 12.0
    """

    if type(a) not in [int, float]:
        raise TypeError

    if a <= 0:
        raise ValueError

    return 4 * a
