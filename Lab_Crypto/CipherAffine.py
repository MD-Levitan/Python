from CipherInterface import CipherInterface
from math import gcd
class CipherAffine (CipherInterface):

    def __init__(self,shift,multiplier):
        try:
            int(shift)
            int(multiplier)
        except ValueError:
            raise Exception("Illegal argument(s).It needs to be number, not line.")
        if gcd(int(multiplier),27)!=1:
            raise Exception("GCD(mu,module)!=1")
        self.shift=int(shift)
        self.multiplier=int(multiplier)
        self.dictionary=[chr(x) for x in range(97,123)]
        self.dictionary.append(' ')
        self.module=27
        self.fun_euler=18

    def encrypt(self,line):
        line=str(line).lower()
        new_line=[self.dictionary[(self.dictionary.index(x)*self.multiplier+self.shift)%self.module] for x in line if x.isalpha() or x.isspace()]
        return ''.join(new_line)

    def decrypt(self,line):
        line = str(line).lower()
        new_line = [self.dictionary[((self.dictionary.index(x) - self.shift)*(self.multiplier**(self.fun_euler-1))) % self.module] for x in line if x.isalpha() or x.isspace()]
        return ''.join(new_line)

