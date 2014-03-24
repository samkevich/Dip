import math
from number import *

class AntonovSaleevIterator:
    def __init__(self, directionNumbers, seqLength):
        self.curNum = TransposedBinNumber()
        self.curIndex = 0
        self.seqLength = seqLength
        self.directNums = [ TransposedBinNumber(Number(x,2,True)._num) \
                            for x in directionNumbers]
        self.lenNum = int(math.log(seqLength,2))+1
        self.switchingSeq = self.switchingSequence(self.lenNum)

    def switchingSequence(self, q):
        if q == 1:
            return [1]
        else:
            res = list(self.switchingSequence(q-1))
            res.append(q)
            res.extend(self.switchingSequence(q-1))
            return res
        
    def __iter__(self):
        return self

    def next(self):
        if self.curIndex == self.seqLength:
            raise StopIteration
        i = self.switchingSeq[self.curIndex]
        self.curIndex += 1
        self.curNum = self.curNum ^ self.directNums[i-1]
        return self.curNum.toNumber()
