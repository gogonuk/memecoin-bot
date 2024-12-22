import unittest
from scripts.roi_calculator import calculate_roi

class TestROICalculator(unittest.TestCase):
    def test_calculate_roi_positive(self):
        buy_price = 10
        sell_price = 15
        roi = calculate_roi(buy_price, sell_price)
        self.assertEqual(roi, 50.0)

    def test_calculate_roi_negative(self):
        buy_price = 15
        sell_price = 10
        roi = calculate_roi(buy_price, sell_price)
        self.assertEqual(roi, -33.333333333333336)

    def test_calculate_roi_zero(self):
        buy_price = 10
        sell_price = 10
        roi = calculate_roi(buy_price, sell_price)
        self.assertEqual(roi, 0.0)

if __name__ == "__main__":
    unittest.main()