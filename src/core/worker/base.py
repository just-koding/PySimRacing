""" Base Worker Definitions """
from threading import Thread
import time


class BaseWorker(Thread):
    """ BaseWorker Class representing a process called in a new thread """

    def __init__(self, *args, **kwargs):
        """ __init__ """
        super().__init__(*args, **kwargs)
        self.running = False

    def run(self):
        """ run """
        print("BaseWorker 'run' not implemented")

    def start(self):
        """ run """
        # thumbnail will be resolved on second OR newly created below thread        
        self.running = True
        thread = Thread(target=self.run)
        thread.start()

    def stop(self):
        """ stop """
        self.running = False


class BaseTimerWorker(BaseWorker):
    """ BaseTimerWorker Class representing a timer called in a new thread """

    def __init__(self, *args, **kwargs):
        """ __init__ """
        super().__init__(*args, **kwargs)
        self.cool_down = 20

    def tick(self):
        """ tick """
        print("BaseTimerWorker 'tick' not implemented")

    def start(self):
        """ start """
        while self.running:
            self.tick()
            time.sleep(self.cool_down)
