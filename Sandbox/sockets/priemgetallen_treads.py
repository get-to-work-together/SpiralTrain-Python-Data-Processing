import time
import os
import re
import sys
from threading import Thread
import threading

NUM_OF_PRIMES = 5000  # the number of primes to find (note it wil find slightly more then this number)
NUM_THR = 23  # should be a prime number for efficient looping
PRIMES = []


class primeit(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number
        print('Thread created for number %s %s' % (str(number), self))

    def isPrime(self, n):
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

    def run(self):
        count = 0
        while True:
            # even numbers are no primary number except 2
            if self.number % 2 == 0 and self.number > 2:
                self.number = self.number + NUM_THR
                continue
            if self.isPrime(self.number):
                count += 1
                PRIMES.append(self.number)
            if PRIMES.__len__() >= NUM_OF_PRIMES:
                break
            self.number = self.number + NUM_THR
        print('%s found %s primes numbers' % (self.name, str(count)))


start = time.time()
primelist = []
for t in range(2, NUM_THR + 2):
    current = primeit(t)
    primelist.append(current)

for th in primelist:
    th.start()

for th in primelist:
    th.join()

end = time.time()
diff = round(end - start, 2)
print('%s priemgetallen in %s seconden' % (str(PRIMES.__len__()), str(diff)))