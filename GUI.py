import tkinter as tk
from tkinter import filedialog, messagebox
import librosa.display
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("RT60 Audio Analyzer")
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange GUI components."""
        self.load_button = tk.Button(self.root, text="Load Audio File", command=self.load_file)
        self.load_button.pack(pady=10)

        self.file_label = tk.Label(self.root, text="No file loaded", wraplength=400)
        self.file_label.pack(pady=5)

        self.figure, self.axs = plt.subplots(1, 1, figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack()

        self.toggle_button = tk.Button(self.root, text="Toggle Frequency Plots", command=self.toggle_plot)
        self.toggle_button.pack(pady=10)

        self.output_label = tk.Label(self.root, text="", wraplength=800, justify="left")
        self.output_label.pack(pady=10)

        self.current_plot_index = 0

    def load_file(self):
        """Load a file and send it to the controller."""
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.aac *m4a")])
        if file_path:
            self.controller.load_file(file_path)

    def update_file_label(self, file_name):
        self.file_label.config(text=f"Loaded File: {file_name}")

    def display_stats(self, stats):
        self.output_label.config(text=stats)

    def plot_waveform(self, audio, sr):
        """Plot the waveform of the audio."""
        self.axs.cla()
        librosa.display.waveshow(audio, sr=sr, ax=self.axs)
        self.axs.set_title("Waveform")
        self.canvas.draw()

    def plot_frequency_rt60(self, freq_name, value):
        """Plot the RT60 for a specific frequency range."""
        self.axs.cla()
        self.axs.bar([freq_name], [value], color='blue')
        self.axs.set_title(f"RT60 for {freq_name}")
        self.axs.set_ylabel("RT60 (s)")
        self.canvas.draw()

    def toggle_plot(self):
        """Toggle through Low, Mid, and High RT60 plots."""
        self.controller.toggle_frequency_plot()


'''window = tk.Tk()
#Convert Audio button
Convert_Audio_Button = tk.Button(window, text = "Convert Audio")
Convert_Audio_Button.grid(column = 2, row = 0, sticky = "ne", padx = 10, pady = 10)
#Load audio button
convert_load = tk.Button (window, text = "Load Audio")
convert_load.grid(column=1, row=0, sticky = "ne", padx =10, pady=10)
window.mainloop()'''
