import tkinter as tk
from scipy import stats
import app
import start as st


def takeResultFromFile():
    result = []
    with open(app.tempFile, 'r') as file1:
        lines = file1.readlines()
        for line in lines:
            result.append(float(line))
    return result

class ShapiroWilkTest(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Shapiro_Wilk Test:", width=40, font="none 14 bold")
        self.answer.pack(pady=50)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.answer2 = tk.Label(self)
        self.answer2.pack(pady=10)

        self.countMeasures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def countMeasures(self):
        self.df = []
        self.df = takeResultFromFile()
        if len(self.df) >= 3:
            self.stat, self.pvalue = stats.shapiro(self.df)
            print("Shapiro_Wilk Test:", str(self.stat), str(self.pvalue))
            self.answer.config(text="Statistic: " + str(self.stat), font="none 14 bold")
            self.answer2.config(text="Pvalue: " + str(self.pvalue), font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 3", font="none 28 bold")
        app.cleanFile(app.tempFile)

