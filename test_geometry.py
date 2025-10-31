import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(3), math.pi * 9)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(3), 2 * math.pi * 3)


class TestRectangle(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(3, 5), 15)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(3, 5), 16)


class TestSquare(unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(square_area(4), 16)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(4), 16)


class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(4, 10), 20)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
