# src/data_utils.py
import pandas as pd
import numpy as np

def clean_data(data_frame):
    
    data_frame.dropna(subset=["Lufttemperatur", "Vindhastighet"])  

    # koverterer kolonner til riktige datatyper (fjerner tekstfil)
    data_frame["Lufttemperatur"] = pd.to_numeric(data_frame["Lufttemperatur"], errors="coerce")
    data_frame["Vindhastighet"] = pd.to_numeric(data_frame["Vindhastighet"], errors="coerce")
    
    # fjerner urealistiske verdier 
    data_frame = data_frame[(data_frame["Lufttemperatur"] > -60) & (data_frame["Lufttemperatur"] < 60)]
    data_frame = data_frame[(data_frame["Vindhastighet"] >= 0) & (data_frame["Vindhastighet"] < 70)]

    return data_frame

# forenklet versjon av formelen vi bruker i hoved koden
def compute_moving_average(data_array, window=3):
    weights = np.ones(window) / window
    return np.convolve(data_array, weights, mode='valid')
