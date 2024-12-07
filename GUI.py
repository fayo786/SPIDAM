import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import librosa
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import RT60


class GUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("RT60 Audio Analyzer")
        self.create_widgets()
        self.RT60 = RT60
    def create_widgets(self):
        """Create widgets for the GUI."""
        # Create a frame to hold the buttons on the left
        self.left_frame = tk.Frame(self.root)  # Add background for better styling
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)  # Align to the left of the root window

        # Buttons in the left frame:
        #individual graph button
        self.plot_individual_button = tk.Button(self.left_frame, text="Individual RT60", command=self.individual_rt60, width=20)
        self.plot_individual_button.pack(pady=5)
        #Combined button
        self.plot_combined_button = tk.Button(self.left_frame, text="Combined RT60", command=self.combined_rt60, width=20)
        self.plot_combined_button.pack(pady=5)
        #diff
        self.difference_button = tk.Button(self.left_frame, text="Difference to 0.5s", command=self.display_difference, width=20)
        self.difference_button.pack(pady=5)
        #spectogram button
        self.extra_button = tk.Button(self.left_frame, text="Additional Visualization", command=self.additional_visualization, width=20)
        self.extra_button.pack(pady=5)
        #Toggle button
        self.toggle_button = tk.Button(self.left_frame, text="Toggle Frequency Plots", command=self.toggle_plot)
        self.toggle_button.pack(padx=5, pady=5)

        # Create the canvas for plot
        self.figure, self.axs = plt.subplots(1, 1, figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack(padx=20, pady=30)

        # Output label below the graph
        self.output_label = tk.Label(self.root, text="", wraplength=400, justify="left")
        self.output_label.pack(pady=10)

        # File label
        self.file_label = tk.Label(self.root, text="No file loaded", wraplength=400, bg="gray", fg="blue", font=("Corbel", 10))
        self.file_label.pack(pady=5)

        # File loading button and label
        self.load_button = tk.Button(self.root, text="Load Audio File", command=self.load_file)
        self.load_button.pack(pady=10)
    #Button functionnality

    def load_file(self):
        """Prompt user to load a file and pass it to the controller."""
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.aac *m4a")])
        if file_path:
            self.controller.load_file(file_path)

    def update_file_label(self, file_name):
        """Update the label with the file name."""
        self.file_label.config(text=f"Loaded File: {file_name}")

    def display_stats(self, stats):
        """Display audio statistics."""
        self.output_label.config(text=stats)

    def plot_waveform(self, audio, sr):
        """Plot the waveform of the audio."""
        self.axs.cla()
        librosa.display.waveshow(audio, sr=sr, ax=self.axs)
        self.axs.set_title("Waveform")
        self.canvas.draw()

    def additional_visualization(self):
        self.controller.display_additional_visualization()

    def toggle_plot(self):
        self.controller.toggle_frequency_plot()

    def plot_frequency_rt60(self, freq_name, value):
        """Plot RT60 for a specific frequency band."""
        self.axs.cla()
        self.axs.bar([freq_name], [value], color='blue')
        self.axs.set_title(f"RT60 for {freq_name}")
        self.axs.set_ylabel("RT60 (s)")
        self.canvas.draw()


    def individual_rt60(self):
        self.RT60.display_individual_plots()

    def combined_rt60(self):
        self.RT60.display_combined_plot()

    def display_difference(self):
        self.RT60.display_difference()

    def toggle_plot(self):
        self.controller.toggle_frequency_plot()
