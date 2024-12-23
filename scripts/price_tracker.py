import requests

def fetch_token_price(token_address):
    sources = {
        "pump_fun": f"https://api.pump.fun/v1/tokens/{token_address}",
        "dexscreener": f"https://api.dexscreener.com/latest/dex/pairs/solana/{token_address}",
    }

    prices = {}
    for name, url in sources.items():
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            prices[name] = data.get("price", "N/A")
        except Exception as e:
            prices[name] = f"Error: {e}"
    return prices
cucu