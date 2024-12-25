import pandas as pd
import os

def calculate_roi(buy_price, sell_price):
    if buy_price <= 0:
        raise ValueError("Buy price must be greater than zero.")
    roi = ((sell_price - buy_price) / buy_price) * 100
    return roi

def batch_calculate_roi(data_file):
    df = pd.read_csv(data_file)
    if 'buy_price' not in df.columns or 'sell_price' not in df.columns:
        raise ValueError("Data must contain 'buy_price' and 'sell_price' columns")

    df['roi'] = df.apply(lambda row: calculate_roi(row['buy_price'], row['sell_price']), axis=1)
    ```python
    return df

# Example usage
if __name__ == "__main__":
    data_file = 'data/trade_data.csv'  # Path to your trade data file
    roi_data = batch_calculate_roi(data_file)
    print(roi_data)