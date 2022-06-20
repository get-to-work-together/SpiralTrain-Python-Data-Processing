import time
import os
import re
import sys
from threading import Thread
import threading

NUM_OF_PRIMES = 5000  # the number of primes to find (note it wil find slightly more then this number)
NUM_THR = 23
PRIMES = []


def isPrime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

def run():
    count = 0
    number = 2
    while True:
        # even numbers are no primary number except 2
        if number % 2 == 0 and number > 2:
            number += 1
            continue

        if isPrime(number):
            count += 1
            PRIMES.append(number)

        if len(PRIMES) >= NUM_OF_PRIMES:
            break

        number += 2

    print('found %d primes numbers' % count)



start = time.time()

primelist = []

current = run()
primelist.append(current)

end = time.time()

diff = round(end - start, 2)
print('%s priemgetallen in %s seconden' % (str(PRIMES.__len__()), str(diff)))