import matplotlib

import numpy as np

matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation

from matplotlib.figure import Figure

import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class Evaluateur(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Evaluation")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = FrameEvaluation(container, self)

        self.frames[FrameEvaluation] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FrameEvaluation)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class FrameEvaluation(tk.Frame):

    def calcFormula(self):
        str = self.entry1.get()
        self.entry1.delete(0, tk.END)
        #self.entry1.insert(0, "np.exp(-x**2/8)")

        x = np.linspace(-1, 2, 100)

        y2 = (eval(str))
        self.a.plot(x, y2)
        self.canvas.draw()
        return

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Evaluation de formules", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        label1 = tk.Label(self, text='formule:')
        label1.pack()
        self.entry1 = tk.Entry(self)
        self.entry1.pack()
        bok = tk.Button(self,text='Evaluer', command=self.calcFormula)
        bok.pack()

        self.f = Figure(figsize=(5, 5), dpi=100)
        self.a = self.f.add_subplot(111)
        x = np.linspace(-1, 2, 100)
        y = np.exp(x)

        self.a.plot(x, y)

        self.a.plot(x, -np.exp(-x))

        self.canvas = FigureCanvasTkAgg(self.f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)




app = Evaluateur()
app.mainloop()