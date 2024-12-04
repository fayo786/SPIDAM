#importing library for the gui
import tkinter as tk
#import matplotlib.pyplot as plt
#from tkinter import Text
#from tkinter import Label
#from tkinter import filedialog
#from tkinter import messagebox

#this is a simple window
window = tk.Tk()
#Convert Audio button
Convert_Audio_Button = tk.Button(window, text = "Convert Audio")
Convert_Audio_Button.grid(column = 2, row = 0, sticky = "ne", padx = 10, pady = 10)
#Load audio button
convert_load = tk.Button (window, text = "Load Audio")
convert_load.grid(column=1, row=0, sticky = "ne", padx =10, pady=10)
window.mainloop()
