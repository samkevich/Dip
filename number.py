# -*- coding: utf-8 -*-
import math

class Number:
    def __init__(self, decNum, radix = 2, transpose = False):
        self.radix = radix
        self._num = self._decToRadix(decNum, radix)
        self.isTranspose = transpose
        if self.isTranspose:
            self.transpose();
    
    def _decToRadix(self, dec, radix):
        res = []
        while(dec >= radix):
            res.append(dec % radix)
            dec = dec / radix
        res.append(dec)
        res.reverse()
        return res

    def transpose(self):
        self.isTranspose = True
        self._num.reverse()

    def toDec(self):
        if self.isTranspose:
            divider = 1.0 / self.radix
            res = 0.0
            for elem in self._num:
                res += elem * divider
                divider /= self.radix
            return res
        else:
            divider = 1
            res = 0
            for elem in reversed(self._num):
                res += elem * divider
                divider *= self.radix
            return res
    
    def __str__(self):
        if self.isTranspose:
            res = "0."
        else:
            res = ""
        for a in self._num:
            res += str(a)
        return res
    
    __repr__ = __str__

class TransposedBinNumber:

    def __init__(self, bitList = []):
        self.bits = bitList

    def __str__(self):
        res = "0."
        for a in self.bits:
            res += str(a)
        return res

    __repr__ = __str__

    def toNumber(self):
        res = Number(0, 2, True)
        res._num = list(self.bits)
        return res

    def __xor__(left, right):
        lLen = len(left.bits)
        rLen = len(right.bits)
        if lLen > rLen:
            res = list(right.bits)
            res.extend([0 for _ in xrange(lLen - rLen)])
            return TransposedBinNumber([res[i] ^ left.bits[i] for i in xrange(lLen)])
        else:
            res = list(left.bits)
            res.extend([0 for _ in xrange(rLen - lLen)])
            return TransposedBinNumber([res[i] ^ right.bits[i] for i in xrange(rLen)])
    
