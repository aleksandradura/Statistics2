import tkinter as tk
import start as s
import oneInput as oi
import twoInputs as ti
import countMeasures as cmes

class ChooseMeasureOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        lab2 = tk.Label(self, text="Choose measure one", font="none 18 bold")
        lab2.grid(row=1, column=1)

        button1 = tk.Button(self, text="Arithmetic mean", width=20, height=1, font="none 14 bold", bg="#3e4444",
                            fg="white", command=lambda: master.switch_frame(cmes.ArithmeticMean))
        button1.grid(row=2, column=0)

        button2 = tk.Button(self, text="Geometric mean", width=20, height=1, font="none 14 bold", bg="#3e4444",
                            fg="white", command=lambda: master.switch_frame(cmes.GeometricMean))
        button2.grid(row=3, column=0)

        button3 = tk.Button(self, text="Harmonic mean", width=20, height=1, font="none 14 bold", bg="#3e4444",
                            fg="white", command=lambda: master.switch_frame(cmes.HarmonicMean))
        button3.grid(row=4, column=0)

        button4 = tk.Button(self, text="Mode", width=20, height=1, font="none 14 bold", bg="#3e4444", fg="white",
                            command=lambda: master.switch_frame(cmes.Mode))
        button4.grid(row=5, column=0)

        button5 = tk.Button(self, text="Quantiles", width=20, height=1, font="none 14 bold", bg="#3e4444", fg="white",
                            command=lambda: master.switch_frame(cmes.Quantile))
        button5.grid(row=6, column=0)

        button6 = tk.Button(self, text="Median", width=20, height=1, font="none 14 bold", bg="#3e4444", fg="white",
                            command=lambda: master.switch_frame(cmes.Median))
        button6.grid(row=7, column=0)

        button7 = tk.Button(self, text="Standard deviation", width=20, height=1, font="none 14 bold", bg="#3e4444",
                            fg="white", command=lambda: master.switch_frame(cmes.StandardDeviation))
        button7.grid(row=8, column=0)

        button8 = tk.Button(self, text="Population std", width=20, height=1, font="none 14 bold", bg="#3e4444",
                            fg="white", command=lambda: master.switch_frame(cmes.PopulationStandardDeviation))
        button8.grid(row=9, column=0)

        button9 = tk.Button(self, text="Mean absolute deviation", width=20, height=1, font="none 14 bold", bg="#3e4444",
                            fg="white", command=lambda: master.switch_frame(cmes.MeanAbsoluteDeviation))
        button9.grid(row=10, column=0)

        button10 = tk.Button(self, text="Interquartile range", width=20, height=1, font="none 14 bold", bg="#3e4444",
                             fg="white", command=lambda: master.switch_frame(cmes.InterquartileRange))
        button10.grid(row=11, column=0)

        button11 = tk.Button(self, text="(A)symmetry", width=26, height=1, font="none 14 bold", bg="#3e4444",
                             fg="white", command=lambda: master.switch_frame(cmes.Skew))
        button11.grid(row=2, column=1)

        button12 = tk.Button(self, text="Tailedness", width=26, height=1, font="none 14 bold", bg="#3e4444", fg="white",
                             command=lambda: master.switch_frame(cmes.Tailedness))
        button12.grid(row=3, column=1)

        button13 = tk.Button(self, text="Shapiro-Wilk test", width=26, height=1, font="none 14 bold", bg="#3e4444",
                             fg="white", command=lambda: master.switch_frame(cmes.ShapiroWilkTest))
        button13.grid(row=4, column=1)

        button14 = tk.Button(self, text="Coef of variation", width=26, height=1, font="none 14 bold", bg="#3e4444",
                             fg="white", command=lambda: master.switch_frame(cmes.VariationCoefficient))
        button14.grid(row=5, column=1)

        button15 = tk.Button(self, text="Sign test", width=26, height=1, font="none 14 bold", bg="#3e4444", fg="white",
                             command=lambda: master.switch_frame(cmes.SignTest))
        button15.grid(row=6, column=1)

        button16 = tk.Button(self, text="Min sample size for population avg\nNormal distribution", width=26, height=1, font="none 14 bold", bg="#3e4444",
                             fg="white", command=lambda: master.switch_frame(cmes.MinSampleCountForPopAVGNormal))
        button16.grid(row=7, column=1)

        button17 = tk.Button(self, text="Min sample size for population avg\nStudent's t-distribution", width=26, height=1, font="none 14 bold",
                             bg="#3e4444", fg="white", command=lambda: master.switch_frame(cmes.MinSampleCountForPopAVGStud_t))
        button17.grid(row=8, column=1)

        button18 = tk.Button(self, text="Box plot", width=26, height=1, font="none 14 bold",
                             bg="#3e4444", fg="white",  command=lambda: master.switch_frame(cmes.BoxPlot))
        button18.grid(row=9, column=1)

        button19 = tk.Button(self, text="Student's t-distribution", width=26, height=1, font="none 14 bold",
                            bg="#3e4444",
                            fg="white", command=lambda: master.switch_frame(cmes.StudentsTDistribution))
        button19.grid(row=10, column=1)

        button20 = tk.Button(self, text="Standardized third central moment", width=26, height=1, font="none 14 bold",
                            bg="#3e4444",
                            fg="white", command=lambda: master.switch_frame(cmes.StandardizedThirdCentralMoment))
        button20.grid(row=11, column=1)

        button21 = tk.Button(self, text="Nonparametric skew", width=26, height=1, font="none 14 bold",
                            bg="#3e4444",
                            fg="white", command=lambda: master.switch_frame(cmes.NonParametricSkew))
        button21.grid(row=2, column=2)

        button22 = tk.Button(self, text="Distribution Of Arithmetic Average", width=26, height=1, font="none 14 bold",
                             bg="#3e4444",
                             fg="white", command=lambda: master.switch_frame(cmes.DistributionOfArithmeticAverage))

        button22.grid(row=3, column=2)

        button23 = tk.Button(self, text="Test for expected value (average)", width=26, height=1, font="none 14 bold",
                             bg="#3e4444",
                             fg="white", command=lambda: master.switch_frame(cmes.TestForExpectedAverage))

        button23.grid(row=4, column=2)

        button24 = tk.Button(self, text="Central limit theorem", width=26, height=1, font="none 14 bold",
                             bg="#3e4444",
                             fg="white", command=lambda: master.switch_frame(cmes.CentralLimitTheorem))

        button24.grid(row=5, column=2)

        button25 = tk.Button(self, text="t-Student test statistics", width=26, height=1, font="none 14 bold",
                             bg="#3e4444",
                             fg="white", command=lambda: master.switch_frame(cmes.TStudentTestStatisticsComputation))

        button25.grid(row=6, column=2)


        buttonExit = tk.Button(self, text="Exit", width=12, height=1, font="none 14 bold", bg="#3e4444", fg="white",
                               command=lambda: master.switch_frame(s.StartPage))
        buttonExit.grid(row=13, column=2)

