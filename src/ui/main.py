""" Main GUI Window """
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


EXTRA_WINDOW = None

class Extra(tk.Toplevel):
    """ Extra """
    def __init__(self):
        super().__init__()
        self.title('extra window')
        self.geometry('300x400')
        ttk.Label(self, text='A label').pack()
        ttk.Button(self, text='A button').pack()
        ttk.Label(self, text='another label').pack(expand=True)


# https://docs.python.org/3/library/tkinter.messagebox.html
def ask_yes_no():
    """ ask_yes_no """
    # answer=messagebox.askquestion('Title', 'Body')
    # print(answer)
    messagebox.showerror('Info title', 'Here is some information')


def create_window():
    """ create_window """
    EXTRA_WINDOW = Extra()
    # EXTRA_WINDOW  =  tk.Toplevel()
    # EXTRA_WINDOW.title('extra window')
    # EXTRA_WINDOW.geometry('300x400')
    # ttk.Label(EXTRA_WINDOW, text = 'A label').pack()
    # ttk.Button(EXTRA_WINDOW, text = 'A button').pack()
    # ttk.Label(EXTRA_WINDOW, text = 'another label').pack(expand = True)


def close_window():
    """ close_window """
    EXTRA_WINDOW.destroy()


# window
window = tk.Tk()
window.geometry('600x400')
window.title('Multiple windows')

button1 = ttk.Button(window, text='open main window', command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(window, text='close main window', command=close_window)
button2.pack(expand=True)

button3 = ttk.Button(window, text='create yes no window', command=ask_yes_no)
button3.pack(expand=True)

# run
window.mainloop()
