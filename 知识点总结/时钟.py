#-*- coding: utf-8 -*-
import time
class 时钟:
    def __init__(self):
        self.time=None
    def show(self):
        while True:
            self.time=time.ctime()
            print("\r{}".format(self.time), end="")
            time.sleep(1)
t=时钟()
t.show()