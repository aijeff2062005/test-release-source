
import unittest

from app import get_version, calculate_total


class TestERPApplication(unittest.TestCase):

    def test_version(self):
        self.assertEqual(get_version(), "2.0.0")

    def test_calculate_total(self):
        self.assertEqual(calculate_total(100, 3), 300)

    def test_zero_quantity(self):
        self.assertEqual(calculate_total(100, 0), 0)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_total(-100, 3)


if __name__ == "__main__":
    unittest.main()
