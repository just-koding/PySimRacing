from core.worker.base import BaseWorker
from ui.windows import Main
import tkinter as tk


class UIWorker(BaseWorker):
    """ UIWorker Class manages the UI data scrapping """

    def __init__(self, *args, **kwargs):
        self.window = tk.Tk()
        self.screen = Main(self.window)
        super().__init__(*args, **kwargs)

    def run(self):
        """ Function called inside a thread """
        self.screen.loop()

    def stop(self):
        """ Function to stop the thread """
        self.screen.stop()
        super().stop()

    def data_update(self):
        """ data_update """
        print("data_update")
