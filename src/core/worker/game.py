from core.worker.base import BaseWorker
from core.data.iracing import IrSdk


class IRacingWorker(BaseWorker):
    """ IRacingWorker Class manages the IRacing data scrapping """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sdk = IrSdk()

    def run(self):
        """ Function called inside a thread """
        self.sdk.check_iracing()
        self.sdk.loop(self.data_update)

    def stop(self):
        """ Function to stop the thread """
        self.sdk.stop_loop()
        super().stop()

    def data_update(self, data):
        """ data_update """
        print("post data_update")
        self.post_event("data_update", data)

    def ui_update(self, data):
        """ data_update """
        if data.get_button_pressed():
            print("Button pressed from UI")
        print(f"IRacingWorker ui_update {data}")
