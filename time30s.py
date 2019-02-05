import time
from threading import Thread
from threading import Event


def time_now():
    now = time.localtime()
    return ('\nTime now: {0}:{1}:{2}'.format(now.tm_hour, now.tm_min, now.tm_sec))


class TimerThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(1):
            print(time_now())



if __name__ == "__main__":
    stopFlag = Event()
    thread = TimerThread(stopFlag)

    thread.start()
    while True:
        if input() == " ":
            stopFlag.set()
            break