import unittest

from difference_of_squares import difference_of_squares



class DifferenceOfSquaresTest(unittest.TestCase):
    def test_difference_of_squares_1(self):
        self.assertEqual(difference_of_squares(1), 0)

    def test_difference_of_squares_5(self):
        self.assertEqual(difference_of_squares(5), 170)

    def test_difference_of_squares_100(self):
        self.assertEqual(difference_of_squares(100), 25164150)


if __name__ == "__main__":
    unittest.main()
