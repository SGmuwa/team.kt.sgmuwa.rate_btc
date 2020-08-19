from os import fork
from time import sleep


class MultiTimer:
    def __init__(self, interval, function, args=[], kwargs={}):
        super(MultiTimer, self).__init__()
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        pid = fork()
        if pid == 0:
            self._tick()

    def cancel(self):
        """Stop the timer if it hasn't finished yet"""
        self.is_cancel = True

    def _tick(self):
        self.is_cancel = False
        while not self.is_cancel:
            self.function(*self.args, **self.kwargs)
            sleep(self.interval)
