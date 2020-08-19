from multiprocessing import Process, Event
from time import sleep


class MultiTimer(Process):
    def __init__(self, interval, function, args=[], kwargs={}):
        super(MultiTimer, self).__init__()
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.p = Process(target=self._tick, args=())
        self.p.start()

    def cancel(self):
        """Stop the timer if it hasn't finished yet"""
        self.is_cancel = True

    def _tick(self):
        self.is_cancel = False
        while not self.is_cancel:
            self.function(*self.args, **self.kwargs)
            sleep(self.interval)
