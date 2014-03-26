
class Polynomial:

    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __str__(self):
        res = ""
        plus = ""
        i = len(self.coeffs) - 1
        for i in xrange(len(self.coeffs)-1, 0, -1):
            if self.coeffs[i] != 0:
                res += plus + str(self.coeffs[i])+'*x^'+str(i)
                plus = ' + '
        if self.coeffs[0] != 0:
            res += plus + str(self.coeffs[0]) 
        return res

    __repr__ = __str__ 

p  = Polynomial([0,2,3,0,0])
print p

