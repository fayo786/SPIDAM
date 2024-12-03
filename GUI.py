#importing library for the gui
import tkinter as tk

#this is a simple window
window = tk.Tk()
Convert_Audio_Button = tk.Button(window, text = "Convert Audio")
Convert_Audio_Button.grid(column = 1, row = 0, sticky = "ne", padx = 10, pady = 10)
window.mainloop()
