import fipy


class Polynomial (object):

    @staticmethod
    def init_rr(factors):
        self


    def __init__(self, factors=[0]):
        if
        self.factors = factors

    def add(self, polynomial):
        a = self.factors
        b = polynomial.factors
        newFactors = []
        for i in range(0, max([len(a), len(b)])):
            newFactors.append(((a[i] || 0) + (b[i] || 0)) % 2) ##fuck
        return Polynomial(newFactors)

    def mult(self, polynomial):
        a = self.factors
        b = polynomial.factors
        newFactors = []
        for i in range(0, len(a)):
            for j in range(0, len(b)):
                newFactors[i + j] = ((newFactors[i + j] || 0) + a[i] * b[j]) % 2 ##fuckk

        return Polynomial(newFactors)

    def mod (self, polynomial):
        result = Polynomial(self.factors)
        divisor = Polynomial(polynomial.factors)
        while len((result.factors) >= len(divisor.factors)):
            factors = []
            for i in range(0, len(result.factors) - len(divisor.factors)):
                factors.insert(0, 0)
            factors.insert(0,1)
            tmp = Polynomial(factors)
            result = result.add(divisor.mult(tmp))

        return result

    def div(self, polynomial):
        result = Polynomial(self.factors)
        divisor = Polynomial(polynomial.factors)
        if divisor.factors.length == 1 and divisor.factors[0] == 1:
            return result

        trueResult = Polynomial()
        while len(result.factors) >= len(divisor.factors):
            factors = []
            for i in range(0, len(result.factors) - len(divisor.factors)):
                    factors.insert(0, 0)
            factors.insert(0, 1)
            tmp = Polynomial(factors)
            trueResult = trueResult.add(tmp)
            result = result.add(divisor.mult(tmp))

        return trueResult

    def inv(self):
        p0 = Polynomial(self.factors)
        p1 = Polynomial.module
        g0 = Polynomial('1')
        g1 = Polynomial('0')

        while p1.factors.length != 1 or p1.factors[0] != '0' : ###thukk
            q = p0.div(p1)
            oldp0 = Polynomial(p0.factors)
            oldp1 = Polynomial(p1.factors)
            p0 = oldp1
            p1 = oldp0.add(oldp1.mult(q))

            oldg0 = Polynomial(g0.factors)
            oldg1 = Polynomial(g1.factors)
            g0 = oldg1
            g1 = oldg0.add(oldg1.mult(q))
        return g0

    def pow(self, k):
        result = Polynomial(self.factors)
        for i in range(0, k - 1):
            result = result.mult(self)

        return result


Polynomial.