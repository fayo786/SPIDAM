import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import librosa
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scipy.io import wavfile
from scipy.signal import butter, lfilter
from scipy.sparse import data
import wave



# Function to create a bandpass filter
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype="band")
    return b, a


# Function to apply the bandpass filter
def bandpass_filter(data, lowcut, highcut, fs, order=4):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Function to calculate RT60 (reverberation time)
def calculate_rt60(audio, sr, band):
    band_filters = {
        "low": (20, 250),
        "mid": (250, 2000),
        "high": (2000, 8000)
    }
    f_min, f_max = band_filters[band]
    audio_filtered = bandpass_filter(audio, f_min, f_max, sr)

    # Compute energy decay curve
    energy = np.cumsum(audio_filtered ** 2)[::-1]

    # Estimate RT60 (time to decay to 10% of initial energy)
    rt60 = 0.5 * np.argmax(energy < (energy[0] * 0.1)) / sr
    return rt60


# Function to process the audio file
def process_audio(file_path):
    global rt60_values, selected_file
    selected_file = file_path
    try:
        audio, sr = librosa.load(file_path, sr=None)
        rt60_values = [calculate_rt60(audio, sr, band) for band in ["low", "mid", "high"]]
        messagebox.showinfo("Success", "RT60 values calculated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not process the file: {e}")


# Function to display individual plots
def display_individual_plots():
    if not rt60_values:
        messagebox.showwarning("Warning", "Please process an audio file first!")
        return
    bands = ["Low", "Mid", "High"]
    # Create a matplotlib Figure
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    bands = ["Low", "Mid", "High"]
    ax.bar(bands, rt60_values, color=["blue", "green", "red"])
    ax.set_title("RT60 Values by Frequency Band")
    ax.set_ylabel("RT60 (s)")
    plt.bar(bands, rt60_values, color=["blue", "green", "red"])
    plt.title("RT60 Values by Frequency Band")
    plt.ylabel("RT60 (s)")
    plt.show(block=False)



# Function to display a combined plot
def display_combined_plot():
    if not rt60_values:
        messagebox.showwarning("Warning", "Please process an audio file first!")
        return
    bands = ["Low", "Mid", "High"]
    plt.plot(bands, rt60_values, marker="o", color="purple")
    plt.title("Combined RT60 Plot")
    plt.ylabel("RT60 (s)")
    plt.show(block=False)


# Function to show the difference needed to reach 0.5 seconds
def display_difference():
    if not rt60_values:
        messagebox.showwarning("Warning", "Please process an audio file first!")
        return
    differences = [round(value - 0.5, 2) for value in rt60_values]
    bands = ["Low", "Mid", "High"]
    plt.bar(bands, differences, color=["orange", "cyan", "pink"])
    plt.title("Difference to Reach 0.5 Seconds")
    plt.ylabel("Time Difference (s)")
    plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
    plt.show(block=False)


def display_additional_visualization():
    if not selected_file:
        messagebox.showwarning("Warning", "Please process an audio file first!")
        return
    try:
        # Load the audio file
        audio, sr = librosa.load(selected_file, sr=None)

        # Generate the Mel spectrogram
        S = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=128, fmax=8000)

        # Convert to decibels for better visualization
        S_dB = librosa.power_to_db(S, ref=np.max)

        # Plot the spectrogram
        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel', cmap='coolwarm')
        plt.colorbar(format='%+2.0f dB')
        plt.title("Mel Spectrogram")
        plt.tight_layout()
        plt.show(block=False)
    except Exception as e:
        messagebox.showerror("Error", f"Could not generate spectrogram: {e}")


# GUI setup
def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select an Audio File",
        filetypes=[("Audio Files", "*.wav *.mp3 *.flac")]
    )
    if file_path:
        process_audio(file_path)
