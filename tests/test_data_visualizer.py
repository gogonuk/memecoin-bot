import unittest
import os
import pandas as pd
from src.data_visualizer import visualize_roi

class TestDataVisualizer(unittest.TestCase):
    def setUp(self):
        # Create a sample CSV file for testing
        self.data_file = 'data/test_roi_data.csv'
        df = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
            'roi': [10, 20, 30]
        })
        df.to_csv(self.data_file, index=False)

    def tearDown(self):
        # Remove the test CSV file after tests
        if os.path.exists(self.data_file):
            os.remove(self.data_file)

    def test_visualize_roi(self):
        # Test visualize_roi function with the sample data file
        try:
            visualize_roi(self.data_file)
            self.assertTrue(os.path.exists('data/plots/roi_over_time.png'))
        except Exception as e:
            self.fail(f"visualize_roi raised an exception: {e}")

if name == 'main':
    unittest.main()