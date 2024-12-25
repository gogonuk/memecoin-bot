import matplotlib.pyplot as plt
import pandas as pd
import os

def visualize_roi(data_file):
    # Load data
    df = pd.read_csv(data_file)
    
    # Ensure the data has the necessary columns
    if 'date' not in df.columns or 'roi' not in df.columns:
        raise ValueError("Data must contain 'date' and 'roi' columns")

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['roi'], marker='o')
    plt.title('ROI Over Time')
    plt.xlabel('Date')
    plt.ylabel('ROI (%)')
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save plot
    plt.savefig('data/plots/roi_over_time.png')
    plt.show()

# Example usage
if __name__ == "__main__":
    data_file = 'data/roi_data.csv'  # Path to your ROI data file
    visualize_roi(data_file)