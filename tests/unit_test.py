import unittest
import pandas as pd
import numpy as np

from formler_fra_kode import clean_data, compute_moving_average

class TestWeatherUtils(unittest.TestCase):

    def test_clean_data_removes_nan(self):
        data_frame = pd.DataFrame({
            "Lufttemperatur": [20.1, np.nan, 15.5],
            "Vindhastighet": [5.0, 3.2, np.nan]
        })

        cleaned_data_frame = clean_data(data_frame)
        self.assertFalse(cleaned_data_frame.isnull().values.any())
        self.assertEqual(len(cleaned_data_frame), 1)

    def test_moving_average(self):
        data = np.array([1, 2, 3, 4, 5])
        expected = np.array([2.0, 3.0, 4.0]) 
        result = compute_moving_average(data, window=3)
        np.testing.assert_array_almost_equal(result, expected)

if __name__ == "__main__":
    unittest.main()
