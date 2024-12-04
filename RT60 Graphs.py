import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import librosa
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter


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
    plt.bar(bands, rt60_values, color=["blue", "green", "red"])
    plt.title("RT60 Values by Frequency Band")
    plt.ylabel("RT60 (s)")
    plt.show()


# Function to display a combined plot
def display_combined_plot():
    if not rt60_values:
        messagebox.showwarning("Warning", "Please process an audio file first!")
        return
    bands = ["Low", "Mid", "High"]
    plt.plot(bands, rt60_values, marker="o", color="purple")
    plt.title("Combined RT60 Plot")
    plt.ylabel("RT60 (s)")
    plt.show()


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
    plt.show()


# Function to display additional visualizations (e.g., spectrogram)
def display_additional_visualization():
    if not selected_file:
        messagebox.showwarning("Warning", "Please process an audio file first!")
        return
    try:
        audio, sr = librosa.load(selected_file, sr=None)
        S = librosa.feature.melspectrogram(audio, sr=sr)
        S_dB = librosa.power_to_db(S, ref=np.max)
        librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel', cmap='coolwarm')
        plt.colorbar(format='%+2.0f dB')
        plt.title("Mel Spectrogram")
        plt.show()
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


# Initialize GUI
app = tk.Tk()
app.title("Audio Processing Tool")
app.geometry("400x300")

rt60_values = []
selected_file = None

# Buttons
upload_button = tk.Button(app, text="Upload Audio File", command=upload_file, width=30)
upload_button.pack(pady=10)

plot_individual_button = tk.Button(app, text="Display Individual RT60 Plots", command=display_individual_plots,
                                   width=30)
plot_individual_button.pack(pady=10)

plot_combined_button = tk.Button(app, text="Display Combined RT60 Plot", command=display_combined_plot, width=30)
plot_combined_button.pack(pady=10)

difference_button = tk.Button(app, text="Show Difference to 0.5s", command=display_difference, width=30)
difference_button.pack(pady=10)

extra_button = tk.Button(app, text="Additional Visualization", command=display_additional_visualization, width=30)
extra_button.pack(pady=10)

# Run the GUI
app.mainloop()