class ChooseMeasureTwo(tk.Frame):
        def __init__(self, master):
            tk.Frame.__init__(self, master)
            lab2 = tk.Label(self, text="Choose measure two", font="none 18 bold")
            lab2.grid(row=1, column=1)

            button1 = tk.Button(self, text="ANOVA", width=24, height=1, font="none 14 bold", bg="#3e4444", fg="white",
                                 command=lambda: master.switch_frame(cmes.ANOVA))
            button1.grid(row=2, column=0)

            button2 = tk.Button(self, text="Correlation table", width=24, height=1, font="none 14 bold",
                                 bg="#3e4444", fg="white", command=lambda: master.switch_frame(cmes.CorrelationTable))
            button2.grid(row=3, column=0)

            button3 = tk.Button(self, text="t-Student test", width=24, height=1, font="none 14 bold", bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(oi.OneInput))
            button3.grid(row=4, column=0)

            button4 = tk.Button(self, text="Pearson x^2 test", width=24, height=1, font="none 14 bold", bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(cmes.ChiSquaredTest))
            button4.grid(row=5, column=0)

            button6 = tk.Button(self, text="Pearson correlation", width=24, height=1, font="none 14 bold",
                                 bg="#3e4444", fg="white", command=lambda: master.switch_frame(cmes.PearsonCorrelation))
            button6.grid(row=6, column=0)

            button7 = tk.Button(self, text="Linear regression", width=24, height=2, font="none 14 bold", bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(cmes.LinearRegression))
            button7.grid(row=7, column=0)

            button8 = tk.Button(self, text="Poisson distribution", width=24, height=1, font="none 14 bold",
                                 bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(cmes.PoissonDistribution))
            button8.grid(row=8, column=0)

            button9 = tk.Button(self, text="central limit theorem", width=24, height=1, font="none 14 bold",
                                 bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(oi.OneInput))
            button9.grid(row=9, column=0)

            button10 = tk.Button(self, text="Interval for variance", width=24, height=1, font="none 14 bold",
                                 bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(oi.OneInput))
            button10.grid(row=10, column=0)

            button11 = tk.Button(self, text="Confidence interval", width=24, height=1, font="none 14 bold",
                                 bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(oi.OneInput))
            button11.grid(row=2, column=1)

            button12 = tk.Button(self, text="Interval for avg (std)", width=24, height=1, font="none 14 bold",
                                 bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(cmes.IntervalAverageNormalPopulation))
            button12.grid(row=3, column=1)

            button13 = tk.Button(self, text="Interval for avg", width=24, height=1, font="none 14 bold", bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(cmes.IntervalAverageNormalPopulationUnkDev))
            button13.grid(row=4, column=1)

            button14 = tk.Button(self, text="Distribution avg (known std)", width=24, height=1, font="none 14 bold",
                                 bg="#3e4444", fg="white", command=lambda: master.switch_frame(oi.OneInput))
            button14.grid(row=5, column=1)

            button15 = tk.Button(self, text="Distribution avg", width=24, height=1, font="none 14 bold", bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(oi.OneInput))
            button15.grid(row=6, column=1)

            button16 = tk.Button(self, text="Distribution variance \nchi squared", width=24, height=2, font="none 14 bold",
                                 bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(cmes.ChiSquared))
            button16.grid(row=7, column=1)

            button17 = tk.Button(self, text="Expected value (avg)", width=24, height=1, font="none 14 bold",
                                 bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(oi.OneInput))
            button17.grid(row=8, column=1)

  #          button18 = tk.Button(self, text="Pearson x^2 test", width=24, height=1, font="none 14 bold", bg="#3e4444",
  #                               fg="white", command=lambda: master.switch_frame(oi.OneInput))
  #          button18.grid(row=9, column=1)

            buttonExit = tk.Button(self, text="Exit", width=12, height=1, font="none 14 bold", bg="#3e4444",
                                 fg="white", command=lambda: master.switch_frame(s.StartPage))
            buttonExit.grid(row=13, column=2)
