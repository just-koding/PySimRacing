""" Main GUI Window """
import tkinter as tk
from tkinter import ttk


class Main(tk.Toplevel):
    """ Main Window """
    def __init__(self):
        self.window = None
        super().__init__()

    def loop(self, callback):
        """ Function call  to start the mainloop from the window """
        self.window = tk.Tk()
        self.window.geometry('600x400')
        self.window.title('Multiple windows')
        ttk.Label(self.window, text='A label').pack()
        ttk.Button(self.window, text='A button', command=callback).pack()
        ttk.Label(self.window, text='another label').pack(expand=True)
        self.window.mainloop()

    def stop(self):
        """ Function to stop the window execution"""
        self.window.destroy()
