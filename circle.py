import math

'''
Импортируем модуль math в котором содержится число pi
'''


def area(r):
    """
    Возвращает площадь окружности по заданному радиусу.

    Параметры:
        r (float): радиус окружности

    Возвращаемое значение:
        s (float): площадь окружности с радиусом r

    Пример вызова:
        area(2.0) --> 12.56
    """
    if type(r) not in [int, float]:
        raise TypeError

    if r <= 0:
        raise ValueError

    return math.pi * r * r


def perimeter(r):
    """
    Возвращает периметр окружности по заданному радиусу.

    Параметры:
        r (float): радиус окружности

    Возвращаемое значение:
        p (float): периметр окружности с радиусом r

    Пример вызова:
        perimeter(2.5) --> 15.7
    """

    if type(r) not in [int, float]:
        raise TypeError

    if r <= 0:
        raise ValueError

    return 2 * math.pi * r
