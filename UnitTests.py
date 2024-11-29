import unittest
import circle
import rectangle
import square
import triangle
import math


class CircleTestCase(unittest.TestCase):

    def test_area(self):
        e = 0.00000000000001
        res1 = circle.area(7)
        self.assertTrue(49 * math.pi - e <= res1 <= 49 * math.pi + e)

        res2 = circle.area(1.5)
        self.assertTrue(2.25 * math.pi - e <= res2 <= 2.25 * math.pi + e)

    def test_perimeter(self):
        e = 0.00000000000001
        res1 = circle.perimeter(26)
        self.assertTrue((52 * math.pi - e) <= res1 <= (52 * math.pi + e))

        res2 = circle.perimeter(3.7)
        self.assertTrue(7.4 * math.pi - e <= res2 <= 7.4 * math.pi + e)

    def test_correct_values(self):
        self.assertRaises(ValueError, circle.perimeter, -1)
        self.assertRaises(ValueError, circle.area, 0)
        self.assertRaises(TypeError, circle.perimeter, "asffsaf")
        self.assertRaises(TypeError, circle.area, False)


class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        e = 0.00000000000001
        res1 = rectangle.area(13, 4)
        self.assertTrue(52 - e <= res1 <= 52 + e)

        res2 = rectangle.area(3.25, 3)
        self.assertTrue(9.75 - e <= res2 <= 9.75 + e)

    def test_perimeter(self):
        res1 = rectangle.perimeter(18, 8)
        self.assertEqual(res1, 52)

        res2 = rectangle.perimeter(9.5, 8.2)
        self.assertEqual(res2, 35.4)

    def test_correct_values(self):
        self.assertRaises(ValueError, rectangle.perimeter, -1, 2)
        self.assertRaises(ValueError, rectangle.area, 9, 0)
        self.assertRaises(TypeError, rectangle.perimeter, "asffsaf", 5)
        self.assertRaises(TypeError, rectangle.area, 10, False)


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        e = 0.00000000000001
        res1 = triangle.area(13, 4)
        self.assertTrue(26 - e <= res1 <= 26 + e)

        res2 = triangle.area(3.3, 3)
        self.assertTrue(4.95 - e <= res2 <= 4.95 + e)

    def test_perimeter(self):
        e = 0.00000000000001
        res1 = triangle.perimeter(20, 19, 13)
        self.assertEqual(res1, 52)

        res2 = triangle.perimeter(9.5, 8.2, 0.4)
        self.assertTrue(18.1 - e <= res2 <= 18.1 + e)

    def test_correct_values(self):
        self.assertRaises(ValueError, triangle.perimeter, -1, 2, 9)
        self.assertRaises(ValueError, triangle.area, 9, 0)
        self.assertRaises(TypeError, triangle.perimeter, "asffsaf", 5, 4)
        self.assertRaises(TypeError, triangle.area, 10, False)


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        e = 0.00000000000001
        res1 = square.area(13)
        self.assertTrue(169 - e <= res1 <= 169 + e)

        res2 = square.area(1.6)
        self.assertTrue(2.56 - e <= res2 <= 2.56 + e)

    def test_perimeter(self):
        res1 = square.perimeter(13)
        self.assertEqual(res1, 52)

        res2 = square.perimeter(3.3)
        self.assertEqual(res2, 13.2)

    def test_correct_values(self):
        self.assertRaises(ValueError, square.perimeter, -1)
        self.assertRaises(ValueError, square.area, 0)
        self.assertRaises(TypeError, square.perimeter, "asffsaf")
        self.assertRaises(TypeError, square.area, False)
