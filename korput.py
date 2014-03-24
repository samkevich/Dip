from number import *

class CorputIterator:
    def __init__(self, radix, startIndex = 1, endIndex = -1):
        if(startIndex < 1):
            raise ValueError("startIndex value must be greater than 0")
        self.curIndex = startIndex
        self.endIndex = endIndex
        self.radix = radix

    def __iter__(self):
        return self

    def next(self):
        if(self.curIndex == self.endIndex):
            raise StopIteration
        n = Number(self.curIndex, self.radix, True)
        self.curIndex += 1
        return n










