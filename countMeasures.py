import math
import tkinter as tk

import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
from scipy import special
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

class Quantile(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Quantiles:", width=40, font="none 14 bold")
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
            self.result = np.quantile(self.df, [.25, .5, .75])
            median = np.quantile(self.df, [.5])
            tertile = np.quantile(self.df, [0.33, 0.66])
            self.array = ""
            for x in self.df:
                self.array += str(x) + "; "
            self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")

            self.answer.config(text="Quartile: " + str(self.result) + "Tertile: " + str(tertile) + "Median: " + str(median), font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 3", font="none 28 bold")
        app.cleanFile(app.tempFile)

class LinearRegression(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Linear regression:", width=40, font="none 14 bold")
        self.answer.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.countMeasures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def countMeasures(self):
        x, y = takeResultFromFile2Lines()
        x = np.array(x)
        y = np.array(y)
        if len(x) >= 3:
            res = stats.linregress(x,y)
            fig = Figure(figsize=(5, 3))
            ax = fig.add_subplot()
            
            ax.plot(x, y, 'o', label='original data')
            ax.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')
            ax.legend()
            self.canvas = FigureCanvasTkAgg(fig, self)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()
            self.answer.config(text="Linear regression formula: Y = " + "{:.2f}".format(res.slope) + " * X + " + "{:.2f}".format(res.intercept), font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 3", font="none 28 bold")
        app.cleanFile(app.tempFile)

class PearsonCorrelation(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Pearson correlation:", width=40, font="none 14 bold")
        self.answer.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.countMeasures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def countMeasures(self):
        x, y = takeResultFromFile2Lines()
        x = np.array(x)
        y = np.array(y)
        if len(x) >= 3:
            r, p = stats.pearsonr(x,y)
            fig = Figure(figsize=(5, 3))
            ax = fig.add_subplot()
            ax.plot(x, y, 'o', label='original data')
            ax.legend()
            self.canvas = FigureCanvasTkAgg(fig, self)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()
            self.answer.config(text="pearson correlation coefficient  P(X,Y)= " + "{:.2f}".format(r), font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 3", font="none 28 bold")
        app.cleanFile(app.tempFile)

class InterquartileRange(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Interquartile Range:", width=40, font="none 14 bold")
        self.answer.pack(pady=50)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)
        self.answer2 = tk.Label(self)
        self.answer2.pack(pady=10)
        self.answer3 = tk.Label(self)
        self.answer3.pack(pady=10)

        self.count_measures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def count_measures(self):
        self.df = []
        self.df = takeResultFromFile()

        if len(self.df) >= 3:
            self.q1 = np.percentile(self.df, 25)
            self.q3 = np.percentile(self.df, 75)

            self.result = self.q3-self.q1

            print("Interquartile Range:", str(self.result))
            self.answer.config(text="Result: " + str(self.result), font="none 14 bold")
            self.answer2.config(text="Q1: " + str(self.q1), font="none 14 bold")
            self.answer3.config(text="Q3: " + str(self.q3), font="none 14 bold")

        else:
            self.answer.config(text="Amount of values need to be more than 3", font="none 28 bold")
        app.cleanFile(app.tempFile)


class BoxPlot(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Box plot", width=40, font="none 14 bold")
        self.answer.pack(pady=1)

        self.count_measures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def count_measures(self):
        self.df = []
        self.df = takeResultFromFile()

        if len(self.df) >= 3:

            self.answer2 = tk.Label(self)
            self.answer2.pack(pady=1)
            self.answer3 = tk.Label(self)
            self.answer3.pack(pady=1)

            fig = Figure(figsize=(5, 3))
            ax = fig.add_subplot()
            labels = ['Data']
            ax.boxplot(self.df, labels=labels)
            self.canvas = FigureCanvasTkAgg(fig, self)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()

            self.q1 = np.percentile(self.df, 25)
            self.q2 = np.percentile(self.df, 50)
            self.q3 = np.percentile(self.df, 75)

            self.answer2.config(text="Q1: " + str(self.q1) + "   Q2 (Median): " + str(self.q2) + "   Q3: " + str(self.q3), font="none 10 bold")
            self.answer3.config(text="IQR (Q3-Q1): " + str(self.q3-self.q1), font="none 10 bold")

        else:
            self.answer.config(text="Amount of values need to be more than 3", font="none 28 bold")
        app.cleanFile(app.tempFile)

class MinSampleCountForPopAVGStud_t(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Minimal sample count for population average\n(Student's t-distribution):", width=40, font="none 14 bold")
        self.answer.pack(pady=30)

        self.label2 = tk.Label(self, text='Margin of error (e.g. 0.45):')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.entry_Mor = tk.Entry(self)
        self.entry_Mor.pack()

        self.label3 = tk.Label(self, text='Confidence level (e.g. 0.95 ; 95%):')
        self.label3.config(font=('helvetica', 10))
        self.label3.pack()
        self.entry_cl = tk.Entry(self)
        self.entry_cl.pack()

        self.label4 = tk.Label(self, text='Standard deviation:')
        self.label4.config(font=('helvetica', 10))
        self.label4.pack()
        self.entry_stdDev = tk.Entry(self)
        self.entry_stdDev.pack()

        self.label4 = tk.Label(self, text='Initial sample:')
        self.label4.config(font=('helvetica', 10))
        self.label4.pack()
        self.entry_initSample = tk.Entry(self)
        self.entry_initSample.pack()

        self.button1 = tk.Button(self, text='Get minimal sample size', command=self.count_measures, bg='brown', fg='white')
        self.button1.pack(pady=20)

        self.answer2 = tk.Label(self)
        self.answer2.pack(pady=20)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def count_measures(self):
        self.df = []
        self.df = takeResultFromFile()

        str_cl = self.entry_cl.get()
        str_mor = self.entry_Mor.get()
        str_sdtdev = self.entry_stdDev.get()
        str_initSample = self.entry_initSample.get()

        if not str_cl or not str_mor or not str_sdtdev or not str_initSample:
            self.answer2.config(text="!!! Fill all data !!!", font="none 14 bold")
        else:
            if "%" in str_cl:
                self.cl = float(str_cl.replace("%", ""))
            else:
                self.cl = float(str_cl.replace(",", "."))*100
                self.initSample = int(str_initSample)
                self.mor = float(str_mor.replace(",", "."))
                self.std_Deviation = float(str_sdtdev.replace(",", "."))
                self.t_alfa = stats.t.ppf(1 - ((100 - self.cl) / 2 / 100), self.initSample - 1)
                self.result = (self.t_alfa*(self.std_Deviation/self.mor))**2
                self.answer2.config(text="Result: " + str(math.ceil(self.result)), font="none 14 bold")

        app.cleanFile(app.tempFile)


class MinSampleCountForPopAVGNormal(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Minimal sample count for population average\n(Normal distribution):", width=40, font="none 14 bold")
        self.answer.pack(pady=30)

        self.label2 = tk.Label(self, text='Margin of error (e.g. 0.45):')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.entry_Mor = tk.Entry(self)
        self.entry_Mor.pack()

        self.label3 = tk.Label(self, text='Confidence level (e.g. 0.95 ; 95%):')
        self.label3.config(font=('helvetica', 10))
        self.label3.pack()
        self.entry_cl = tk.Entry(self)
        self.entry_cl.pack()

        self.label4 = tk.Label(self, text='Standard deviation:')
        self.label4.config(font=('helvetica', 10))
        self.label4.pack()
        self.entry_stdDev = tk.Entry(self)
        self.entry_stdDev.pack()

        self.button1 = tk.Button(self, text='Get minimal sample size', command=self.count_measures, bg='brown', fg='white')
        self.button1.pack(pady=20)

        self.answer2 = tk.Label(self)
        self.answer2.pack(pady=20)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def count_measures(self):
        self.df = []
        self.df = takeResultFromFile()

        str_cl = self.entry_cl.get()
        str_mor = self.entry_Mor.get()
        str_sdtdev = self.entry_stdDev.get()

        if not str_cl or not str_mor or not str_sdtdev:
            self.answer2.config(text="!!! Fill all data !!!", font="none 14 bold")
        else:
            if "%" in str_cl:
                self.cl = float(str_cl.replace("%", ""))/100.0
            else:
                self.cl = float(str_cl.replace(",", "."))
                self.mor = float(str_mor.replace(",", "."))
                self.std_Deviation = float(str_sdtdev.replace(",", "."))
                self.z_alfa = stats.norm.ppf((1 + self.cl) / 2.)
                print(self.z_alfa)
                self.result = (self.z_alfa*(self.std_Deviation/self.mor))**2
                self.answer2.config(text="Result: " + str(math.ceil(self.result)), font="none 14 bold")

        app.cleanFile(app.tempFile)

class ArithmeticMean(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Arithmetic mean:", width=40, font="none 14 bold")
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

        if len(self.df) > 0:
            self.result = np.mean(self.df)
            self.array = ""
            for x in self.df:
                self.array += str(x) + "; "
            self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")

            self.answer.config(text="Arithmetic Mean: " + str(self.result),  font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 0", font="none 28 bold")
        app.cleanFile(app.tempFile)

class HarmonicMean(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Harmonic mean:", width=40, font="none 14 bold")
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
        self.correctValue = True

        if len(self.df) > 0:
            for x in self.df:
                if x == 0.0:
                    self.correctValue = False
                    self.answer.config(text="Values must be not equal 0", font="none 28 bold")

            if self.correctValue:
                self.array = ""
                for x in self.df:
                    if x == 0.0:
                        self.answer.config(text="Amount of values need to be more than 0", font="none 28 bold")
                    self.array += str(x) + "; "

                self.result = stats.hmean(self.df)

                self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")

                self.answer.config(text="Harmonic Mean: " + str(round(self.result,4)),  font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 0", font="none 28 bold")
        app.cleanFile(app.tempFile)

class VariationCoefficient(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Coefficient of variation:", width=40, font="none 14 bold")
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

        if len(self.df) > 0:
            self.mean = np.mean(self.df)
            if self.mean == 0.0:
                self.answer.config(text = "Wrong dataset, arithmetic mean = 0", font="none 28 bold")
            else:
                self.result = np.std(self.df)/self.mean
                self.array = ""
                for x in self.df:
                    self.array += str(x) + "; "
                self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")

                self.answer.config(text="Coefficient of variation: " + str(round(self.result,4)),  font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 0", font="none 28 bold")
        app.cleanFile(app.tempFile)
