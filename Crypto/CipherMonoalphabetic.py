from CipherInterface import CipherInterface
class CipherMonoalphabetic  (CipherInterface):
    def __init__(self,key):
        self.module = 27
        self.key=str(key)
        if len(self.key)<self.module:
            raise Exception("Illegal arguments. Key is too short.")
        for alpha in self.key:
            if not alpha.isalpha() and not alpha.isspace():
                raise Exception("Illegal arguments. There are some illegal symbols in key.")
        self.dictionary=[chr(x) for x in range(97,123)]
        self.dictionary.append(' ')
        self.dictionary_key=list(self.key)


    def decrypt(self, line):
        return ''.join([self.dictionary[self.dictionary_key.index(x)] for x in str(line).lower() if x.isspace()
                         or x.isalpha()])

    def encrypt(self, line):
        return ''.join([self.dictionary_key[self.dictionary.index(x)] for x in str(line).lower() if x.isspace()
                         or x.isalpha()])