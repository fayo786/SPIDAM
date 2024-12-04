import tkinter as tk
from tkinter import filedialog, messagebox
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pydub import AudioSegment
import os


class RT60AnalyzerApp:
    def __init__(self, root):
        """Initialize the main application."""
        self.root = root
        self.root.title("RT60 Analyzer")
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange GUI components."""
        # Load audio button
        self.load_button = tk.Button(self.root, text="Load Audio File", command=self.load_audio)
        self.load_button.pack(pady=10)

        # Label to display the file name
        self.file_name_label = tk.Label(self.root, text="No file loaded", wraplength=400)
        self.file_name_label.pack(pady=5)

        # Canvas to display plots
        self.figure, self.axs = plt.subplots(1, 1, figsize=(8, 6))  # Single plot area
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack()

        # Button to toggle frequency plots
        self.toggle_plot_button = tk.Button(self.root, text="Toggle Frequency Plots", command=self.toggle_frequency_plot)
        self.toggle_plot_button.pack(pady=10)

        # Output label
        self.output_label = tk.Label(self.root, text="", wraplength=800, justify="left")
        self.output_label.pack(pady=10)

        self.current_plot_index = 0
        self.plots = ['Low Frequency', 'Mid Frequency', 'High Frequency']

    def load_audio(self):
        """Handle the loading and processing of an audio file."""
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.*")])  # Accept any file format
        if not file_path:
            return  # No file selected

        try:
            self.file_name_label.config(text=f"Loaded File: {file_path}")
            audio, sr = self.process_audio(file_path)
            self.analyze_audio(audio, sr)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process the audio file:\n{e}")

    def process_audio(self, file_path):
        """Convert non-WAV formats to WAV if necessary."""
        if not file_path.endswith(".wav"):
            try:
                audio = AudioSegment.from_file(file_path)
                wav_path = file_path.rsplit(".", 1)[0] + ".wav"
                audio.export(wav_path, format="wav")
                file_path = wav_path
            except Exception as e:
                raise Exception(f"Failed to convert the file: {e}")

        audio, sr = librosa.load(file_path, sr=None, mono=True)
        return audio, sr

    def analyze_audio(self, audio, sr):
        """Perform analysis on the loaded audio file."""
        duration = librosa.get_duration(y=audio, sr=sr)

        rt60_low = self.compute_rt60(audio, sr, [125, 250])
        rt60_mid = self.compute_rt60(audio, sr, [500, 1000])
        rt60_high = self.compute_rt60(audio, sr, [2000, 4000])

        max_amp_freq = self.find_max_amplitude_frequency(audio, sr)

        self.plot_waveform(audio, sr)

        self.output_label.config(
            text=(
                f"Duration: {duration:.2f} seconds\n"
                f"RT60 Low (125-250 Hz): {rt60_low:.2f} s\n"
                f"RT60 Mid (500-1000 Hz): {rt60_mid:.2f} s\n"
                f"RT60 High (2000-4000 Hz): {rt60_high:.2f} s\n"
                f"Frequency of Max Amplitude: {max_amp_freq} Hz\n"
                f"RT60 Difference to Reduce to 0.5s: "
                f"Low: {rt60_low - 0.5:.2f} s, Mid: {rt60_mid - 0.5:.2f} s, High: {rt60_high - 0.5:.2f} s"
            )
        )

        self.rt60_values = {'Low': rt60_low, 'Mid': rt60_mid, 'High': rt60_high}

    def compute_rt60(self, audio, sr, freq_range):
        """Estimate RT60 for a specific frequency range."""
        return np.random.uniform(0.4, 0.8)  # Placeholder

    def find_max_amplitude_frequency(self, audio, sr):
        """Find the frequency with the maximum amplitude."""
        fft = np.fft.fft(audio)
        freqs = np.fft.fftfreq(len(fft), 1 / sr)
        magnitude = np.abs(fft)
        max_index = np.argmax(magnitude)
        return int(freqs[max_index])

    def plot_waveform(self, audio, sr):
        """Plot the audio waveform."""
        self.axs.cla()
        librosa.display.waveshow(audio, sr=sr, ax=self.axs)
        self.axs.set_title("Waveform")
        self.figure.tight_layout()
        self.canvas.draw()

    def plot_frequency_rt60(self, freq_range_name):
        """Plot RT60 value for a specific frequency range."""
        self.axs.cla()
        self.axs.bar([freq_range_name], [self.rt60_values[freq_range_name]], color='blue')
        self.axs.set_title(f"RT60 for {freq_range_name} Frequency")
        self.axs.set_ylabel("RT60 (s)")
        self.figure.tight_layout()
        self.canvas.draw()

    def toggle_frequency_plot(self):
        """Toggle between Low, Mid, and High frequency RT60 plots."""
        current_frequency = self.plots[self.current_plot_index]
        self.plot_frequency_rt60(current_frequency)

        self.current_plot_index = (self.current_plot_index + 1) % len(self.plots)


# Main entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = RT60AnalyzerApp(root)
    root.mainloop()
