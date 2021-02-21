import tkinter as tk
import chooseMeasure as cm
import app

class OneInput(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.initLabel = tk.Label(self, text="Put the number", width=20, font="none 24 bold")
        self.initLabel.pack(pady=20)

        self.entry = tk.Entry(self, width="10")
        self.entry.pack(pady=30)

        self.button = tk.Button(self, text="Add number", width=16, height=2, font="none 14 bold", bg="#3e4444", fg="white", command=self.saveNumbers)
        self.button.pack(pady=10)

        self.button2 = tk.Button(self, text="Measures", width=16, height=2, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(cm.ChooseMeasureOne))
        self.button2.pack(pady=10)

        self.answer = tk.Label(self, text='')
        self.answer.pack(pady=30)

    def saveNumbers(self):
        with open(app.tempFile, 'a') as file1:
            try:
                self.answer.config(text=float(self.entry.get()), font="none 14 bold")
                file1.write(str(self.entry.get()))
                file1.write('\n')
            except ValueError:
                self.answer.config(text="Wrong Value. Try again.", font="none 14 bold")

