import unittest
from scripts.trade_executor import execute_trade

class TestTradeExecutor(unittest.TestCase):
    def test_execute_trade_buy(self):
        wallet = "test_wallet_address"
        token_address = "test_token_address"
        action = "buy"
        result = execute_trade(wallet, token_address, action=action, amount=1)
        self.assertIn("Executing", result)

    def test_execute_trade_sell(self):
        wallet = "test_wallet_address"
        token_address = "test_token_address"
        action = "sell"
        result = execute_trade(wallet, token_address, action=action, amount=1)
        self.assertIn("Executing", result)

if __name__ == "__main__":
    unittest.main()