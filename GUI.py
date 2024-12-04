#importing library for the gui
import tkinter as tk
from tkinter import messagebox, filedialog


#import matplotlib.pyplot as plt
#from tkinter import Text
#from tkinter import Label
#from tkinter import filedialog
#from tkinter import messagebox

#this is a simple window
class GUI:
    def __init__(self,root,controller):
        self.root = root
        self.controller = controller
        self.root.title("Audio Analysis Tools")
      #creting widgets
        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self.root, text="Load File", command=self.load_file)
        self.load_button.pack()

        self.stats_label = tk.Label(self.root, text="Statistics:")
        self.stats_label.pack()

        self.stats_text = tk.Text(self.root, height=10, width=50)
        self.stats_text.pack()

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.aac")])
        if file_path:
            data = self.controller.load_file(file_path)
            if data:
                self.controller.process_data(data)

    def show_message(self, message):
        messagebox.showinfo("Info", message)

    def display_stats(self, stats):
        self.stats_text.delete(1.0, tk.END)
        for key, value in stats.items():
            self.stats_text.insert(tk.END, f"{key}: {value}\n")
'''window = tk.Tk()
#Convert Audio button
Convert_Audio_Button = tk.Button(window, text = "Convert Audio")
Convert_Audio_Button.grid(column = 2, row = 0, sticky = "ne", padx = 10, pady = 10)
#Load audio button
convert_load = tk.Button (window, text = "Load Audio")
convert_load.grid(column=1, row=0, sticky = "ne", padx =10, pady=10)
window.mainloop()'''
