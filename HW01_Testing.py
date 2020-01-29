import unittest
from HW01 import classify_triangle


class TestTriangle(unittest.TestCase):
    """Class is used to test triangles"""

    def test_triangle(self):
        self.assertEqual(classify_triangle(8,8,8),"equilateral triangle")
        self.assertEqual(classify_triangle(0,0,0),"not a triangle")           #failed testcase the program doesnt handle it and returns equilateral triangle
        self.assertEqual(classify_triangle(8,5,25),"not a triangle")
        self.assertEqual(classify_triangle(3,4,5),"right triangle")
        self.assertEqual(classify_triangle(13,5,12),"right triangle")
        self.assertEqual(classify_triangle(8,8,7),"isosceles triangle")
        self.assertEqual(classify_triangle(8,8,1),"not a triangle")     #test case passes even though it qualifies isosceles properties as it has two same lengths it isnt a triangle
        self.assertEqual(classify_triangle(7,8,9),"scalene triangle")
        self.assertEqual(classify_triangle(10,11,12),"scalene triangle")
        self.assertEqual(classify_triangle(16,15,30),"scalene triangle")
        self.assertEqual(classify_triangle(-1,-4,1),"not a triangle")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)