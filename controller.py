import wave
from modulefinder import Module
from tkinter import messagebox
import librosa
import numpy as np
from librosa.core import audio
from matplotlib import pyplot as plt
from scipy.constants import value
from scipy.signal import butter, lfilter
import RT60
import module
from module import DataProcessor
from GUI import GUI
import tkinter as tk


#running module test
class Controller:
    def __init__(self):
        self.module = module
        self.points = None
        self.root = tk.Tk()
        self.view = GUI(self.root, self)
        self.processor = DataProcessor()
        self.audio_data = None
        self.rt60_values = {}
        self.plots = ["Low", "Mid", "High"]
        self.current_plot_index = 0
        self.RT60 = RT60
#loading files 
    def load_file(self, file_path):
        """Load and process the selected audio file."""
        try:
            global newfile_path
            newfile_path = file_path
            self.audio_data = self.processor.load_audio(file_path)
            self.view.update_file_label(self.audio_data["file_name"])

            self.analyze_audio()
            self.RT60.process_audio(file_path)
            self.RT60.audio_filter(newfile_path)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading file: {e}")

#analizyn audio data
    def analyze_audio(self):
        """Analyze the audio file and display statistics."""
        stats = self.processor.calculate_statistics(self.audio_data)
        rt60_low = self.processor.compute_rt60(self.audio_data, [125, 250])
        rt60_mid = self.processor.compute_rt60(self.audio_data, [500, 1000])
        rt60_high = self.processor.compute_rt60(self.audio_data, [2000, 4000])
        max_freq = self.processor.find_max_amplitude_frequency(self.audio_data)


        self.rt60_values = {"Low": rt60_low, "Mid": rt60_mid, "High": rt60_high}

        stats_text = (
            f"Duration: {stats['Duration']:.2f} seconds\n"
            f"RT60 Low: {rt60_low:.2f} s\n"
            f"RT60 Mid: {rt60_mid:.2f} s\n"
            f"RT60 High: {rt60_high:.2f} s\n"
            f"Frequency of Max Amplitude: {max_freq} Hz\n"
        )
        self.view.display_stats(stats_text)
        self.view.plot_waveform(self.audio_data["data"], self.audio_data["sr"])


#toggle between different plots
    def toggle_frequency_plot(self):
        wf = wave.open('audio_lowcut.wav', 'rb')
        print("opening doc")
        frames = wf.readframes(wf.getnframes())
        print("framing")
        audio_data = np.frombuffer(frames, dtype=np.int16)
        # Normalize data if needed
        audio_data = audio_data / (2 ** (wf.getsampwidth() * 8 - 1))
        # Create bins and count frequencies
        bins = np.linspace(audio_data.min(), audio_data.max(), 20)
        hist, _ = np.histogram(audio_data, bins=bins)
        # Plot the histogram
        plt.bar(bins[:-1], hist, width=np.diff(bins))
        plt.xlabel("Amplitude")
        plt.ylabel("Frequency")
        plt.title("Lowcut File Histogram")
        plt.show()

#******************Histogram***********
    def display_wav_histogram(self):
        """Plots a histogram of amplitude values from a WAV file."""
        if not newfile_path:
            messagebox.showwarning("Warning", "Please process an audio file first!")
            return
        try:
            with wave.open(newfile_path, 'r') as wav:

            # Read the audio data
                signal = wav.readframes(-1)
                signal = np.frombuffer(signal, dtype=np.int16)

            # Plot the histogram
                plt.hist(signal, bins=50)
                plt.title('Amplitude Histogram of ' + newfile_path)
                plt.xlabel('Amplitude')
                plt.ylabel('Frequency')
                plt.show()
        except Exception as e:
            messagebox.showerror("Error", f"Could not generate histogram: {e}")

#********************Spectrogram Graph&***********
    def display_additional_visualization(self):
        if not newfile_path:
            messagebox.showwarning("Warning", "Please process an audio file first!")
            return
        try:
            # Load the audio file
            audio, sr = librosa.load(newfile_path, sr=None)

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
            plt.show()
        except Exception as e:
            messagebox.showerror("Error", f"Could not generate spectrogram: {e}")


    def run(self):
        self.root.mainloop()

