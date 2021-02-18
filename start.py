import tkinter as tk
import oneInput as oi
import twoInputs as ti


class StartPage(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)
        lab = tk.Label(self, text='Welcome to Statistics program', font="none 28 bold")
        lab.pack(pady=20)

        startButton1 = tk.Button(self, text="Put one column", width=16, height=2, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(oi.OneInput))
        startButton1.pack(pady=20)

        startButton2 = tk.Button(self, text="Put two columns", width=16, height=2, font="none 14 bold", bg="#3e4444", fg="white", command=lambda: master.switch_frame(ti.TwoInputs))
        startButton2.pack(pady=20)

        exitButton = tk.Button(self, text ="Exit", width=16, height=2, font="none 14 bold", bg = "#3e4444", fg="white", command=self.destroy)
        exitButton.pack(pady=40)


