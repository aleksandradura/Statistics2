import math
import tkinter as tk

import numpy as np
from math import sqrt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
from scipy import special
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.stats.descriptivestats import sign_test
import seaborn as sns
import statistics as statistics_native

import app
import start as st
import oneInput as oi
import twoInputs as ti



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

class StudentsTDistribution(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.fig = Figure(figsize=(5, 3))
        self.ax = self.fig.add_subplot()
        self.ax.set_title("Student's t-Distribution")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)

        self.answer = tk.Label(self, text="Student's t-Distribution:", width=40, font="none 14 bold")
        self.answer.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.answer2 = tk.Label(self)
        self.answer2.pack(pady=10)

        self.values = []
        self.label2 = tk.Label(self, text='Degrees of freedom:')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.entry_df = tk.Entry(self)
        self.entry_df.pack()

        self.button1 = tk.Button(self, text='Draw the figure', command=self.countMeasures, bg='brown',
                                 fg='white')
        self.button1.pack(pady=10)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)


    def countMeasures(self):
        str_df = self.entry_df.get()
        self.values.append(str_df)
        self.canvas.get_tk_widget().pack_forget()
        handles = []
        lines = []

        if (len(self.values) > 0):
            #and str_df[0] != '-' and str_df[0] != '0'):

            for i in self.values:
                if int(i) > 0:
                    self.x = np.linspace(stats.t.ppf(0.01, float(i)), stats.t.ppf(0.99, float(i)), 100)
                    """self.array = ""
                    for x in self.df:
                        self.array += str(x) + "; "
                    self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")"""
                    line, = self.ax.plot(self.x, stats.t.pdf(self.x, float(i)))
                    handles.append(str("k = " + str(i)))
                    lines.append(line)
                    self.ax.legend(lines, handles)
                    self.canvas.draw()
                    self.canvas.get_tk_widget().pack()

                else:
                    self.answer2.config(text="Wrong value - must be greater then 0", font="none 14 bold")
            self.answer.config(text="Resize the window to see the figure",  font="none 14 bold")
        else:
            self.answer.config(text = "Degrees of freedom must be not empty", font="none 18 bold")
        app.cleanFile(app.tempFile)

