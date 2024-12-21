import pandas as pd
import matplotlib.pyplot as plt

def plot_roi(file_path):
    data = pd.read_csv(file_path)
    plt.plot(data["timestamp"], data["roi"])
    plt.xlabel("Time")
    plt.ylabel("ROI (%)")
    plt.title("ROI Over Time")
    plt.show()

plot_roi("data/roi_analysis.csv")
