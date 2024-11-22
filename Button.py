import tkinter as tk

window = tk.Tk()

window.grid_columnconfigure(1,weight=1)


convert_load = tk.Button (window, text = "Load Audio")
convert_load.grid(column=1, row=0, sticky = "ne", padx =10, pady=5)

window.mainloop()
