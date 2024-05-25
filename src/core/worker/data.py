from core.worker.base import BaseWorker
from core.data.IRSDK import IRSDK


class IRacingWorker(BaseWorker):
    """ IRacingWorker Class manages the IRacing data scrapping """

    def __init__(self, *args, **kwargs):
        self.sdk = IRSDK()
        super().__init__(*args, **kwargs)

    def run(self):
        self.sdk.check_iracing()
        self.sdk.loop()

    def stop(self):
        self.sdk.stop_loop()
        super().stop()
