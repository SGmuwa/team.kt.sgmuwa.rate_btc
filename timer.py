from multiprocessing import Process, Event


class MultiTimer(Process):
    def __init__(self, interval, function, args=[], kwargs={}):
        super(MultiTimer, self).__init__()
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_cancel = False
        self.finished = Event()

    def cancel(self):
        """Stop the timer if it hasn't finished yet"""
        self.is_cancel = True
        self.finished.set()

    def run(self):
        self.is_cancel = False
        while not self.is_cancel:
            self.finished = Event()
            self.finished.wait(self.interval)
            if not self.finished.is_set():
                self.function(*self.args, **self.kwargs)
            self.finished.set()