class ChiSquaredTest(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Pearson Chi-squere test:", width=40, font="none 14 bold")
        self.answer.pack(pady=20)

        self.arrayText = tk.Label(self)
        self.arrayText.pack(pady=10)

        self.arrayText2 = tk.Label(self)
        self.arrayText2.pack(pady=10)

        self.label2 = tk.Label(self, text='Trust level:')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.entry_ddof = tk.Entry(self)
        self.entry_ddof.pack()

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.button1 = tk.Button(self, text='Count Chi-square test', command=self.countMeasures, bg='brown',
                                 fg='white')
        self.button1.pack(pady=20)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def countMeasures(self):
        self.df1, self.df2 = [], []
        self.df1, self.df2 = takeResultFromFile2Lines()

        str_ddof = self.entry_ddof.get()

        if len(self.df1) > 0 and len(self.df2) > 0:

            a,b  = stats.chisquare(np.array(self.df1),np.array(self.df2),float(str_ddof))
            self.array1 = ""
            self.array2 = ""
            for x in self.df1:
                self.array1 += str(x) + "; "
            for y in self.df2:
                self.array2 += str(y) + "; "
            self.arrayText.config(text="Array: " + str(self.array1), font="none 14 bold")
            self.arrayText2.config(text="Array: " + str(self.array2), font="none 14 bold")

            self.answer.config(text="The chi-squared test statistic: " + str(round(a,2)) + " and the p-value if the test is: " + str(round(b,4)), font="none 14 bold")

        else:
            self.answer.config(text = "Minimum one number in each array required", font="none 28 bold")
        app.cleanFile(app.tempFile)

class SignTest(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Sign test:", width=40, font="none 14 bold")
        self.answer.pack(pady=10)

        self.arrayText = tk.Label(self)
        self.arrayText.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.countMeasures()

        self.button = tk.Button(self, text="Insert data", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(oi.OneInput))
        self.button.pack(pady=5)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def countMeasures(self):
        self.df = []
        self.df= takeResultFromFile()

        if len(self.df) > 3:
            h_median = self.df[0]
            self.df.pop(0)
            data_set = self.df
            result = sign_test(data_set, h_median)

            if result[0] == 0:
                self.result = "the number of values above and below the hypothetical median " + str(h_median) + " is is the same.\nIt means that this is the median of given sample and we cannot reject H0. "
            else:
                self.result = "The number of values above and below the hypothetical median " + str(h_median) + " is not the same."
                if result[1] < 0.05:
                    self.result += "\nAssumming alpha = 0.05 we can reject H0, that number: " + str(h_median) + " is a median of given data set."
                else:
                    self.result += "\nAssumming alpha = 0.05 we cannot reject H0, that number: " + str(h_median) + " is a median of given data set. "

            # self.result += " " + str(result)

            self.array = ""
            iter = 6
            for x in data_set:
                self.array += str(x) + "; "
                iter += 1
                if iter % 8 == 0:
                    self.array += "\n"
            self.arrayText.config(text="Given hypothetical median: " + str(h_median) + "\n\nGiven numbers to verify "
                                                                                         "hypothesis: " + str(
                self.array), font="none 14 bold")

            print("Sign test:", str(self.result))
            self.answer.config(text="Result: " + str(self.result), font="none 14 bold")
        else:
            self.answer.config(text="Sign test checks hypothesis if given number\nis a median of the data set.\n\n "
                                    "Input format:\n  - first number: hypothetical median\n  - next numbers: data set"
                                    "\nTest assumes alpha = 0.05",
                               font="none 14 bold", justify='left')
        app.cleanFile(app.tempFile)


class ANOVA(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="ANOVA:", width=40, font="none 14 bold")
        self.answer.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.arrayText1 = tk.Label(self)
        self.arrayText1.pack(pady=10)

        self.arrayText2 = tk.Label(self)
        self.arrayText2.pack(pady=10)

        self.countMeasures()

        self.button = tk.Button(self, text="Insert data", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(ti.TwoInputs))
        self.button.pack(pady=5)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def countMeasures(self):
        self.df1, self.df2 = [], []
        self.df1, self.df2 = takeResultFromFile2Lines()

        if len(self.df1) > 2:
            result = stats.f_oneway(self.df1, self.df2)

            self.result = ""
            if result[1] < 0.05:
                self.result += "Assuming alpha = 0.05 we can reject H0, that given groups have the same population."
            else:
                self.result += "Assuming alpha = 0.05 we cannot reject H0, that given groups have the same population."

            # self.result += " " + str(result)

            self.array = ""
            for x in self.df1:
                self.array += str(x) + "; "
            self.arrayText1.config(text="Given measures for first group: " + str(self.array), font="none 14 bold")

            self.array = ""
            for x in self.df2:
                self.array += str(x) + "; "
            self.arrayText2.config(text="Given measures for second group: " + str(self.array), font="none 14 bold")

            print("ANOVA:", str(self.result))
            self.answer.config(text="Result: " + str(self.result), font="none 14 bold")
        else:
            self.answer.config(text="The one-way ANOVA tests H0 that two \ngroups have the same population mean.\n\n"
                                    "Input format:\n  - first column: measurements for first group\n"
                                    "  - second column: measurements for second group\n"
                                    "Test assumes alpha = 0.05",
                               font="none 14 bold", justify='left')
        app.cleanFile(app.tempFile)

class ChiSquared(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Chi squared distribution:", width=40, font="none 14 bold")
        self.answer.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.arrayText1 = tk.Label(self)
        self.arrayText1.pack(pady=10)

        self.arrayText2 = tk.Label(self)
        self.arrayText2.pack(pady=10)

        self.countMeasures()

        self.button = tk.Button(self, text="Insert data", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(ti.TwoInputs))
        self.button.pack(pady=5)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def countMeasures(self):
        self.df1, self.df2 = [], []
        self.df1, self.df2 = takeResultFromFile2Lines()

        if len(self.df1) > 0:
            result = stats.chisquare(self.df1,  f_exp=self.df2)

            self.result = ""
            self.result += "degrees of freedom: " + str(len(self.df1)-1)
            self.result += "\n" + str(result)

            self.array = ""
            for x in self.df1:
                self.array += str(x) + "; "
            self.arrayText1.config(text="Observed frequencies: " + str(self.array), font="none 14 bold")

            self.array = ""
            for x in self.df2:
                self.array += str(x) + "; "
            self.arrayText2.config(text="Expected frequencies: " + str(self.array), font="none 14 bold")

            print("Chi squared:", str(self.result))
            self.answer.config(text="Result: " + str(self.result), font="none 14 bold")
        else:
            self.answer.config(text="The chi-square test tests H0 that the categorical \n"
                                    "data has the given frequencies.\n\n "
                                    "Input format:\n  - first column: observed frequencies\n"
                                    "  - second column: expected frequencies",
                               font="none 14 bold", justify='left')
        app.cleanFile(app.tempFile)

class StandardizedThirdCentralMoment(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Standardized third central moment:", width=40, font="none 14 bold")

        self.answer.pack(pady=50)

        self.arrayText = tk.Label(self)
        self.arrayText.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.countMeasures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444",
                                    fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def countMeasures(self):
        self.df = np.array(takeResultFromFile())
        self.correctValue = True

        if len(self.df) > 0:
            self.array = ", ".join([str(i) for i in self.df])
            self.result = stats.moment(self.df, moment=3) / (pow(self.df.std(), 3))

            self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")
            self.answer.config(text="Standardized third central moment: " + str(round(self.result, 4)), font="none 14 bold")
        else:
            self.answer.config(text="Amount of values need to be more than 0", font="none 28 bold")
        app.cleanFile(app.tempFile)

class NonParametricSkew(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Nonparametric skew:", width=40, font="none 14 bold")

        self.answer.pack(pady=50)

        self.arrayText = tk.Label(self)
        self.arrayText.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.countMeasures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444",
                                    fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def countMeasures(self):
        self.df = takeResultFromFile()
        self.correctValue = True

        if len(self.df) > 0:
            self.array = ", ".join([str(i) for i in self.df])
            self.result = stats.skew(self.df)

            self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")
            self.answer.config(text="Nonparametric skew: " + str(round(self.result, 4)), font="none 14 bold")
        else:
            self.answer.config(text="Amount of values need to be more than 0", font="none 28 bold")
        app.cleanFile(app.tempFile)

class Median(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Minimal sample count for population average\n(Normal distribution):", width=40, font="none 14 bold")
        self.answer.pack(pady=30)

        self.answer2 = tk.Label(self)
        self.answer2.pack(pady=20)

        self.count_measures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def count_measures(self):
        self.df = []
        self.df = takeResultFromFile()

        self.result = np.median(self.df)
        self.answer2.config(text="Result: " + str(self.result), font="none 14 bold")

        app.cleanFile(app.tempFile)

class Tailedness(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Tailedness:", width=40, font="none 14 bold")

        self.answer.pack(pady=50)

        self.arrayText = tk.Label(self)
        self.arrayText.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.countMeasures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444",
                                    fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=40)

    def countMeasures(self):
        self.df = takeResultFromFile()
        self.correctValue = True

        if len(self.df) > 5:
            self.array = ", ".join([str(i) for i in self.df])
            self.result = stats.kurtosis(self.df)

            self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")
            self.answer.config(text="Tailedness: " + str(round(self.result, 4)), font="none 14 bold")
        else:
            self.answer.config(text="Amount of values need to be more than 5", font="none 28 bold")
        app.cleanFile(app.tempFile)


class CorrelationTable(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Correlation table:", width=40, font="none 14 bold")
        self.answer.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.countMeasures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def countMeasures(self):
        self.first, self.second = takeResultFromFile2Lines()

        if len(self.first) >= 2:
            self.data = {0: np.array(self.first),
                         1: np.array(self.second)}

            self.df = pd.DataFrame(self.data)
            self.corrTable = self.df.corr()
            self.labels = ["First series", "Second series"]

            fig = Figure(figsize=(5, 3))
            ax = fig.add_subplot()
            ax.matshow(self.corrTable)

            # add labels to corr table
            for i in range(len(self.corrTable)):
                for j in range(len(self.corrTable.columns)):
                    ax.text(j, i, round(self.corrTable[i][j], 4), ha="center", va="center", color="w")

            ax.set_xticks(np.arange(len(self.labels)))
            ax.set_yticks(np.arange(len(self.labels)))
            ax.set_xticklabels(self.labels)
            ax.set_yticklabels(self.labels)
            self.canvas = FigureCanvasTkAgg(fig, self)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()
        else:
            self.answer.config(text = "Amount of values need to be more than 2", font="none 28 bold")
        app.cleanFile(app.tempFile)

class Median(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Median:", width=40, font="none 14 bold")
        self.answer.pack(pady=30)

        self.answer2 = tk.Label(self)
        self.answer2.pack(pady=20)

        self.count_measures()

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def count_measures(self):
        self.df = []
        self.df = takeResultFromFile()

        self.result = np.median(self.df)
        self.answer2.config(text="Result: " + str(self.result), font="none 14 bold")

        app.cleanFile(app.tempFile)


class DistributionOfArithmeticAverage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.fig = Figure(figsize=(5, 3))
        self.ax = self.fig.add_subplot()
        self.ax.set_title("Distribution Of Arithmetic Average")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)

        self.answer = tk.Label(self, text="Distribution Of Arithmetic Average", width=40, font="none 14 bold")
        self.answer.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.answer2 = tk.Label(self)
        self.answer2.pack(pady=10)

        self.values = []
        self.label2 = tk.Label(self, text='Degrees of freedom')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.entry_df = tk.Entry(self)
        self.entry_df.pack()

        self.button1 = tk.Button(self, text='Draw the figure', command=self.countMeasures, bg='brown',
                                 fg='white')
        self.button1.pack(pady=10)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)


    def countMeasures(self):
        x = np.array(takeResultFromFile()).astype(np.float)
        str_df = self.entry_df.get()
        self.values.append(str_df)
        self.canvas.get_tk_widget().pack_forget()
        if (len(self.values) > 0):
            for i in self.values:
                if int(i) > 1:
                    sample_props = np.zeros(10000)
                    for s in range(10000):
                        sample = np.random.choice(x, int(i))
                        sample_props[s] = sample.mean()

                    fig, ax = plt.subplots()
                    sns.distplot(sample_props, color='darkblue',
                                 hist_kws={'edgecolor' 'black'}).set(xlabel='Sample Mean',
                                                                            ylabel='Density')
                    ax.set_title("Distribution Of Arithmetic Average")
                    self.canvas = FigureCanvasTkAgg(fig, master=self)

                    self.canvas.draw()
                    self.canvas.get_tk_widget().pack()
                else:
                    self.answer2.config(text="Wrong value - must be greater then 1", font="none 14 bold")
            self.answer.config(text="Resize the window to see the figure",  font="none 14 bold")
        else:
            self.answer.config(text="Degrees of freedom must be not empty", font="none 18 bold")
        app.cleanFile(app.tempFile)


class IntervalAverageNormalPopulation(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Interval for average of a normal population\n(known Standard deviation):", width=40, font="none 14 bold")
        self.answer.pack(pady=30)

        self.label2 = tk.Label(self, text='Sample size:')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.entry_siz = tk.Entry(self)
        self.entry_siz.pack()

        self.label3 = tk.Label(self, text='Sample average:')
        self.label3.config(font=('helvetica', 10))
        self.label3.pack()
        self.entry_av = tk.Entry(self)
        self.entry_av.pack()

        self.label4 = tk.Label(self, text='Standard deviation:')
        self.label4.config(font=('helvetica', 10))
        self.label4.pack()
        self.entry_sdv = tk.Entry(self)
        self.entry_sdv.pack()

        self.label4 = tk.Label(self, text='Confidence:')
        self.label4.config(font=('helvetica', 10))
        self.label4.pack()
        self.entry_conf = tk.Entry(self)
        self.entry_conf.pack()

        self.button1 = tk.Button(self, text='Get interval', command=self.count_measures, bg='brown', fg='white')
        self.button1.pack(pady=20)

        self.answer2 = tk.Label(self)
        self.answer2.pack(pady=20)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def count_measures(self):
        self.df = []
        self.df = takeResultFromFile()

        str_siz = self.entry_siz.get()
        str_av = self.entry_av.get()
        str_sdv = self.entry_sdv.get()
        str_conf = self.entry_conf.get()

        if not str_siz or not str_av or not str_sdv or not str_conf:
            self.answer2.config(text="!!! Fill all data !!!", font="none 14 bold")
        else:
            if "%" in str_conf:
                self.conf = float(str_conf.replace("%", ""))
            else:
                self.conf = float(str_conf.replace(",", "."))*100
            self.siz = int(str_siz)
            self.av = float(str_av.replace(",", "."))
            self.std_Deviation = float(str_sdv.replace(",", "."))
            self.z_area = stats.norm.ppf((1 - (self.conf/100))/2)
            self.result = (self.z_area*(self.std_Deviation/math.sqrt(self.siz)))
            self.a1 = (self.av-self.result)
            self.a2 = (self.av + self.result)
            self.answer2.config(text="Result: (" + str(round(self.a2, 4)) +", "+ str(round(self.a1, 4)) + ")", font="none 14 bold")

        app.cleanFile(app.tempFile)

class IntervalAverageNormalPopulationUnkDev(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Interval for average of a normal population\n(unknown Standard deviation):", width=40, font="none 14 bold")
        self.answer.pack(pady=30)

        self.label2 = tk.Label(self, text='Sample size (<30):')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.entry_siz = tk.Entry(self)
        self.entry_siz.pack()

        self.label3 = tk.Label(self, text='Sample average:')
        self.label3.config(font=('helvetica', 10))
        self.label3.pack()
        self.entry_av = tk.Entry(self)
        self.entry_av.pack()

        self.label4 = tk.Label(self, text='Standard deviation computed from the sample:')
        self.label4.config(font=('helvetica', 10))
        self.label4.pack()
        self.entry_sdv = tk.Entry(self)
        self.entry_sdv.pack()

        self.label4 = tk.Label(self, text='Confidence:')
        self.label4.config(font=('helvetica', 10))
        self.label4.pack()
        self.entry_conf = tk.Entry(self)
        self.entry_conf.pack()

        self.button1 = tk.Button(self, text='Get interval', command=self.count_measures, bg='brown', fg='white')
        self.button1.pack(pady=20)

        self.answer2 = tk.Label(self)
        self.answer2.pack(pady=20)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=1, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def count_measures(self):
        self.df = []
        self.df = takeResultFromFile()

        str_siz = self.entry_siz.get()
        str_av = self.entry_av.get()
        str_sdv = self.entry_sdv.get()
        str_conf = self.entry_conf.get()

        if not str_siz or not str_av or not str_sdv or not str_conf:
            self.answer2.config(text="!!! Fill all data !!!", font="none 14 bold")
        else:
            if "%" in str_conf:
                self.conf = float(str_conf.replace("%", ""))
            else:
                self.conf = float(str_conf.replace(",", "."))*100
            self.siz = int(str_siz)
            self.av = float(str_av.replace(",", "."))
            self.std_Deviation = float(str_sdv.replace(",", "."))
            self.t_stud = stats.t.ppf((1 - (self.conf/100))/2, self.siz-1)
            self.result = (self.t_stud*(self.std_Deviation/math.sqrt(self.siz)))
            self.a1 = (self.av-self.result)
            self.a2 = (self.av + self.result)
            self.answer2.config(text="Result: (" + str(round(self.a2, 4)) +", "+ str(round(self.a1, 4)) + ")", font="none 14 bold")

        app.cleanFile(app.tempFile)
class GeometricMean(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Geometric mean:", width=40, font="none 14 bold")
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
            geomean = stats.gmean(self.df)
            self.result = geomean
            self.array = ""
            for x in self.df:
                self.array += str(x) + "; "
            self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")

            if(str(self.result)!="nan"):
                self.answer.config(text="Geometric Mean: " + str(self.result),  font="none 14 bold")
            else:
                self.answer.config(text="Geometric mean cannot be calculated for negative values.",  font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 0", font="none 28 bold")
        app.cleanFile(app.tempFile)

class Mode(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Mode:", width=40, font="none 14 bold")
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
            mode = stats.mode(np.array(self.df))
            self.result = float(mode[0])
            self.array = ""
            for x in self.df:
                self.array += str(x) + "; "
            self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")

            self.answer.config(text="Mode: " + str(self.result),  font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 0", font="none 28 bold")
        app.cleanFile(app.tempFile)

class Skew(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.answer = tk.Label(self, text="Skewness:", width=40, font="none 14 bold")
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
            skewness = stats.skew(self.df)
            self.result = skewness
            self.array = ""
            for x in self.df:
                self.array += str(x) + "; "
            self.arrayText.config(text="Array: " + str(self.array), font="none 14 bold")

            self.answer.config(text="0Skewness: " + str(self.result),  font="none 14 bold")
        else:
            self.answer.config(text = "Amount of values need to be more than 0", font="none 28 bold")
        app.cleanFile(app.tempFile)

class TestForExpectedAverage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.significance_levels = {
            0.2: 1.282,
            0.1: 1.645,
            0.05: 1.96,
            0.02: 2.326,
            0.01: 2.576
        }

        self.answer = tk.Label(self, text="Test for expected value (average):", width=40, font="none 12 bold")
        self.answer.pack(pady=50)

        self.label2 = tk.Label(self, text='Observed mean')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.observed_mean = tk.Entry(self)
        self.observed_mean.pack()

        self.label2 = tk.Label(self, text='Mean based on normal distribution')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.mean_from_normal_dist = tk.Entry(self)
        self.mean_from_normal_dist.pack()

        self.label2 = tk.Label(self, text='Variance based on normal distribution')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.variance_from_normal_dist = tk.Entry(self)
        self.variance_from_normal_dist.pack()

        self.label2 = tk.Label(self, text='Number of samples')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.number_of_samples = tk.Entry(self)
        self.number_of_samples.pack()

        self.label2 = tk.Label(self, text='Significance')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.significance = tk.Entry(self)
        self.significance.pack()

        self.button1 = tk.Button(self, text='Validate H0', command=self.count_measures, bg='brown',
                                 fg='white')
        self.button1.pack(pady=10)

        self.answer = tk.Label(self)
        self.answer.pack(pady=10)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=4, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def count_measures(self):
        observed_mean = float(self.observed_mean.get())
        mean_from_normal_dist = float(self.mean_from_normal_dist.get())
        variance_from_normal_dist = float(self.variance_from_normal_dist.get())
        number_of_samples = float(self.number_of_samples.get())
        significance = float(self.significance.get())

        expected_value = ((observed_mean - mean_from_normal_dist) / sqrt(variance_from_normal_dist) * sqrt(number_of_samples))
        msg = str()
        msg += self.expected_larger_than_z_alpha(expected_value, significance)
        msg += self.expected_lower_than_z_alpha(expected_value, significance)
        msg += self.expected_different_from_z_alpha(expected_value, significance)
        self.answer.config(text=msg, font="none 10")

    def expected_larger_than_z_alpha(self, expected_value, significance):
        msg = "H1 = m > m1: "
        if expected_value > self.significance_levels[significance]:
            msg += "H0 can be rejected: H1 " + str(expected_value) + " larger than H0 " + str(
                self.significance_levels[significance]) + "\n"
        else:
            msg += "H0 cannot discredited: H1 " + str(expected_value) + " is not larger than H0 " + str(
                self.significance_levels[significance]) + "\n"
        return msg

    def expected_lower_than_z_alpha(self, expected_value, significance):
        msg = "H1 = m < m1: "
        if expected_value <= -self.significance_levels[significance]:
            msg += "H0 can be rejected: H1 " + str(expected_value) + " lower than H0 " + str(
                self.significance_levels[significance]) + "\n"
        else:
            msg += "H0 cannot discredited: H1 " + str(expected_value) + " is not lower than H0 " + str(
                self.significance_levels[significance]) + "\n"
        return msg

    def expected_different_from_z_alpha(self, expected_value, significance):
        msg = "H1 = m != m1: "
        if expected_value != self.significance_levels[significance * 2]:
            msg+="H0 can be rejected: H1 " + str(expected_value) + " is different from H0 " + str(
                self.significance_levels[significance]) + "\n"
        else:
            msg += "H0 cannot discredited: H1 " + str(expected_value) +  "is not different from H0 -" + str(
                -self.significance_levels[significance]) + "\n"
        return msg

        app.cleanFile(app.tempFile)

class CentralLimitTheorem(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.label = tk.Label(self, text="Central limit theorem", width=40, font="none 12 bold")
        self.label.pack(pady=30)

        self.label2 = tk.Label(self, text='Mean')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.mean_input = tk.Entry(self)
        self.mean_input.pack()

        self.label2 = tk.Label(self, text='Standard Deviation')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.std_dev_input = tk.Entry(self)
        self.std_dev_input.pack()

        self.label2 = tk.Label(self, text='Number of samples')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.number_of_samples_input = tk.Entry(self)
        self.number_of_samples_input.pack()

        self.label2 = tk.Label(self, text='Range of probability')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.range_input = tk.Entry(self)
        self.range_input.pack()

        self.button1 = tk.Button(self, text='Validate H0', command=self.count_measures, bg='brown',
                                 fg='white')
        self.button1.pack(pady=10)

        self.answer = tk.Label(self, text="", width=40, font="none 12 bold")
        self.answer.pack(pady=15)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=4, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def count_measures(self):

        mean = float(self.mean_input.get())
        std_deviation = float(self.std_dev_input.get())
        number_of_samples = int(self.number_of_samples_input.get())
        range_of_probability = self.convert_list_of_strings_to_numericals(self.range_input.get().split(","))

        probability_lower = (range_of_probability[0] - mean) / (std_deviation / sqrt(number_of_samples))
        probability_higher = (range_of_probability[1] -mean) / (std_deviation / sqrt(number_of_samples))

        probability = stats.norm.pdf(probability_higher, 0, 1) - stats.norm.pdf(probability_lower, 0, 1)

        msg = "Probability that the value would be in range\n" + str(range_of_probability[0]) + " - " \
              + str(range_of_probability[1]) + "\nis equal to: " + str(probability)

        self.answer.config(text=msg, font="none 10")

        return

    def convert_list_of_strings_to_numericals(self, list):
        list_of_numericals = []
        for element in list:
            try:
                val_to_append = int(element)
            except ValueError:
                try:
                    val_to_append = float(element)
                except ValueError:
                    continue
            list_of_numericals.append(val_to_append)
        return list_of_numericals

class TStudentTestStatisticsComputation(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.first_dataset = []
        self.second_dataset = []

        self.first_sample_size = int()
        self.second_sample_size = int()

        self.first_mean = float()
        self.second_mean = float()

        self.first_variance = float()
        self.second_variance = float()

        self.label = tk.Label(self, text="t-Student test - computation of the statistics", width=40, font="none 12 bold")
        self.label.pack(pady=30)

        self.label2 = tk.Label(self, text='Application of t-student test to compare averages of two populations')
        self.label2.config(font=('helvetica', 10))

        self.label2 = tk.Label(self, text='First dataset for comparison')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.dataset_1 = tk.Entry(self)
        self.dataset_1.pack()

        self.label2 = tk.Label(self, text='Second dataset for comparison')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.dataset_2 = tk.Entry(self)
        self.dataset_2.pack()

        self.label2 = tk.Label(self, text='Significance level')
        self.label2.config(font=('helvetica', 10))
        self.label2.pack()
        self.significance_level = tk.Entry(self)
        self.significance_level.pack()

        self.button1 = tk.Button(self, text='Validate H0', command=self.count_measures, bg='brown',
                                 fg='white')
        self.button1.pack(pady=10)

        self.answer = tk.Label(self, text="", width=40, font="none 12 bold")
        self.answer.pack(pady=15)

        self.buttonExit = tk.Button(self, text="Exit", width=14, height=4, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(st.StartPage))
        self.buttonExit.pack(pady=10)

    def count_measures(self):
        self.first_dataset = self.convert_list_of_strings_to_numericals(self.dataset_1.get().split(","))
        self.second_dataset = self.convert_list_of_strings_to_numericals(self.dataset_2.get().split(","))

        self.first_sample_size = len(self.first_dataset)
        self.second_sample_size = len(self.second_dataset)

        self.first_mean = statistics_native.mean(self.first_dataset)
        self.second_mean = statistics_native.mean(self.second_dataset)

        self.first_variance = statistics_native.variance(self.first_dataset)
        self.second_variance = statistics_native.variance(self.second_dataset)

        significance_level = float(self.significance_level.get())
        if self.calculate_t() == self.get_ref_t(significance_level):
            msg = "H0 Cannot be rejected"
        else:
            msg = "H0 Rejected: population averages not equal"
        self.answer.config(text=msg, font="none 10")

    def convert_list_of_strings_to_numericals(self, list):
        list_of_numericals = []
        for element in list:
            try:
                val_to_append = int(element)
            except ValueError:
                try:
                    val_to_append = float(element)
                except ValueError:
                    continue
            list_of_numericals.append(val_to_append)
        return list_of_numericals

    def calculate_t(self):
        sqrt_first_part = ((self.first_sample_size - 1) * self.first_variance + (
                    self.second_sample_size - 1) * self.second_variance) / (
                                      self.first_sample_size + self.second_sample_size - 2)
        sqrt_second_part = (1 / self.first_sample_size + 1 / self.second_sample_size)
        denominator = sqrt(sqrt_first_part * sqrt_second_part)
        t = (self.first_mean - self.second_mean) / denominator
        return t

    def get_ref_t(self, alpha):
        gl = self.first_sample_size + self.second_sample_size - 2
        return stats.t.ppf(1- (alpha / 2), gl)

