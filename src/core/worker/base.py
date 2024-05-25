""" Base Worker Definitions """
from threading import Thread
from collections import defaultdict
import time


class EnventBase(Thread):
    """ Class adding events """

    def __init__(self, *args, **kwargs):
        """ __init__ """
        super().__init__(*args, **kwargs)
        self.subscribers = defaultdict(list)

    def subscribe(self, event_type, fn):
        """ subscribe """
        self.subscribers[event_type].append(fn)

    def post_event(self, event_type, data):
        """ post_event """
        if event_type in self.subscribers:
            for fn in self.subscribers[event_type]:
                fn(data)


class BaseWorker(EnventBase):
    """ BaseWorker Class representing a process called in a new thread """

    def __init__(self, *args, **kwargs):
        """ __init__ """
        super().__init__(*args, **kwargs)
        self.running = False

    def run(self):
        """ function called inside a thread"""
        print("BaseWorker 'run' not implemented")

    def start(self):
        """ start """
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
