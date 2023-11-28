import unittest
from ..helpers.coords import calc_avg_coords

"""
run with:

python -m unittest 10_24/code_along/tests/test_coords.py

This runs our script as a "module" rather than just a simple Python file.
This is important for when we are creating a project that links to multiple
modules/packages inside of our own project.
"""


class TestCoords(unittest.TestCase):

    def setUp(self):
        self.good_coordinates = [
            (40.8499, -73.8769),
            (40.9125, -73.8478),
            (40.8165, -73.9025),
            (40.8790, -73.9060),
            (40.8450, -73.8320)
        ]

        self.str_coordinates = [
            ("40.8499", "-73.8769"),
            ("40.9125", "-73.8478"),
            ("40.8165", "-73.9025"),
            ("40.8790", "-73.9060"),
            ("40.8450", "-73.8320")
        ]

        self.error = [None]

        self.computed = (40.86058, -73.87304)

    def test_happy_path(self):
        self.assertEqual(
            calc_avg_coords(self.good_coordinates), self.computed)

    """
    def test_str_path(self):
        self.assertEqual(
            calc_avg_coords(self.str_coordinates), self.computed)
    """

    def test_graceful(self):
        with self.assertRaises(TypeError):
            calc_avg_coords(self.error)


if __name__ == '__main__':
    unittest.main()
