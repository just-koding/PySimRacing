# from "Python Coobook 2nd Edition", section 11.9, page 439.
# Modified to work in Python 2 & 3.
from __future__ import print_function
import queue
import random
import threading
import time
import tkinter as tk


class GuiPart(object):
    """ GuiPart """
    def __init__(self, master, queue, end_command):
        self.queue = queue
        self.master = master
        # Set up the GUI
        self.button = tk.Button(master, text='Done', command=end_command)
        self.button.pack()
        # Add more GUI stuff here depending on your specific needs

    def update_component(self, msg):
        """ update_component """
        for obj in self.master.panes():
            c = self.master.nametowidget(str(obj))
            if isinstance(c, tk.Button):
                c.text = msg

    def process_incoming(self):
        """ Handle all messages currently in the queue, if any. """
        while self.queue.qsize():
            try:
                msg = self.queue.get_nowait()
                # Check contents of message and do whatever is needed. As a
                # simple example, let's print it (in real life, you would
                # suitably update the GUI's display in a richer fashion).
                self.update_component(msg)
            except queue.Empty:
                # just on general principles, although we don't expect this
                # branch to be taken in this case, ignore this exception!
                pass


class ThreadedClient(object):
    """
    Launch the main part of the GUI and the worker thread. periodic_call()
    and end_application() could reside in the GUI part, but putting them
    here means that you have all the thread controls in a single place.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads.  We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well.  We spawn a new thread for the worker (I/O).
        """
        self.master = master
        # Create the queue
        self.queue = queue.Queue()

        # Set up the GUI part
        self.gui = GuiPart(master, self.queue, self.end_application)

        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = True
        self.thread1 = threading.Thread(target=self.worker_thread1)
        self.thread1.start()

        # Start the periodic call in the GUI to check the queue
        self.periodic_call()

    def periodic_call(self):
        """ Check every 200 ms if there is something new in the queue. """
        self.master.after(200, self.periodic_call)
        self.gui.process_incoming()
        if not self.running:
            # This is the brutal stop of the system.  You may want to do
            # some cleanup before actually shutting it down.
            self.master.destroy()

    def worker_thread1(self):
        """
        This is where we handle the asynchronous I/O.  For example, it may be
        a 'select()'.  One important thing to remember is that the thread has
        to yield control pretty regularly, be it by select or otherwise.
        """
        while self.running:
            # To simulate asynchronous I/O, create a random number at random
            # intervals. Replace the following two lines with the real thing.
            time.sleep(random.Random().random() * 1.5)
            msg = random.Random().random()
            self.queue.put(msg)

    def end_application(self):
        """  end_application """
        self.running = False  # Stops worker_thread1 (invoked by "Done" button).
