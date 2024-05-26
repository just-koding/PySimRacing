from core.worker.base import BaseWorker
from core.data.event_data import UIData
from ui.thread_window import ThreadedClient
import tkinter as tk


class UIWorker(BaseWorker):
    """ UIWorker Class manages the UI data scrapping """

    def __init__(self, *args, **kwargs):
        # self.screen = Main()
        self.screen = None
        self.client = None
        self.ui_data = UIData()
        super().__init__(*args, **kwargs)

    def run(self):
        """ Function called inside a thread """
        # self.screen.loop(self.ui_update)
        self.screen = tk.Tk()
        self.client = ThreadedClient(self.screen)
        self.screen.mainloop()

    def stop(self):
        """ Function to stop the thread """
        self.screen.stop()
        super().stop()

    def data_update(self, data):
        """ data_update """
        print(f"UIWorker data_update time is: {data.get_time()}")

    def ui_update(self):
        """ data_update """
        print("post ui_update")
        self.ui_data.set_button_pressed(True)
        self.post_event("ui_update", self.ui_data)
