import tkinter as tk
from scipy import stats
from scipy import special
import numpy as np
import app
import start as st

def takeResultFromFile():
    result = []
    with open(app.tempFile, 'r') as file1:
        lines = file1.readlines()
        for line in lines:
            result.append(float(line))
    return result

def takeResultFromFile2Lines():
    result, result1 = [], []
    with open(app.tempFile, 'r') as file1:
        lines = file1.readlines()
        for line in lines:
            x = line.split(' ')
            result.append(float(x[0]))
            result1.append(float(x[1]))
        return result, result1

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

class StandardDeviation(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Standard deviation:", width=40, font="none 14 bold")
        self.answer.pack(pady=50)

        self.arrayText = tk.Label(self)
        self.arrayText.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.countMeasures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def countMeasures(self):
        self.df = []
        self.df = takeResultFromFile()

        if len(self.df) >= 3:
            self.result = stats.tstd(self.df)

            self.array = ""
            for x in self.df:
                self.array += str(x) + "; "
            self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")

            print("Standard deviation:", str(self.result))
            self.answer.config(text="Result: " + str(self.result), font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 3", font="none 28 bold")
        app.cleanFile(app.tempFile)

class PopulationStandardDeviation(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Population standard deviation:", width=40, font="none 14 bold")
        self.answer.pack(pady=50)

        self.arrayText = tk.Label(self)
        self.arrayText.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.countMeasures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def countMeasures(self):
        self.df = []
        self.df = takeResultFromFile()

        if len(self.df) >= 3:
            self.result = stats.tstd(self.df, ddof=0)

            self.array = ""
            for x in self.df:
                self.array += str(x) + "; "
            self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")

            print("Population standard deviation:", str(self.result))
            self.answer.config(text="Result: " + str(self.result), font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 3", font="none 28 bold")
        app.cleanFile(app.tempFile)

class MeanAbsoluteDeviation(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Mean Absolute Deviation:", width=40, font="none 14 bold")
        self.answer.pack(pady=50)

        self.arrayText = tk.Label(self)
        self.arrayText.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.countMeasures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def countMeasures(self):
        self.df = []
        self.df = takeResultFromFile()

        if len(self.df) >= 3:
            self.mean = stats.tmean(self.df)
            self.sum = 0
            for x in self.df:
                self.sum += abs(x - self.mean)
            self.result = self.sum / len(self.df)

            self.array = ""
            for x in self.df:
                self.array += str(x) + "; "
            self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")

            print("Mean Absolute Deviation:", str(self.result))
            self.answer.config(text="Result: " + str(self.result), font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 3", font="none 28 bold")
        app.cleanFile(app.tempFile)

class PoissonDistribution(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Poisson Distribution:", width=40, font="none 14 bold")
        self.answer.pack(pady=50)

        self.t1 = tk.Label(self)
        self.t1.pack(pady=10)
        self.t2 = tk.Label(self)
        self.t2.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=20)

        self.countMeasures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def countMeasures(self):
        self.df1, self.df2 = [], []
        self.df1, self.df2 = takeResultFromFile2Lines()

        if len(self.df1) == 1 & len(self.df2) == 1:
            self.result = (np.power(self.df1[0], self.df2[0]) * np.exp(-self.df1[0])) / special.factorial(self.df2[0])

            self.t1.config(text="Expected number of events : " + str(self.df1[0]), font="none 14 bold")
            self.t2.config(text="Number of occurrences: " + str(self.df2[0]), font="none 14 bold")
            print("Poisson Distribution:", str(self.result))
            self.answer.config(text="Result: " + str(self.result), font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be exactly one in each array", font="none 28 bold")
        app.cleanFile(app.tempFile)