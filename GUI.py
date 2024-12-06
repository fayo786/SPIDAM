import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import librosa
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("RT60 Audio Analyzer")
        self.create_widgets()

    def create_widgets(self):
        # Create a frame to hold the buttons on the left
        self.left_frame = tk.Frame(self.root)  # Add background for better styling
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)  # Align to the left of the root window

        # Buttons in the left frame
        self.plot_individual_button = tk.Button(
        self.left_frame, text="Individual RT60", command="", width=20)
        self.plot_individual_button.pack(pady=5)

        self.plot_combined_button = tk.Button(
        self.left_frame, text="Combined RT60", command="", width=20)
        self.plot_combined_button.pack(pady=5)

        self.difference_button = tk.Button(
        self.left_frame, text="Difference to 0.5s", command="", width=20)
        self.difference_button.pack(pady=5)

        self.extra_button = tk.Button(
        self.left_frame, text="Additional Visualization", command="", width=20)
        self.extra_button.pack(pady=5)

        # Toggle button
        self.toggle_button = tk.Button(
        self.left_frame, text="Toggle Frequency Plots", command="")
        self.toggle_button.pack(padx=5, pady=5)

        # Create the canvas for plot
        self.figure, self.axs = plt.subplots(1, 1, figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack(padx=20, pady=30)
        # Output label below the graph
        self.output_label = tk.Label(self.root, text="", wraplength=400, justify="left")
        self.output_label.pack(pady=10)
        self.file_label = tk.Label(
            self.root,
            text="No file loaded",
            wraplength=400,
            bg="gray",
            fg="blue",
            font=("Corbel", 10),
        )
        self.file_label.pack(pady=5)
        # File loading button and label
        self.load_button = tk.Button(self.root, text="Load Audio File", command="")
        self.load_button.pack(pady=10)

        self.current_plot_index = 0
"""import tkinter as tk
from tkinter import filedialog, messagebox, ttk
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
        #Toggle plots
        self.toggle_button = tk.Button(self.root, text="Toggle Frequency Plots", command=self.toggle_plot)
        self.toggle_button.pack(padx=5,pady=5)
        # Button with blue background and white text
        self.load_button = tk.Button(self.root, text="Load Audio File", command=self.load_file)
        self.load_button.pack(pady=10)


        self.file_label = tk.Label( self.root, text="No file loaded", wraplength=400, bg="gray",fg="blue", font=("Corbel", 10))
        self.file_label.pack(pady=5)


        #Display individual RT60 graphs
        self.plot_individual_button = tk.Button(self.root, text="Individual RT60", command="",width=10)
        self.plot_individual_button.pack(side="left", padx=5, pady=5)
        #combined RT60 button
        self.plot_combined_button = tk.Button(self.root, text="Combined RT60", command="",width=10)
        self.plot_combined_button.pack(pady=5)
        #canvas!
        self.figure, self.axs = plt.subplots(1, 1, figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack(padx=20, pady=30)


        #Differenceto0.5
        self.difference_button = tk.Button(self.root, text="Difference to 0.5s", command="", width=20)
        self.difference_button.pack(side="left",padx=5,pady=5)

        #additional vizualization stuff
        self.extra_button = tk.Button(self.root, text="Additional Visualization", command="",width=30)
        self.extra_button.pack(side="left",padx=5,pady=10)



        self.output_label = tk.Label(self.root, text="", wraplength=800, justify="left")
        self.output_label.pack(pady=10)

        self.current_plot_index = 0

  def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.aac *m4a")])
        if file_path:
            self.controller.load_file(file_path)

    def update_file_label(self, file_name):
        self.file_label.config(text=f"Loaded File: {file_name}")

    def display_stats(self, stats):
        self.output_label.config(text=stats)

    def plot_waveform(self, audio, sr):
       
        self.axs.cla()
        librosa.display.waveshow(audio, sr=sr, ax=self.axs)
        self.axs.set_title("Waveform")
        self.canvas.draw()

    def plot_frequency_rt60(self, freq_name, value):
    
        self.axs.cla()
        self.axs.bar([freq_name], [value], color='blue')
        self.axs.set_title(f"RT60 for {freq_name}")
        self.axs.set_ylabel("RT60 (s)")
        self.canvas.draw()

    def toggle_plot(self):
      
        self.controller.toggle_frequency_plot()"""
