from korput import *
from primes import *

class HaltonIterator:
    def __init__(self, dimention, startIndex = 1, endIndex = -1):
        self.primes = [x for x in PrimesIterator(dimention)]
        self.corputIt = [CorputIterator(radix, startIndex, endIndex) for radix in self.primes]

    def __iter__(self):
        return self

    def next(self):
        return [it.next().toDec() for it in self.corputIt]
