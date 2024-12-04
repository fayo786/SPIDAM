from view import GUI
from module import DataProcessor #improting a different module
import tkinter as tk

#controller adds functionality and initializes
class Controller:
    def __init__(self):
      #Initializing window
        self.root = tk.Tk()
      #calling the GUI method and class
        self.view = GUI(self.root, self)
      #importing processing function
        self.processor = DataProcessor()

  #functional load button
    def load_file(self, file_path):
        try:
            data = self.processor.load_data(file_path)
            self.view.show_message("File loaded successfully!")
            return data
        except Exception as e:
            self.view.show_message(f"Error loading file: {e}")
            return None
#funtionality of processing function
    def process_data(self, data):
        try:
            cleaned_data = self.processor.clean_data(data)
            stats = self.processor.calculate_statistics(cleaned_data)
            self.view.display_stats(stats)
            self.processor.plot_waveform(cleaned_data)
        except Exception as e:
            self.view.show_message(f"Error processing data: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Controller()
    app.run()
