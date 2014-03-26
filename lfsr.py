from collections import deque
from polynomial import *

class lfsr:
    
    def __init__(self, polynomial, length = -1):
        self.poly = polynomial
        self.bits = deque([0 for _ in xrange(0, len(self.poly.coeffs)-1)])
        self.bits.append(1)
        print self.bits
        self.curIdx = 0
        self.length = length

    def _nextBit(self):
        res = 0
        for i,x in enumerate(self.poly.coeffs):
            if x != 0:
                res ^= self.bits[i]
        return res

    def _shift(self):
        x = self.bits.popleft()
        self.bits.append(x)

    def __iter__(self):
        return self

    def next(self):
        if self.curIdx == self.length:
            raise StopIteration
        x = self._nextBit()
        self.bits.popleft()
        self.bits.append(x)
        self.curIdx += 1
        return self.bits

for i in lfsr(Polynomial([1,2,0,4]), 10):
    print i

