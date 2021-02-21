import tkinter as tk
import chooseMeasure as cm
import app


class TwoInputs(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)

        self.initLabel = tk.Label(self, text="Put the number", width=20, font="none 24 bold")
        self.initLabel.pack(pady=20)

        self.entry = tk.Entry(self, width="10")
        self.entry.pack(pady=10)
        self.entry2 = tk.Entry(self, width="10")
        self.entry2.pack(pady=30)

        self.button = tk.Button(self, text="Add numbers", width=16, height=2, font="none 14 bold", bg="#3e4444", fg="white", command=self.saveNumbers)
        self.button.pack(pady=20)
        self.button2 = tk.Button(self, text="Measures", width=16, height=2, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(cm.ChooseMeasureTwo))
        self.button2.pack(pady=10)

        self.answer = tk.Label(self, text='')
        self.answer.pack(pady=10)
        self.answer2 = tk.Label(self, text='')
        self.answer2.pack(pady=10)

    def saveNumbers(self):
        with open(app.tempFile, 'a') as file1:
            try:
                if (float(self.entry.get()) or float(self.entry2.get())):
                    self.answer.config(text=float(self.entry.get()), font="none 14 bold")
                    self.answer2.config(text=float(self.entry2.get()), font="none 14 bold")
                    file1.write(str(self.entry.get()) + " " + str(self.entry2.get()))
                    file1.write('\n')
            except ValueError:
                self.answer.config(text="Wrong Value. Try again.", font="none 14 bold")
                self.answer2.config(text=" ", font="none 14 bold")

    # def takeResultFromFile(self):
    #     result, result1 = [], []
    #     with open(app.tempFile, 'r') as file1:
    #         # lines = file1.readlines()
    #         for line in file1:
    #             x = line.split(' ')
    #             result.append(float(x[0]))
    #             result1.append(float(x[1]))
    #     return result, result1
    #
    # def showResult(self):
    #     res, res2 = [], []
    #     a = 0.0
    #     res, res2 = self.takeResultFromFile()
    #     for i in range(len(res)):
    #         print(str(i) + ": " + str(res[i]))
    #         print(str(i) + ": " + str(res2[i]))
            # self.answer.config(text=a, font="none 14 bold")