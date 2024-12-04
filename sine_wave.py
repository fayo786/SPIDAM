import tkinter as tk
import os
from tkinter import filedialog, messagebox
from pydub import AudioSegment
AudioSegment.ffmpeg = r"C:\ffmpeg\downloads\ffmpeg.exe"




# Function to load and convert audio
def load_audio():
   # Open file dialog to choose an audio file
   file_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio Files", "*.wav;*.mp3;*.flac;*.ogg;*.m4a")])


   if file_path:
       try:
           # Check the file extension
           file_extension = os.path.splitext(file_path)[1].lower()


           # If it's not a .wav file, convert it
           if file_extension != '.wav':
               audio = AudioSegment.from_file(file_path)
               new_file_path = file_path.rsplit('.', 1)[0] + ".wav"
               audio.export(new_file_path, format="wav")
               messagebox.showinfo("Success", f"File converted to .wav and saved as {new_file_path}")
               print(f"Converted file saved as {new_file_path}")
           else:
               messagebox.showinfo("Success", f"File loaded: {file_path}")
               print(f"File loaded: {file_path}")


       except Exception as e:
           messagebox.showerror("Error", f"Failed to load or convert audio: {e}\n")
           print(f"Error: {e}")





# Create the main window
root = tk.Tk()
root.title("Audio Processing")


# Set window size




# Create a frame for the buttons at the top (bug fix)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)


# Create buttons
load_audio_button = tk.Button(button_frame, text="Load Audio", command = load_audio)
load_audio_button.grid(row=0, column=0, padx=10)


convert_audio_button = tk.Button(button_frame, text="Convert Audio")
convert_audio_button.grid(row=0, column=1, padx=10)


show_graph_button = tk.Button(button_frame, text="Show Graph")
show_graph_button.grid(row=0, column=2, padx=10)


display_graphs_button = tk.Button(button_frame, text="Merge Graphs")
display_graphs_button.grid(row=0, column=3, padx=10)


alternate_graphs_button = tk.Button(button_frame, text="Alternate Between Graphs")
alternate_graphs_button.grid(row=0, column=4, padx=10)


# Create a label or canvas for the graph display at the bottom
graph_frame = tk.Frame(root, width=400, height=200, bg="lightgray")
graph_frame.pack(pady=20)


# Start the GUI loop
root.mainloop()


