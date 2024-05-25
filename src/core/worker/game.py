from core.worker.base import BaseWorker
from core.data.iracing import IrSdk


class IRacingWorker(BaseWorker):
    """ IRacingWorker Class manages the IRacing data scrapping """

    def __init__(self, *args, **kwargs):
        self.sdk = IrSdk()
        super().__init__(*args, **kwargs)

    def run(self):
        """ Function called inside a thread """
        self.sdk.check_iracing()
        self.sdk.loop()

    def stop(self):
        """ Function to stop the thread """
        self.sdk.stop_loop()
        super().stop()
