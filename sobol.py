import math
from number import *

class SobolIterator:
    def __init__(self, directionNumbers, startIndex, endIndex):
        self.curIndex = startIndex
        self.endIndex = endIndex
        self.directNums = [ TransposedBinNumber(Number(x,2,True)._num) \
                            for x in directionNumbers]
        self.lenNum = int(math.log(endIndex-1 ,2)) + 1

    def __iter__(self):
        return self

    def next(self):
        if self.curIndex == self.endIndex:
            raise StopIteration
        n = Number(self.curIndex)
        self.curIndex += 1
        index = list(n._num)
        res = self.directNums[len(index)-1]
        for i in xrange(1, len(index)):
            if index[i] != 0:
                res = res ^ self.directNums[len(index) - i - 1]
        return res.toNumber()
        
