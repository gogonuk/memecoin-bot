import pandas as pd

def calculate_roi(buy_price, sell_price):
    return (sell_price - buy_price) / buy_price * 100

# Example usage
data = pd.read_csv("data/roi_analysis.csv")
for _, row in data.iterrows():
    roi = calculate_roi(row["buy_price"], row["sell_price"])
    print(f"Token: {row['token']}, ROI: {roi:.2f}%")
