from core.worker.base import BaseWorker
from core.data.iracing import IrSdk


class IRacingWorker(BaseWorker):
    """ IRacingWorker Class manages the IRacing data scrapping """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sdk = IrSdk()
        self.data = None
        self.post_event("sdk_data_update", self.data)

    def run(self):
        """ Function called inside a thread """
        self.sdk.check_iracing()
        self.sdk.loop()

    def stop(self):
        """ Function to stop the thread """
        self.sdk.stop_loop()
        super().stop()
