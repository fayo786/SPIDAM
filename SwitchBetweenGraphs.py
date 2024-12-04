import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

##########doing a cosine and sin code to display the main functionality that we are looking for,
##########3the button that switches between low, med and high plots

### creates the x values, from - to +
xAXIS = np.linspace(-2 * np.pi, 2 * np.pi, 400)

### Calculate sine and cosine for each y axis
YAXISsin = np.sin(xAXIS)
YAXIScos = np.cos(xAXIS)

# # Create a tkinter window
root = tk.Tk()
root.title("Graphs")

fig, ax = plt.subplots(figsize=(6, 4))

# Plot sine initially
line, = ax.plot(xAXIS, YAXISsin, label='sin(x)', color='blue')
ax.set_title('Sine Function')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.legend()

# Add the figure to the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

####bug fix so the code works
is_cos = True  ########## True for sine, False for cosine
#Function to toggle between sine and cosine
def toggle_graph():
    global is_cos


 ###restart so the graph aren't overlapping
    ax.clear()


#Alternate between sine and cosine
    if is_cos:
        ax.plot(xAXIS, YAXIScos, label='cos(x)', color='red')
        ax.set_title('Cosine Function')

        ax.set_ylabel('cos(x)')
    else:
        ax.plot(xAXIS, YAXISsin, label='sin(x)', color='blue')


        ax.set_title('Sine Function')
        ax.set_ylabel('sin(x)')

    ax.set_xlabel('x')

    ax.grid(True)


    ax.legend()

    ######Redraw the graphs window
    canvas.draw()

    is_cos = not is_cos


###########Create the button to change between the graphs
button = tk.Button(root, text="Switch Graph", command=toggle_graph)

button.pack()

# idk what this does but it is necessary for the code to work
root.mainloop()
