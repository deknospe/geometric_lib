def area(a, b):
    """
    Возвращает площадь прямоугольника по двум заданным сторонам.

    Параметры:
        a (float): первая сторона прямоугольника
        b (float): вторая сторона прямоугольника (смежная с первой)

    Возвращаемое значение:
        s (float): площадь прямоугольника со сторонами a и b

    Пример вызова:
        area(2.0, 3.5) --> 7.0
    """

    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError

    if a <= 0 or b <= 0:
        raise ValueError

    return a * b 


def perimeter(a, b):
    """
    Возвращает периметр прямоугольника по двум заданным сторонам.

    Параметры:
        a (float): первая сторона прямоугольника
        b (float): вторая сторона прямоугольника (смежная с первой)

    Возвращаемое значение:
        p (float): периметр прямоугольника со сторонами a и b

    Пример вызова:
        perimeter(2.0, 3.5) --> 11.0
    """

    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError

    if a <= 0 or b <= 0:
        raise ValueError

    return 2 * (a + b)
