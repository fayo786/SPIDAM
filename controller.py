import librosa
import module
from module import DataProcessor
from GUI import GUI
import tkinter as tk

#running module test
class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.view = GUI(self.root, self)
        self.processor = DataProcessor()
        self.audio_data = None
        self.rt60_values = {}
        self.plots = ["Low", "Mid", "High"]
        self.current_plot_index = 0

    def load_file(self, file_path):
        """Load and process the selected audio file."""
        try:
            self.audio_data = self.processor.load_audio(file_path)
            self.view.update_file_label(self.audio_data["file_name"])

            self.analyze_audio()
        except Exception as e:
            messagebox.showerror("Error", f"Error loading file: {e}")

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

    def toggle_frequency_plot(self):
        """Toggle RT60 plots for Low, Mid, and High frequencies."""
        freq = self.plots[self.current_plot_index]
        value = self.rt60_values[freq]
        self.view.plot_frequency_rt60(freq, value)
        self.current_plot_index = (self.current_plot_index + 1) % len(self.plots)

    def run(self):
        self.root.mainloop()
