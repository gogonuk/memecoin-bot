import unittest
from scripts.price_tracker import fetch_token_price

class TestPriceTracker(unittest.TestCase):
    def test_fetch_token_price_valid(self):
        # Test with a sample valid token address
        token_address = "valid_token_address"
        prices = fetch_token_price(token_address)
        self.assertIsInstance(prices, dict)
        self.assertTrue(len(prices) > 0)

    def test_fetch_token_price_invalid(self):
        # Test with an invalid token address
        token_address = "invalid_token_address"
        prices = fetch_token_price(token_address)
        for source, price in prices.items():
            self.assertIn("Error", price)

if __name__ == "__main__":
    unittest.main()