# SPIDAM
Scientific Python Interactive Data Acoustic Modeling
Software that allows users to make any audio file into a graph, such as a bar chart, waveform, histogram, spectrogram, or graph of the low, mid, and high frequencies.

---
## Table of Contents
* [Needed files](#files)
* [Nedded Modules](#modules)
* [Installation Instructions](#instructions)
* [Usage](#how-to-use)

---
<a name="instructions"></a>
## Installation Instructions
1) Attain the files `controller.py`, `module.py`, `GUI.py`, `RT60.py`, and `main.py` via forking
2) Open up Command Prompt and use `cd` to get into the directory/folder where you downloaded the source code.
3) Use `python -m venv .venv` to create a virtual environment if you don't want to download all the Python modules globally on your computer. (Syntax may vary for different terminals or operating systems)
4) Use `.\.venv\Scripts\activate` to activate the virtual environment. (Syntax may vary for different terminals or operating systems)
5) Install all the modules to the virtual environment with `pip install -r requirements.txt`.
6) Run the program with `python main.py` or `python3 main.py`
> There are different ways to do this, but I only cover one that works.
---
<a name="how-to-use"></a>
## Usage Instructions
* Importing an audio file
  > After opening the program, press the `Load File` button to open your File Explorer/Finder. Please select the audio file you'd like to import into the software.
  
  > After selecting the file, ensure that you press `Open` for the software to convert the file to .wav and store it for use in the program.

* Seeing statistics (details of files) 
  > After downloading a file, Statistic will show .....
  > A waveform of the audio will be displayed automatically

* Displaying a graph of the audio 
  > After downloading a file, you can select the "Plot" buttons to plot the data. This will cause a separate window to appear with the desired graph. 
  
* Closing the program
  > To close the program anytime, use the `X` button built into the window.
---
<a name="files"></a>
## Needed Files
#### [`main.py`](https://github.com/fayo786/SPIDAM/blob/main/main.py)
  > Runs the program calling the other modules

#### [`GUI.py`](https://github.com/fayo786/SPIDAM/blob/main/GUI.py)
  > Contains the class **GUI**, which possesses the methods to load a file, display stats, and define widget functions.

  > Contains the code that is later used in **controller** and **RT60**. 

#### [`module.py`](https://github.com/fayo786/SPIDAM/blob/main/module.py)
  > Contains the class **Module** and the methods that ensure data is processed, the audio is clean, and the graphs are plotted.

#### [`controller.py`](https://github.com/fayo786/SPIDAM/blob/main/controller.py)
  > Contains the class **controller**, which entails the load file button function and the process data.

#### [`RT60.py`](https://github.com/fayo786/SPIDAM/blob/main/RT60.py)
  > Contains functions, which entails the functionality of buttons to display graphs.

---
<a name="modules"></a>
## Needed Modules
The modules (and their versions) that are necessary to run the program from are listed in the file [`requirements.txt`](""). A general list of the modules used are below:

* [matplotlib](https://matplotlib.org/stable/index.html) (*pyplot*)
* [numpy](https://numpy.org/doc/)
* [os](https://docs.python.org/3/library/os.html)
* [pydub](https://github.com/jiaaro/pydub) (*AudioSegment*)
* [scipy.io](https://docs.scipy.org/doc/) (*wavfile*)
* [tkinter](https://docs.python.org/3/library/tk.html) (*Text*, *Label*, *filedialog*)
* [wave](https://docs.python.org/3/library/wave.html)

The files [`controller.py`](https://github.com/fayo786/SPIDAM/blob/main/controller.py), [`module.py`](https://github.com/fayo786/SPIDAM/blob/main/module.py), [`GUI.py`](https://github.com/fayo786/SPIDAM/blob/main/GUI.py),[`RT60.py`](https://github.com/fayo786/SPIDAM/blob/main/RT60.py),[`main.py`](https://github.com/fayo786/SPIDAM/blob/main/main.py) must also be imported in order for the program to run.
