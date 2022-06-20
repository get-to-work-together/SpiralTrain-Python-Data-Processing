from threading import Thread
import time
import random

class MyTread(Thread):

    def __init__(self, name):
        super().__init__()
        self.__name = name

    def run(self):
        delay = random.random()*5
        for __ in range(100):
            print('%s' % self.__name, end='')
            time.sleep(delay)

#---------------------------------

th1 = MyTread('1')
th2 = MyTread('2')
th3 = MyTread('3')
th4 = MyTread('4')
th5 = MyTread('5')

th1.start()
th2.start()
th3.start()
th4.start()
th5.start()