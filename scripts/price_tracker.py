import requests
import logging
import os

class PriceTracker:
    def __init__(self, api_url):
        self.api_url = api_url
        logging.basicConfig(filename='data/logs/price_tracker.log', level=logging.INFO)

    def fetch_price(self, token_address):
        try:
            response = requests.get(f"{self.api_url}/price/{token_address}")
            response.raise_for_status()
            price_data = response.json()
            return price_data['price']
        except Exception as e:
            logging.error(f"Failed to fetch price for {token_address}: {e}")
            return None

    def track_prices(self, token_addresses):
        prices = {}
        for address in token_addresses:
            price = self.fetch_price(address)
            if price is not None:
                prices[address] = price
        return prices

# Example usage
if __name__ == "__main__":
    api_url = os.getenv("PRICE_API_URL", "https://api.example.com")
    tracker = PriceTracker(api_url)
    token_addresses = ["TOKEN_ADDRESS_1", "TOKEN_ADDRESS_2"]
    prices = tracker.track_prices(token_addresses)
    print(prices)