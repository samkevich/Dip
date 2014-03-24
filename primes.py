import import math

class PrimesIterator:
    def __init__(self, length):
        self.length = length
        self.curNum = 0
        self.oldN = 16
        self._initPrimes(self.oldN)
        while(len(self._sieve) < self.length):
            self.newN = self.oldN*2
            self._extendPrimes(self.newN, self.oldN)
            self.oldN = self.newN
        self.primes = list(self._sieve)
              
    def _initPrimes(self, N):
        self._sieve = set(range(2, N+1))
        for i in range(2, long(math.sqrt(N)+1)):
            if i in self._sieve:
                self._sieve -= set(range(2*i, N+1, i))
        return self._sieve

    def _extendPrimes(self, newN, oldN):
        newSieve = set(range(oldN, newN+1))
        sqrtOldN = int(math.sqrt(oldN))
        for i in self._sieve:
            newSieve -= set(range((sqrtOldN / i) * i, newN+1, i))
        self._sieve |= newSieve
        for i in range(oldN, long(math.sqrt(newN)+1)):
            if i in self._sieve:
                self._sieve -= set(range(2*i, newN+1, i))
        return self._sieve

    def __iter__(self):
        return self

    def next(self):
        if self.curNum == self.length:
            raise StopIteration
        res = self.primes[self.curNum]
        self.curNum += 1
        return res
