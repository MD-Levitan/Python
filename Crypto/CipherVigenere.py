from CipherInterface import CipherInterface
class CipherVigenere(CipherInterface):

    def __init__(self,key):
        for x in str(key):
            if not x.isalpha():
                raise Exception("Illegal arguments. There are some digits in key.")
        self.key=str(key)
        self.dictionary=[chr(x) for x in range(97,123)]
        self.dictionary.append(' ')
        self.module=27

    def create_long_key(self,lenx):
        mu_line = lenx/(len(self.key))
        if mu_line > 1:
             return str((self.key * int(mu_line+1))[:lenx + 1])
        else:
            return self.key

    def encrypt(self,line):
        line=str(line).lower()
        key_line=self.create_long_key(len(line))
        return ''.join([(self.dictionary[(self.dictionary.index(p)+self.dictionary.index(k))%self.module]) for p,k in zip(line,key_line)])


    def decrypt(self,line):
        line = str(line).lower()
        key_line = self.create_long_key(len(line))
        return ''.join(
            [(self.dictionary[(self.dictionary.index(p) - self.dictionary.index(k)) % self.module]) for p, k in zip(line, key_line)])


