""" Main GUI Window """
import tkinter as tk
from tkinter import ttk


class Main(tk.Toplevel):
    """ Main Window """
    def __init__(self, window):
        super().__init__()
        ttk.Label(self, text='A label').pack()
        ttk.Button(self, text='A button').pack()
        ttk.Label(self, text='another label').pack(expand=True)
        self.window = window

    def loop(self):
        """ Function call  to start the mainloop from the window """
        self.window = tk.Tk()
        self.window.geometry('600x400')
        self.window.title('Multiple windows')
        self.window.mainloop()

    def stop(self):
        """ Function to stop the window execution"""
        self.window.destroy()
