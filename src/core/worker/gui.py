from core.worker.base import BaseWorker
from ui.windows import Main


class UIWorker(BaseWorker):
    """ UIWorker Class manages the UI data scrapping """

    def __init__(self, *args, **kwargs):
        self.screen = Main()
        super().__init__(*args, **kwargs)

    def run(self):
        """ Function called inside a thread """
        self.screen.loop(self.ui_update)

    def stop(self):
        """ Function to stop the thread """
        self.screen.stop()
        super().stop()

    def data_update(self):
        """ data_update """
        print("UIWorker data_update")

    def ui_update(self):
        """ data_update """
        print("post ui_update")
        self.post_event("ui_update", None)
