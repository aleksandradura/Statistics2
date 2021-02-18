import tkinter as tk
import start as s
tempFile = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\example.csv'

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(s.StartPage)
        self.geometry('800x500')
        self.title("Statistic measures")
        self.configure(bg='#bdcebe')

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

def cleanFile(tempFile):
    f = open(tempFile, 'r+')
    f.truncate()
    f.close()

cleanFile(tempFile)
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()