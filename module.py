import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.io.wavfile import write

#data process class
class DataProcessor:
    def load_data(self, file_path):
        data, sr = librosa.load(file_path, sr=None, mono=False)
        return {"data": data, "sr": sr}

    def clean_data(self, audio):
        data, sr = audio["data"], audio["sr"]
        # Handle metadata and channels
        if data.ndim > 1:
            data = np.mean(data, axis=0)  # Convert to mono
        return {"data": data, "sr": sr}

    def calculate_statistics(self, audio):
        data, sr = audio["data"], audio["sr"]
        length = len(data) / sr
        peaks, _ = find_peaks(data, height=0)
        freq = len(peaks) / length
        rt60 = self.estimate_rt60(data, sr)
        return {"Length (s)": length, "Peaks per second": freq, "RT60 (s)": rt60}

    def estimate_rt60(self, data, sr):
        energy = np.cumsum(data ** 2)
        rt60 = np.log10(np.max(energy) / energy[-1])
        return round(rt60, 2)

    def plot_waveform(self, audio):
        data, sr = audio["data"], audio["sr"]
        plt.figure(figsize=(10, 4))
        plt.plot(np.arange(len(data)) / sr, data)
        plt.title("Waveform")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.show()
